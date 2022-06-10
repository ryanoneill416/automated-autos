"""
Write your code to expect a terminal of 80 characters wide and 24 rows high
Accessing our automated_autos google sheet for data handling and manipulation
Utilising figlet to use ASCI fonts for the application
"""

import gspread
from google.oauth2.service_account import Credentials
from pyfiglet import Figlet
from simple_term_menu import TerminalMenu

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


def display_homepage():
    """
    Displays the homepage of the application
    Provides the user with a header
    Declares the functionality of the application
    Brief accreditation
    """
    fig_font = Figlet(font='slant')
    print(fig_font.renderText('Automated\nAuto Dealer\n'))
    print('------ Inventory Management Tool For Auto Traders ------')
    print('--------------- Created By RyanONeill416 ---------------\n\n')


def display_menu():
    """
    Displays the user selection menu
    Provides the user with clear declarations for available functionality
    Displayed continuously until the user selects to quit
    Displays secondary user selection menus to confirm data
    that will be added to spreadsheet
    """
    main_menu = ["(1) ADD INVENTORY", "(2) REGISTER INVENTORY SALE",
                 "(3) EDIT INVENTORY", "(4) QUIT"]

    menu_loop = True
    while menu_loop:

        print('              ________ MAIN MENU ________\n')
        selected_main_menu = main_menu[TerminalMenu(main_menu).show()]

        if selected_main_menu == "(1) ADD INVENTORY":
            print(f"You selected {selected_main_menu}\n")
            add_inventory()
        elif selected_main_menu == "(2) REGISTER INVENTORY SALE":
            print(f"You selected {selected_main_menu}\n")
            add_sale()
        elif selected_main_menu == "(3) EDIT INVENTORY":
            print(f"You selected {selected_main_menu}\n")
        elif selected_main_menu == "(4) QUIT":
            menu_loop = False


def add_inventory():
    """
    Adds a new vehicle to the inventory list for the dealership
    Ensures data input from the user is valid
    """
    new_inventory = []
    print("Enter the following data to add a vehicle to your inventory.\n")

    def add_registration():
        add_reg = input("[1] Enter vehicle registration:\n\n")

        if len(add_reg) < 4:
            print("\nOperation cancelled:")
            print("Value must be 4 or more characters to be valid.\n\n")
        elif (add_reg.isalpha() is True) or (add_reg.isnumeric() is True):
            print("\nOperation cancelled:")
            print("Value must be alphanumeric to be valid.\n\n")
        elif add_reg.isalnum() is False:
            print("\nOperation cancelled:")
            print("Value must be alphanumeric to be valid.\n\n")
        else:
            add_reg = add_reg.upper()
            new_inventory.append(add_reg)
            print(new_inventory)
            add_car_make()

    def add_car_make():
        add_make = input("\n[2] Enter vehicle make (e.g Volkswagen):\n\n")

        if add_make.isalpha() is False:
            print("\nOperation cancelled:")
            print("Car make value must be alphabetical e.g BMW.\n\n")
        elif len(add_make) < 2:
            print("\nOperation cancelled:")
            print("Car make value must be > 1 character long e.g. KIA\n\n")
        else:
            add_make = add_make.capitalize()
            new_inventory.append(add_make)
            print(new_inventory)
            add_car__model()

    def add_car__model():
        add_model = input("\n[3] Enter vehicle model (e.g Golf):\n\n")

        if add_model.isalnum() is False:
            print("\nOperation cancelled:")
            print("Car model value must be alphanumeric e.g 440i, M3\n\n")
        elif len(add_model) < 2:
            print("\nOperation cancelled:")
            print("Car model value must be > 1 character long e.g M3\n\n")
        else:
            add_model = add_model.capitalize()
            new_inventory.append(add_model)
            print(new_inventory)
            add_car_price()

    def add_car_price():
        add_price = input("\n[4] Enter vehicle sale price in euro:\n\n")
        add_menu = ["(1) YES", "(2) NO"]

        if add_price.isnumeric() is False:
            print("\nOperation cancelled:")
            print("Vehicle price value must be numeric to be valid e.g. 5000.")
        elif len(add_price) < 4:
            print("\nOperation cancelled:")
            print("Value entered is not profitable, must be at least 1000")
        else:
            new_inventory.append(add_price)
            print(f"\nAdd {new_inventory} to current inventory?\n\n")
            selected_add_menu = add_menu[TerminalMenu(add_menu).show()]
            if selected_add_menu == "(1) YES":
                update_worksheet(new_inventory, "inventory")

    add_registration()


def add_sale():
    """
    Adds a vehicle to the sales worksheet
    Removes that same vehicle from the inventory worksheet
    """

    sale_reg = input("\nEnter vehicle registration e.g 12D61460:\n\n").upper()
    check_reg = inventory.find(sale_reg)
    print(check_reg)


def update_worksheet(data, worksheet):
    """
    Retrieves a list of data and a worksheet for the data to be appended to
    Updates the current worksheet with provided data
    """

    print(f"Updating {worksheet} worksheet...")
    worksheet_to_append = SHEET.worksheet(worksheet)
    worksheet_to_append.append_row(data)
    print(f"{worksheet} worksheet updated successfully :)\n\n")


def main():
    """
    Commences the running of the application
    Runs all functions of the program
    """
    display_homepage()
    display_menu()


main()
# check_reg = inventory.find("85D5282")
# print(check_reg)
# print(check_reg.row)
# sales.append_row(inventory.row_values(check_reg.row))
# inventory.delete_rows(check_reg.row)
