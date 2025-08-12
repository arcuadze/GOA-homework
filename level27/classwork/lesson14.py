animals = ["dog", "cat", "bird"]

# შუა ინდექსი: (სიის სიგრძე) // 2 = 3 // 2 = 1
middle_index = len(animals) // 2

animals.insert(middle_index, "fish")

print(animals)