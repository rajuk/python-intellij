import os
import sys

import pytest

def test_foo():
    condition = True
    assert condition

if __name__ == "__main__":
    args = os.environ.get("_PYTEST_ARGS_", "").split("\n")
    assert("-s" in args)
    assert("--verbose" in args)
    sys.exit(pytest.main(args))
