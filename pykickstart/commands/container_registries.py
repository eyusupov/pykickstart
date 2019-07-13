from pykickstart.version import F29
from pykickstart.base import KickstartCommand
from pykickstart.errors import KickstartParseError
from pykickstart.options import KSOptionParser, commaSplit
from pykickstart.i18n import _

class F29_ContainerRegistries(KickstartCommand):
    def __init__(self, writePriority=11, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.search = kwargs.get("search", [])
        self.insecure = kwargs.get("insecure", [])
        self.op = self._getParser()

    def _getParser(self):
        op = KSOptionParser(prog="container_registries", description="""
                            Setup container registries that will be used to pull
                            boot container image and additional images, if any are specified.""",
                            version=F29)
        op.add_argument("--search",
                        type=commaSplit,
                        metavar="<search1>,<search2>,...,<searchN>",
                        help="Registry URLs",
                        version=F29)
        op.add_argument("--insecure",
                        type=commaSplit,
                        metavar="<insecure1>,<insecure2>,...,<insecureN>",
                        help="Insecure registries",
                        version=F29)
        return op

    def __str__(self):
        retval = KickstartCommand.__str__(self)
        if not self.seen:
            return retval

        retval += "container_registries"
        if self.search:
            retval += " --search=" + ",".join(self.search)
        if self.insecure:
            retval += " --insecure=" + ",".join(self.insecure)

        retval += "\n"
        return retval

    def parse(self, args):
        if len(args) == 0:
            raise KickstartParseError(_("options need to be specified for container_registries command"), lineno=self.lineno)
        ns = self.op.parse_args(args=args, lineno=self.lineno)
        self.set_to_self(ns)
        return self
