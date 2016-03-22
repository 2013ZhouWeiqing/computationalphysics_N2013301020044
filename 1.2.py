x = []
end_time = int(raw_input('input a number'))
t=[]
dt = 0.05
v = 40
x.append(0)
t.append(0)
for i in range(int(end_time/dt)):
    tmp = x[i] + v*dt
    x.append(tmp)
    t.append(dt*(i+1))
    print x[-1],t[-1]

import matplotlib.pyplot as plt
plt.plot(t,x)
plt.show()
plt.savefig('1.2.jpg')

 
