required_skills = ['python','github','linux']

candidates = {
    'anna':{'java','linux','github','python','full stack','windows'},
    'bob':{'python','linux','python'},
    'carol':{'linux','javascript','html','python','github'},
    'ekani':{'html','css','github','python','linux'},
    'fenna':{'linux','pascal','java','c','lisp','modula-2','perl','github'}
}
interviewees = set()
for candidate,skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):
        interviewees.add(candidate)
print(interviewees)