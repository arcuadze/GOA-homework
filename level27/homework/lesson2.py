# ვთქვათ ვისწავლეთ 5 სტრინგის მეთოდი
methods_list = ["upper", "lower", "capitalize", "strip", "replace"]

# მაგალითის სტრინგები:
strings = [" hello world ", "python", "STRING methods", "  code  ", "replace-me"]

# თითოეულ სტრინგზე გამოვიყენოთ ყველა მეთოდი:
for s in strings:
    print("ორიგინალი სტრინგი:", repr(s))  # repr აჩვენებს ცარიელ ადგილებსაც
    print("upper():", s.upper())
    print("lower():", s.lower())
    print("capitalize():", s.capitalize())
    print("strip():", s.strip())
    print("replace('e', '*'):", s.replace('e', '*'))
    print("-" * 30)