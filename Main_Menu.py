# This is the Main Menu

import questionary
from Habit_List import HabitList
from Actions import Actions
from Statistics import Statistics
from Exit import ExitHandler

class MainMenu:
    def show_menu(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside show_menu function of Main_Menu.py")
        
        """
        Display the main menu to the user and handle their choices.
        
        This method presents the user with a main menu containing several options.
        It uses the `questionary` library to prompt the user for input and navigate
        to the corresponding submenu based on their choice.
        """
        while True:
            choice = questionary.select(
                r"""
          ___________________________________
        / Welcome to the  Habit Tracker.      \
        \ Let's work on our habits together!  /
          -----------------------------------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/\
                        ||----- |
                        ||     ||
        """,
                choices=[
                    "1. View Habit List",
                    "2. Actions",
                    "3. View Habit Statistics",
                    "4. Exit"
                ]
            ).ask()

            # Program takes the user to their chosen menu for further actions
            if choice == "1. View Habit List":
                submenu = HabitList()
                submenu.show_menu()
            elif choice == "2. Actions":
                submenu = Actions()
                submenu.show_menu()
            elif choice == "3. View Habit Statistics":
                submenu = Statistics()
                submenu.show_menu()
            elif choice == "4. Exit":
                if ExitHandler.confirm_exit():
                    ExitHandler.exit_app()
                else:
                    continue