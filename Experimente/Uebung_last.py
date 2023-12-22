
# %%

import numpy as np
import matplotlib.pyplot as plt

m = np.ones((2,5))
v = np.asarray([1,2,3,4,5])

m.dot(v)
m.dot(m.transpose())

r = np.random.uniform(size=(30,30,4))
plt.imshow(r)

# %%