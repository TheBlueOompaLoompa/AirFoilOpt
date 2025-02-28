import neuralfoil as nf
import numpy as np
import aerosandbox as asb

import matplotlib as mpl
import matplotlib.pyplot as plt
X = np.linspace(0, 2*np.pi, 100)
Y = np.cos(X)
fig, ax = plt.subplots()
ax.plot(X, Y, color='green')
print(X)
plt.show()

aero = nf.get_aero_from_airfoil(
    airfoil=asb.Airfoil("naca4412"),
    alpha=5, Re=200133,
    model_size='xxxlarge',
    device='cpu'
)

print(aero)

