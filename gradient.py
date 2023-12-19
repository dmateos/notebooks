import numpy as np

# Create random input and output data
x = 2
y = 32
a = np.random.randn()
b = np.random.randn()

learning_rate = 0.1
for t in range(4):
    y_pred = a + (b*x) + 3
    grad_y_pred = 2.0 * (y_pred - y)

    grad_a = grad_y_pred
    grad_b = grad_y_pred * x 
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b

print(f'Result: y = {a} + ({b}*{x})+3')