
my_list = ["ვაშლი", "ბანანი", "კიტრი", "სტაფილო", "ატამი"]


user_index = int(input("შეიყვანე ინდექსი (რიცხვი): "))


if user_index >= len(my_list):
    print("გურამი error")  
else:
    print("შენი არჩეული ელემენტია:", my_list[user_index])  