import numpy as np
import matplotlib.pyplot as plt

# Constants
frequency = 1e6  # Radar signal frequency (1 MHz)
duration = 1e-3  # Signal duration (1 ms)
sampling_rate = 1e7  # Sampling rate (10 MHz)

# Time array
time = np.linspace(0, duration, int(sampling_rate * duration))

# Original radar signal (sine wave)
signal = np.sin(2 * np.pi * frequency * time)

# Add noise to the signal
noise = np.random.normal(0, 0.5, len(time))
noisy_signal = signal + noise

# Plot original and noisy signals
plt.figure(figsize=(12, 6))
plt.plot(time, noisy_signal, label="Noisy Signal", alpha=0.7)
plt.plot(time, signal, label="Original Signal", linestyle="--", alpha=0.9)
plt.title("Radar Signal with Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
