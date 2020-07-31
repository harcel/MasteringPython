import numpy as np
npoints = 1000
ndim = 3
# X = np.random.random((npoints, ndim))  # Take from the dumb example to compare in the last line
diff = X.reshape(1000, 1, 3) - X
D = (diff**2).sum(2)
i = np.arange(npoints)
D[i, i] = np.inf
nearest_neighbors = np.argmin(D, 1)

# Check with the dumb, but correct, solution from the example:
(ngbs == nearest_neighbors).all()

# Note: sklearn has a nearest neighbor calculator. It basically does just this.
