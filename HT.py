# HT.py is the Habit Tracker's main file.

import os
from Main_Menu import MainMenu
from Database import DatabaseManager

def main():
    """
    Main function to start the application.
    This function initializes the main menu and displays it to the user.
    """
    db_file = "database.db"

    # Check if the database file exists
    if os.path.isfile(db_file):
        print("DEBUG: Database found. Opening Database...")
    else:
        print("DEBUG: No Database file was found. Creating new Database...")

    # Create an instance of the DatabaseManager class
    db_manager = DatabaseManager(db_file)
    # Call the method to create tables in the database
    db_manager.create_tables()

    # Create an instance of the MainMenu class
    main_menu = MainMenu()
    # Display the main menu to the user
    main_menu.show_menu()   

# Call the main function if the script is run directly
if __name__ == "__main__":
    main()