from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

values = list(range(30, 70))
sample = np.random.normal(loc=50, scale=5, size=1000)
sample_mean = np.mean(sample)
sample_std = np.std(sample)
print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))
dist = norm(sample_mean, sample_std)
probabilities = dist.pdf(values)

plt.figure(figsize=(5, 4))
plt.hist(sample, bins=20, density=True, color='blue', alpha=0.7)
plt.plot(values, probabilities, color='orange', linewidth=2)
plt.title('Grafik curah hujan')
plt.xlabel('Nilai')
plt.ylabel('Probabilitas')
plt.legend()
plt.show()