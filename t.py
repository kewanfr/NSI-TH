import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 10, 100)


def f(x):
    return np.where(x <= -1, x + 2, x**2)
    # if x <= -1:
    #     return x + 2
    # else:
    #     return x**2


fig = plt.figure()
plt.plot(x, f(x), "-")
# plt.plot(x, np.cos(x), '--');
plt.show()
