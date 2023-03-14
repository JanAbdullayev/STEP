class soda:
    adds = {1:"Limon" , 2:"Lime", 3:"Strawberry", 4:"Orange", 5:"Cherry", 6:"Banana", 7:"Blueberry", 8:"Watermelon"}
    print(" 1. Limon \n 2. Lime \n 3. Starwberry \n 4. Orange \n 5. Cherry \n 6. Banana \n 7. Blueberry \n 8. Watermelon \n 9. Standard")
    add_choice = int(input("Choose addition : "))

    if add_choice != 9:
        print("You have soda with", adds.get(add_choice))
    else:
        print("You have standard soda")



