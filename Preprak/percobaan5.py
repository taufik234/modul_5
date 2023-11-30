from matplotlib import pyplot as plt


from numpy.random import normal

from numpy import mean,std

from scipy.stats import norm

sample = normal (loc=50, scale=5, size=1000)


sample_mean = mean(sample)
sample_std = std(sample)

dist = norm(sample_mean, sample_std)
dist

values = [value for value in range(30, 70)]

probabilitas = [dist.pdf(value) for value in values]

probabilitas

plt.figure(figsize=(5,4))
plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilitas)


plt.show()