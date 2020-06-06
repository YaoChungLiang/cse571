clc
clear

syms g l m k1 k2 k3 k4 s
syms y1 y2 y3 y4

eqns = [ -6*g*k1/(13*m*l) == y1*y2*y3*y4, ...
         -6*g*k3/(13*m*l) == -y1*y2*y3-y1*y2*y4-y1*y3*y4-y2*y3*y4, ...
         (6*k2-24*m*g+4*k1*l)/(13*m*l) == y1*y2 + y1*y3 + y1*y4 + y2*y3 + y2*y4 + y3*y4, ...
         (6*k4+4*k3*l)/(13*m*l) == -y1-y2-y3-y4];
S = solve(eqns, [k1, k2, k3, k4])
S.k1
S.k2
S.k3
S.k4           