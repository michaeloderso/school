# def retrieve_patient_data():
#     patient_name = input("Enter Patient Name: ")
#     ahv_number = input("Enter AHV Number: ")
#     age = input("Enter Age: ")
#     temperature = input("Enter Temperature (in Celsius): ")
#     heart_rate = input("Enter Heart Rate (in bpm): ")
#     blood_pressure = input("Enter Blood Pressure (in mmHg)(Format systolic/diastolic is required: ")

#     print(f"""Patient Name: {patient_name}
# AHV Number: {ahv_number}
# Age: {age} years
# Temperature: {temperature} °C
# Heart Rate: {heart_rate} bpm
# Blood Pressure: {blood_pressure} mmHg""")


# Aufgabe 4.1
def get_patient_data():
    errors_checked = False # Gehört zu keiner Aufgabe, ist einfach nur für bessere Inputs
    while not errors_checked: # Gehört zu keiner Aufgabe, ist einfach nur für bessere Inputs

        patient_name = input("Enter Patient Name: ")
        ahv_number = input("Enter AHV Number: ")
        age = input("Enter Age: ")
        temperature = input("Enter Temperature (in Celsius): ")
        heart_rate = input("Enter Heart Rate (in bpm): ")
        blood_pressure = input("Enter Blood Pressure (in mmHg)(Format systolic/diastolic is required: ")

        errors_checked = error_check(blood_pressure) # Gehört zu keiner Aufgabe, ist einfach nur für bessere Inputs

    return {
    'AHV Number': ahv_number,
    'Patient Name': patient_name,
    'Age': age,
    'Temperature': temperature,
    'Heart Rate': heart_rate,
    'Blood Pressure': blood_pressure
}


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

def analyze_blood_pressure_age(blood_pressure, age):
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

def patient_analysis(patient_data):
    temperature = patient_data['Temperature']
    age = patient_data['Age']
    blood_pressure = patient_data['Blood Pressure']

    temperature_analysis = analyze_temperature_age(temperature, age)
    blood_pressure_analysis = analyze_blood_pressure_age(blood_pressure, age)

    print(f"""Temperature Analysis: {temperature_analysis}
Blood Pressure Analysis: {blood_pressure_analysis}""")
    


# Aufgabe 4.2

def mass_data_entry():
    patient_data = []
    while True:
        patient = get_patient_data()
        patient_data.append(patient)

        another_entry = input("Enter another patient? (yes/no): ")
        if another_entry.lower() != 'yes':
            break

    return patient_data


# Aufgabe 5

def index_patient_data(patient_data):
    indexed_data = {}
    for patient in patient_data:
        ahv_number = patient['AHV Number']
        indexed_data[ahv_number] = patient

    return indexed_data


# Aufgabe 6

def retrieve_and_analyze_patient_data(ahv_number, indexed_data):
    if ahv_number in indexed_data:
        patient_data = indexed_data[ahv_number]
        print("Patient Name:", patient_data['Patient Name'])
        patient_analysis(patient_data)
    else:
        print("Patient data not found for AHV Number:", ahv_number)


# Aufgabe 7

def medical_data_system():
    patient_data_list = mass_data_entry()
    indexed_data = index_patient_data(patient_data_list)

    while True:
        ahv_number_input = input("Enter AHV Number (or type 'quit' to exit): ")
        if ahv_number_input.lower() == 'quit':
            break

        retrieve_and_analyze_patient_data(ahv_number_input, indexed_data)


def error_check(blood_pressure): # Gehört zu keiner Aufgabe, ist einfach nur für bessere Inputs
    systolic_and_diastolic = []
    if "/" in blood_pressure:
        systolic, diastolic = blood_pressure.split("/")
        if systolic and diastolic:
            return True
    else:
        print("There is something wrong with the data you inserted (Blood pressure)")



# finally
medical_data_system()
