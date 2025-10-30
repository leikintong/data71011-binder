import numpy as np
import matplotlib.pyplot as plt

print("Hello, reproducible world!")

x = np.arange(0, 10)
y = x ** 2
plt.plot(x, y)
plt.title("My First Binder Plot")
plt.show()
