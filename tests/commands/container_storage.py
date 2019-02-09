import unittest
from tests.baseclass import CommandTest
from pykickstart.errors import KickstartDeprecationWarning

class F29_TestCase(CommandTest):
    command = "container_storage"

    def runTest(self):
        self.assert_parse_error("container_storage")

        self.assert_parse("container_storage runroot=/var/lib/containers graphroot=/var/run/containers driver=overlay",
                          "container_storage runroot=/var/lib/containers graphroot=/var/run/containers driver=overlay\n")

        command = self.handler().commands[self.command]
        self.assertEqual(command.options, None)
