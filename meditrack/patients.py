from . import data
from . import utils
from datetime import date


def add_patient(name,dob,gender,blood_group,*allergies,**extra):
    if not utils.is_valid_blood_group(blood_group):
        raise ValueError(f"invalid blood group")
    patient={
            "id": utils.generate_patient_id(),
            "name": utils.clean_name(name),
            "dob": dob,
            "gender": gender,
            "blood_group": blood_group.upper(),
            "allergies": set(allergies),          # set
            "vitals": {                                    # nested dict
                "height_cm": extra.get("height_cm",0.0),
                "weight_kg": extra.get("weight_kg",0.0),
                "systolic": extra.get("systolic",0),
                "diastolic": extra.get("diastolic",0),
                "heart_rate": extra.get("heart rate",0),
                "temperature_c": extra.get("temprature",0),
            },
            "visits": [],
        }
    # data.PATIENTS.append(patient)
    return patient

# print(add_patient("harpal singh", "2003-07-18", "M", "B+", "cactus"))

# #In patients.py', write:
# find_by_id(patient_id) loop through patients, return on the first match,
# else return None.
# search_by_name(keyword) loop through patients, continue when the name
# doesn't contain the keyword (case-insensitive), collect the rest into a list.

def find_by_id(patient_id):
    for patient in data.PATIENTS:
        if patient["patient_id"] == patient_id:
            return patient
    return None


def search_by_name(keyword):
    result = []
    keyword = keyword.lower()
    for patient in data.PATIENTS:
        if keyword not in patient["name"].lower():
            continue
        result.append(patient)

    return result

# Write 'add_visit(patient_id, date fone, reasons) that:
# finds the patient (return 'False if missing)
# defaults 'date' to today's date when not given
# joins the reasons into one string
# appends a (date, reason) **tuple** to that patient's 'visits

def add_visit(patient_id, date=None, reasons=None):
    patient = find_by_id(patient_id)
    if patient is None:
        return False
    if date is None:
        date = str(date.today())
    if reasons is None:
        reasons = []
    reason = ", ".join(reasons) if reason else "general consultation"
    patient["visits"].append((date, reason))
    return True

def all_allergies():
    combined = set()
    for patient in data.PATIENTS:
        combined |= patient["allergies"]
    return combined

print(all_allergies())