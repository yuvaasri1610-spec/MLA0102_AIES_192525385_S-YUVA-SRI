% CROP DISEASE ADVISORY EXPERT SYSTEM

% Crop Facts
crop(tomato).
crop(rice).
crop(wheat).

% Symptom Facts
symptom(tomato, yellow_leaves).
symptom(tomato, brown_spots).
symptom(tomato, leaf_curling).

symptom(rice, leaf_spots).
symptom(rice, wilting).

symptom(wheat, white_powder).

% Soil Facts
soil(tomato, high_moisture).
soil(rice, excess_water).
soil(wheat, normal).

% Weather Facts
weather(tomato, high_humidity).
weather(rice, high_humidity).
weather(wheat, high_humidity).

% Production Rules

% Rule 1: Leaf Spot
disease(Crop, leaf_spot) :-
    symptom(Crop, brown_spots),
    weather(Crop, high_humidity).

% Rule 2: Root Rot
disease(Crop, root_rot) :-
    soil(Crop, excess_water),
    symptom(Crop, wilting).

% Rule 3: Powdery Mildew
disease(Crop, powdery_mildew) :-
    symptom(Crop, white_powder),
    weather(Crop, high_humidity).

% Rule 4: Viral Disease
disease(Crop, viral_disease) :-
    symptom(Crop, leaf_curling),
    symptom(Crop, yellow_leaves).

% Advisory Rules

advice(leaf_spot,
       'Remove infected leaves and improve air circulation.').

advice(root_rot,
       'Reduce excess watering and improve soil drainage.').

advice(powdery_mildew,
       'Improve ventilation and reduce excessive humidity.').

advice(viral_disease,
       'Remove infected plants and control disease vectors.').

% Diagnosis
diagnose(Crop, Disease, Advice) :-
    disease(Crop, Disease),
    advice(Disease, Advice).
