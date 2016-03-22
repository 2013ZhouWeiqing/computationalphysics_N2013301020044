v=[]
t = []
dt= 0.1
g = 9.8
v.append(0)
t.append(0)
end_time = 10
for i in range(int(end_time/dt)):
    tmp = v[i] + g*dt
    v.append(tmp)
    t.append(dt*(i+1))
    print t[-1],v[-1]

import matplotlib.pyplot as plt
plt.plot(t,v)
plt.show()
plt.savefig('1.1.jpg')


