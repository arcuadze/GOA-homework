def grade_status(score):
    if score >= 90:
        return "შესანიშნავი"
    elif 60 <= score < 90:
        return "დამაკმაყოფილებელი"
    else:
        return "ჩაჭრილია"