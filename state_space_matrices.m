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

Kf_1=rand(4,4);
Kf_2=rand(4,1);
Kf_3=rand(4,1);