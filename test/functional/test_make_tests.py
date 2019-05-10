"""Placeholder module to remind you to write tests."""
import pytest

pytestmark = [pytest.mark.local, pytest.mark.functional]


@pytest.mark.xfail(strict=True)
def test_write_tests():
    assert False
