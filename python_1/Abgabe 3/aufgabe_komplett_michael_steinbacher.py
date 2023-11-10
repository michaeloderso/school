# Aufgabe 1 (Ohne Modifikation)
# def retrieve_user_data():
#     name = input("Name of Patient: ")
#     ahv_number = input("AHV number: ")
#     age = input("Age: ")
#     temperature = input("Temperature: ")
#     heart_rate = input("Heart rate: ")
#     blood_pressure = input("Blood pressure: (Format: systolic/diastolic is required: ")
#     print(f"""Patient Name: {name}
# AHV Number: {ahv_number}
# Age: {age} years
# Temperature: {temperature} °C
# Heart Rate: {heart_rate} bpm
# Blood Pressure: {blood_pressure} mmHg""")



# Aufgabe 2
def analyze_temperature_age(temperature, age):

    temperature = int(temperature)
    age = int(age)

    if temperature >= 37 and age >= 18:
        return "You're healthy!"
    elif temperature < 37 and age < 18:
        return "You're too young to be healthy!"
    else:
        return "You're too old to be healthy!"
    # todo: überarbeiten!
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


# Aufgabe 3
def patient_analysis():
    return f"""Patient Name: {name}
Temperature Analysis: {analyze_temperature_age(temperature, age)}
Blood Pressure Analysis: {analyze_age_blood_pressure(age, blood_pressure)}"""
# todo: überarbeiten!
# Aufgabe 4
patient_list = []
# Aufgabe 4.1 (Aufgabe 1 mit Modifikation)
def get_patient_data(name, ahv_number, age, temperature, heart_rate, blood_pressure):
    patient_data = {"Name": name, "AHV number": ahv_number, "Age": age, "Temperature": temperature, "Heart rate": heart_rate, "Blood pressure": blood_pressure}
    return patient_data
# Aufgabe 4.2
def mass_data_entry():

    add_another = True
    while add_another == True:

        name = input("Name of Patient: ")
        ahv_number = input("AHV number: ")
        age = input("Age: ")
        temperature = input("Temperature: ")
        heart_rate = input("Heart rate: ")
        blood_pressure = input("Blood pressure: (Format: systolic/diastolic is required: ")

        patient_list.append(get_patient_data(name, ahv_number, age, temperature, heart_rate, blood_pressure))

        print("Enter another person? (yes/no): ")
        if input() == "yes":
            add_another = True
        else:
            add_another = False
            return patient_list
    






# ________________________________________________________________
# ! Change when code is complete
# name = "John Doe" # variable for testing
# ahv_number = "1234567890" # variable for testing
# age = "30" # variable for testing
# temperature = "38" # variable for testing
# heart_rate = "90" # variable for testing
# blood_pressure = "130/85" # variable for testing

mass_data_entry()

print(patient_list)