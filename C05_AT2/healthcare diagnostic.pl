% ==========================================
% HEALTHCARE DIAGNOSTIC EXPERT SYSTEM
% ==========================================

% ----------- Symptoms -----------

symptom(fever).
symptom(cough).
symptom(body_pain).
symptom(fatigue).
symptom(headache).
symptom(sore_throat).
symptom(runny_nose).
symptom(breathing_difficulty).


% ----------- Diagnostic Rules -----------

diagnosis(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain),
    symptom(fatigue).

diagnosis(common_cold) :-
    symptom(cough),
    symptom(runny_nose),
    symptom(sore_throat).

diagnosis(respiratory_infection) :-
    symptom(fever),
    symptom(cough),
    symptom(breathing_difficulty).

diagnosis(severe_respiratory_condition) :-
    symptom(fever),
    symptom(breathing_difficulty),
    symptom(fatigue).


% ----------- Recommendations -----------

recommendation(flu) :-
    write('Consult a healthcare professional and take adequate rest.').

recommendation(common_cold) :-
    write('Take adequate rest and monitor symptoms.').

recommendation(respiratory_infection) :-
    write('Seek medical evaluation for breathing difficulty.').

recommendation(severe_respiratory_condition) :-
    write('Seek immediate professional medical attention.').


% ----------- Display Diagnosis -----------

show_diagnosis :-
    diagnosis(Disease),
    write('Possible Condition: '),
    write(Disease),
    nl,
    write('Recommendation: '),
    recommendation(Disease),
    nl,
    fail.

show_diagnosis.


% ----------- Explanation -----------

explain(flu) :-
    write('Reason: Fever, cough, body pain and fatigue are present.'), nl.

explain(common_cold) :-
    write('Reason: Cough, runny nose and sore throat are present.'), nl.

explain(respiratory_infection) :-
    write('Reason: Fever, cough and breathing difficulty are present.'), nl.

explain(severe_respiratory_condition) :-
    write('Reason: Fever, breathing difficulty and fatigue are present.'), nl.


% ----------- Complete Expert System -----------

expert_system :-
    diagnosis(Disease),
    write('Possible Condition: '),
    write(Disease),
    nl,
    explain(Disease),
    write('Recommendation: '),
    recommendation(Disease),
    nl,
    nl,
    fail.

expert_system.
