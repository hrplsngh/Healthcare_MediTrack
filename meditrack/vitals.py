# task create "meditrack/vitals.py" write calculate_bmi(weight_kg,height_cm)
# -convert height in cm-meters
# comute weight/(height_m**2)
# return it rounded to 1 decimal place

def calculate_bmi(weight_kg,height_cm):
    if height_cm<=0 or weight_kg<=0:
        return 0.0
    height_m=height_cm/100
    bmi = weight_kg/(height_m**2)
    return round(bmi,1)

# print(calculate_bmi(90,175))

# In `vitals.py`, add:
#   - `bmi_category(bmi)` → `"Underweight" / "Normal" / "Overweight" / "Obese"`.
#   - `bp_category(systolic, diastolic)` → returns a BP stage string.
#   - `has_fever(temperature_c)` → returns a **bool** (`True` if temp ≥ 38.0).


# bmi_category
# bmi <= -> N/A
# bmi < 18.5 -> Underweight
# bmi < 25 -> Normal
# bmi < 30 -> Overweight
# else Obese

def bmi_category(bmi):
    if bmi <= 18.5:
        return "underweight"
    elif bmi>18.5 and bmi<=25:
        return "normal"
    elif bmi>25 and bmi<=30:
        return "overweight"
    else:
        return "obese"

# print(bmi_category(30))

# bp_category
# systolic <120 and diastolic <80 -> Normal
# systolic <130 and diastolic <80 -> Elevated
# systolic <140 and diastolic <90 -> Hypertesion Stage 1
# otherwise -> Hypertesion Stage 2

def bp_category(systolic, diastolic):
    if systolic <120 and diastolic<80:
        return "normal"
    elif systolic in range(120,141) and diastolic<80:
        return "elevated"
    elif systolic<140 and diastolic in range(80,91):
        return "Hypertesion Stage 1"
    else:
        return "Hypertesion Stage 2"

# print(bp_category(140,97))

# In `vitals.py`, write `risk_score(patient)`:
#   - start `score = 0`
#   - add points for high BMI, high BP stage, abnormal heart rate, and fever
#   - cap the final score at 100 and return it

      # BMI Contribution
      # if bmi >= 30 -> score += 30
      # if bmi >= 25 -> score += 15

      # BP Contribution
      # if stage = Hypertesion Stage 2 -> score += 35
      # if stage = Hypertesion Stage 1 -> score += 20
      # if stage = Elevated -> score += 10

      # Heart Rate Contribution
      # Heart-rate > 100 or Heart-rate < 50 -> score += 15

      # Fever Contribution
      # if patient has fever then  score += 10

      # the value we are areturning from this function is score and should not pass 100

      # return min(score, 100)

def risk_score(patient):
    score=0
    v=patient.get('vitals',{})
    bmi=calculate_bmi(v.get("weight_kg",0),v.get("height_cm",0))
    if bmi>=30:
        score+=30
    elif bmi>=25:
        score+=15

    bp=bp_category(v["systolic"],v["diastolic"])
    if bp == "Hypertesion Stage 2":
        score +=35
    elif bp == "Hypertesion Stage 1":
        score +=20
    elif bp=="elevated":
        score+=10

    heart=v["heart_rate"]
    if heart>100 or heart<50:
        score+=15

    fever = v["temperature_c"]
    if fever > 38:
        score+=10

    return min(score, 100)

def risk_label(score):
    if score<30:
        return "low"
    elif score in range(30,60):
        return "modrate"
    elif score >=60:
        return "high"

if __name__=="__main__":
    test={
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
    s=risk_score(test)
    print(risk_label(s))