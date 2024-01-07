"""Test generics about the python packaging itself."""
from __future__ import annotations

from app import __version__


def test_version():
    """Test the version exists."""
    assert __version__.split(".")
