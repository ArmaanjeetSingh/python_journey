from data import plants_list

# with open('planting_instructions.txt','w',encoding='utf-8') as output_file:
#     for plant in plants_list:
#         where_to_plant = 'window box' if plant.lifecycle == 'Perennial' else 'garden'
#         if plant.lifecycle == 'Perennial':
#             where_to_plant = 'window'
#         else:
#             where_to_plant = 'garden'
#         print(f'{plant.name} : {where_to_plant}',file=output_file)


def sort_perennials(item)->str:
    if item.lifecycle.casefold() == 'perennial':
        return '1' + item.name
    else:
        return '0' + item.name
plants_list.sort(key=lambda item : '1'+item.name if item.lifecycle.casefold() == 'perennial' else '0'+item.name)
print(plants_list)



with open('planting_instructions.txt','w',encoding='utf-8') as output_file:
    for plant in plants_list:
        where_to_plant,who  = ('window box','me') if plant.lifecycle == 'Perennial' else ('garden','gardener')
        # if plant.lifecycle == 'Perennial':
        #     where_to_plant = 'window'
        #     who = 'me'
        # else:
        #     where_to_plant = 'garden'
        #     who = 'gardener'
        # print(f'{plant.name} : {where_to_plant} by {who}',file=output_file)

# name = input("Please enter your name : ")
# age = int(input("How old are you , {0} ? ".format(name)))
# print(age)

# message = "You are old enough to vote" if age >= 18 else "Please come back in {0} years".format(18-age)
# print(message)