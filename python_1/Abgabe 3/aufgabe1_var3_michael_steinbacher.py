def retrieve_user_data1(name, ahv_number, age, temperature, heart_rate, blood_pressure):
    return f"""Patient Name: {name}
AHV Number: {ahv_number}
Age: {age} years
Temperature: {temperature} °C
Heart Rate: {heart_rate} bpm
Blood Pressure: {blood_pressure} mmHg"""


name = input("Name of Patient: ")
ahv_number = input("AHV number: ")
age = input("Age: ")
temperature = input("Temperature: ")
heart_rate = input("Heart rate: ")
blood_pressure = input("Blood pressure: ")


# ! testing
# name = "John Doe"
# ahv_number = "1234567890"
# age = "20"
# temperature = "20"
# heart_rate = "100"
# blood_pressure = "100"
# print("________________________________________________________________")

print(retrieve_user_data1(name, ahv_number, age, temperature, heart_rate, blood_pressure))