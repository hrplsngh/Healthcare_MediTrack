import random
from datetime import datetime, timedelta

VALID_BLOOD_GROUPS = frozenset(
    {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
)

def clean_name(raw_name):
    return ' '.join(raw_name.strip().split()).title()

def is_valid_blood_group(bg):
    return bg.strip().upper() in VALID_BLOOD_GROUPS

_id_counter = 1000
def generate_patient_id():
    global _id_counter
    _id_counter += 1
    random_suffix = random.randint(1000, 9999)
    return f"PAT-{_id_counter}-{random_suffix}"

def today_str():
    return datetime.now().strftime('%Y-%m-%d')

def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, '%Y-%m-%d')
    today = datetime.now()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

def next_appointment_slots(start_hour=9, count=4, gap_minutes=30):
    """GENERATOR of appointment time strings.

    Uses default parameters. Yields values lazily with `yield`"""
    base = datetime.now().replace(hour=start_hour, minute=0,
                                  second=0, microsecond=0)
    for i in range(count):
        slot = base + timedelta(minutes=gap_minutes * i)
        yield slot.strftime("%I:%M %p")

def clear_screen():
    pass

def divider(title=""):
    line = "=" * 52          
    if title:
        return f"{line}\n  {title.upper()}\n{line}"
    return line

if __name__ == '__main__':
    print("HP")
    print(clean_name("   john   DOE "))
    print(is_valid_blood_group('o-'))
    print(generate_patient_id())
    print(type(today_str()))
    print(calculate_age('2000-08-04'))
    print(clean_name("   john   DOE "))