from scipy.integrate import odeint
import numpy as np 
import matplotlib.pyplot as plt 

def test_u(x,t,u):
    return [x[1],-x[1]+0.2-x[0]+u]

def test(x,t):
    return [x[1],-x[1]+0.2-x[0]]


t = np.linspace(0,50,1000)
u = 10*np.sin(2*3.1415*t)
y0 = np.array([10, 10])
sol = odeint(test,y0,t)

# plt.plot(t,sol)
# plt.show()

i = 0
tp = np.empty([1,1])
y = np.zeros([2,1])
y[:,0] = [10,10]
for a,b in zip(t,u):
    if i == 1:
        tint = [tp, a]
        sol = odeint(test_u,y[:,-1],tint,args = (b,))
        y  = np.column_stack((y,sol[-1,:]))
    tp = a 
    i = 1


plt.plot(y.T)
plt.show()