from pykickstart.version import F29
from pykickstart.base import KickstartCommand
from pykickstart.errors import KickstartParseError
from pykickstart.options import KSOptionParser, commaSplit

class F29_ContainerRegistries(KickstartCommand):
    def __init__(self, writePriority=11, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.urls = kwargs.get("urls", None)
        self.op = self._getParser()

    def _getParser(self):
        op = KSOptionParser(prog="container_registries", description="""
                            Setup container registries that will be used to pull
                            boot container image and additional images, if any are specified.""",
                            version=F29)
        op.add_argument("urls",
                        metavar="[urls]",
                        nargs='+',
                        help="Registry URLs",
                        version=F29)
        return op

    def __str__(self):
        retval = KickstartCommand.__str__(self)
        if not self.urls:
            return retval

        retval += "container_registries " + ' '.join(self.urls) + "\n"

        return retval

    def parse(self, args):
        ns = self.op.parse_args(args=args, lineno=self.lineno)
        self.set_to_self(ns)
        return self
