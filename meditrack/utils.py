import random

id= 1000
# Task: Start a new file meditrack/utils.py. At the top, create a constant VALID_BLOOD_GROUPS as a frozenset of the 8 blood groups (A+ A- B+ B- AB+ AB- O+ O-).
VALID_BLOOD_GROUPS = frozenset(
    {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
)

# Task: In utils.py, write a function clean_name(raw_name) that:
# removes leading/trailing spaces
# collapses multiple spaces between words into one
# capitalises each word (Title Case)
# returns the cleaned string
# clean_name(" john DOE ") must return "John Doe".

def clean_name(raw):
    clean = raw.strip()
    clean = " ".join(clean.split())
    clean = clean.title()
    return clean

# print(clean_name("harpal singh"))
# Task: In utils.py, write is_valid_blood_group(bg) that returns True/False depending on whether bg (after .strip().upper()) is in VALID_BLOOD_GROUPS.

def is_valid_blood_group(bg):
    bg = bg.strip()
    bg = bg.upper()
    if bg in VALID_BLOOD_GROUPS:
        return True
    else:
        return False

# print(is_valid_blood_group("a+"))

# Task: In utils.py:
# import random at the top.
# Create a module-level variable _id_counter = 1000.
# Write generate_patient_id() that uses global _id_counter, increments it by 1, adds a random 4-digit suffix, and returns a string like "PAT-1001-8842".

def generate_patient_id():
    global id
    id += 1
    suffix = random.randint(1000, 9999)
    return f"PAT-{id}-{suffix}"

# print(generate_patient_id())