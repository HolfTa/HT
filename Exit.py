# This is 4. Exit menu

import time

class ExitHandler:
    @staticmethod
    def confirm_exit():
        """
        Ask the user if they are sure they want to exit the application.
        
        Returns:
            bool: True if the user confirms the exit, False otherwise.
        """
        confirm = input(r"""
      ____________________________________
    < Are you sure you want to exit? (y/n) >
      ------------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----- |
                    ||     ||
    """)

        if confirm.strip().lower() == 'y':
            return True
        else:
            print(r"""
      _________________________
    < Returning to main menu... >
      -------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----- |
                    ||     ||
    """)
            # Add a 3-second delay before returning to the main menu, remove if you like
            print("Returning in 3...", end='', flush=True)
            time.sleep(1)
            print("\rReturning in 2...", end='', flush=True)
            time.sleep(1)
            print("\rReturning in 1...", end='', flush=True)
            time.sleep(1)
            print("\r")
            return False

    @staticmethod
    def exit_app():
        """
        Exit the application.
        """
        print(r"""
      _________________________________
    < Exiting the application. Goodbye! >
      ---------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----- |
                    ||     ||
    """)
        
        # Add a 3-second delay before exiting the app, remove if you like
        print("Exiting in 3...", end='', flush=True)
        time.sleep(1)
        print("\rExiting in 2...", end='', flush=True)
        time.sleep(1)
        print("\rExiting in 1...", end='', flush=True)
        time.sleep(1)
        print("\r")
        exit()
