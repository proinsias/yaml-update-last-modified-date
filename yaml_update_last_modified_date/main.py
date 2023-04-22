"""Set the last modified date in YAML front matter of edited markdown files.

Credit to Michael Rose (@mmistakes) for the basis of this script.
https://mademistakes.com/notes/adding-last-modified-timestamps-with-git/

Credit to ChatGPT for help converting it to python.
"""

import datetime as dt
import os
import tempfile
import typing

import git
import rich.pretty
import typer

import yaml_update_last_modified_date


app = typer.Typer()
rich.pretty.install()


def version_callback(
    value: bool,
) -> None:
    if value:
        typer.echo(f"{yaml_update_last_modified_date.__name__} version: {yaml_update_last_modified_date.__version__}")
        raise typer.Exit()


@app.command()
def main(
    *,
    version: typing.Optional[bool] = typer.Option(
        False,
        "--version",
        "-v",
        help=f"print the version of {yaml_update_last_modified_date.__name__}",
        callback=version_callback,
        is_eager=True,
    ),
    field: typing.Optional[str] = typer.Option(
        'last_modified_at',
        "--field",
        "-f",
        help="the YAML field name for the date the file was last modified",
    ),
    datetime_format: typing.Optional[str] = typer.Option(
        '%Y-%m-%d %H:%M:%S',
        "--datetime-format",
        "-d",
        help="the format for the last modified date field",
    ),
) -> None:
    """Set the last modified date in YAML front matter of edited markdown files."""
    # Use Git to get a list of modified Markdown files.
    repo = git.Repo(search_parent_directories=True)
    diff_index = repo.index.diff('HEAD')
    modified_files = [diff.a_path for diff in diff_index if diff.change_type != 'D']
    modified_files = [file for file in modified_files if file.endswith('.md')]

    # Update the last_modified_at field in each file.
    tmpfile = tempfile.mktemp()
    last_modified_at = dt.datetime.now(dt.timezone.utc).strftime(datetime_format)
    for file in modified_files:
        with open(file, 'r') as f:
            lines = f.readlines()
        with open(tmpfile, 'w') as f:
            for line in lines:
                if line.startswith(f'{field}:'):
                    f.write(f'{field}: {last_modified_at}\n')
                    typer.echo(f'Updated {field} for {file}.')
                else:
                    f.write(line)
        os.replace(tmpfile, file)
        repo.git.add(file)


if __name__ == "__main__":
    app()
