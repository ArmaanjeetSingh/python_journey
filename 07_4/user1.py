class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def get_profile(self):
        print(f"Name: {self.name}, Email: {self.email}")

    def get_profile(self):
        return {
            "role":self.role(),
            "name":self.name,
            "email":self.email
        }


class Doctor(User):
    def __init__(self,name,email,specialization):
        super().__init__(name,email)
        self.specialization = specialization

    def role(self):
        return "Doctor"

    def get_profile(self):
        data = super().get_profile()
        data['specialization'] = self.specialization
        return data


class Patient(User):
    def __init__(self,name,email,disease):
        super().__init__(name,email)
        self.disease = disease

    def role(self):
        return "Patient"

    def get_profile(self):
        data = super().get_profile()
        data['disease'] = self.disease
        return data

def get_user_data(users:list):
    result = []
    for user in users:
        result.append(user.get_profile())
    return result

patient1 = Patient("Sumit", "sumit@gmail.com", "cough")
doctor1 = Doctor("Shweta", "sh@gmail.com", "ENT")

users = [patient1, doctor1]

print(get_user_data(users))