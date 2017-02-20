#! /usr/bin/env python

from optparse import OptionParser
import time

import valon_synth
from valon_synth import SYNTH_B


# Simple example of using the Valon Synth directly
def main(port):
    print """
Connect a Valon 5007 to a spectrum analyser -- a 20dB attenuator is used.
The Valon 5007 is specified to have a range of 137 MHz to 4400MHz.
"""
    raw_input('Enter to connect to Valon')

    # MTS uses only one of the available synthesizers (currently SYNTH 2)
    synth = valon_synth.Synthesizer(port, timeout=None)

    if synth.get_rf_level(SYNTH_B) != -4:
        synth.set_rf_level(SYNTH_B, -4)

    # Set CW signal frequency
    synth.set_frequency(SYNTH_B, freq=137, chan_spacing=1.)
    print 'CW frequency set to %s MHz' % synth.get_frequency(SYNTH_B)
    raw_input('Enter to continue')

    print 'Setting Valon to Low Spur Mode'
    synth.set_options(SYNTH_B, low_spur=1)
    raw_input('Enter to continue')

    print 'Settings Valon to Low Noise Mode'
    synth.set_options(SYNTH_B, low_spur=0)
    raw_input('Enter to continue')

    print 'Sweep over frequencies 137MHz to 1500MHz'
    for freq_mhz in range(137, 1500, 20):
        synth.set_frequency(SYNTH_B, freq=freq_mhz, chan_spacing=1.)
        print 'CW frequency set to %s MHz' % synth.get_frequency(SYNTH_B)
        raw_input('Enter to continue')

    print 'Sweep over frequencies 137MHz to 4400MHz'
    raw_input('Enter to continue')
    for freq_mhz in range(137, 4400, 100):
        synth.set_frequency(SYNTH_B, freq=freq_mhz, chan_spacing=1.)
        print 'CW frequency set to %s MHz' % synth.get_frequency(SYNTH_B)
        time.sleep(1)


if __name__ == '__main__':
    parser = OptionParser(version="%prog 0.1")
    parser.add_option('-p', '--port',
                      action='store',
                      dest='tty',
                      default='/dev/ttyUSB0',
                      help="Set Serial Port, default is '%default'.")
    (opts, _) = parser.parse_args()
    main(opts.tty)

# -fin-
