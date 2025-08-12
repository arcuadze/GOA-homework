text = input("შეიყვანე ტექსტი: ")

# ტექსტის კონვერტაცია პატარა ასოებად
text_lower = text.lower()

# "p"-ის პოზიციის მოძებნა
pos = text_lower.find('p')

print("პატარ-ასოებით ტექსტი:", text_lower)

if pos != -1:
    print(f"'p' სიმბოლო მოიძებნა პოზიციაზე: {pos}")
else:
    print("'p' სიმბოლო ტექსტში არ არის")