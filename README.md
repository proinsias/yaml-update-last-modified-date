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

## Table of Contents

<!-- toc -->

- [Credits](#credits)
- [Updating the Table of Contents of this file](#updating-the-table-of-contents-of-this-file)

<!-- tocstop -->

## Credits

Thanks to [Michael Rose](https://github.com/mmistakes) for the original script he
[posted](https://mademistakes.com/notes/adding-last-modified-timestamps-with-git/).

## Updating the Table of Contents of this file

We use [markdown-toc](https://github.com/jonschlinkert/markdown-toc)
to automatically generate the table of contents for this file. You can
update the TOC using:

```bash
# npm install --global markdown-toc

markdown-toc -i README.md
```
