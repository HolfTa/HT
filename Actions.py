# This is 2. Actions menu

import datetime
import time
import questionary
from Database import DatabaseManager
from Return import Return
from tabulate import tabulate

class Actions:
    def show_menu(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside show_menu function in Actions.py")
        
        """
        Display the Actions submenu to the user and handle their choices.

        This method presents the user with options related to actions on habits.
        It allows the user to add, edit, or delete habits, and also provides
        an option to return to the main menu.
        """
        while True:
            choice = questionary.select(
                r"""
          ___________________________
        / Welcome to the Actions menu.\
        \ What would you like to do?  /
          ---------------------------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/\
                        ||----- |
                        ||     ||
        """,
                choices=[
                    "1. Add Habit",
                    "2. Edit Habit",
                    "3. Delete Habit",
                    "4. Add Date",
                    "6. Edit Start Date",
                    "7. Return to Main Menu"
                ]
            ).ask()

            if choice == "1. Add Habit":
                self.add_habit()
            elif choice == "2. Edit Habit":
                self.edit_habit()
            elif choice == "3. Delete Habit":
                self.delete_habit()
            elif choice == "4. Add Date":
                self.add_date()
            elif choice == "5. Edit Date":
                self.edit_date()
            elif choice == "6. Edit Start Date":
                self.edit_start_date()
            elif choice == "7. Return to Main Menu":
                Return.return_to_main_menu()
                return

    def __init__(self):
        self.db_manager = DatabaseManager("database.db")

    def add_habit(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside add_habit function in Actions.py")
        
        """
        Add a new habit to the database.

        This method prompts the user to input details about a new habit, including its name,
        details, category, and periodicity. It then validates the inputs and adds the habit
        to the database using the DatabaseManager. If the user cancels the operation by typing 
        cancel during any input prompt, the method exits.
        """
        # Add 1 second delay, delete if you please
        print("Adding a new habit...", end='', flush=True)
        time.sleep(1)

        while True:
            try:
                # Get input for name
                name = input("\rEnter the name of the habit (type 'cancel' to exit): ").strip()
                if name.lower() == 'cancel':
                    print("\nAdding Habit cancelled.")
                    # Add a delay before returning to the Actions menu choices, remove if you please
                    print("Returning to Actions menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    return
                
                if not name:
                    raise ValueError("Habit name cannot be empty.")

                # Function to check if input consists of only letters and spaces
                def is_valid_name(input_str):
                    return all(char.isalpha() or char.isspace() for char in input_str)

                # Validate the name input
                if not is_valid_name(name):
                    raise ValueError("Habit name should only contain letters and spaces.")

                # Get input for details
                details = input("Enter details about the habit (type 'cancel' to exit, optional): ").strip()
                if details.lower() == 'cancel':
                    print("\nAdding Habit cancelled.")
                    # Add a delay before returning to the Actions menu choices, remove if you please
                    print("Returning to Actions menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    return

                # Get input for category
                category = input("Enter the category of the habit (type 'cancel' to exit, positive/negative): ").strip().lower()
                if category == 'cancel':
                    print("\nAdding Habit cancelled.")
                    # Add a delay before returning to the Actions menu choices, remove if you please
                    print("Returning to Actions menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    return
                elif category not in ['positive', 'negative']:
                    raise ValueError("Category should be 'positive' or 'negative'.")

                # Get input for periodicity
                periodicity = input("Enter the periodicity of the habit (type 'cancel' to exit, daily/weekly/monthly): ").strip().lower()
                if periodicity == 'cancel':
                    print("\nAdding Habit cancelled.")
                    # Add a delay before returning to the Actions menu choices, remove if you please
                    print("Returning to Actions menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    return
                elif periodicity not in ['daily', 'weekly', 'monthly']:
                    raise ValueError("Periodicity should be 'daily', 'weekly', or 'monthly'.")

                # Call the add_habit method in the DatabaseManager
                habit_id = self.db_manager.add_habit(name, details, category, periodicity)
                if habit_id:
                    print(f"Habit added successfully! Habit ID: {habit_id}")
                    # Add a delay before returning to the Actions menu choices, remove if you please
                    print("Returning to Actions menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    break  # Exit the loop if habit added successfully
                else:
                    print("Failed to add habit. Please try again.")
                    # Add a delay before returning to the Actions menu choices, remove if you please
                    print("Returning to Actions menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")

            except ValueError as ve:
                print(f"Error: {ve}")
                # Add a delay before asking the user to enter the name again, remove if you please
                print("Please try again in 3...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 2...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")

    def edit_habit(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside edit_habit function in Actions.py")
        
        """
        Display a tabulated list of habits for editing.

        This method retrieves all habit basics from the database and displays them in a tabulated format.
        Each habit is represented by its ID, name, details, category, periodicity, and date added.
        """
        while True:
            # Get all habits from the database
            habits = self.db_manager.get_habits_basics()

            # Tabulate habit data for display
            habit_data = []
            for habit in habits:
                habit_data.append([habit[0], habit[1], habit[2], habit[3], habit[4], habit[5]])

            # Display habit data in tabulated format
            print(tabulate(habit_data, headers=["ID", "Name", "Details", "Category", "Periodicity", "Date Added"]))
            
            # Print message below the table
            print("\nAbove you can see your habits.")
            print("Choose the ID of the habit you want to edit.")
            
            # Ask the user for the ID of the habit to edit
            habit_id = input("Enter the ID of the habit (type 'cancel' to exit): ").strip()

            # Check the representation of habit_id for debugging
            print("habit_id:", repr(habit_id))

            # Check if the user wants to cancel
            if habit_id.lower() == 'cancel':
                print("Editing habit cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                break

            # Check if the entered ID exists in the database
            habit_exists = False
            habit = None
            for h in habits:
                if h[0] == int(habit_id):
                    habit_exists = True
                    habit = h
                    break

            # If the entered ID does not exist, prompt the user to try again
            if not habit_exists:
                print("Error: The ID you entered does not exist. Please try again.")
                # Add a delay before asking the user to enter the ID again, remove if you please
                print("Please try again in 3...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 2...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                continue

            # If the entered ID exists, proceed with editing the habit
            print("The provided ID exists in the Database.")
            print(f"You can now edit your {habit[1]} habit.")
            print("If you do not wish to edit something, leave it empty.")

            # Get input for name
            edited_name = input(f"Enter the new name of the habit (current name: {habit[1]}): ").strip()
            if edited_name.lower() == 'cancel':
                print("\nEditing Habit cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return
            # Retain existing name if not provided
            edited_name = edited_name or habit[1]  

            # Validate the name input
            def is_valid_name(input_str):
                return all(char.isalpha() or char.isspace() for char in input_str)

            if edited_name and not is_valid_name(edited_name):
                print("Error: Habit name should only contain letters and spaces.")
                # Add a delay before asking the user to enter the name again, remove if you please
                print("Please try again in 3...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 2...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                continue
            
            # Get input for details
            edited_details = input(f"Enter new details about the habit (current details: {habit[2]}): ").strip()
            if edited_details.lower() == 'cancel':
                print("\nEditing Habit cancelled.")
                # Add a delay before returning to the Actions menu choices ,remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return
            # Retain existing details if not provided
            edited_details = edited_details or habit[2]  

            # Get input for category
            edited_category = input(f"Enter new category of the habit (current category: {habit[3]}): ").strip().lower()
            if edited_category.lower() == 'cancel':
                print("\nEditing Habit cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return
            # Retain existing category if not provided
            edited_category = edited_category or habit[3]  
            if edited_category not in ['positive', 'negative']:
                    print("Error: Category should be 'positive' or 'negative'.")
                    # Add a delay before asking the user to enter the category again, remove if you please
                    print("Please try again in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    continue
                
            # Get input for periodicity
            edited_periodicity = input(f"Enter new periodicity of the habit (current periodicity: {habit[4]}): ").strip().lower()
            if edited_periodicity.lower() == 'cancel':
                print("\nEditing Habit cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return
            edited_periodicity = edited_periodicity or habit[4]  # Retain existing periodicity if not provided
            if edited_periodicity not in ['daily', 'weekly', 'monthly']:
                    print("Error: Periodicity should be 'daily', 'weekly', or 'monthly'.")
                    # Add a delay before asking the user to enter the periodicity again, remove if you please
                    print("Please try again in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    continue

            # Update the habit's details in the database
            if self.db_manager.edit_habit_basics(habit_id, edited_name, edited_details, edited_category, edited_periodicity):
                print("Habit details updated successfully!")
            else:
                print("Failed to update habit details. Please try again.")
                continue
                
            # Display all habits after editing
            self.edit_habit()
                
            # Add a delay before returning to the Actions menu choices, remove if you please
            print("Returning to Actions menu in 3...", end='', flush=True)
            time.sleep(1)
            print("\rReturning to Actions menu in 2...", end='', flush=True)
            time.sleep(1)
            print("\rReturning to Actions menu in 1...", end='', flush=True)
            time.sleep(1)
            print("\r")
            
    def delete_habit(self):
            
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside delete_habit function in Actions.py")
        
        while True:
            # Get all habits from the database
            habits = self.db_manager.get_habits_basics()

            # Tabulate habit data for display
            habit_data = []
            for habit in habits:
                habit_data.append([habit[0], habit[1], habit[2], habit[3], habit[4], habit[5]])

            # Display habit data in tabulated format
            print(tabulate(habit_data, headers=["ID", "Name", "Details", "Category", "Periodicity", "Date Added"]))
            
            # Print message below the table
            print("\nAbove you can see your habits.")
            print("Choose the ID of the habit you want to delete.")
            
            # Ask the user for the ID of the habit to edit
            habit_id = input("Enter the ID of the habit (type 'cancel' to exit): ").strip()

            # Check the representation of habit_id for debugging
            print("habit_id:", repr(habit_id))

            # Check if the user wants to cancel
            if habit_id.lower() == 'cancel':
                print("Deleting habit cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                break

            # Check if the entered ID exists in the database
            habit_exists = False
            habit = None
            for h in habits:
                if h[0] == int(habit_id):
                    habit_exists = True
                    habit = h
                    break

            # If the entered ID does not exist, prompt the user to try again
            if not habit_exists:
                print("Error: The ID you entered does not exist. Please try again.")
                # Add a delay before asking the user to enter the ID again, remove if you please
                print("Please try again in 3...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 2...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                continue

            # If the entered ID exists, proceed with deleting the habit, remove if you please
            print("The provided ID exists in the Database.")
            print("Deleting Habit from Database in 3...", end='', flush=True)
            time.sleep(1)
            print("\rDeleting Habit from Database in 2...", end='', flush=True)
            time.sleep(1)
            print("\rDeleting Habit from Database in 1...", end='', flush=True)
            time.sleep(1)
            print("\r")

            # Delete the habit and associated data from the database
            if self.db_manager.delete_habit_all(int(habit_id)):
                print("Habit and associated data deleted successfully!")
            else:
                print("Failed to delete habit and associated data.")

            # Add a delay before returning to the Actions menu choices, remove if you please
            print("Returning to Actions menu in 3...", end='', flush=True)
            time.sleep(1)
            print("\rReturning to Actions menu in 2...", end='', flush=True)
            time.sleep(1)
            print("\rReturning to Actions menu in 1...", end='', flush=True)
            time.sleep(1)
            print("\r")
            break 
        
    def add_date(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside add_date function in Actions.py")
        
        """
        Add a new check-in date for a habit.

        This method allows the user to select a habit and add a new check-in date for it.
        """
        while True:
            print(
                r"""
      __________________________________________
    / Here you can add date when you successfully\
    \ reinforced your new habit!                 /
      ------------------------------------------
           \   ^__^
            \  (oo)\_______
               (__)\       )\/\
                   ||----- |
                   ||     ||
        """)
            # Get all habits from the database
            habits = self.db_manager.get_habits_basics()
            
            # Tabulate habit data for display
            habit_data = []
            for habit in habits:
                habit_data.append([habit[0], habit[1], habit[2], habit[3], habit[4], habit[5]])

            # Display habit data in tabulated format
            print(tabulate(habit_data, headers=["ID", "Name", "Details", "Category", "Periodicity", "Date Added"]))
            print("Select a habit to add a new date:")
            
            # Ask the user to select a habit
            habit_id = input("Enter the ID of the habit (type 'cancel' to exit): ").strip()

            # Check if the user wants to cancel
            if habit_id.lower() == 'cancel':
                print("Adding Date(s) cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                break

            # Check if the entered ID exists in the database
            habit_exists = False
            habit_name = None
            for h in habits:
                if h[0] == int(habit_id):
                    habit_exists = True
                    habit_name = h[1]
                    break

            # If the entered ID does not exist, prompt the user to try again
            if not habit_exists:
                print("Error: The ID you entered does not exist. Please try again.")
                # Add a delay before asking the user to enter the ID again, remove if you please
                print("Please try again in 3...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 2...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                continue
            
            # If the entered ID exists, proceed with adding a date
            print("The provided ID exists in the Database.")
            print(f"You can now add date(s) to {habit_name} habit.")
            
            while True:
                # Get the check-in date from the user
                check_in_date = input("Enter the check-in date (YYYY-MM-DD): ").strip()

                if not check_in_date:
                    print("Error: You must enter a valid Date")
                    # Add a delay before asking the user to enter the category again, remove if you please
                    print("Please try again in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    continue
                
                # Check if the user wants to cancel
                if check_in_date.lower() == 'cancel':
                    print("Adding Date(s) cancelled.")
                    # Add a delay before returning to the Actions menu choices, remove if you please
                    print("Returning to Actions menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    break
                
                # Validate the date format
                try:
                    datetime.datetime.strptime(check_in_date, '%Y-%m-%d')
                except ValueError:
                    print("Error: Incorrect date format. Please use YYYY-MM-DD.")
                    # Add a delay before asking the user to enter the category again, remove if you please
                    print("Please try again in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    continue
                
                # Add the check-in date to the database
                if self.db_manager.add_check_in(int(habit_id), check_in_date):
                    print("Check-in date added successfully!")

                    # Ask if the user wants to add another date
                    choice = input("Would you like to add another date? (y/n): ").strip().lower()
                    if choice != 'y':
                        # Add a delay before returning to the Actions menu choices, remove if you please
                        print("Returning to Actions menu in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to Actions menu in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to Actions menu in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        return
                    else:
                        break
                else:
                    print("Failed to add check-in date.")
                    break

    def edit_date(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside edit_date function in Actions.py")
        
        """
        Edit previously added dates for habits.

        This method allows the user to select a habit and edit the dates associated with it.
        Users can choose a date to edit, enter a new date, and replace the existing one.
        """
    
        while True:
            print(
                r"""
      __________________________________________
    / Here you can edit the dates you previously \
    \ added.                                     /
      ------------------------------------------
           \   ^__^
            \  (oo)\_______
               (__)\       )\/\
                   ||----- |
                   ||     ||
        """)
            # Get all habits from the database
            habits = self.db_manager.get_habits_basics()
            
            # Tabulate habit data for display
            habit_data = []
            for habit in habits:
                habit_data.append([habit[0], habit[1], habit[2], habit[3], habit[4], habit[5]])

            # Display habit data in tabulated format
            print(tabulate(habit_data, headers=["ID", "Name", "Details", "Category", "Periodicity", "Date Added"]))
            print("Select a habit to add a new date:")
            
            # Ask the user to select a habit
            habit_id = input("Enter the ID of the habit (type 'cancel' to exit): ").strip()

            # Check if the user wants to cancel
            if habit_id.lower() == 'cancel':
                print("Adding Date(s) cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                break

            # Check if the entered ID exists in the database
            habit_exists = False
            habit_name = None
            for h in habits:
                if h[0] == int(habit_id):
                    habit_exists = True
                    habit_name = h[1]
                    break

            # If the entered ID does not exist, prompt the user to try again
            if not habit_exists:
                print("Error: The ID you entered does not exist. Please try again.")
                # Add a delay before asking the user to enter the ID again, remove if you please
                print("Please try again in 3...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 2...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                continue
            
            # If the entered ID exists, proceed with adding a date
            print("The provided ID exists in the Database.")
            print(f"You can now edit your date(s) to {habit_name} habit.")
            
            # Retrieve all dates for the selected habit
            habit_dates = self.db_manager.get_all_dates()
            
            # Display dates for the selected habit
            if habit_dates and int(habit_id) in habit_dates:
                print(f"\nDates for {habit_name} habit:")
                dates = habit_dates[int(habit_id)]['dates']
                print(tabulate(enumerate(dates, start=1), headers=["#", "Date"]))
                
                while True:
                    # Ask the user to select a date to edit
                    date_number = input("Enter the number of the date to edit (type 'cancel' to exit): ").strip()
                    
                    # Check if the user wants to cancel
                    if date_number.lower() == 'cancel':
                        print("Edit Date(s) cancelled.")
                        # Add a delay before returning to the Actions menu choices, remove if you please
                        print("Returning to Actions menu in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to Actions menu in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to Actions menu in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        return
                    
                    # Validate the user input
                    if not date_number.isdigit() or int(date_number) < 1 or int(date_number) > len(dates):
                        print("Error: Please enter a valid date number.")
                        # Add a delay before asking the user to enter the ID again, remove if you please
                        print("Please try again in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rPlease try again in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rPlease try again in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        continue
                    
                    # Get the selected date to edit
                    selected_date = dates[int(date_number) - 1]
                    
                    # Get the new date from the user
                    new_date = input("Enter the new date (YYYY-MM-DD) or 'cancel' to exit: ").strip()
                    
                    # Check if the user wants to cancel
                    if new_date.lower() == 'cancel':
                        print("Edit Date(s) cancelled.")
                        # Add a delay before returning to the Actions menu choices, remove if you please
                        print("Returning to Actions menu in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to Actions menu in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to Actions menu in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        return
                    
                    # Validate the date format
                    try:
                        datetime.datetime.strptime(new_date, '%Y-%m-%d')
                    except ValueError:
                        print("Error: Incorrect date format. Please use YYYY-MM-DD.")
                        # Add a delay before asking the user to enter the ID again, remove if you please
                        print("Please try again in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rPlease try again in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rPlease try again in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        continue
                    
                    # Update the date in the database
                    if self.db_manager.update_check_in_date(int(habit_id), new_date):
                        print("Date updated successfully!")
                        break
                    else:
                        print("Failed to update date.")
                        # Add a delay before asking the user to enter the ID again, remove if you please
                        print("Please try again in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rPlease try again in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rPlease try again in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        continue
                    
                # Ask if the user wants to edit another date
                choice = input("Would you like to edit another date for this habit? (y/n): ").strip().lower()
                if choice != 'y':
                        # Add a delay before returning to the Actions menu choices, remove if you please
                        print("Returning to Actions menu in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to Actions menu in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to Actions menu in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        return
            else:
                print("No dates found for this habit.")
                print("Returning to Actions menu...")
                break
            
    def edit_start_date(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside edit_start_date function in Actions.py")
        
        """
        Edit the start date of a habit.
        """
        
        while True:
            print(
                r"""
          __________________________________________
        / Here you can edit the start date of your  \
        \ previously added habit.                   /
          ------------------------------------------
               \   ^__^
                \  (oo)\_______
                   (__)\       )\/\
                       ||----- |
                       ||     ||
            """)
            
            # Display warning message, remove if you please
            print("WARNING: Editing your start date could mean you are cheating with your habits.")
            print("Cheating yourself will not help through a troubling period with trying to reinforce a habit.")
            print("You may want to reconsider your action!")
            
            # Retrieve all habits from the database
            habits = self.db_manager.get_habits_basics()

            # Display habits in tabulated format
            habit_data = []
            for habit in habits:
                habit_data.append([habit[0], habit[1], habit[2]])

            print(tabulate(habit_data, headers=["ID", "Name", "Start Date"]))

            # Ask the user to select a habit to edit the start date
            habit_id = input("Enter the ID of the habit you want to edit the start date for: ").strip()
            
            # Check if the user wants to cancel
            if habit_id.lower() == 'cancel':
                print("Edit Start Date cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return

            # Check if the entered ID exists in the database
            habit_exists = False
            for habit in habits:
                if habit[0] == int(habit_id):
                    habit_exists = True
                    break

            if not habit_exists:
                print("Error: The ID you entered does not exist.")
                # Add a delay before asking the user to enter the ID again, remove if you please
                print("Please try again in 3...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 2...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return

            # Ask the user to enter the new start date
            new_start_date = input("Enter the new start date for the habit (YYYY-MM-DD): ").strip()
            
            # Check if the user wants to cancel
            if new_start_date.lower() == 'cancel':
                print("Edit Start Date cancelled.")
                # Add a delay before returning to the Actions menu choices, remove if you please
                print("Returning to Actions menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Actions menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return

            # Validate the format of the new start date
            try:
                datetime.datetime.strptime(new_start_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Please enter the date in the format YYYY-MM-DD.")
                # Add a delay before asking the user to enter the ID again, remove if you please
                print("Please try again in 3...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 2...", end='', flush=True)
                time.sleep(1)
                print("\rPlease try again in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return

            # Update the start date of the habit in the database
            self.db_manager.update_habit_start_date(int(habit_id), new_start_date)

            print("Start date updated successfully!")
            
            # Ask the user if they want to edit the start date of another habit
            edit_another = input("Would you like to edit the start date of another habit? (y/n): ").strip().lower()
            if edit_another == 'n':
                # Add a delay before returning to Actions Menu, remove if you please
                print("Returning back to Actions Menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning back to Actions Menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning back to Actions Menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return
            elif edit_another == 'y':
                # Add a delay before returning to Edit Start Date Menu, remove if you please
                print("Returning back to Edit Start Date in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning back to Edit Start Date in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning back to Edit Start Date in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                continue
            else:
                print("Invalid choice. Returning back to Actions Menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning back to Actions Menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning back to Actions Menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return