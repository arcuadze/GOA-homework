text = input("შეიყვანე ტექსტი: ")

pos = text.find('d')

if pos != -1:
    print(f"'d' სიმბოლო ტექსტში არის პოზიციაზე: {pos}")
else:
    print("'d' სიმბოლო ტექსტში არ მოიძებნა")