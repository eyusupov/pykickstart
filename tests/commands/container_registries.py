import unittest
from tests.baseclass import CommandTest
from pykickstart.errors import KickstartDeprecationWarning

class F29_TestCase(CommandTest):
    command = "container_registries"

    def runTest(self):
        self.assert_parse_error("container_registries")

        self.assert_parse("container_registries --search registry.fedoraproject.org",
                          "container_registries --search=registry.fedoraproject.org\n")

        self.assert_parse("container_registries --search registry.fedoraproject.org,docker.io",
                          "container_registries --search=registry.fedoraproject.org,docker.io\n")

        self.assert_parse("container_registries --search registry.fedoraproject.org,docker.io,localhost:5000 --insecure localhost:5000",
                          "container_registries --search=registry.fedoraproject.org,docker.io,localhost:5000 --insecure=localhost:5000\n")

        command = self.handler().commands["container_registries"]
        self.assertEqual(command.insecure, [])
        self.assertEqual(command.search, [])
        self.assertEqual(command.__str__(), "")
