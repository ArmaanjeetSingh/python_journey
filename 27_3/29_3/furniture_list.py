furnitures_list = ['Chair','Table','Almirah','Cupboard','Sofa','Bed']
available_list = ['Add an item','Remove an item','Show purchase items','Show available items']
purchase_list = []
valid_choices = [str(i+1) for i in range(len(available_list))]

def show_items():
    if not furnitures_list:
        print("Empty")
        return
    for index,val in enumerate(furnitures_list,start=1):
        print(index,'-',val)
    print("*"*40)

def show_purchased():
    if not purchase_list:
        print("Empty")
        return

    for index,item in enumerate(purchase_list,start=1):
        print(index,'-',item)
    print("*"*40)

choice = ''
while True:
            
    for index,val in enumerate(available_list,start=1):
            print(index,'-',val)
    print('0 - Exit')
    choice = input("Enter your choice (0-6) ")
                 

    if choice == '0':
        print("Exit")
        break
    
    elif choice in valid_choices:
        
        if choice == '1':
            show_items()
            print(available_list[int(choice)-1])
            current_choice = int(input("Enter your choice for item to be added "))
            current_choice -= 1
            if 0 <= current_choice <= len(furnitures_list)-1:
                purchase_list.append(furnitures_list[current_choice])
                furnitures_list.remove(furnitures_list[current_choice])
            else:
                print("Invalid choice")


        elif choice == '2':
            print(available_list[int(choice)-1])
            show_purchased()
            current_choice = int(input("Enter your choice for item to be removed "))
            if not purchase_list:
                print('empty list')
            current_choice -= 1
            if 0 <= current_choice <= len(purchase_list)-1:
                removed_item = purchase_list.pop(current_choice)
                furnitures_list.append(removed_item)
                print('Item {} is removed from purchase list and added to furnitures'.format(removed_item))

                
        elif choice == '3':
            print(available_list[int(choice)-1])
            show_purchased()

        elif choice == '4':
            print(available_list[int(choice)-1])
            show_items()

   