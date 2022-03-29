import csv

'''
    This first part will open the file in read mode and read the data assuming it is a CSV file. I did this because the
    structure of the data looks like a CSV and doing so made it easier to break the data out. I tried to abstract away 
    all parts of my program so that it could be used with any headless CSV file. This script uses the built in csv
    library.
'''
users_by_household = {}
with open("input_file.txt", "r") as user_data:
    csv_reader = csv.reader(user_data, delimiter=",")
    # After splitting data by comma go through the resulting list and normalize the data
    for row in csv_reader:
        row[0] = row[0].title()
        row[1] = row[1].title()
        row[2] = row[2].lower().strip(".").strip().split(",")
        row[2] = "".join(row[2])
        row[3] = row[3].title()
        row[4] = row[4].title()
        row[5] = int(row[5])

    '''
        See if the occupants address is already part of the user_by_household python dictionary. If not added to the 
        dictionary insert a key that is the occupants address and a value that is a list of their data. If address
        already exist then add user to the list of occupants that belong to that address and the sort by last name then
        first name.
    '''

    if row[2] in users_by_household:
        users_by_household[row[2]].append(row)
        users_by_household[row[2]] = sorted(users_by_household[row[2]],
                                            key=lambda user_value: (user_value[1], user_value[0]))
    else:
        users_by_household[row[2]] = [row]
'''
    This part of the program opens a file called output_data.txt if the file does not exist it will create it. Then
    it will write the street address and the number of occupants that belong to it. Followed by the name, full address, 
    and age of all occupants of that address that are over the age of 18. The with open method auto closes when the
    program is down with the file. It also outputs to the terminal as each household is written to the file. The file is
    opened in the write mode so it will over write the file each time it is ran.
'''
with open("output_data.text", "w") as output_file:
    output_file.write("Household and Occupants\n\n")
    print("Household and Occupants\n\n")
    for household in users_by_household:
        household_data = f"{household}: {len(users_by_household[household])} \n"
        output_file.write(household_data)
        print(household_data)
        output_file.write("Users over the age of 18: \n")
        print("Users over the age of 18: \n")
        for user in users_by_household[household]:
            if user[5] > 18:
                user_output = f"First Name: {user[0]}, Last name: {user[1]}, Address: {user[2]} {user[3]} {user[4]}, " \
                              f"Age: {user[5]} \n "
                output_file.write(
                    f"First Name: {user[0]}, Last name: {user[1]}, Address: {user[2]} {user[3]} {user[4]}, "
                    f"Age: {user[5]} \n")
                print(user_output)
        output_file.write("\n\n")
        print(f"{household}.....done")
