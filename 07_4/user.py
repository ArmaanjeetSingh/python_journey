class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def get_profile(self):
        print(f"Name: {self.name}, Email: {self.email}")

    def get_user_data(self,users:list)->None:
        for user in users:
            user.get_profile()

class Doctor(User):
    def __init__(self,name,email,specialization):
        super().__init__(name,email)
        self.specialization = specialization

    def role(self):
        return "Doctor"

    def get_profile(self):
        print(f"Role : {self.role()}, Name: {self.name}, Email: {self.email}, Specialization : {self.specialization}")

class Patient(User):
    def __init__(self,name,email,disease):
        super().__init__(name,email)
        self.disease = disease

    def role(self):
        return "Patient"

    def get_profile(self):
        print(f"Role : {self.role()}, Name: {self.name}, Email: {self.email}, Disease : {self.disease}")


if __name__ == '__main__':
    patient1 = Patient("Sumit","sumit@gmail.com","cough")
    doctor1 = Doctor("Shweta","sh@gmail.com","ENT")
    user_list = [patient1,doctor1]
    doctor1.get_user_data(user_list)