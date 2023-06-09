# yaml-update-last-modified-date

Automatically set the last modified date in YAML front matter of edited markdown files.

## Quick start

Just `cd` into a folder containing a git repository, and run:

```shell
curl --location --remote-name \
    https://raw.githubusercontent.com/proinsias/yaml-update-last-modified-date/main/yaml-update-last-modified-date \
&& /usr/bin/env bash yaml-update-last-modified-date
```

This script will:

1. look for markdown files that differ from the current `HEAD`,
2. check to see if they contain the specified last-modified-date variable (`last modified date` by default)
   in their YAML front matter, if present, and
3. update the value of that variable to the current Universal Time Coordinated (UTC) time.

See below for instructions on how to install this script as a local command or as a
[pre-commit](https://github.com/pre-commit/pre-commit) git hook.

## Table of Contents

<!-- toc -->

-   [Credits](#credits)
-   [Updating the Table of Contents of this file](#updating-the-table-of-contents-of-this-file)

<!-- tocstop -->

## Installation yaml-update-last-modified-date via homebrew

If necessary, first install [homebrew](https://docs.brew.sh)!

Then:

```shell
brew install proinsias/yaml-update-last-modified-date/yaml-update-last-modified-date
```

## Using yaml-update-last-modified-date with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/proinsias/yaml-update-last-modified-date
  rev: '' # Use the sha / tag you want to point at
  hooks:
      - id: yaml-update-last-modified-date
```

## Credits

Thanks to [Michael Rose](https://github.com/mmistakes) for the
[original script](https://mademistakes.com/notes/adding-last-modified-timestamps-with-git/).

## License

See [LICENSE](LICENSE).

## Updating the Table of Contents of this file

We use [markdown-toc](https://github.com/jonschlinkert/markdown-toc)
to automatically generate the table of contents for this file. You can
update the TOC using:

```bash
# npm install --global markdown-toc

markdown-toc -i README.md
```
