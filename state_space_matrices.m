% State-Space Matrices
A = [0    1     0    0;
    -k/m1 -b/m1  k/m1 0;
     0    0     0    1;
     k/m2  0   -k/m2 0];

B = [0 0;1/m1 0;0 0;0 1/m2];  % Input applied to first mass

C_1 = eye(4);           % Identity matrix (observing all states)
C_2 =[1 0 0 0];          % observing the first state variable
C_3 =[0 0 1 0];          % observing the third state variable


D_1 = zeros(4, 2);      % No direct feedthrough
D_2 = zeros(1, 2);      % No direct feedthrough
D_3 = zeros(1, 2);      % No direct feedthrough

Q=[0.01 0 0 0;
    0 1 0 0;
    0 0 0.01 0;
    0 0 0 1];
R=1;


Kf_1=lqr(A',C_1',Q,R)';
Kf_2=lqr(A',C_2',Q,R)';
Kf_3=lqr(A',C_3',Q,R)';

