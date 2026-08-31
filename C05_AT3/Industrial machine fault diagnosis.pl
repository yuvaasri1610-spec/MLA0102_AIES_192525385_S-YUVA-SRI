% INDUSTRIAL MACHINE FAULT DIAGNOSIS
% Question 2

% -------- FACTS --------

% Machine M1
abnormal_vibration(m1).
unusual_noise(m1).

% Machine M2
high_temperature(m2).
reduced_speed(m2).

% Machine M3
pressure_variation(m3).
reduced_speed(m3).


% -------- RULES --------

% Rule 1: Bearing Fault
bearing_fault(X) :-
    abnormal_vibration(X),
    unusual_noise(X).

% Rule 2: Motor Overheating
motor_overheating(X) :-
    high_temperature(X),
    reduced_speed(X).

% Rule 3: Pump Fault
pump_fault(X) :-
    pressure_variation(X),
    reduced_speed(X).

% Rule 4: Mechanical Fault
mechanical_fault(X) :-
    abnormal_vibration(X),
    unusual_noise(X).

% Rule 5: Production Performance Problem
performance_problem(X) :-
    reduced_speed(X).


% -------- DIAGNOSIS --------

diagnose(X, bearing_fault) :-
    bearing_fault(X).

diagnose(X, motor_overheating) :-
    motor_overheating(X).

diagnose(X, pump_fault) :-
    pump_fault(X).

diagnose(X, mechanical_fault) :-
    mechanical_fault(X).

diagnose(X, performance_problem) :-
    performance_problem(X).
