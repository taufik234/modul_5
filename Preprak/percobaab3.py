import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])


plt.plot(y1, label='garis 1')
plt.plot(y2, label='garis 2')


plt.title('plot dua garis')
plt.xlabel('nilai x')
plt.ylabel('nilai y')

plt.legend()
plt.show()
