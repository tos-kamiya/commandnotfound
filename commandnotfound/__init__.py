import sys
import os
import subprocess
import contextlib


command_not_found_command_list = [
    "/usr/lib/command-not-found",  # apt-based distribution
    "/usr/libexec/pk-command-not-found",  # yum-based distribution
]


def _print(e: FileNotFoundError) -> None:
    for cnfc in command_not_found_command_list:
        if os.path.exists(cnfc):
            command_name = e.filename
            ret_code = subprocess.call([cnfc, command_name])


def _exit() -> None:
    sys.exit(127)


def report(e: FileNotFoundError, exit: bool = True) -> None:
    """Print help message with a command-not-found command, if it exists.
    Then terminate process with exit code 127.
    """
    _print(e)
    if exit:
        _exit()


@contextlib.contextmanager
def handler(exit: bool = True):
    """When FileNotFound raises, print help message with a command-not-found command, if it exists.
    Then terminate process with exit code 127.
    """
    try:
        yield
    except FileNotFoundError as e:
        _print(e)
        if exit:
            _exit()
