# This is Return.py and handles returning to the main menu from submenus

import time

class Return:
    @staticmethod
    def return_to_main_menu():
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside return_to_main_menu function in Return.py")
        
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
        
        # Add a 3-second delay before returning to main menu, remove if you like
        print("Returning in 3...", end='', flush=True)
        time.sleep(1)
        print("\rReturning in 2...", end='', flush=True)
        time.sleep(1)
        print("\rReturning in 1...", end='', flush=True)
        time.sleep(1)
        print("\r")