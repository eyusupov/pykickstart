import unittest
from tests.baseclass import CommandTest
from pykickstart.errors import KickstartDeprecationWarning

class F29_TestCase(CommandTest):
    command = "container_boot_image"

    def runTest(self):
        self.assert_parse_error("container_boot_image")

        self.assert_parse("container_boot_image fedora:latest",
                          "container_boot_image fedora:latest\n")

        command = self.handler().commands[self.command]
        self.assertEqual(command.__str__(), "")
