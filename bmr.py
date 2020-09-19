def bmi(w,h,a,g):
    weight = float(w)
    height = float(h)
    age = int(a)
    gender=str(g)
    if gender=='m':
        bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    bmr = round(bmr)
    
    return str(bmr)+"clories\day"
