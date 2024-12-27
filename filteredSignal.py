from scipy.signal import butter, filtfilt

# Design a low-pass filter
def low_pass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Apply the low-pass filter
cutoff_frequency = 2e6  # Cutoff frequency (2 MHz)
filtered_signal = low_pass_filter(noisy_signal, cutoff_frequency, sampling_rate)

# Plot filtered signal
plt.figure(figsize=(12, 6))
plt.plot(time, noisy_signal, label="Noisy Signal", alpha=0.7)
plt.plot(time, filtered_signal, label="Filtered Signal", color="red")
plt.title("Filtered Radar Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
