import os
import pytest
import sys

def test_foo():
    assert 1

if __name__ == "__main__":
    args = os.environ.get("_PYTEST_ARGS_", "").split("\n")
    sys.exit(pytest.main())