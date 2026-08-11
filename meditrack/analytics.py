from . import vitals
from functools import reduce

def high_risk_patients(patients, threshold=60):
    return list(filter(lambda p:vitals.risk_score(p) >= threshold, patients))

def summarise(patients):
    return list (map(lambda p:{
        'id':p['id'],
        'name':p['name'],
        'risk':vitals.risk_score(p),
        'label':vitals.risk_label(vitals.risk_score(p))
    }, patients))

def average_age(patients, calculate_age):
    if not patients:
        return 0
    ages = list(map(lambda p:calculate_age(p['dob']), patients))
    total = reduce(lambda a, b : a + b, ages)
    return round(total/(len(ages)), 1)

def patient_stream(patients):
    for patient in patients:
        yield patient

def risk_report_lines(patients):
    for p in patient_stream(patients):
        score = vitals.risk_score(p)
        yield f"{p['id']:<16} {p['name']:<16} risk={score:>3} ({vitals.risk_label(score)})"

def first_high_risk(patients):
    high = high_risk_patients(patients)
    it = iter(high)
    try:
        return next(it)
    except StopIteration:
        return None


def count_departments(node):
    children = node.get('sub', node.get('departments', []))
    total = 0
    for child in children:
        total += 1 + count_departments(child)
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
