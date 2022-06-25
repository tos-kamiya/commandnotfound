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


def exit(e: FileNotFoundError) -> None:
    _print(e)
    _exit()


@contextlib.contextmanager
def handler():
    try:
        yield
    except FileNotFoundError as e:
        _print(e)
        _exit()
