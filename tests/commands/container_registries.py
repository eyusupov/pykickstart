import unittest
from tests.baseclass import CommandTest
from pykickstart.errors import KickstartDeprecationWarning

class F29_TestCase(CommandTest):
    command = "container_registries"

    def runTest(self):
        self.assert_parse_error("container_registries")

        self.assert_parse("container_registries registry.fedoraproject.org",
                          "container_registries registry.fedoraproject.org\n")


        command = self.handler().commands["container_registries"]
        self.assertEqual(command.urls, None)
        self.assertEqual(command.__str__(), "")
