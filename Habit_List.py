# This is 1. View Habit List menu

import time
import questionary
from Database import DatabaseManager
from Return import Return
from tabulate import tabulate

class HabitList:
        
    def show_menu(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside show_menu function in Habit_List.py")
        
        """
        Display the Habit List submenu to the user and handle their choices.
        
        This method presents the user with options related to the habit list.
        It allows the user to view habits and their details and also provides
        an option to return to the main menu.
        """
        
        choice = questionary.select(
                r"""
          ___________________________________
        / Welcome to the View Habit List menu.\
        \ What would you like to do?          /
          -----------------------------------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/\
                        ||----- |
                        ||     ||
        """,
                choices=[
                    "1. View Habits",
                    "2. Return to Main Menu"
                ]
            ).ask()

        if choice == "1. View Habits":
                self.view_habits()
        elif choice == "2. Return to Main Menu":
                Return.return_to_main_menu()
                return
            
    def __init__(self):
        self.db_manager = DatabaseManager("database.db")
            
    def view_habits(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside view_habits function in Habit_List.py")

        while True:
             # Get all habits from the database
            habits = self.db_manager.get_habits_basics()

            # Tabulate habit data for display
            habit_data = []
            for habit in habits:
                habit_data.append([habit[0], habit[1], habit[2], habit[3], habit[4], habit[5]])

            # Display habit data in tabulated format
            print(tabulate(habit_data, headers=["ID", "Name", "Details", "Category", "Periodicity", "Date Added"]))
            
            inspect_habit = input("Do you want to inspect a habit? (y/n): ").strip().lower()

            if inspect_habit == "n":
                # Add a delay before returning to the Main menu choices, remove if you please
                print("Returning to Main menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Main menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to VMain menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                return
            elif inspect_habit == "y":
                habit_id = input("Enter the ID of the habit you want to inspect (type 'cancel' to exit): ").strip()

                if habit_id.lower() == 'cancel':
                    print("Viewing habit list cancelled.")
                    # Add a delay before returning to the View Habits menu choices, remove if you please
                    print("Returning to Actions menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Actions menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    break

                else:
                    # Check if the entered ID exists in the database
                    habit_exists = False
                    for h in habits:
                        if h[0] == int(habit_id):
                            habit_exists = True
                            break

                    if not habit_exists:
                        print("Error: The ID you entered does not exist. Please try again.")
                        print("Please try again in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rPlease try again in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rPlease try again in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        continue

                    # Retrieve all dates for the selected habit
                    habit_dates = self.db_manager.get_all_dates()

                    # Display dates for the selected habit
                    if habit_dates and int(habit_id) in habit_dates:
                        dates = habit_dates[int(habit_id)]['dates']
                        print(f"\nDates for Habit ID {habit_id} - {habit_dates[int(habit_id)]['name']} habit:")
                        print(tabulate(enumerate(dates, start=1), headers=["#", "Date"]))
                        print()

                        while True:
                            return_to_menu = input("Would you like to return to the View Habit List menu? (y/n): ").strip().lower()
                            if return_to_menu == 'y':
                                break
                            elif return_to_menu == 'n':
                                # Add a delay before returning to the Main menu choices, remove if you please
                                print("Returning to Main menu in 3...", end='', flush=True)
                                time.sleep(1)
                                print("\rReturning to Main menu in 2...", end='', flush=True)
                                time.sleep(1)
                                print("\rReturning to Main menu in 1...", end='', flush=True)
                                time.sleep(1)
                                print("\r")
                                return
                            else:
                                print("Invalid choice. Please enter 'y' or 'n'.")
                    else:
                        print("No dates found for this habit.")
                        # Add a delay before returning to the View Habits menu choices, remove if you please
                        print("Returning to View Habits menu in 3...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to View Habits menu in 2...", end='', flush=True)
                        time.sleep(1)
                        print("\rReturning to View Habits menu in 1...", end='', flush=True)
                        time.sleep(1)
                        print("\r")
                        return
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")