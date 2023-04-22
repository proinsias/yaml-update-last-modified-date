# yaml-update-last-modified-date

Automatically set the last modified date in YAML front matter of edited markdown files.

## Quick start

1. `cd` into a folder containing a git repository.
2. `git add` a modified markdown (`.md`) file that has `last_modified_at` in its YAML front matter.
3. Install this via:
   a. (Recommended) `pipx install yaml-update-last-modified-date` to install into its own virtual environment,
   b. `brew install proinsias/yaml-update-last-modified-date/yaml-update-last-modified-date`, or
   c. `python -m pip install yaml-update-last-modified-date`.
4. Run!: `yaml-update-last-modified-date`.

This script will:

1. Look for markdown files that differ from the current `HEAD`,
2. Check to see if they contain the specified last-modified-date variable (`last_modified_at` by default)
   in their YAML front matter, if present, and
3. Update the value of that variable to the current Universal Time Coordinated (UTC) time
   using the specified datetime format (`"%Y-%m-%d %H:%M:%S"` by default).

See below for instructions on how to install this as a
[pre-commit](https://github.com/pre-commit/pre-commit) git hook.

## Table of Contents

<!-- toc -->

-   [Using yaml-update-last-modified-date with pre-commit](#using-yaml-update-last-modified-date-with-pre-commit)
-   [Credits](#credits)
-   [License](#license)

<!-- tocstop -->

## Using yaml-update-last-modified-date with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/proinsias/yaml-update-last-modified-date
  rev: '' # Use the sha / tag you want to point at
  hooks:
      - id: yaml-update-last-modified-date
```

<!-- FIXME: Add full docs.
## Full documentation

Available here: [./docs](./docs).

-->

## Credits

Thanks to [Michael Rose](https://github.com/mmistakes) for the
[original script](https://mademistakes.com/notes/adding-last-modified-timestamps-with-git/).

## License

See [LICENSE](LICENSE).
