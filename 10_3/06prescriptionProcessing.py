from prescription import patients
trial_patients = [
    "Rahul",
    "Simran",
    "Neha",
    "Aman",
    "Rohit",
    "Priya",
    "Karan",
    "Meera"
]

while  trial_patients:
    patient = trial_patients.pop()
    print(patient,end = " : ")
    prescription = patients[patient]
    print(prescription)