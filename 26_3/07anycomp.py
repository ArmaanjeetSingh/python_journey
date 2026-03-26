from data import people, basic_plants_list, plants_list,plants_dict


if bool (people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipient")


if any([plant.plant_type == 'Grass' for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")



if any(plant.plant_type == 'Grass' for plant in plants_dict.values()):
    print("This dict contains grass")
else:
    print("No grasses in dict")

if any(plants_dict[key].plant_type == 'Cactus' for key in plants_dict):
    print("This dict contains Cactus")

    print("No grasses in dict")
