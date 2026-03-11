amlodipine = ("Amlodipine", "Blood pressure")
metformin = ("Metformin", "Type 2 Diabetes")
aspirin = ("Aspirin", "Pain / Blood thinner")
ibuprofen = ("Ibuprofen", "Pain relief")
atorvastatin = ("Atorvastatin", "Cholesterol control")
warfarin = ("Warfarin", "Blood thinner")
lisinopril = ("Lisinopril", "Hypertension")
omeprazole = ("Omeprazole", "Acid reflux")

drugs = [
    amlodipine, metformin, aspirin, ibuprofen,
    atorvastatin, warfarin, lisinopril, omeprazole
]

adverse_interactions = [
    {"Metformin", "Amlodipine"},
    {"Aspirin", "Warfarin"},
    {"Ibuprofen", "Warfarin"},
    {"Atorvastatin", "Amlodipine"},
    {"Lisinopril", "Ibuprofen"},
    {"Omeprazole", "Warfarin"}
]

patients = {
    "Rahul": {metformin, amlodipine},
    "Simran": {aspirin, warfarin},
    "Aman": {metformin, ibuprofen, warfarin},
    "Neha": {ibuprofen, aspirin},
    "Rohit": {atorvastatin, amlodipine},
    "Priya": {lisinopril, ibuprofen},
    "Karan": {omeprazole, warfarin},
    "Meera": {metformin, lisinopril}
}

