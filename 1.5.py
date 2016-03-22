N = []
n = []
t = []
tau_N = int(raw_input('tau_N:'))
tau_n = int(raw_input('tau_n:'))
dt = 0.05
end_time= 20
N.append(10000)
n.append(10000)
t.append(0)
for i in range(int(end_time/dt)):
    A = N[i] + (n[i]/tau_n - N[i]/tau_N)*dt
    N.append(A)
    B = n[i] + (N[i]/tau_N - n[i]/tau_n)*dt
    n.append(B)
    print t[-1],N[-1],n[-1]

