from scipy.integrate import odeint
from pylab import *

r1 = 20
N1 = 2500
q1 = -0.03
k1 = 0.0001

r2 = 30
N2 = 1000
q2 = -0.015
k2 = 0.0003

def sol(y,t,w0,v0):
    return (r1*y[0]*(1-y[0]/N1)+q1*y[0]*y[1]+k1*y[0],r2*y[1]*(1-y[1]/N2)+q2*y[1]*y[0]+k1*y[1])

t = linspace(0,1,1000)
y = odeint(sol,(1500,800),t,args = (10,10))

figure()

plot(t,y[:,0],label='Local Fishes')
plot(t,y[:,1],label="Asian Fishes")

xlabel('time')
ylabel('number')

legend()
show()
