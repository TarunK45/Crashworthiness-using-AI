% ----------------------------------------------------------------------- %
% Example of use of the funcion MOPSO.m, which performs a Multi-Objective %
% Particle Swarm Optimization (MOPSO), based on Coello2004.               %
% ----------------------------------------------------------------------- %
%   Author:  Victor Martinez Cagigal                                      %
%   Date:    15/03/2017                                                   %
%   E-mail:  vicmarcag (at) gmail (dot) com                              %
% ----------------------------------------------------------------------- %
%   References:                                                           %
%       Coello, C. A. C., Pulido, G. T., & Lechuga, M. S. (2004). Handling%
%       multiple objectives with particle swarm optimization. IEEE Tran-  %
%       sactions on evolutionary computation, 8(3), 256-279.              %
% ----------------------------------------------------------------------- %
clear all; clc;

% Multi-objective function
MultiObjFnc = 'Schaffer';
%MultiObjFnc = 'Kursawe';
%MultiObjFnc = 'Poloni';
%MultiObjFnc = 'Viennet2';
%MultiObjFnc = 'Viennet3';
%MultiObjFnc = 'ZDT1';
%MultiObjFnc = 'ZDT2';
%MultiObjFnc = 'ZDT3';
%MultiObjFnc = 'ZDT6';

switch MultiObjFnc
    case 'Schaffer'         % Schaffer
        f_3=(@ p_3);
        f_2=@ p_2;
        f_1=@ p_1;
       
        MultiObj.fun = @(x) [f_1(x(:,1),x(:,2),x(:,3)),f_2(x(:,1),x(:,2),x(:,3))];
        MultiObj.nVar = 3;
        MultiObj.var_min = [-30, 2,2];
        MultiObj.var_max = [30, 5,5];
        

end

% Parameters
params.Np = 20;        % Population size
params.Nr = 40;        % Repository size
params.maxgen = 200;    % Maximum number of generations
params.W = 0.4;         % Inertia weight
params.C1 = 2;          % Individual confidence factor
params.C2 = 2;          % Swarm confidence factor
params.ngrid = 20;      % Number of grids in each dimension
params.maxvel = 5;      % Maxmium vel in percentage
params.u_mut = 0.5;     % Uniform mutation percentage

% MOPSO
REP = MOPSO(params,MultiObj);

% Display info
display('Repository fitness values are stored in REP.pos_fit');
display('Repository particles positions are store in REP.pos');


    