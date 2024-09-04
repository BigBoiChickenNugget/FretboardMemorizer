import sounddevice as sd
import numpy as np

from scipy.fft import fft, fftfreq

# Parameters (I'll play around with these)
sample_rate = 44100


# Record a note
def record_note(duration):
    print("NOW...")
    audio = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1)
    sd.wait()

    return np.squeeze(audio)


def get_fft(audio, sampling_rate):
    N = len(audio)
    yf = fft(audio)
    xf = fftfreq(N, 1 / sampling_rate)

    # Get peak frequency
    idx = np.argmax(np.abs(yf))
    peak_freq = xf[idx]

    return peak_freq


def note_name(frequency):

    A4 = 440.0
    C0 = A4 * pow(2, -4.75)

    if frequency == 0:
        return None

    h = round(12 * np.log2(frequency / C0))
    octave = h // 12
    note = h % 12

    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    # return notes[note] + str(octave)
    return notes[note]


def get_note(duration):
    audio = record_note(duration)
    frequency = get_fft(audio, sample_rate)
    return note_name(frequency)
