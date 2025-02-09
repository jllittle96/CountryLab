# Name: Jalen Little
# Course: CIS 261
# Lab: Country Dictionary Program

# This function displays the program heading and menu options
def display_heading():
    # TODO: Print the program title "The Country List Program"
    print("The Country List Program")
    show_menu()
    
    # TODO: Print the command menu with these options:
def show_menu():
    print("\nCOMMAND MENU")
    print("view - View a country")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program")


# This function creates and returns the initial dictionary of countries
def create_countries():
    # TODO: Create a dictionary with at least 3 countries
    # Use country abbreviations as keys (like "USA") 
    # and full names as values (like "United States")
    countries = {
        "USA": "United States",
        "CAN": "Canada",
        "MEX": "Mexico"
        # Add at least 3 countries here
        # Example format: "USA": "United States"
    }
    return countries


# This function displays all dictionary keys and lets user view a country
def view_country(countries):
    # TODO: Print all dictionary keys (country abbreviations)
    print("\nDictionary Keys:")
    # Write a for...in loop to print all keys
    for key in countries.keys():
        print(key)
    
    key = input("Enter a key: ").upper()
    
        
    # TODO: Ask user to enter a key
    key = input("Enter a key: ").upper()
    
    # TODO: If the key exists in countries, print the country name
    # If not, print "Invalid key."
    # Write an if...else statement here
    if key in countries:
        print(f"The country name is {countries[key]}.")
    else:
        print("Invalid key.")


# This function adds a new country to the dictionary
def add_country(countries):
    # TODO: Ask user for country abbreviation (key)
    key = input("Enter country abbreviation: ").upper()
    
    # TODO: Check if key already exists
    # If it does, print "Key already exists."
    # If it doesn't:
    #   - Ask for country name
    #   - Add to dictionary
    #   - Print confirmation message
    # Write your if...else statement here
    if key in countries:
        print("Key already exists.")
    else:
        country_name = input("Enter country name: ")
        countries[key] = country_name
        print(f"{country_name} has been added.")


# This function deletes a country from the dictionary
def delete_country(countries):
    # TODO: Ask user for country abbreviation (key)
    key = input("Enter country abbreviation: ")
    
    # TODO: If key exists in countries:
    #   - Remove country from dictionary
    #   - Print confirmation message
    # If not, print "Invalid key."
    # Write your if...else statement here
    if key in countries:
        del countries[key]
        print(f"{key} has been deleted.")
    else:
        print("Invalid key.")


# This is the main function that runs the program
def main():
    # Create the dictionary of countries
    countries = create_countries()
    
    # Display the heading and menu
    display_heading()
    
    # Start the program loop
    while True:
        # TODO: Get command from user
        command = input("\nCommand: ")
        
        # TODO: Add if/elif/else statements to handle each command:
        # - "view" calls view_country()
        # - "add" calls add_country()
        # - "del" calls delete_country()
        # - "exit" prints "Bye!" and breaks the loop
        # - anything else prints "Not a valid command. Please try again."
        # Write your if/elif/else structure here
        if command == "view":
            view_country(countries)
        elif command == "add":
            add_country(countries)
        elif command == "del":
            delete_country(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")


# This line tells Python to start the program by calling main()
if __name__ == "__main__":
    main()