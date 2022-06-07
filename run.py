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
    """
    main_menu = ["( 1 ) ADD INVENTORY", "( 2 ) REMOVE INVENTORY", "( 3 ) EDIT INVENTORY", "( 4 ) QUIT"]
    menu_loop = True
    while menu_loop:

        print('              ________ MAIN MENU ________\n')
        selected_option = main_menu[TerminalMenu(main_menu).show()]

        if selected_option == "( 1 ) ADD INVENTORY":
            print(f"You selected {selected_option}\n")
        elif selected_option == "( 2 ) REMOVE INVENTORY":
            print(f"You selected {selected_option}\n")
        elif selected_option == "( 3 ) EDIT INVENTORY":
            print(f"You selected {selected_option}\n")
        elif selected_option == "( 4 ) QUIT":
            menu_loop = False


def main():
    """
    Commences the running of the application
    Runs all functions of the program
    """
    display_homepage()
    display_menu()


main()
