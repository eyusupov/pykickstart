from pykickstart.version import F29
from pykickstart.base import KickstartCommand
from pykickstart.errors import KickstartParseError
from pykickstart.options import KSOptionParser, commaSplit

class F29_ContainerStorage(KickstartCommand):
    def __init__(self, writePriority=6, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.options = kwargs.get("options", None)
        self.op = self._getParser()

    def _getParser(self):
        op = KSOptionParser(prog="container_storage", description="""
                            Setup local container storage.
                            See ```man storage.conf``` for configuration options details.""",
                            version=F29)
        op.add_argument("options",
                        metavar="[options]",
                        nargs='+',
                        help="Storage configuration options",
                        version=F29)
        return op

    def __str__(self):
        retval = KickstartCommand.__str__(self)

        retval += "container_storage"
        if self.options:
            retval += ' ' + ' '.join(self.options)
        retval += "\n"

        return retval

    def parse(self, args):
        ns = self.op.parse_args(args=args, lineno=self.lineno)
        self.set_to_self(ns)
        return self
