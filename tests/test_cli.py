import logging
import os

import click
from click.testing import CliRunner

from bottery.cli import cli, debug_option


def test_debug_option():
    logger = logging.getLogger('bottery')

    @click.command()
    @debug_option
    def hello(debug):
        pass

    runner = CliRunner()
    runner.invoke(hello, ['--debug'])

    assert logger.level == logging.DEBUG


def test_startproject():
    runner = CliRunner()
    with runner.isolated_filesystem():
        project_name = 'librarybot'
        project_files = ['patterns.py', 'settings.py']

        result = runner.invoke(cli, ['startproject', project_name])

        assert result.exit_code == 0
        assert os.listdir() == [project_name]
        assert os.listdir(project_name) == project_files
