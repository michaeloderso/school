categories = ["Patient Name", "AHV Number", "Age", "Temperature", "Heart Rate", "Blood Pressure"]
input_list = []

def retrieve_user_data(category):
    user_data = input("Please input your " + category + ": ")
    if category == "Age":
        suffix = " years"
    elif category == "Temperature":
        suffix = " °C"
    elif category == "Heart Rate":
        suffix = " bpm"
    elif category == "Blood Pressure":
        suffix = " mmHg"
    else:
        suffix = ""
    return category + ": " + user_data + suffix



for category in categories:
    input_list.append(retrieve_user_data(category))

print(input_list)

# Noch nicht fertig