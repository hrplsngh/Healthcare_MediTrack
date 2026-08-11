from . import data
from . import utils

def add_patient(name, dob, gender, blood_group, *allergies, **extra):
    if not utils.is_valid_blood_group(blood_group):
        raise ValueError(f"Invalid blood group: {blood_group}")

    patient = {
        "id": utils.generate_patient_id(),
        "name": utils.clean_name(name),
        "dob": dob,
        "gender": gender.upper(),
        "blood_group": blood_group.strip().upper(),
        "allergies": set(allergies),         
        "vitals": {                                   
            "height_cm": extra.get("height_cm", 0.0),
            "weight_kg": extra.get("weight_kg", 0.0),
            "systolic": extra.get("systolic", 120),
            "diastolic": extra.get("diastolic", 80),
            "heart_rate": extra.get("heart_rate", 72),
            "temperature_c": extra.get("temperature_c", 36.6),
        },
        "visits": [],                                     
    }
    data.PATIENTS.append(patient)
    return patient

def find_by_id(patient_id):
    for patient in data.PATIENTS:
        if patient["id"] == patient_id:
            return patient
    return None

def search_by_name(keyword):
    keyword = keyword.lower().strip()
    matches = []
    for patient in data.PATIENTS:
        if keyword not in patient["name"].lower():
            continue
        matches.append(patient)
    return matches   

def add_visit(patient_id, date=None, *reasons):
    patient = find_by_id(patient_id)
    if patient is None:
        return False
    date = date or utils.today_str()   
    reason = ", ".join(reasons) if reasons else "General consultation"   
    patient["visits"].append((date, reason))   
    return True

def all_allergies():
    combined = set()
    for patient in data.PATIENTS:
        combined |= patient["allergies"]
    return combined