import numpy as np
import matplotlib.pyplot as plt

frequency = [39, 42, 45, 45, 42, 41, 39, 39, 32, 35, 35, 31, 31, 40, 50, 55, 55, 30, 31, 30, 31, 51, 55, 40, 40, 41, 42, 41, 43, 50]


# Calculate the standard deviation
StandardDeviation = np.std(frequency)


# Plotting the histogram
plt.hist(frequency, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title(f'standard deviation for time of delivery: {StandardDeviation:.2f}')
plt.xlabel('standard deviation of the given time')
plt.ylabel('frequency of receiving time')

plt.axhline(np.max(plt.gca().get_ylim()) * 0.95, color='r', linestyle='dashed', linewidth=1.3,
            label="latest")  # max line
plt.axhline(np.mean(plt.gca().get_ylim()), color='b', linestyle='dashed', linewidth=1.3,
            label='average of time')  # average line
plt.axhline(np.min(plt.gca().get_ylim()) + 0.99, color='g', linestyle='dashed', linewidth=1.3,
            label="earliest")  # min line
plt.legend()
plt.show()
