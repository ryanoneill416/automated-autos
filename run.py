"""
Write your code to expect a terminal of 80 characters wide and 24 rows high
Accessing our automated_autos google sheet for data handling and manipulation
Utilising figlet to use ASCI fonts for the application
"""
from os import system, name
import gspread
from google.oauth2.service_account import Credentials
from pyfiglet import Figlet
from simple_term_menu import TerminalMenu
from tabulate import tabulate
from colorama import Style, Fore


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('automated_autos')

inventory = SHEET.worksheet('inventory')
sales = SHEET.worksheet('sales')
add_menu = ["[1] YES", "[2] NO"]


def display_homepage():
    """
    Displays the homepage of the application
    Provides the user with a header
    Declares the functionality of the application
    Brief accreditation
    """
    fig_font = Figlet(font='slant')
    print(Fore.CYAN + (fig_font.renderText('Automated\nAuto Dealer\n')))
    print('------ Inventory Management Tool For Auto Traders -------')
    print('--------------- Created By RyanONeill416 ----------------\n'
          + Style.RESET_ALL)


def display_menu():
    """
    Displays the user selection menu
    Provides the user with clear declarations for available functionality
    Displayed continuously until the user selects to quit
    Displays secondary user selection menus to confirm data
    that will be added to spreadsheet
    """
    main_menu = ["[1] VIEW INVENTORY/ RECENT SALES", "[2] ADD INVENTORY",
                 "[3] REGISTER VEHICLE SALE", "[4] EDIT INVENTORY", "[5] QUIT"]
    view_menu = ["[1] VIEW CURRENT INVENTORY", "[2] VIEW RECENT SALES",
                 "[3] BACK TO MENU"]
    menu_loop = True
    while menu_loop:

        print(Fore.CYAN + ('\n              ________ MAIN MENU ________\n')
              + Style.RESET_ALL)
        selected_main_menu = main_menu[TerminalMenu(main_menu).show()]

        if selected_main_menu == "[1] VIEW INVENTORY/ RECENT SALES":
            print(f"You selected {selected_main_menu}\n")
            selected_view_menu = view_menu[TerminalMenu(view_menu).show()]
            if selected_view_menu == "[1] VIEW CURRENT INVENTORY":
                print(tabulate(inventory.get_all_values(), headers="firstrow"))
            elif selected_view_menu == "[2] VIEW RECENT SALES":
                print(tabulate(sales.get_all_values(), headers="firstrow"))
        elif selected_main_menu == "[2] ADD INVENTORY":
            print(f"You selected {selected_main_menu}\n")
            add_inventory()
        elif selected_main_menu == "[3] REGISTER VEHICLE SALE":
            print(f"You selected {selected_main_menu}\n")
            add_sale()
        elif selected_main_menu == "[4] EDIT INVENTORY":
            print(f"You selected {selected_main_menu}\n")
            edit_inventory()
        elif selected_main_menu == "[5] QUIT":
            menu_loop = False
            end_application()


def add_inventory():
    """
    Allows user to enter vehicle data for new inventory acquired
    Adds a new vehicle to the inventory list for the dealership
    Ensures data input from the user is valid
    User can exit the process by entering Q or a single character
    """
    new_inventory = []
    print("Enter the following data to add a vehicle to your inventory.")
    print("Enter Q to go back to the main menu.\n")

    def add_registration():
        """
        Retrieves the registration number of new inventory from user
        Validates the information before appending to empty list
        """
        add_reg = input("[1] Enter vehicle registration:\n\n").upper()
        check_reg = inventory.find(add_reg)

        if check_reg is not None:
            print(Fore.RED + "\nOperation cancelled:")
            print("This vehicle is already listed in your inventory.")
        elif len(add_reg) == 1:
            print(Fore.RED + "\nOperation cancelled.")
        elif len(add_reg) < 4:
            print(Fore.RED + "\nOperation cancelled:")
            print("Value must be 4 or more characters to be valid.")
        elif (add_reg.isalpha() is True) or (add_reg.isnumeric() is True):
            print(Fore.RED + "\nOperation cancelled:")
            print("Value must be alphanumeric to be valid.")
        elif add_reg.isalnum() is False:
            print(Fore.RED + "\nOperation cancelled:")
            print("Value must be alphanumeric to be valid.")
        else:
            new_inventory.append(add_reg)
            add_car_make()

    def add_car_make():
        """
        Retrieves the car make of new inventory from user
        Validates the information before appending to empty list
        User can exit process by entering Q or a single character
        """
        add_make = input("\n[2] Enter vehicle make (e.g Volkswagen):\n\n")

        if len(add_make) == 1:
            print(Fore.RED + "\nOperation cancelled.")
        elif add_make.isalpha() is False:
            print(Fore.RED + "\nOperation cancelled:")
            print("Car make value must be alphabetical e.g BMW.")
        elif len(add_make) < 2:
            print(Fore.RED + "\nOperation cancelled:")
            print("Car make value must be > 1 character long e.g. KIA.")
        else:
            add_make = add_make.capitalize()
            new_inventory.append(add_make)
            add_car__model()

    def add_car__model():
        """
        Retrieves the model of new inventory from user
        Validates the information before appending to empty list
        User can exit process by entering Q or a single character
        """
        add_model = input("\n[3] Enter vehicle model (e.g Golf):\n\n")

        if len(add_model) == 1:
            print(Fore.RED + "\nOperation cancelled.")
        elif add_model.isalnum() is False:
            print(Fore.RED + "\nOperation cancelled:")
            print("Car model value must be alphanumeric e.g 440i, M3.")
        else:
            add_model = add_model.capitalize()
            new_inventory.append(add_model)
            add_car_price()

    def add_car_price():
        """
        Retrieves starting sale price of new inventory from user
        Validates the information before appending to empty list
        Presents total inputted data as a list and prompts for confirmation
        If user is happy with data, the vehicle is added to inventory
        User can exit process by entering Q or a single character
        """
        add_price = input("\n[4] Enter vehicle sale price in euro:\n\n")

        if len(add_price) == 1:
            print(Fore.RED + "\nOperation cancelled.")
        elif add_price.isnumeric() is False:
            print(Fore.RED + "\nOperation cancelled:")
            print("Vehicle price value must be numeric to be valid e.g. 5000.")
        elif len(add_price) < 4:
            print(Fore.RED + "\nOperation cancelled:")
            print("Value entered is not profitable, must be at least 1000.")
        else:
            new_inventory.append(add_price)
            print("\nAdd this vehicle to current inventory?\n")
            print(tabulate([["Car reg.:", "Make:", "Model:", "Price(€):"],
                            new_inventory], headers="firstrow"))
            print("")
            selected_add_menu = add_menu[TerminalMenu(add_menu).show()]
            if selected_add_menu == "[1] YES":
                update_worksheet(new_inventory, "inventory")

    add_registration()


def add_sale():
    """
    Searches for a vehicle in inventory by checking registration
    If no vehicle with selected reg. is found, user is notified of that
    Allows user to verify if they want to mark the found vehicle as sold
    Adds a vehicle to the sales worksheet
    Removes that same vehicle from the inventory worksheet
    User can exit process by entering Q or a single character
    """
    print("Enter the following data to register a vehicle as sold.")
    print("Enter Q to go back to the main menu.\n")
    sale_reg = input("Enter vehicle registration e.g 12D61460:\n\n").upper()
    check_reg = inventory.find(sale_reg)

    if len(sale_reg) == 1:
        print(Fore.RED + "\nOperation cancelled.")
    elif check_reg is None:
        print(Fore.RED + "\nOperation cancelled:")
        print("No vehicle with this registration was found.\n\n")
    else:
        print("\nInventory data found:")
        print("Register the following vehicle as sold?\n")
        print(tabulate([["Car reg.:", "Make:", "Model:", "Price(€):"],
                       inventory.row_values(check_reg.row)],
                       headers="firstrow"))
        print("")
        selected_add_menu = add_menu[TerminalMenu(add_menu).show()]
        if selected_add_menu == "[1] YES":
            update_worksheet(inventory.row_values(check_reg.row), "sales")
            inventory.delete_rows(check_reg.row)


def edit_inventory():
    """
    Searches for a vehicle in inventory by checking registration
    Allows user to verify the correct vehicle was inputted
    Gives user selection of what they wish to edit about the inventory selected
    Each option contains value validation and double-checking before completion
    Deposit can be added, but only if no existing deposit is existing
    Deposit can be moved, however process halted if no deposit exists
    User can exit by entering q or a single character
    """
    print("Enter the following data to register a vehicle as sold.")
    print("Enter Q to go back to the main menu.\n")
    inv_reg = input("Enter vehicle registration e.g. 12A3456:\n\n").upper()
    check_reg = inventory.find(inv_reg)
    edit_menu = ["[1] EDIT PRICE", "[2] DEPOSIT TAKEN",
                 "[3] REMOVE DEPOSIT", "[4] BACK TO MENU"]

    if len(inv_reg) == 1:
        print(Fore.RED + "\nOperation cancelled.")
    elif check_reg is None:
        print(Fore.RED + "\nOperation cancelled:")
        print("No vehicle with this registration was found in inventory.\n")
    else:
        print("\nInventory data found:")
        print("Edit the following vehicle?\n")
        print(tabulate([inventory.row_values(1),
                       inventory.row_values(check_reg.row)],
                       headers="firstrow"))
        print("")
        selected_add_menu = add_menu[TerminalMenu(add_menu).show()]
        if selected_add_menu == "[1] YES":
            selected_edit_menu = edit_menu[TerminalMenu(edit_menu).show()]
            if selected_edit_menu == "[1] EDIT PRICE":
                add_price = input("\nEnter new vehicle sale price:\n\n")

                if add_price.isnumeric() is False:
                    print(Fore.RED + "\nOperation cancelled:")
                    print("Vehicle price value must be numeric to be valid.\n")
                elif len(add_price) < 4:
                    print(Fore.RED + "\nOperation cancelled:")
                    print("Value entered is not profitable,"
                          " must be at least 1000.\n")
                else:
                    print("Editing price...")
                    inventory.update_cell(check_reg.row, 4, add_price)
                    print("Vehicle price has been updated successfully.\n")
                    print(tabulate([inventory.row_values(1),
                                   inventory.row_values(check_reg.row)],
                                   headers="firstrow"))
                    print("")

            elif selected_edit_menu == "[2] DEPOSIT TAKEN":
                if inventory.cell(check_reg.row, 5).value:
                    print(Fore.RED + "\nOperation cancelled:")
                    print("There is an existing deposit on this vehicle\n")
                else:
                    add_deposit = input("\n[4] Enter deposit amount paid:\n\n")
                    if len(add_deposit) == 1:
                        print(Fore.RED + "\nOperation cancelled.")
                    elif add_deposit.isnumeric() is False:
                        print(Fore.RED + "\nOperation cancelled:")
                        print("Value must be numeric to be valid e.g 500.\n")
                    elif int(add_deposit) < 500:
                        print(Fore.RED + "\nOperation cancelled:")
                        print("Value must be at least 500 to be valid.\n")
                    else:
                        print("Adding deposit to selected vehicle...")
                        inventory.update_cell(check_reg.row, 5, add_deposit)
                        print("Deposit amount updated successfully.\n")
                        print(tabulate([inventory.row_values(1),
                                       inventory.row_values(check_reg.row)],
                                       headers="firstrow"))
                        print("")

            elif selected_edit_menu == "[3] REMOVE DEPOSIT":
                if inventory.cell(check_reg.row, 5).value:
                    print("Remove deposit taken from the selected vehicle?\n")
                    selected_add_menu = add_menu[TerminalMenu(add_menu).show()]
                    if selected_add_menu == "[1] YES":
                        print("Removing deposit from selected vehicle...\n")
                        inventory.update_cell(check_reg.row, 5, "")
                        print("Deposit has been removed successfully.\n")
                        print(tabulate([inventory.row_values(1),
                                       inventory.row_values(check_reg.row)],
                                       headers="firstrow"))
                        print("")
                    else:
                        print("")
                else:
                    print(Fore.RED + "\nOperation cancelled:")
                    print("There is no deposit being held on this vehicle\n")


def update_worksheet(data, worksheet):
    """
    Retrieves a list of data and a worksheet for the data to be appended to
    Updates the current worksheet with provided data
    """
    print(f"Updating {worksheet} worksheet...")
    worksheet_to_append = SHEET.worksheet(worksheet)
    worksheet_to_append.append_row(data)
    print(f"The {worksheet} worksheet has been updated successfully.\n")


def main():
    """
    Commences the running of the application
    Runs all functions of the program
    """
    display_homepage()
    display_menu()


def end_application():
    """
    Clears the current displayed terminal
    Displays application homepage with added exit message
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    display_homepage()
    print("\n            Application closed successfully.")
    print("\n      Thank you for using 'Automated Auto Dealer' :)\n\n")
    print(Fore.CYAN +
          ("---------------------------------------------------------")
          + Style.RESET_ALL)


main()
