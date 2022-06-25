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

## How it works

In some apt-based distributions such as Ubuntu, shows a hint as an error message, when a user types wrong command name, e.g.:

```sh
$ converT

Command 'converT' not found, did you mean:

  command 'convert' from deb imagemagick-6.q16 (8:6.9.10.23+dfsg-2.1ubuntu11.4)
....
```

This help system is implemented as `/usr/lib/command-not-found`, and the bash call it when a command is not found on PATH directories.

The help system does not work when you run command in a Python code with `subprocess.run`, e.g.:

```sh
$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import subprocess 
>>> subprocess.run(["converT"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
....
FileNotFoundError: [Errno 2] No such file or directory: 'converT'
>>> 
```

So the commandnotfound wrapper wraps `subprocess.run` and detects `FileNotFoundError` is thrown or not, and in case it thrown, call the help command `/usr/lib/command-not-found`.

```sh
$ python3 
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import subprocess
>>> import commandnotfound
>>> with commandnotfound.handler():
...     subprocess.run(["converT"])
... 

Command 'converT' not found, did you mean:

  command 'convert' from deb imagemagick-6.q16 (8:6.9.10.23+dfsg-2.1ubuntu11.4)
....
$ 
```

## Usage

Context manager `handler`:

```python
import subprocess
import commandnotfound

with commandnotfound.handler():
    subprocess.run(["converT"])
```

Function `report`:

```python
import subprocess
import commandnotfound

try:
    subprocess.run(["converT"])
except FileNotFoundError as e:
    commandnotfound.report(e)
```

#### Options

Both `commandnotfound.handler` and `commandnotfound.report` has a keyword argument `exit`. By passing a false value like `exit=False`, these functions does not terminate the process.
