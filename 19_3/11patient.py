class Patient:
    def __init__(self,name,age,disease):
        self._info = (name,age,disease)

    def display_info(self):
        name,age,disease = self._info
        print(f'{name} : {age}, diagnosed with {disease}')

    def get_name(self):
        return self._info[0]


class PatientManager:
    def __init__(self):
        self._patient_list = []

    def add_patient(self):
        name = input("Enter patient name")
        age = int(input("Enter patient age"))
        disease = input("Enter patient disease")
        patient = Patient(name,age,disease)
        self._patient_list.append(patient)
        print(f'{name}"s details added!!')

    def show_patients(self):
        if self._patient_list != []:
            for patient in self._patient_list:
                patient.display_info()

        else:
            print(f"No details found !!")

    def search_patient(self,name):
        for index, patient in enumerate(self._patient_list):
            if patient.get_name() == name:
                print("Patient Found!!")
                patient.display_info()
                return index

        print(f"Patient {name} is not in records")
        return -1             

    def count_patients(self):
        return f"The patient count at present is {len(self._patient_list)}"

    def delete_patient(self,name):
        found_at = self.search_patient(name)
        if found_at != -1:
            deleted_patient = self._patient_list.pop(found_at)
            print(f'{deleted_patient.name} is removed')
        
        else:
            print("Not present in records")



if __name__ == "__main__":
    manager = PatientManager()

    p1 = Patient("Karan", 21, "Fever")
    p2 = Patient("Rahul", 25, "Cold")
    p3 = Patient("Simran", 22, "Flu")

    manager._patient_list.append(p1)
    manager._patient_list.append(p2)
    manager._patient_list.append(p3)

    manager.show_patients()
    print(manager.count_patients())


