from pykickstart.version import F29
from pykickstart.base import KickstartCommand
from pykickstart.errors import KickstartParseError
from pykickstart.options import KSOptionParser, commaSplit

class F29_ContainerBootImage(KickstartCommand):
    def __init__(self, writePriority=6, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.image = kwargs.get('image', None)
        self.op = self._getParser()

    def _getParser(self):
        op = KSOptionParser(prog="container_boot_image", description="""
                            Container image to pull from registry and use for the boot container.""",
                            version=F29)
        op.add_argument("image",
                        help='image reference',
                        version=F29)
        return op

    def __str__(self):
        retval = KickstartCommand.__str__(self)

        retval += "container_boot_image " + self.image + "\n"

        return retval

    def parse(self, args):
        ns = self.op.parse_args(args=args, lineno=self.lineno)
        self.set_to_self(ns)
        return self
