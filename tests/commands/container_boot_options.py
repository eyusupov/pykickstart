import unittest
from tests.baseclass import CommandTest
from pykickstart.errors import KickstartDeprecationWarning

class F29_TestCase(CommandTest):
    command = "container_boot_options"

    def runTest(self):
        self.assert_parse("container_boot_options",
                          "container_boot_options\n")

        self.assert_parse("container_boot_options -- -v /home:/home",
                          "container_boot_options -- -v /home:/home\n")

        self.assert_parse("container_boot_options --nodefaults",
                          "container_boot_options --nodefaults\n")

        self.assert_parse("container_boot_options --nodefaults -- -v /boot:/boot -v /etc:/etc",
                          "container_boot_options --nodefaults -- -v /boot:/boot -v /etc:/etc\n")

        command = self.handler().commands[self.command]
        self.assertEqual(command.options, None)
        self.assertEqual(command.defaults, True)
        self.assertEqual(command.__str__(), "")
