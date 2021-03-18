# import numpy as np
# import wave
# import struct
# import matplotlib.pyplot as plt
# import sys
# import contextlib

# infile = sys.argv[1]

# with contextlib.closing(wave.open(infile,'r')) as f:
#     num_samples = f.getnframes()
#     frame_rate = f.getframerate()

# wav_file = wave.open(infile, 'r')
# data = wav_file.readframes(num_samples)
# wav_file.close()

# data = struct.unpack('{n}h'.format(n=num_samples), data)
# data = np.array(data)

# data_fft = np.fft.fft(data)
# frequencies = np.abs(data_fft)

# print("The frequency is {} Hz".format(np.argmax(frequencies)))
# print("{} samples".format(num_samples))
# print("__________________")

# plt.subplot(2,1,1)
# plt.plot(data[:20000])
# plt.title("Original audio wave")
# plt.subplot(2,1,2)
# plt.plot(frequencies)
# plt.title("Frequencies found")
# plt.xlim(0,1200)
# plt.show()
# plt.close


import librosa