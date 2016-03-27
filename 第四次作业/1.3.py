v = []
t = []
a = 9.8
b = 1
dt = 0.05
v.append(0)
t.append(0)
end_time = int(raw_input('input a number:'))
for i in range(int(end_time/dt)):
    tmp = v[i] + (a - b*v[i])*dt
    v.append(tmp)
    t.append(dt*(i+1))
    print v[-1],t[-1]


