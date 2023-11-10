def retrieve_user_data(name, ahv_number, age, temperature, heart_rate, blood_pressure):
    print(f"Patient Name: {name}")
    print(f"AHV Number: {ahv_number}")
    print(f"Age: {age} years")
    print(f"Temperature: {temperature} °C")
    print(f"Heart Rate: {heart_rate} bpm")
    print(f"Blood Pressure: {blood_pressure} mmHg")

name = input("Name of Patient: ")
ahv_number = input("AHV Number of Patient:")
age = input("Age of Patient: ")
temperature = input("Temperature of Patient: ")
heart_rate = input("Heart Rate of Patient: ")
blood_pressure = input("Blood pressure of patient: ")

retrieve_user_data(name, ahv_number, age, temperature, heart_rate, blood_pressure)
