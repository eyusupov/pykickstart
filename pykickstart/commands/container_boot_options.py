from pykickstart.version import F29
from pykickstart.base import KickstartCommand
from pykickstart.errors import KickstartParseError
from pykickstart.options import KSOptionParser, commaSplit

class F29_ContainerBootOptions(KickstartCommand):
    def __init__(self, writePriority=6, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.options = kwargs.get('options', None)
        self.defaults = kwargs.get("defaults", True)
        self.op = self._getParser()

    def _getParser(self):
        op = KSOptionParser(prog="container_boot_options", description="""
                            This command specifies which options to pass to the
                            container tool when creating the boot container.""",
                            version=F29)
        op.add_argument("--nodefaults",
                        dest="defaults",
                        action="store_false",
                        version=F29,
                        help="Inhibit default options.")

        op.add_argument("options",
                        metavar="[options]",
                        nargs='*',
                        help="See ``man podman``.",
                        version=F29)
        return op

    def __str__(self):
        retval = KickstartCommand.__str__(self)

        retval += "container_boot_options"
        if not self.defaults:
            retval += ' --nodefaults'
        if self.options:
            retval += ' -- ' + ' '.join(self.options)
        retval += "\n"

        return retval

    def parse(self, args):
        ns = self.op.parse_args(args=args, lineno=self.lineno)
        self.set_to_self(ns)
        return self
