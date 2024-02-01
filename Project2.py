# # Project 2
# # Name: James Railey Cabrera
# # Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# # 1. Add contact
# # 2. View contacts
# # 3. Delete contact
# # 4. Save contacts to csv file
# # 5. Next Birthday
# # 0. Quit

# # Import the csv module, datetime module
# import csv
# import datetime as dt

# # Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

# print("Welcome to the Contact List Program")

# # There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# # Name,Phone,Email,Birthday
# # The program will be menu driven and will display the menu as shown above. The program will run until the user selects option 0 to quit. The program will be implemented in a file called Project2.py. The program will use the following functions:


# # import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# # Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# # Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# # Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# # Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# # Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# # Hint6: Use the FileNotFoundError exception to catch if the file does not exist.


# # add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# # Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# # Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]


# # view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# # Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# # Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.


# # delete_contact(id) - This function will delete a contact from the dictionary. The function will take one parameter, the name of the contact to delete. The function will return True if the contact was deleted and False if the contact was not deleted. The function will display an error message if the contact does not exist.

# # next_birthday() - This function will display the next birthday. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. The function will display a message if there are no birthdays in the next 30 days. The function will display the next birthday and name if there is a birthday in the next 30 days. Use string formatting to display the next birthday. The next birthday should be sorted by the next birthday. The next birthday should be formatted as mm/dd/yyyy.
# # Hint: We dont care about the year, only the month and day. There are many ways to solve this issue. 1st you could replace all the years with the current year.2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.

# # save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.

# # The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.


# def main():
#     """Add Code here to call the functions and run the program"""
#     pass  # Remove this line when you start writing your code


# if __name__ == "__main__":
#     main()



import csv
import datetime as dt
from tabulate import tabulate
from operator import itemgetter
import re




def import_csv(filename):
    """
    Imports contacts from a CSV file and returns a dictionary where
    the contact names are keys, and the values are dictionaries containing
    phone number, email address, and birthday. Handles file not found errors.
    Skips the first line of the file.
    """
    contacts = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                # Convert birthday to a datetime object
                birthday = dt.datetime.strptime(row[3], '%m/%d/%Y')
                # Create a dictionary for phone number, email, and birthday
                contact_details = {'Phone': row[1], 'Email': row[2], 'Birthday': birthday}
                # Add the contact to the dictionary
                contacts[row[0]] = contact_details
        print(f"Contacts successfully imported from {filename}")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    return contacts


def add_contact(contacts, name, phone, email, birthday):
    """
    Adds a contact to the dictionary. Returns True if the contact was added,
    False if the contact was not added. Displays an error message if the contact already exists
    or if the phone number or email format is invalid.
    """
    while True:
        # Validate name format
        if not re.match(r'^[A-Za-z\s]+$', name):
            print("Invalid name format. Please enter a valid name.")
            name = input("Enter name: ")
        else:
            break  # Break out of the loop if the name is in a valid format

    while True:
        # Validate phone number format
        if not re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
            print("Invalid phone number format. Please use xxx-xxx-xxxx.")
            phone = input("Enter phone: ")
        else:
            break  # Break out of the loop if the phone number is in a valid format

    while True:
        # Validate email format
        if not re.match(r'^\S+@\S+\.\S+$', email):
            print("Invalid email format. Please enter a valid email address.")
            email = input("Enter email: ")
        else:
            break  # Break out of the loop if the email is in a valid format

    # Loop until valid birthday is provided
    while True:
        try:
            # Convert birthday to datetime object
            birthday_date = dt.datetime.strptime(birthday, '%m/%d/%Y')
            break  # Break out of the loop if the conversion is successful
        except ValueError:
            print("Invalid birthday format. Please use mm/dd/yyyy.")

        # Ask for input again
        birthday = input("Enter birthday (mm/dd/yyyy): ")

    # Adjust the birthday for the next year if it has already passed
    today_datetime = dt.datetime.now()
    if today_datetime > birthday_date:
        birthday_date = birthday_date.replace(year=today_datetime.year + 1)

    # Checks if contact exists
    if name in contacts:
        print(f"{name} already exists")
        return False

    # Adds contact to dictionary
    contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday_date}
    print(f"{name} was successfully added")
    return True


def view_contacts(contacts):
    """Display the contacts in a table format using tabulate."""
    if not contacts:
        print("No contacts in the dictionary.")
        return

    # Convert contacts dictionary to a list of dictionaries
    contacts_list = [{'Name': name, **details} for name, details in contacts.items()]
    # Sort contacts by name
    sorted_contacts = sorted(contacts_list, key=itemgetter('Name'))
    # Display the table using tabulate
    table = tabulate(sorted_contacts, headers='keys', tablefmt='fancy_grid')
    print(table)


def delete_contact(contacts, name):
    """
    Deletes a contact from the dictionary. Returns True if the contact was deleted,
    False if the contact was not deleted. Displays an error message if the contact does not exist.
    """
    # Checks if contact exists
    if name not in contacts:
        print(f"{name} does not exist")
        return False
    # Deletes the contact
    del contacts[name]
    print(f"{name} was successfully deleted")
    return True


def next_birthday(contacts):
    """
    Display the next birthday. Displays a message if there are no contacts or
    if there are no birthdays in the next 30 days. Displays the next birthday and name
    if there is a birthday in the next 30 days.
    """
    if not contacts:
        print("No contacts in the dictionary.")
        return

    # Get today's date
    today = dt.datetime.now().date()

    # Find the next birthday within the next 30 days
    next_birthday = None
    for name, details in contacts.items():
        # Ensure the birthday is a datetime object
        birthday = details['Birthday'].replace(year=today.year, month=details['Birthday'].month, day=details['Birthday'].day)

        # Convert today to datetime object for consistent types
        today_datetime = dt.datetime(today.year, today.month, today.day)

        # Calculate the difference in days using timedelta
        days_until_birthday = (birthday - today_datetime).days % 365  # % 365 to handle leap years

        if 0 <= days_until_birthday <= 30:
            if next_birthday is None or birthday < next_birthday[1]['Birthday']:
                next_birthday = (name, details)

    if next_birthday is None:
        print("No birthdays in the next 30 days.")
    else:
        print(f"Next Birthday: {next_birthday[0]}, Date: {next_birthday[1]['Birthday'].strftime('%m/%d/%Y')}")


def save_csv(contacts, filename):
    """Save contacts to a CSV file. Returns True if successful, False otherwise."""
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
            # Write contacts
            for name, details in contacts.items():
                writer.writerow([name, details['Phone'], details['Email'], details['Birthday'].strftime('%m/%d/%Y')])
        print(f"Contacts successfully saved to {filename}")
        return True
    except FileNotFoundError:
        print(f"Error: File not found - {filename}")
        return False
    except PermissionError:
        print(f"Error: Permission denied - {filename}")
        return False
    except Exception as e:
        print(f"Error saving contacts to {filename}: {e}")
        return False


def main():
    # Initialize contacts from the CSV file
    contacts = import_csv("contacts.csv")

    while True:
        print("\nMenu")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete contact")
        print("4. Save contacts to csv file")
        print("5. Next Birthday")
        print("0. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            birthday = input("Enter birthday (mm/dd/yyyy): ")
            add_contact(contacts, name, phone, email, birthday)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)

        elif choice == "4":
            filename = input("Enter filename to save contacts: ")
            save_csv(contacts, filename)

        elif choice == "5":
            next_birthday(contacts)

        elif choice == "0":
            # Save contacts before quitting
            save_csv(contacts, "contacts.csv")
            print("Goodbye!")
            
            # Now you can use the contacts variable for further analysis
            names_starting_with_A = sum(name.startswith('A') for name in contacts)
            print("Number of names starting with A:", names_starting_with_A)

            yahoo_emails = sum(details['Email'].endswith('@yahoo.com') for details in contacts.values())
            print("Number of Yahoo emails:", yahoo_emails)

            org_emails = sum(details['Email'].endswith('.org') for details in contacts.values())
            print("Number of .org emails:", org_emails)

            january_birthdays = sum(details['Birthday'].month == 1 for details in contacts.values())
            print("Number of contacts with a birthday in January:", january_birthdays)

            break  # Exit the loop when user chooses to quit

        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


if __name__ == "__main__":
    main()

