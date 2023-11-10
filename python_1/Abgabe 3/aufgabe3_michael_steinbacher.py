def analyze_name(name):
    if name == "Michael":
        return "Nice!"
    else:
        return "That's a stupid name!"
    
def analyze_temperature_age(temperature, age):
    if temperature >= 37 and age >= 18:
        return "You're healthy!"
    elif temperature < 37 and age < 18:
        return "You're too young to be healthy!"
    else:
        return "You're too old to be healthy!"




# def analyze_age_blood_pressure(age, blood_pressure):
#     if age >= 18 and blood_pressure >= 120:
#         return "You're healthy!"
#     elif age < 18 and blood_pressure < 120:
#         return "You're too young to be healthy!"
#     else:
#         return "You're too old to be healthy!"
    

# ! testing
name = "John Doe"
ahv_number = "1234567890"
age = "30"
temperature = "38"
heart_rate = "100"
blood_pressure = "100"
print("________________________________________________________________")



# todo: finish all following
def patient_analysis

result_name = analyze_name(name)
result_temp_age = analyze_temperature_age(int(temperature), int(age))
