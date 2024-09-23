import numpy as np
import matplotlib.pyplot as plt  # Corrected import for matplotlib

Ts = 0.01
f_1=2
f_2=3
t=5
k=int(t/Ts)


Ad = np.array([[0.9516, 0.0959, 0.0484, 0.0016],
                [-0.9430, 0.9037, 0.9430, 0.0484],
                [0.0492, 0.0016, 0.9508, 0.0983],
                [0.9672, 0.0484, -0.9672, 0.9508]])

Bd = np.array([[0.0049, 0.0000],
                [0.0959, 0.0016],
                [0.0000, 0.0050],
                [0.0016, 0.0983]])

T = np.arange(0, t, Ts)  

u1 = np.sin(f_1 * T)  
u2 = np.sin(f_2 * T)  

U = np.vstack((u1, u2))

X = np.zeros((4, 1))
Xk = []  

# Simulate the system
for i in range(k):
    X = np.dot(Ad, X) + np.dot(Bd, U[:, i]) 
    Xk.append(X)

Xk = np.array(Xk)

X_1= Xk[:, 0, 0]
X_2= Xk[:, 1, 0] 
X_3= Xk[:, 2, 0] 
X_4= Xk[:, 3, 0]  

# Plot XK_1 vs time
plt.plot(T[:k], X_1[:k])
plt.xlabel('Time (s)')
plt.ylabel('XK_1')
plt.title('XK_1 vs Time')
plt.grid(True)
plt.show()


plt.plot(T[:k], X_2[:k])
plt.xlabel('Time (s)')
plt.ylabel('XK_1')
plt.title('XK_1 vs Time')
plt.grid(True)
plt.show()

plt.plot(T[:k], X_3[:k])
plt.xlabel('Time (s)')
plt.ylabel('XK_1')
plt.title('XK_1 vs Time')
plt.grid(True)
plt.show()

plt.plot(T[:k], X_4[:k])
plt.xlabel('Time (s)')
plt.ylabel('XK_1')
plt.title('XK_1 vs Time')
plt.grid(True)
plt.show()