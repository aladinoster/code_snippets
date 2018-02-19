"""
This is just a test for
"""

# The following code just runs cells inside VSCode
# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.show()


# %%
x = np.linspace(0, 4 * np.pi, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.show()


def update(hello):
    pass
