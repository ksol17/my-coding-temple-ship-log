
def add_patient(patients, patient_id, name, age):
    if patient_id not in patients:
        patients[patient_id] = {"name": name, "age": age, "visits": []}
        print(f"Patient '{name}' added with ID: {patient_id}.")
    else:
        print(f"Patient with ID {patient_id} already exists.")

def add_visit(patients, patient_id, date, notes):
    if patient_id in patients:
        patients[patient_id]["visits"].append({"date": date, "notes": notes})
        print(f"Visit on {date} recorded for patient ID: {patient_id}.")
    else:
        print(f"Patient with ID {patient_id} not found.")

def display_patient_record(patients, patient_id):
    if patient_id in patients:
        patient = patients[patient_id]
        print(f"Patient ID: {patient_id}\nName: {patient['name']}\nAge: {patient['age']}\nVisits:")
        for visit in patient["visits"]:
            print(f"  Date: {visit['date']}, Notes: {visit['notes']}") 
    else:
        print(f"Patient with ID {patient_id} not found.")

clinic_patients = {}

add_patient(clinic_patients, "P001", "Alice Smith", 30)
add_visit(clinic_patients, "P001", "2021-10-05", "Routine check-up")
add_visit(clinic_patients, "P001", "2021-11-05", "Follow-up visit")
display_patient_record(clinic_patients, "P001")