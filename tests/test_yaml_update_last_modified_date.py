import toml

from yaml_update_last_modified_date import __version__


def test_version():
    assert __version__ == "2.0.0"

    # Check that PyProject and __version__ are equivalent.
    result = toml.load('pyproject.toml')['tool']['poetry']['version']
    assert result == __version__
