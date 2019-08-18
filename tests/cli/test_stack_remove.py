from wo.utils import test
from wo.cli.main import get_test_app


class CliTestCaseStack(test.WOTestCase):

    def test_wo_cli(self):
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_remove_web(self):
        self.app = get_test_app(argv=['stack', 'remove', '--web', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_admin(self):
        self.app = get_test_app(argv=['stack', 'remove', '--admin', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_nginx(self):
        self.app = get_test_app(argv=['stack', 'remove', '--nginx', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_php(self):
        self.app = get_test_app(argv=['stack', 'remove', '--php', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_mysql(self):
        self.app = get_test_app(argv=['stack', 'remove', '--mysql', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_wpcli(self):
        self.app = get_test_app(argv=['stack', 'remove', '--wpcli', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_phpmyadmin(self):
        self.app = get_test_app(argv=['stack', 'remove',
                                      '--phpmyadmin', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_adminer(self):
        self.app = get_test_app(
            argv=['stack', 'remove', '--adminer', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_utils(self):
        self.app = get_test_app(argv=['stack', 'remove', '--utils', '--force'])
        self.app.setup()
        self.app.run()
        self.app.close()
