from . import vitals
from functools import reduce

#Create meditrack/analytics.py and import vitals:
# from. import vitals. Write thigh_risk_patients(patients, threshold=60)
# using 'filter' a 'lambda that keeps patients whose 'risk_score z threshold.

def high_risk_patients(patients, threshold=60):
    return list(filter(lambda patient: vitals.risk_score(patient) >= threshold,patients))

# In analytics.py', write summarise(patients) that uses map +
# a lambda to turn each patient dict into a small summary dict:
# "{"id", "name", "risk", "label"}`. Return it as a list.\

def summarise(patients):
    return list(map(lambda patient: {
            "id": patient["id"],
            "name": patient["name"],
            "risk": vitals.risk_score(patient),
            "label": vitals.risk_label(vitals.risk_score(patient))
        },
        patients
    ))

#In `analytics.py', add from functools import reduce.
# Write average_age(patients, calculate_age) that:
# uses reduce to *sum* the ages
# returns the average (sum count), rounded to 1 decimal

def average_age(patients,calculate_age):
    if not patients:
        return 0
    ages=list(map(lambda p:calculate_age(p["dob"]), patients))
    total=reduce(lambda a,b:a+b,ages)
    return round(total/(len(ages)),1)

# In analytics.py", write two generators:
# patient_stream(patients) yield's patients one at a time.
# # risk_report_lines(patients) yield's a formatted string per patient
# (id, name, risk, label) -> "{pl'id']:<16) (p['name']:<16) risk=(score:>3) ((vitals.risk_label(score)}

def patient_stream(patients):
    pass

def risk_report_lines():
    pass