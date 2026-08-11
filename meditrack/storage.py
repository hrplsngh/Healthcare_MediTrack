import os                      

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(_PROJECT_DIR, "data")
PATIENTS_FILE = os.path.join(DATA_DIR, "patients.txt")
VISIT_LOG_FILE = os.path.join(DATA_DIR, "patient_visits.txt")

_HEADER = ("id|name|dob|gender|blood_group|allergies|"
           "height_cm|weight_kg|systolic|diastolic|heart_rate|temperature_c")


def _ensure_data_dir():
    """Create the data/ folder if it doesn't exist (Class 18: os)."""
    os.makedirs(DATA_DIR, exist_ok=True)

def save_patients(patients, path=PATIENTS_FILE):
    _ensure_data_dir()
    lines = [_HEADER + "\n"]
    for p in patients:
        v = p["vitals"]
        allergy_csv = ",".join(sorted(p["allergies"]))
        line = "|".join([
            p["id"], p["name"], p["dob"], p["gender"], p["blood_group"],
            allergy_csv,
            str(v["height_cm"]), str(v["weight_kg"]),
            str(v["systolic"]), str(v["diastolic"]),
            str(v["heart_rate"]), str(v["temperature_c"]),
        ]) + "\n"
        lines.append(line)
    with open(path, "w") as f:
        f.writelines(lines)
    return len(patients)

def load_patients(path=PATIENTS_FILE):
    patients = []
    try:
        with open(path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return patients

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) != 12:
            continue
        (pid, name, dob, gender, bg, allergy_csv,
         height, weight, sys_bp, dia_bp, hr, temp) = parts

        allergies = {a for a in allergy_csv.split(",") if a}   # set
        patient = {
            "id": pid, "name": name, "dob": dob,
            "gender": gender, "blood_group": bg,
            "allergies": allergies,
            "vitals": {
                "height_cm": float(height), "weight_kg": float(weight),
                "systolic": int(sys_bp), "diastolic": int(dia_bp),
                "heart_rate": float(hr), "temperature_c": float(temp),
            },
            "visits": [],  
        }
        patients.append(patient)
    return patients

def log_visit(patient_id, name, symptom, path=VISIT_LOG_FILE):
    _ensure_data_dir()
    with open(path, "a") as f:
        f.write(f"{patient_id}, {name}, {symptom}\n")


def read_visit_log(path=VISIT_LOG_FILE):
    log = []
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    log.append(line)
    except FileNotFoundError:
        return log
    return log

def preview_file(path, n_lines=3):
    preview = []
    try:
        with open(path, "r") as f:
            for _ in range(n_lines):
                line = f.readline()
                if not line:
                    break
                preview.append(line.strip())
            position = f.tell()
            f.seek(0)
    except FileNotFoundError:
        return [], 0
    return preview, position