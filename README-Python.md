# Valon Synth

## Installation

In order to use the Python code, it is necessary to build the C++
library first:

    $ make

This should create a `libValonSynth.so` shared object.

The Python software can now be installed for development use.  As a
first step, create a Python virtual environment.

    $ virtualenv venv

Optionally, activate it; the steps below assumes that the virtual
environment has not been activated.

Use the virtual environment to setup the package:

    $ ./venv/bin/pip install -r requirements.txt

To be able to use the package, we also need to be able to import it.
Normally the source directory name matches the package name, but
unfortunately in this instance it doesn't.  We create a symbolic link to
fudge it.

    $ ln -s src valon_synth

## Communication checks

We provide a example script that tests basic communications.  It
requires knowledge of the (USB-connected) serial port the Valon is
connected to.  In Linux, plug in both USB plugs on the Valon, and do

    $ dmesg

The last lines in the log should be similar to the following:

    usb 5-1: FTDI USB Serial Device converter now attached to ttyUSB0

This indicates the port we are interested in is `/dev/ttyUSB0`, which
coincidentally is the default port in the communications test example
script.

To run the communications check, simply do:

    $ ./venv/bin/python example/commtest.py --port /dev/ttyUSB0

Feel free to replace `/dev/ttyUSB0` in the command shown above with your
locally identified port.
