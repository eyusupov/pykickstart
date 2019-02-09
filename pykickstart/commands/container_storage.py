from pykickstart.version import F29
from pykickstart.base import KickstartCommand
from pykickstart.errors import KickstartParseError
from pykickstart.options import KSOptionParser, commaSplit
from pykickstart.i18n import _

class F29_ContainerStorage(KickstartCommand):
    def __init__(self, writePriority=11, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.options = kwargs.get("options", {})
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
        for key, value in self.options.items():
            retval += ' ' + key + '=' + value
        retval += "\n"

        return retval

    def parse(self, args):
        if not len(args):
            raise KickstartParseError(_("options need to be specified for container_storage command"), lineno=self.lineno)
        i = 0
        while i < len(args):
            option = args[i]
            i += 1
            if '=' in option:
                option, _sep, value = option.partition('=')
            else:
                value = args[i]
                i += 1
            self.options[option] = value
        return self
