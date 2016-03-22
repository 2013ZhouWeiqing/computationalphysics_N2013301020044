N = []
n = []
t = []
tau_N = int(raw_input('tau_N:'))
tau_n = int(raw_input('tau_n:'))
dt = 0.05
t.append(0)
N.append(10000)
n.append(10000)
end_time = 20
for i in range(int(end_time/dt)):
    A = N[i] - N[i]/tau_N*dt
    N.append(A)
    B = n[i] + (N[i]/tau_N - n[i]/tau_n)*dt
    n.append(B)
    t.append(dt*(i+1))
    print t[-1],N[-1],n[-1]	
  
  


