import numpy as np
x = np.array([[2104], [1416], [1534],[852]])
X = np.column_stack((np.ones(len(x)), x))
thetas = np.array([
                   [-40, 200, -150], #theta zeros in order
                   [0.25, 0.1, 0.4] #theta ones in order

])


predictions = np.dot(X, thetas)
predictions
