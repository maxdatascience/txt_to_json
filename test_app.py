import unittest
import


class TestApp(unittest.TestCase):
    def test_main(self, argv):
        path_to_orders_file = argv[0]
        path_to_dependencies_file = argv[1]
        path_to_output_file = argv[2]
        cmd_args = [path_to_orders_file,
                    path_to_dependencies_file, path_to_output_file]
        cmd_args_test = ["/samba/alldev/github/venv/Hatchway/txt_to_json/data/orders.txt",
                         "/samba/alldev/github/venv/Hatchway/txt_to_json/data/dependencies.txt", "/samba/alldev/github/venv/Hatchway/txt_to_json/data/output-my.json"]
        # test filenames
        self.assertEqual(cmd_args, cmd_args_test)
        # test created
        self.assertEaual(

if __name__ == "__main__":
    unittest.main()
