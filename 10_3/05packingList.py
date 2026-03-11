amlodipine = ("Amlodipine", "Blood pressure")
metformin = ("Metformin", "Type 2 Diabetes")
aspirin = ("Aspirin", "Pain / Blood thinner")
ibuprofen = ("Ibuprofen", "Pain relief")
atorvastatin = ("Atorvastatin", "Cholesterol control")
warfarin = ("Warfarin", "Blood thinner")

drugs = [amlodipine, metformin, aspirin, ibuprofen, atorvastatin, warfarin]

adverse_interactions = [
    {"Metformin", "Amlodipine"},
    {"Aspirin", "Warfarin"},
    {"Ibuprofen", "Warfarin"},
    {"Atorvastatin", "Amlodipine"}
]

patients = {
    "Rahul": {metformin, amlodipine},
    "Simran": {aspirin, warfarin},
    "Aman": {metformin,ibuprofen, warfarin},
    "Neha": {ibuprofen, aspirin}
}


trial_patients = ["Rahul","Simran","Neha","Aman"]

for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(aspirin)
        print(patient,patients[patient])
    else:
        print(f"Patient {patient} is not taking warfarin."
              f"Please remove {patient} from trial")