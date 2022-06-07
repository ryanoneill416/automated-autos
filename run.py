"""
Write your code to expect a terminal of 80 characters wide and 24 rows high

The creation of a command-line interface application to assist the day-to-day
operations of a car dealership
"""

import gspread
from google.oauth2.service_account import Credentials
from pyfiglet import Figlet

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
    print('--------------- Created By RyanONeill416 ---------------')
