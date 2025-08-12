text = input("შეიყვანე ტექსტი: ")

positions = []
for i, char in enumerate(text):
    if char == 'd':
        positions.append(i)

if positions:
    print(f"'d' სიმბოლოები მოიძებნა პოზიციებზე: {positions}")
else:
    print("'d' სიმბოლო ტექსტში არ არის")