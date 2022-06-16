# Automated Auto Dealer

## Data-Centric Frontend Development Milestone Project.

![Responsiveness](./images/automated_autos.webp)

Welcome to Automated Auto Dealer! An inventory management tool for car dealerships to manage incoming inventory and
and outgoing sales.

The command-line application is built to provide ease in data management and editing for any caliber of auto trading
business. With a concise layout with extensive input validation, it provides the user with the means of manipulating 
and changing current stock, analysing recent sales and keeping key information within an easily accessible platform.

My goal is to achieve an industry-standard application with true purpose and efficient functionality for the user
and or business owner.

The application utilises two Google sheets to manipulate and store data. 
[View a published representation of the spreadsheets](https://docs.google.com/spreadsheets/d/e/2PACX-1vQXu3XEV_6LwiIKBBGe7yLibX8Np6Uud8U3TJmXO-_bpWvDfx8slS3pM8W0kmvMhrkH5313yMxmiKO5/pubhtml#)

The application is currently deployed as a mock terminal through heroku and feel free to check it out for yourself :)

## [View the deployed website here!](https://automated-autos.herokuapp.com/)
---

# Table of contents

- [UX](#ux)
    - [Website Owner Business Goals](#website-owner-business-goals)
    - [User Goals](#user-goals)
        - [New User Goals](#new-user-goals)
        - [Returning User Goals](#returning-user-goals)
    - [User Story](#user-story)
    - [Flowchart](#flowchart)
- [Features](#features)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
    - [Functionality Testing](#functionality-testing)
    - [Bugs Encountered During Development](#bugs-encountered-during-development)
    - [Code Validation](#code-validation)
- [Deployment](#deployment)
- [Credits](#credits)

___
# UX

## Website owner business goals

The motive for making this application was to create an application for auto trader/ auto dealership data management.
The application displays all relevant and recent inventory.
The application records newly registered sales, which can be listed in their entirety.
The application allows for data editing and manipulation when needed by the business owner, inventory manager or
sales leader.

## User goals

### New user goals:
- New user is able to navigate through the application menus with ease.
- New user can navigate the menu by arrow keys or by keyboard shortcut.
- New user can understand simply and effectively displayed data when that's what is desired.
- New user can confidently add inventory because of thorough input validation.
- New user can register recent sales/ edit inventory as a result of explicit validation to check for inventory and
confirm changes.

### Returning user goals:
- Returning User can easily navigate the well-defined navigation menus.
- Returning User can view up-to-date data at the end of each day without fault.
- Returning User can monitor business performance by comparing outgoing/ incoming inventory.
- Returning User can edit the current inventory if needed e.g. if a vehicle price needs to be reduced.
- Returning User can register a deposit being taken for a vehicle as well as remove a deposit if required.

## User story

### As a business owner:
* I would like to manage my auto trader business through a single application.
* I want to mitigate strenuous tasks such as accessing, editing and updating multiple spreadsheets.
* I need to remove the need for paper stock management as it leads to error and mishandling of information.
* I want to view current inventory/ past sales when requested.
* I would like to add/ remove deposits taken for vehicle sales, as well as know if there is already an existing
deposit outstanding on the vehicle.

___
# Flowchart

To aid the development process of building the application, I used [Lucid Chart](https://www.lucidchart.com/) to 
visualise the organisational flow. This also helped me organise and demonstrate extensive input validation to 
ensure that key data being sent to both the inventory spreadsheet and sales spreadsheet is completely valid.

![Automated Auto Dealer Flowchart](./images/automated-autos-flow.jpeg)

[Back to Table of contents](#table-of-contents)

___
# Features

## Homepage

The homepage is displayed when the application is initially ran and again when the terminal is cleared if 
the user wishes to exit the program. 
It uses ASCII font to display an application title. As well as this, it is accompanied by a subheading that
describes the purpose of the application as well as a cheeky accreditation for the creator ;)

![Automated Auto Dealer Homepage](./images/automated-autos-home.webp)

## Main menu

The main menu is displayed when the application is initally ran, as well as when the user has completed
any of the applications processes.

It gives the user five options, including four application processes and one exit function.

I used the simple_term_menu python library to display the menu as one in which can be used using arrow keys
as well as the keyboard shortcut number for each option.

![Automated Auto Dealer Menu](./images/automated-autos-menu.webp)

## [1] View inventory

The edit inventory function gives the user three options: view current inventory, view recent sales or back
to the menu.

![Automated Auto Dealer View Data Options](./images/automated-autos-view.jpeg)

When either of the two first options are chosen, the application fetches the data from the Google Sheets and
displays the data in an easily understandable manner.

![Automated Auto Dealer View Data ](./images/automated-autos-view1.jpg)

If the back to menu option is chosen, the menu is then displayed again, the same occurs after the processes
of the first two options is complete.

## [2] Add inventory

The add inventory option presents the user with a series of user inputs to complete, which account for the
necessary car details for recording inventory data which are: registration, make, model and price.

The inputs are passed through extensive input validation to ensure the data is valid e.g. the price has to be 
numeric and the registration must be alphanumeric.

The application also checks whether a vehicle with that registration aready exists in the inventory, hence,
preventing unwanted duplication of data.

If user input is deemed invalid the application will display "Operation Cancelled:" and the reason for such.

![Invalid Input Message Example](./images/automated-autos-add-fail.jpg)

On the other hand, if the user input is valid, the user will be shown a summary of the information they
provided and the vehicle will be added to the inventory Google sheet if the user selects "Yes".

If the user selects no as a result of an error in their inputting of the data, the menu will be displayed 
again.

![Add Inventory Process](./images/automated-autos-add.jpg)

## [3] Register vehicle sale

The register vehicle option requests a user input of a vehicle registration and with this, checks if a 
vehicle with this registration is found in the inventory worksheet.

If no vehicle is found, the user is notified and the menu is displayed again.

![(Sale) Vehicle not found](./images/automated-autos-sale.jpg)

If a vehicle with that registration is found, it is displayed and the user can select to register that
vehicle as sold. Doing so will remove said vehicle from the inventory worksheet and subsequently add it to
the corresponding sales worksheet.

![(Sale) Vehicle with that registration found](./images/automated-autos-sale1.jpg)

## [4] Edit inventory

The edit inventory, like the "Register vehicle sale", also checks for an existing vehicle of the inputted 
registration in order for the process to run successfully.

Upon finding a vehicle in the inventory with the inputted registration, the user can choose to edit the price
of the vehicle, register that a deposit has been paid for the vehicle or to remove an existing deposit.

Before choosing which operation they want to carry out, the application displays the details of the vehicle found 
so the user can ensure they selected the correct vehicle.

![Edit Inventory Menu](./images/automated-autos-edit.jpg)

[1] Edit price:
* The new price for the vehicle will be verified by various input validation measures.
* If new price is a valid value the price of the vehicle will be changed.
* The application will display the new vehicle data for the edited vehicle

![Successful Edit Price](./images/automated-autos-edit-price.jpg)

[2] Add deposit:
* The vehicle selected will be checked for if there is an existing deposit being held by it.
* If a deposit is already held on the vehicle, the user will be notified, the operation will be cancelled and
the menu will be displayed again.
* If no deposit is held on the vehicle, the user is prompted to enter the amount of a deposit taken.
* If deposit value passes input validation e.g. must be at least 500, the deposit will be added and the 
updated vehicle data will be displayed to the user.

![Successful Deposit Added](./images/automated-autos-add-dep.jpg)

[3] Add deposit:
* The vehicle selected will be checked for if there is an existing deposit being held by it.
* If there is no existing deposit for the vehicle, the user will be notified, the operation will be cancelled and
the menu will be displayed again.
* If there is an existing deposit that needs to be removed, the user will be prompted to answer are they sure that
they wish to remove it.
* The deposit is then removed and the updated car details are displayed to the user.

![Successful Deposit Removal](./images/automated-autos-remove-dep.jpg)

[4] Back to menu:
* If this option is selected, the user is brought back to the main menu where they can choose to utilise another 
operation or to quit the application.

## [5] Quit

The quit option simply closes the application for the user and displays both the homepage and the exit page.

It notifies the user that the application has been closed succesfully and thanks them for using 'Automated Auto Dealer'.

![Application Closing Page](./images/automated-autos-quit.jpg)

[Back to Table of contents](#table-of-contents)

___
# Data Model

For this application I made use of the GSpread python library and two Google spreadsheets to hold both the current
inventory and the recent sales of the auto trader/ car dealership.
[View a published representation of the spreadsheets here!](https://docs.google.com/spreadsheets/d/e/2PACX-1vQXu3XEV_6LwiIKBBGe7yLibX8Np6Uud8U3TJmXO-_bpWvDfx8slS3pM8W0kmvMhrkH5313yMxmiKO5/pubhtml#)

The spreadsheet is used to hold data in a confidential manner whilst also aiding the presentation of important information
for viewing as well as future implications of business analysation/ monitoring.

The inventory holds values for registration, make, model, price and an optional value for a deposit. The add inventory 
functions runs the user inputs through input validation before adding them to the selected spreadsheet as a categorised
list.

Similarly, the register vehicle sale function checks for the registration the user enters and if valid, will remove that
vehicle from the inventory spreadsheet and into the sales spreadsheet. The edit function also checks an inputted registration
and allows the user to edit options such as pricing and deposits held.

[Back to Table of contents](#table-of-contents)

___
# Technologies Used

For this application, In utilised the following six imported libraries: -

### ***Gspread:***
  * GSpread is a python library I used to access external google sheets for the purpose of data management and manipulation.

### ***Google auth:***
  * Google auth is used to authorise the program to securely access the data and have the necessary permissions to do so,
  without making the application's data available to the public for anybody to manipulate/edit.

### ***os:***
  * Used in line with a cls/clear command to clear the command line interface when the application is closed by the user.

### ***Pyfiglet:***
  * Pyfiglet is a python library which was used to utilise a funky ASCII font for the application home screen.

### ***Simple_term_menu:***
  * I imported the Simple_term_menu library to implement functional and iterable main menu/ side-menu options so that the user
   could navigate by using both arrow keys as well as by pressing the appropriate keyboard shortcut.

### ***Tabulate:***
  * Tabulate is a python library I used to display the present state of inventory/sales data to the user. It presents the
   data in a more easily understandable way than just printing a list of lists.

[Back to Table of contents](#table-of-contents)

___
# Testing

## Functionality testing:

I extensively tested the entirety of the application by trying to find a way to input unrealistic or false inputs. As a result
of this I have created, what I believe to be, a thorough user input validation system that allows nothing but the necessary
components for completing the requested process for the user/ business user.

This meant that I was testing the code I was writing thoroughly at every small incrementation of the developed product.
This includes ensuring that the user can always cancel operations if they made a mistake and that the application runs in a
conventional and familiar way for new and returning users without exception.

## Bugs Encountered During Development

### Data presentation:
  * Information was being presented to the user in a way that was easy to understand for fellow developers but not new users/
  people that could be solely business owners and employees.
  * This was a mistake made by me and it only came to my attention in the final stages of development.
  * To fix this I used the tabulate library which I used to display all data in an appealing and easily understandable way.

### Inventory duplication:
  * The add_inventory() function was working great regardless of something I overlooked... inventory duplication.
  * The function didn't check if that vehicle already exists in the inventory data so could be easily duplicated which 
  would result in errors with selling and managing stock/ data.
  * To fix this I added functionality that the function will check if the registration of the vehicle already exists and 
  will only continue if it's not present in the data already.

### Deposit checking:
  * Similarly to the inventory duplication bug/error. The application would overwrite an existing deposit if the user
  chose to add a deposit to an inventory item that already has a deposit taken for it.
  * Even though the data presented when the registration is checked would reveal all the vehicle data, including if there
  was a deposit existing, this wasn't sufficient.
  * I amended this bug so that when adding a deposit, the operation is cancelled if an existing deposit is present.

## Code Validation

In order to ensure the code used to produce this CLI application was valid and of good practices, I ran [PEP8 Validator](http://pep8online.com/)
to validate my code.

The code validator returned that there were no errors to be found. See results below:

[PEP8 Validation Results](./images/automated-autos-pep8.jpg)

[Back to Table of contents](#table-of-contents)

___
# Deployment

This project was made using the specialised Code Institute template that presents the CLI in the web browser. As a result of this
my guide to deploying the application are in line with this. The steps are as follows:

1) Fork or clone this github repository.

2) Install the requirements listed in requirements.txt using the terminal command "pip3 install -r requirements.txt".

3) Log-in to [Heroku](https://www.heroku.com) or create an account, then choose the "Create App" option.

4) After appropriately naming your application, you'll be brought to the "Deploy" menu.

5) From here, navigate to the "Settings" tab and go to the "Configer Vars" section.

6) Click the button labelled "Reveal Config Vars" and enter the "key" as port, the "value" as 8000 and click the "add" button.

7) Here so that the deployed application has the permissions to manage and manipulate the spradsheets, add your credentials file as
the "key" and the contents as the "value"

7) Scroll down to the buildpacks section of the settings page and click the button labeled "Add Buildpack", choose "Python," and click "Save Changes".
Repeat this step and add "Node.js". **IMPORTANT** It must be in this order with Python visibly above Node.js for the application to work.

8) Navigate back to the "Deploy" page and select "Github" as the deployment method.

9) From here, connect to your Github account and find the repository your project is.

10) Now you can enable automatic deploys or manual deploys and then when you have decided, your application has been deployed.

[Back to Table of contents](#table-of-contents)




