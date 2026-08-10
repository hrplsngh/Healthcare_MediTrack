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
    for patient in patients:
        yield patient

def risk_report_lines(patients):
    for p in patients:
        score = p["risk"]
        label = vitals.risk_label(score)

        yield f"{p['id']:<16} {p['name']:<16} risk={score:>3} {label}"

# write first_high_risk(patients) that get an **iterator** over the
# high-risk list and returns the first item using 'next()', returning 'None'
# if there are none

def first_high_risk(patients):
    high=high_risk_patients(patients)
    it=iter(high)
    try:
        return next(it)
    except StopIteration:
        return None

# in analytics.py write:
# count_department(node)-recursively count every department
# list_department(node)-Recursively returns an **indented** list of names

def count_department(node):
    children=node.get('sub',node.get('department',[]))
    total=0
    for child in children:
        total+=1+count_department(child)
        print(child,total)
    return total

def list_departments(node, depth=0, acc=None):
    if acc is None:
        acc = []
    name = node.get("name", "")
    if name and depth > 0:
        acc.append(("  " * (depth - 1)) + "- " + name)
    for child in node.get("sub", node.get("departments", [])):
        list_departments(child, depth + 1, acc)
    return acc