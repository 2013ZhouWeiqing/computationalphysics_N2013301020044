N = []
t = []
N0 = float(raw_input('N0:'))
a = float(raw_input('a:'))
b = float(raw_input('b:'))
N.append(N0)
t.append(0)
end_time = 10
dt = 0.05
for i in range(int(end_time/dt)):
    A = N[i] + (a*N[i] - b*N[i]**2)*dt
    N.append(A)
    t.append((i+1)*dt)
    print N[-1],t[-1]

