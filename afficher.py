import matplotlib.pyplot as plt
import numpy as np
import sigmf

# Figure 1 (Signal en sortie)
handle = sigmf.sigmffile.fromfile('C:/Users/cleme/Desktop/ProjetS9/icassp2024rfchallenge-0.2.0/dataset/demod_train/CommSignal2/CommSignal2_demod_train_0000.sigmf-data')
sample = handle.read_samples() # returns all timeseries data
handle.get_global_info() # returns 'global' dictionary
handle.get_captures() # returns list of 'captures' dictionaries
handle.get_annotations() # returns list of all annotations

plt.figure(1)
plt.plot(np.real(sample[1:500]))
plt.title("Output")


# Figure 2 (Interferénces CommSignal2)
handle_2 = sigmf.sigmffile.fromfile('C:/Users/cleme/Desktop/ProjetS9/icassp2024rfchallenge-0.2.0/dataset/demod_train/Components/CommSignal2/Interference/CommSignal2_demod_train_0000.sigmf-data')
sample_2 = handle_2.read_samples() # returns all timeseries data

plt.figure(2,figsize=(6.4*1.2, 4.8*1.2))
plt.subplot(121)
plt.plot(np.real(sample_2[1:500]))
plt.title("Interferences")

# Spectrogram
plt.subplot(122)
plt.specgram(sample_2)
plt.title("Spectrogram")

# Figure 3 (Interferénces CommSignal3)
handle_3 = sigmf.sigmffile.fromfile('C:/Users/cleme/Desktop/ProjetS9/icassp2024rfchallenge-0.2.0/dataset/demod_train/Components/CommSignal3/Interference/CommSignal3_demod_train_0000.sigmf-data')
sample_3 = handle_3.read_samples() # returns all timeseries data

plt.figure(3,figsize=(6.4*1.2, 4.8*1.2))
plt.subplot(121)
plt.plot(np.real(sample_3[1:500]))
plt.title("Interferences")

# Spectrogram
plt.subplot(122)
plt.specgram(sample_3)
plt.title("Spectrogram")

# Figure 3 (Interferénces EMISignal1)
handle_4 = sigmf.sigmffile.fromfile('C:/Users/cleme/Desktop/ProjetS9/icassp2024rfchallenge-0.2.0/dataset/demod_train/Components/EMISignal1/Interference/EMISignal1_demod_train_0000.sigmf-data')
sample_4 = handle_4.read_samples() # returns all timeseries data

plt.figure(4,figsize=(6.4*1.2, 4.8*1.2))
plt.subplot(121)
plt.plot(np.real(sample_4[1:500]))
plt.title("Interferences")

# Spectrogram
plt.subplot(122)
plt.specgram(sample_4)
plt.title("Spectrogram")

# Figure 3 (Signal en entrée)
handle_5 = sigmf.sigmffile.fromfile('C:/Users/cleme/Desktop/ProjetS9/icassp2024rfchallenge-0.2.0/dataset/demod_train/Components/CommSignal2/QPSK/CommSignal2_demod_train_0000.sigmf-data')
sample_5 = handle_5.read_samples() # returns all timeseries data

plt.figure(5)
plt.plot(np.real(sample_5[1:500]))
plt.title("Inpout")

# Show
plt.show()
