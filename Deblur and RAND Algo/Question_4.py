# Question_4.py
# Somesh Herath Bandara (sgherath)
# Taylor Olsen
# Travis Lawrence

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Part (a)
mat_contents = scipy.io.loadmat('deblur.mat')
A = mat_contents.get("A")
bn = mat_contents.get("bn")
xtrue = mat_contents.get("xtrue")

# Part (b)
f, (ax1,ax2) = plt.subplots(1,2)
ax1.imshow(xtrue.reshape(64,64))
ax1.set_title('True image', fontsize = 16)
ax2.imshow(bn.reshape(64,64))
ax2.set_title('Blur + noise image', fontsize = 16)
plt.show()

# Part (c)
xn = np.linalg.solve(A,bn)
plt.figure()
plt.imshow(xn.reshape(64,64))
plt.colorbar()
plt.title('Naive solution', fontsize = 18)
plt.show()

# Part (d)
print("The condition number of the matrix is ",  np.linalg.cond(A))
u,s,vh = np.linalg.svd(A, full_matrices = False)

# Second part is written.

# Part (e)
klst = range(400,3601,400)
err = np.zeros((len(klst),), dtype = 'd')
f, axarray = plt.subplots(3,3, sharex = True, sharey = True, figsize = (12,8))

for i, ax in enumerate(axarray.flatten()):
    k = klst[i]
    uk = u[:,:k]; sk = s[:k]; vhk = vh[:k,:]
    xk = vhk.T @ (np.diag(1/sk) @ (uk.T @ bn))
    err[i] = np.linalg.norm(xk.flatten()-xtrue.flatten())
    ax.imshow( xk.reshape(64,64))
    ax.set_title('k = ' + str(k), fontsize = 20)
plt.show()

# Part (f)
err /= np.linalg.norm(xtrue)
plt.plot(np.array(klst),err, 'k-', linewidth = 2.0)
plt.ylabel('Relative error', fontsize = 16)
plt.xlabel('Truncation index  k', fontsize = 16)
plt.title('Relative error vs k', fontsize = 18)
print("The index with lowest error is k =", klst[np.argmin(err)])
plt.show()

# part (g)
# This part is written.