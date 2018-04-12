from scipy.integrate import odeint
import numpy as np 
import matplotlib.pyplot as plt 

def test_u(x,t,u):
    return [x[1],-x[1]+0.2-x[0]+u]

def test(x,t):
    return [x[1],-x[1]+0.2-x[0]]


tx = np.linspace(0,50,1000)
u = 10*np.sin(2*3.1415*tx)
y0 = np.array([10, 10])
sol = odeint(test,y0,tx)

# plt.plot(t,sol)
# plt.show()

i = 0
tp = np.empty([1,1])
y = np.zeros([2,1])
y[:,0] = [10,10]
for a,b in zip(tx,u):
    if i == 1:
        tint = [tp, a]
        sol = odeint(test_u,y[:,-1],tint,args = (b,))
        y  = np.column_stack((y,sol[-1,:]))
    tp = a 
    i = 1


## This may be the best alternative, considering that it is completely numpy based and it supports the size of the vector of time as a reference, initial condition can be freely asigned from 

n_it = len(tx)+1
y = np.zeros([2,n_it])  
y[:,0] = np.array([10,10])
tp = tx[0]
y0 = y[:,0]
i = 1
for t, a in zip(tx,u):
    if t != tp: 
        t_int = [tp, t]            
        y_sol = odeint(test_u,y0,t_int,args=(a,))            
        y[:,i] = y_sol[-1]
        y0 = y_sol[-1]
    i+=1
    tp = t

y = y[:,:-1]

print(y.shape)

plt.plot(tx,y[1,])
plt.plot(tx,y[0,])
plt.show()