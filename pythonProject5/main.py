import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt


def f(x):
    return np.arccos(np.exp(x)) / x

x = np.linspace(-2, -0.0001, 1000)
y = f(x)

plt.figure(figsize=(8,6))
plt.plot(x, y, label = r'$y = \frac{arccos(e^x)}{x}$')
plt.ylabel('$y$', fontsize=15)
plt.xlabel('$x$', fontsize=15)
plt.grid()
plt.legend(fontsize=20)
plt.show()


norm_loc = [-1, 1]
norm_scale = [0.5, 2]

plt.figure(figsize=(8,6))
plt.title('Графики нормального распределения с различными параметрами')
x = np.linspace(-7.5, 7.5, 100)
norm_rv = sts.norm(loc=0, scale=1)

pdf = norm_rv.pdf(x)
plt.plot(x, pdf, label='loc=0 scale=1')


for loc in norm_loc:
    for scale in norm_scale:
        norm_rv = sts.norm(loc=loc, scale=scale)
        pdf = norm_rv.pdf(x)
        plt.plot(x, pdf, label='loc=%s scale=%s'%(loc, scale))
plt.grid()
plt.legend()
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.show();