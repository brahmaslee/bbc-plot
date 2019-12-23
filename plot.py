#!/usr/bin/env python

"""
This is just an example script intended to show what the stylesheet generates
"""

import numpy as np
from scipy.stats import gaussian_kde

import matplotlib.pyplot as plt
plt.style.use("bbc")

x_coord = np.array([1,2,3])
y_coord = np.array([4,5,6])
matrix  = [[1,2,3],[4,5,6],[7,8,9]]

np.random.seed(0)
normal = np.random.normal(loc=3, size=1000)
uniform= np.random.uniform(size=1000)
exponential= np.random.exponential(size=1000)
chisq = np.random.chisquare(df=5, size=1000)

normal_pdf = gaussian_kde(normal)
uniform_pdf= gaussian_kde(uniform)
exponential_pdf=gaussian_kde(exponential)
chisq_pdf=gaussian_kde(chisq)

vector = np.arange(0, 3.01, 0.001)

### Plot a simple scatterplot
fig, axes = plt.subplots(2,2)

ax = axes.flatten()

ax[0].plot(x_coord, y_coord, marker = 'o', label = "Some plot")
ax[0].set_title("Basic")
ax[0].set_ylabel("Y-axis")
ax[0].set_xlabel("X-axis")
ax[0].legend()

ax[1].plot(vector, [normal_pdf.evaluate(x) for x in vector], label = 'Normal distribution')
ax[1].plot(vector, [uniform_pdf.evaluate(x) for x in vector], label = 'Uniform Distribution')
ax[1].plot(vector, [exponential_pdf.evaluate(x) for x in vector], label = 'Exponential Distribution')
ax[1].plot(vector, [chisq_pdf.evaluate(x) for x in vector], label = 'Chi-square Distribution')

ax[1].set_title("Basic2")
ax[1].set_ylabel("Y-axis2")
ax[1].set_xlabel("X-axis2")
ax[1].legend(ncol=2) # For 2-column legend
ax[1].legend()

# This is just non-sensical but what the heck.
ax[2].scatter(normal, exponential, alpha = 0.2)
ax[2].scatter(normal, chisq, alpha = 0.2)
ax[2].set_title("Messy")

ax[3].imshow(matrix, interpolation = 'nearest')
ax[3].set_title("Heatmap - unmodified")

fig.set_size_inches((8,8))
plt.tight_layout()
plt.savefig("Example.png") # Default DPI is 150
plt.show()
