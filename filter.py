#! /usr/env python

#setup to run with ipython

from __future__ import print_function, division
#replace qt5 depending on env setup e.g. (osx)
%matplotlib qt5

import thinkdsp
import thinkplot

# import warnings
# warnings.filterwarnings('ignore')

from IPython.html.widgets import interact, fixed
from IPython.display import display

wave = thinkdsp.read_wave('170255__dublie__trumpet.wav')
wave.normalize()
wave.make_audio()


wave.plot()

#Interactive Version
def filter_wave(wave, start, duration, cutoff):
segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()

    spectrum.plot(high=5000, color='0.7')
    spectrum.low_pass(cutoff)
    spectrum.plot(high=5000, color='#045a8d')
    thinkplot.config(xlabel='Frequency (Hz)')

    audio = spectrum.make_wave().make_audio()
     display(audio)

    interact(filter_wave, wave=fixed(wave),
         start=(0, 5, 0.1), duration=(0, 5, 0.1), cutoff=(0, 5000, 100));
