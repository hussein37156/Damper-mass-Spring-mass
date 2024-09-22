%to use in py code
Ad=expm(A*Ts);
Bd = integral(@(tau) expm(A * tau) * B, 0, Ts, 'ArrayValued', true);
