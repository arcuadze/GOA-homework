def first_and_last(s):
    if len(s) == 1:
        return s * 2
    else:
        return s[0] + s[-1]