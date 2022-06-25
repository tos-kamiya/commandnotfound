# commandnotfound

This package provides a wrapper of command-not-found handlers:

* Apt-based distribution's `/usr/lib/command-not-found`
* Yum-based distribution's `/usr/libexec/pk-command-not-found`

You know that when a command is not found in a command line of a shell, you will see the name of a similar command or a message prompting you to install the required package.

However, this trick does not work when you try to run a command in `subprocess.run`.

Wrap `subprocess.run` call with the `handler` context manager of this package.
Then, when the command is not found, such messages will be printed to the console.

## Installation

Install:

```sh
python3 -m pip install git+https://github.com/tos-kamiya/commandnotfound.git
```

Uninstall:

```sh
pip3 uninstall commandnotfound
```

## Usage

Context manager `handler`:

```python
import subprocess
import commandnotfound

with commandnotfound.handler():
    subprocess.run(["gitk"])
```

Function `exit`:

```python
import subprocess
import commandnotfound

try:
    subprocess.run(["gitk"])
except FileNotFoundError as e:
    commandnotfound.exit(e)
```

