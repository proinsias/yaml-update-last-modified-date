import os
import pathlib
import tempfile

import git
import typer.testing

from yaml_update_last_modified_date import __name__, __version__
from yaml_update_last_modified_date.main import app

runner = typer.testing.CliRunner()


def test_main__version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout
    assert __name__ in result.stdout


def test_main():
    with tempfile.TemporaryDirectory() as temporaryDirectory:
        dir = pathlib.Path(temporaryDirectory)
        repo_path = dir / "repo"
        repo = git.Repo.init(repo_path)
        file = repo_path / "file.md"
        with file.open(mode="w") as f:
            file.write_text(
                """
---
modified_at: 2000-01-01
---
"""
            )
            repo.index.add([file.name])
            repo.index.commit("Added a new markdown file.")
            file.write_text(
                """
Adding text to file.
"""
            )
            repo.index.add([file.name])

            prev_cwd = pathlib.Path.cwd()
            os.chdir(repo_path)
            result = runner.invoke(app, ["--field", "modified_at", "--datetime-format", "%Y-%m-%d"])
            os.chdir(prev_cwd)
            assert result.exit_code == 0
            assert file.name in result.stdout  # FIXME: Why does this not work?
