def calculate_bmr(gender, age, weight, height):
    if gender == "Female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return bmr


def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extra Active": 1.9
    }
    return bmr * activity_multipliers[activity_level]


def calculate_macros(tdee):
    protein = (tdee * 0.30) / 4
    carbs = (tdee * 0.40) / 4
    fats = (tdee * 0.30) / 9
    return protein, carbs, fats
