def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():  # გადაყავს პატარა ასოებად, რომ A == a
        if char in vowels:
            count += 1
    return count