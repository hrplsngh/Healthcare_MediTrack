from . import data
from . import utils

def add_patient(name,dob,gender,blood_group,*allergies,**extra):
    if not utils.is_valid_blood_group(blood_group):
        raise ValueError(f"invalid blood group")
    patient={
            "id": utils.generate_patient_id(),
            "name": utils.clean_name(name),
            "dob": "1990-05-14",
            "gender": "M",
            "blood_group": "O+",
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
    data.PATIENTS.append(patient)
    return patient

# print(add_patient("harpal singh", "2003-07-18", "M", "B+", "cactus"))