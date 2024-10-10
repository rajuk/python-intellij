load("@python_3_9//:defs.bzl", _py_binary = "py_binary", _py_test = "py_test")
load("@rules_python//python:defs.bzl", _py_library = "py_library")

py_binary = _py_binary
py_library = _py_library


def py_test(name, pytest_args = None, **kwargs):
    if not pytest_args:
        pytest_args = []
    pytest_args = pytest_args + [
        "--verbose", "-s", "--ignore=external/",
    ]

    env = kwargs.pop("env", {})
    env["_PYTEST_ARGS_"] = "\n".join(pytest_args)

    _py_test(
        name = name,
        env = env,
        **kwargs,
    )
