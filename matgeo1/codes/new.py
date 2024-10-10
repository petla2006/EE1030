import numpy as np
import matplotlib.pyplot as plt

# Read the unit vector from the output.txt file
with open('output.txt', 'r') as file:
    line = file.readline()
    x, y = map(float, line.split())

# Calculate the angle of the vector in degrees
angle = np.degrees(np.arctan2(y, x))

# Plotting the vector
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='b', label=f'({x:.2f}, {y:.2f})\nAngle: {angle:.2f}°')

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.title('Unit Vector in XY Plane')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Adding a legend
plt.legend(loc='upper right')

# Save the plot as figure1.png
plt.savefig('figure1.png')
plt.show()

