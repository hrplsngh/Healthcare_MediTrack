def calculate_bmi(weight_kg, height_cm):
    if height_cm <= 0 or weight_kg <= 0:
        return 0.0
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi <= 0:
        return "N/A"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
def bp_category(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif systolic < 130 and diastolic < 80:
        return "Elevated"
    elif systolic < 140 or diastolic < 90:
        return "Hypertension Stage 1"
    else:
        return "Hypertension Stage 2"

def has_fever(temperature_c):
    return temperature_c >= 38.0

def risk_score(patient):
    v = patient.get('vitals', {})
    bmi = calculate_bmi(v.get('weight_kg', 0), v.get('height_cm', 0))

    score = 0

    if bmi >= 30:
        score += 30
    elif bmi >= 25:
        score += 15

    stage = bp_category(v["systolic"], v["diastolic"])
    if stage == "Hypertension Stage 2":
        score += 35
    elif stage == "Hypertension Stage 1":
        score += 20
    elif stage == "Elevated":
        score += 10

    if v["heart_rate"] > 100 or v["heart_rate"] < 50:
        score += 15

    # Fever contribution
    if has_fever(v["temperature_c"]):
        score += 10   

    return min((score, 100))

def risk_label(score):
    if score <= 30:
        return "LOW"
    elif score > 30 and score <=60:
        return "MODERATE"
    else:
        return "HIGH"

if __name__ == '__main__':
    patient = {
            "id": "PAT-1001-4821",
            "name": "Aarav Sharma",
            "dob": "1990-05-14",
            "gender": "M",
            "blood_group": "O+",
            "allergies": {"penicillin", "dust"},          # set
            "vitals": {                                    # nested dict
                "height_cm": 175.0,
                "weight_kg": 82.0,
                "systolic": 128,
                "diastolic": 84,
                "heart_rate": 78,
                "temperature_c": 37.0,
            },
            "visits": [                                    # list of tuples
                ("2026-06-10", "Routine checkup"),
                ("2026-07-02", "Fever"),
            ],
        }


    pp=risk_score(patient)
    print(risk_label(pp))