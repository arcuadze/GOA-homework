s = " hello world "

# upper() - აბრუნებს სტრინგს დიდი ასოებით
print(s.upper())  # " HELLO WORLD "

# lower() - აბრუნებს სტრინგს პატარა ასოებით
print(s.lower())  # " hello world "

# capitalize() - პირველი ასო იქნება დიდი, დანარჩენი პატარა
print(s.capitalize())  # " hello world " → " hello world "

# strip() - შლის ცარიელ ადგილებს სტრინგის დასაწყისში და ბოლოში
print(s.strip())  # "hello world"

# replace(old, new) - სტრინგში ცვლის სიმბოლოებს
print(s.replace("l", "*"))  # " he**o wor*d "

# ▶️ string არის immutable
# ეს ნიშნავს, რომ სტრინგის შიგთავსს პირდაპირ ვერ შეცვლი, შეგიძლია მხოლოდ ახალი სტრინგი შექმნა მეთოდებით
# მაგ:
new_s = s.upper()  # შევქმენით ახალი სტრინგი
print(s)           # მაინც დარჩა ძველი: " hello world "