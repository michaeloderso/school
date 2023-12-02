import csv
from datetime import datetime


# Exercise 2: Read Patient Data
def read_patient_records(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        newdict = {}
        for row in reader:
            newkey = row.pop("Patient ID")
            newdict.update({f"{newkey}": f"{row}"})
            
    return newdict


# Exercise 3: View Patient Records
def view_patient_records(records):
    for record in records:
        values = eval(records[record]) # eval() weil dict "record" für string gehalten wird
        # Formatiert "Date of Birth" von "** BBY" zu "**"
        values.update({"Date of Birth": f"{datetime.now().year - int((values['Date of Birth']).replace(' BBY', ''))}"})
        print(f"""Name: {values['Name']} (ID: {record})
Birth Year: {values["Date of Birth"]}
Height: {values["Height"]}
Weight: {values["Weight"]}
----------------------------""")


# Exercise 4: Add Patient Record
def add_patient_record(records):
    # Create new ID + Informations with inputs
    ids = []
    for record in records:
        ids.append(record)
    ids.sort()
    new_id = int(ids[-1]) + 1
    # User Inputs
    new_name = input("Name: ")
    new_year = input("Age: ") + " BBY"
    new_height = input("Height (cm): ") + " cm"
    new_weight = input("Weight: ") + " kg"
    data = {"Name": new_name, "Date of Birth": new_year, "Height": new_height, "Weight": new_weight}
    records.update({f"{new_id}": f"{data}"})
    print(records)


# Exercise 5: Update Patient Record
def update_patient_record(records):
        key = input("Please enter Patient ID for updating records: ")
        print("\nWhich record should be updated?")
        print("1. Name")
        print("2. Age")
        print("3. Height")
        print("4. Weight")
        choice = int(input("Enter your choice: "))
        list = ["Null", "Name", "Date of Birth", "Height", "Weight"]
        userinput = input(f"Enter input ({list[choice]}, {choice}): ")
        for record in records:
            if record == key:
                values = eval(records[record]) 
                values.update({f"{list[choice]}": f"{userinput}"})
                print("Record succesfully Updated!")


# Exercise 6: Delete Patient Record
def delete_patient_record(records):
    patient_id = input("Enter the Patient ID for deleting entry: ")
    
    if patient_id in records:
        del records[patient_id]
        print(f"Record for Patient ID {patient_id} has been deleted.")
    else:
        print(f"No record found for Patient ID {patient_id}.")


# General: Writing Data Back to CSV
def write_patient_records(filename, records):
    fieldnames = ["Patient ID", "Name", "Date of Birth", "Weight", "Height"]  
    with open(filename, 'r+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            reformat = {"Patient ID" : record}
            reformat.update(eval(records[record]))
            writer.writerow(reformat)


# Main function with the menu system
def main():
    records = read_patient_records("patient_records.csv")
    while True:
        print("\nPatient Records Management System")
        print("1. Add Patient Record")
        print("2. View Patient Records")
        print("3. Update Patient Record")
        print("4. Delete Patient Record")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '2':
            view_patient_records(records)
        elif choice == '3':
            update_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '4':
            delete_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()