# def analyze_name(name):
#     if name == "Michael":
#         return "Nice!"
#     else:
#         return "That's a stupid name!"
    
def analyze_temperature_age(temperature, age):

    temperature = int(temperature)
    age = int(age)

    if temperature >= 37 and age >= 18:
        return "You're healthy!"
    elif temperature < 37 and age < 18:
        return "You're too young to be healthy!"
    else:
        return "You're too old to be healthy!"
    
    

def analyze_age_blood_pressure(age, blood_pressure):

    systolic, diastolic = blood_pressure.split("/")
    systolic = int(systolic)
    diastolic = int(diastolic)
    age = int(age)

    def inline_analyze_age_blood_pressure(systolic_min, systolic_max, diastolic_min, diastolic_max):
        if (systolic_min <= systolic <= systolic_max) and (diastolic_min <= diastolic <= diastolic_max):
            return "You're healthy!"
        elif systolic_min > systolic or diastolic_min > diastolic:
            return "Blood pressure too low for Age Group"
        elif systolic_max < systolic or diastolic_max < diastolic:
            return "Elevated blood pressure for Age Group"
    
    if 2 <= age <= 13:
        return inline_analyze_age_blood_pressure(40, 120, 40, 80)
    elif 14 <= age <= 18:
        return inline_analyze_age_blood_pressure(90, 120, 50, 80)
    elif 19 <= age <= 40:
        return inline_analyze_age_blood_pressure(95, 135, 60, 80)
    elif 41 <= age <= 60:
        return inline_analyze_age_blood_pressure(110, 145, 70, 90)

print(analyze_temperature_age(temperature, age))

print(analyze_age_blood_pressure(age, blood_pressure))

# ! testing
name = "John Doe"
ahv_number = "1234567890"
age = "30"
temperature = "38"
heart_rate = "90"
blood_pressure = "130/85"


print("________________________________________________________________")

print(analyze_temperature_age(temperature, age))

print(analyze_age_blood_pressure(age, blood_pressure))