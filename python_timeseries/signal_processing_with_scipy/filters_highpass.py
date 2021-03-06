from matplotlib import pyplot as plt
import numpy as np
from scipy import signal

t = np.linspace(0, 1, 1000, False)
f1 = 3
f2 = 50
sig = np.sin(f1 * 2 * np.pi * t) + 1 *  np.sin(f2 * 2 * np.pi * t)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.plot(t, sig)
ax1.set_title('Signal')
ax1.axis([0, 1, -2, 2])
plt.show()

def butter_bandpass(highcut, fs, order=5):
    nyq = 0.5 * fs
    high = highcut / nyq
    b, a = signal.butter(order, high, 'high', analog=False)
    return b, a

def butter_bandpass_filter(data, highcut, fs, order=5):
    b, a = butter_bandpass(highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y, b, a

fs = 1000
res, b, a = butter_bandpass_filter(sig, 20, fs, order=5)

w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
plt.plot(t, res)
ax1.set_title('Filtered Signal')
ax1.axis([0, 1, -2, 2])
plt.show()
