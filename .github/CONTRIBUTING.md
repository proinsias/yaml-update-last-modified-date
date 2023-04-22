# Contributing to _yaml-update-last-modified-date_

Welcome! Happy to see you willing to make the project better.

## How to contribute

All contributions are very welcome! You can contribute in many ways:

1. Report bugs on the GitHub [issue tracker](https://github.com/proinsias/yaml-update-last-modified-date/issues).
2. Submit pull requests on the GitHub [repository](https://github.com/proinsias/yaml-update-last-modified-date/).

I look forward to seeing your contributions!

## Code Quality

There is a [pre-commit](https://pre-commit.com) configuration to prevent various small problems before they are committed:

```shell
pipx install pre-commit
# Or: brew install pre-commit
# Or: python -m pip install pre-commit
pre-commit install
```

## Tests

Please do run the tests before submitting a pull request:

```shell
poetry run pytest
```

yaml-update-last-modified-date targets Python 3.8 and above. You can use tox to test this locally, and all tests are run with Github Actions.

## Table of Contents

<!-- toc -->

-   [Updating Table of Contents](#updating-table-of-contents)

<!-- tocstop -->

## Updating Table of Contents

We use [markdown-toc](https://github.com/jonschlinkert/markdown-toc)
to automatically generate the table of contents for our markdown files. You can
update the TOC using:

```bash
# npm install --global markdown-toc

markdown-toc -i filename.md
```
