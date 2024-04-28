# This is 3. View Habit Statistics

import calendar
import datetime
import time
import questionary
from Database import DatabaseManager
from Return import Return
from tabulate import tabulate

class Statistics:
    def show_menu(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside show_menu function in Statistics.py")
        
        """
        Display the Statistics submenu to the user and handle their choices.
        
        This method presents the user with options related to viewing statistics on their habits.
        It allows the user to view various statistics and provides an option to return to the main menu.
        """
        while True:
            choice = questionary.select(
                r"""
          ______________________________
        / Welcome to the Statistics menu.\
        \ What would you like to do?     /
          ------------------------------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/\
                        ||----- |
                        ||     ||
        """,
                choices=[
                    "1. Overall Habit Success Rate",
                    "2. Success Rate by Habit",
                    "3. Failure Rate by Habit",
                    "4. Return to Main Menu"
                ]
            ).ask()

            if choice == "1. Overall Habit Success Rate":
                self.show_overall_success_rate()
            elif choice == "2. Success Rate by Habit":
                self.show_success_rate_by_habit()
            elif choice == "3. Failure Rate by Habit":
                self.show_failure_rate_by_habit()
            elif choice == "4. Return to Main Menu":
                Return.return_to_main_menu()
                return
    
    def __init__(self):
        self.db_manager = DatabaseManager("database.db")

    def show_overall_success_rate(self):
            
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside show_overall_success_rate function in Statistics.py")
        
        """
        Display the overall success rate statistics for all habits.

        This method calculates and displays the overall success rate statistics for all habits
        regardless of their periodicity (daily/weekly/monthly).
        """
        
        while True:
            print(
                r"""
    ____________________________________________
    / Here you can see all your habits along with \                
    \ overall success rate and statistics.        /
    --------------------------------------------
           \   ^__^
            \  (oo)\_______
               (__)\       )\/\
                   ||----- |
                   ||     ||
        """)

            # Get all habits from the database
            habits = self.db_manager.get_habits_basics()

            # Initialize variables for overall success rate calculation
            total_days = 0
            total_successful_days = 0
            total_weeks = 0
            total_successful_weeks = 0
            total_months = 0
            total_successful_months = 0

            # Calculate overall success rate statistics for all habits
            for habit in habits:
                # Retrieve all dates for the habit using the database method
                habit_dates = self.db_manager.get_dates_by_habit_id(habit[0])

                # Get today's date
                current_date = datetime.datetime.today().date()

                try:
                    # Calculate success rate for daily habits
                    if habit[4] == 'daily':
                        try:
                            days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
                            successful_days = sum(1 for date_str in habit_dates if int(date_str.split('-')[2]) <= days_in_month)
                            total_days += days_in_month
                            total_successful_days += successful_days
                        except Exception as e:
                            print(f"An error occurred while calculating success rate for habit '{habit[1]}': {e}")

                    # Calculate success rate for weekly habits
                    elif habit[4] == 'weekly':
                        try:
                            if current_date.month <= 6:
                                start_date = datetime.date(current_date.year, 1, 1)
                                end_date = datetime.date(current_date.year, 6, 30)
                            else:
                                start_date = datetime.date(current_date.year, 7, 1)
                                end_date = datetime.date(current_date.year, 12, 31)
                            num_weeks = (end_date - start_date).days // 7
                            successful_weeks = len(set(int(date_str.split('-')[1]) for date_str in habit_dates if start_date <= datetime.datetime.strptime(date_str, '%Y-%m-%d').date() <= end_date))
                            total_weeks += num_weeks
                            total_successful_weeks += successful_weeks
                        except Exception as e:
                            print(f"An error occurred while calculating success rate for habit '{habit[1]}': {e}")
                                            
                    # Calculate success rate for monthly habits
                    elif habit[4] == 'monthly':
                        try:
                            current_year = current_date.year
                            current_month = current_date.month
                            successful_months = sum(1 for date_str in habit_dates if int(date_str.split('-')[0]) == current_year and int(date_str.split('-')[1]) == current_month)
                            total_months += 1
                            total_successful_months += successful_months
                        except Exception as e:
                            print(f"An error occurred while calculating success rate for habit '{habit[1]}': {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Calculate overall success rates
            overall_success_rate_daily = (total_successful_days / total_days) * 100 if total_days > 0 else 0
            overall_success_rate_weekly = (total_successful_weeks / total_weeks) * 100 if total_weeks > 0 else 0
            overall_success_rate_monthly = (total_successful_months / total_months) * 100 if total_months > 0 else 0

            # Display overall success rates
            print("\nOverall Success Rates:")
            print(f"Daily habits: {overall_success_rate_daily:.2f}% success rate")
            print(f"Weekly habits: {overall_success_rate_weekly:.2f}% success rate")
            print(f"Monthly habits: {overall_success_rate_monthly:.2f}% success rate")

            # Prompt the user to return to Statistics
            while True:
                choice = input("Type 'back to statistics' when you're ready to return: ").strip().lower()
                if choice == 'back to statistics':
                    # Add a delay before returning to the Statistics menu choices, remove if you please
                    print("Returning to Statistics menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Statistics menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Statistics menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    return
                else:
                    print("Error: Please enter 'back to statistics'.")
                    # Add a delay before asking the user to enter the return promt again, remove if you please
                    print("Please try again in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    continue           
                
    def show_success_rate_by_habit(self):
        
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside show_success_rate_by_habit function in Statistics.py")
        
        """
        Display the success rate statistics for a selected habit based on its periodicity.
        """
        while True:
            print(
                r"""
        __________________________________________
        / Here you can see your habits you previously \
        < added. If you want to ispect the statistics  >
        \ please provide the Habit ID.                /
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
            print("Select a habit to inspect:")
            
            # Ask the user to select a habit
            habit_id = input("Enter the ID of the habit (type 'cancel' to exit): ").strip()

            # Check if the user wants to cancel
            if habit_id.lower() == 'cancel':
                print("Viewing Statistics cancelled.")
                # Add a delay before returning to the Statistics menu choices, remove if you please
                print("Returning to Statistics menu in 3...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Statistics menu in 2...", end='', flush=True)
                time.sleep(1)
                print("\rReturning to Statistics menu in 1...", end='', flush=True)
                time.sleep(1)
                print("\r")
                break

            # Check if the entered ID exists in the database
            habit_exists = False
            for h in habits:
                if h[0] == int(habit_id):
                    habit_exists = True
                    habit_name = h[1]
                    periodicity = h[4]
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
            
            # If the entered ID exists, proceed with viewing statistics
            print("The provided ID exists in the Database.")
            print(f"You can now see your habit, {habit_name}'s statistics.")
            
            # Retrieve all dates for the selected habit
            habit_dates = self.db_manager.get_all_dates()
            
            # Display dates for the selected habit
            if habit_dates and int(habit_id) in habit_dates:
                print(f"\nDates for {habit_name} habit:")
                dates = habit_dates[int(habit_id)]['dates']
                print(tabulate(enumerate(dates, start=1), headers=["#", "Date"]))
            
            # Get today's date
            current_date = datetime.datetime.today().date()

            # Initialize success_rate to None
            success_rate = None

            # Calculate success rate for daily habits
            if periodicity == 'daily':
                try:
                    # Get the number of days in the current month
                    days_in_month = current_date.day
                    # Calculate the number of successful days
                    successful_days = sum(1 for date in habit_dates[int(habit_id)]['dates'] if int(date.split('-')[2]) <= days_in_month)
                    # Calculate success rate
                    success_rate = (successful_days / days_in_month) * 100

                    print(f"Success rate for habit '{habit_name}' in the current month: {success_rate:.2f}%")
                    print(f"Successful days: {successful_days}/{days_in_month}")
                except ZeroDivisionError:
                    print("Error: Division by zero occurred when calculating success rate for daily habit.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    
            # Calculate success rate for weekly habits
            elif periodicity == 'weekly':
                try:
                    # Calculate the start and end dates for the period based on the current date
                    if current_date.month <= 6:
                        # Start of the year
                        start_date = datetime.date(current_date.year, 1, 1)
                        # End of the first half of the year
                        end_date = datetime.date(current_date.year, 6, 30)
                    else:
                        # Start of the second half of the year
                        start_date = datetime.date(current_date.year, 7, 1)
                        # End of the year
                        end_date = datetime.date(current_date.year, 12, 31)

                    # Calculate the number of weeks in the period
                    num_weeks = (end_date - start_date).days // 7

                    # Calculate the number of successful weeks
                    successful_weeks = len([date for date in habit_dates[int(habit_id)]['dates'] if start_date <= date <= end_date])

                    # Calculate success rate
                    success_rate = (successful_weeks / num_weeks) * 100
                except ZeroDivisionError:
                    print("Error: Division by zero occurred when calculating success rate for weekly habit.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    
            # Calculate success rate for monthly habits
            elif periodicity == 'monthly':
                try:
                    # Get the current year
                    current_year = current_date.year
                    # Get the current month
                    current_month = current_date.month

                    # Initialize variables to track successful months and total months
                    successful_months = 0
                    total_months = 0

                    # Iterate through all habit dates
                    for date in habit_dates[int(habit_id)]['dates']:
                        # Extract year and month from the date
                        habit_year = date.year
                        habit_month = date.month

                        # Check if the date falls within the current year and month
                        if habit_year == current_year and habit_month == current_month:
                            successful_months += 1

                        total_months += 1

                    # Calculate success rate
                    if total_months > 0:
                        success_rate = (successful_months / total_months) * 100
                    else:
                        success_rate = 0

                    print(f"Success rate for habit '{habit_name}' in the current month: {success_rate:.2f}%")
                    print(f"Successful months: {successful_months}/{total_months}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Print message based on success rate
            if success_rate is not None:
                if success_rate <= 25:
                    print("This month was a bit difficult, but you gave your best. Let's work hard together to make the next month better!")
                elif 25 < success_rate <= 50:
                    print("You have been working hard and you are on the right track! Let's continue working hard on this habit!")
                elif 50 < success_rate <= 75:
                    print("You did a great job so far! You are working on this habit a lot and you can clearly see the results. I am proud of you!")
                else:
                    print("Woah you have been working so hard. I really hope you are proud of your achievement and you are enjoying the results.")
                    
            # Prompt the user to return to Statistics
            while True:
                choice = input("Type 'back to statistics' when you're ready to return: ").strip().lower()
                if choice == 'back to statistics':
                    # Add a delay before returning to the Statistics menu choices, remove if you please
                    print("Returning to Statistics menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Statistics menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Statistics menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    return
                else:
                    print("Error: Please enter 'back to statistics'.")
                    # Add a delay before asking the user to enter the return promt again, remove if you please
                    print("Please try again in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    continue           
                
    def show_failure_rate_by_habit(self):
            
        # Uncomment for testing purposes, it is just a debug statement
        #print("DEBUG: Inside show_failure_rate_by_habit function in Statistics.py")
        
        """
        Display the failure rate statistics for all habits and a selected habit based on its periodicity.

        This method calculates and displays the failure rate statistics for all habits and a selected habit,
        taking into account their periodicity (daily/weekly/monthly). 
        """

        while True:
            print(
        r"""
        __________________________________________
        / Here you can see your habits you previously \
        \ added and your failure rate.                 /
        ------------------------------------------
               \   ^__^
                \  (oo)\_______
                   (__)\       )\/\
                       ||----- |
                       ||     ||
            """)

            # Get all habits from the database
            habits = self.db_manager.get_habits_basics()

            # Initialize variables for failure rate calculation
            total_days = 0
            total_failed_days = 0
            total_weeks = 0
            total_failed_weeks = 0
            total_months = 0
            total_failed_months = 0

            # Calculate failure rate statistics for all habits
            for habit in habits:
                # Retrieve all dates for the habit using the database method
                habit_dates = self.db_manager.get_dates_by_habit_id(habit[0])

                # Get today's date
                current_date = datetime.datetime.today().date()

                try:
                    # Calculate failure rate for daily habits
                    if habit[4] == 'daily':
                        try:
                            days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
                            failed_days = days_in_month - sum(1 for date_str in habit_dates if int(date_str.split('-')[2]) <= days_in_month)
                            total_days += days_in_month
                            total_failed_days += failed_days
                        except Exception as e:
                            print(f"An error occurred while calculating failure rate for habit '{habit[1]}': {e}")

                    # Calculate failure rate for weekly habits
                    elif habit[4] == 'weekly':
                        try:
                            if current_date.month <= 6:
                                start_date = datetime.date(current_date.year, 1, 1)
                                end_date = datetime.date(current_date.year, 6, 30)
                            else:
                                start_date = datetime.date(current_date.year, 7, 1)
                                end_date = datetime.date(current_date.year, 12, 31)
                            num_weeks = (end_date - start_date).days // 7
                            failed_weeks = num_weeks - len(set(int(date_str.split('-')[1]) for date_str in habit_dates if start_date <= datetime.datetime.strptime(date_str, '%Y-%m-%d').date() <= end_date))
                            total_weeks += num_weeks
                            total_failed_weeks += failed_weeks
                        except Exception as e:
                            print(f"An error occurred while calculating failure rate for habit '{habit[1]}': {e}")

                    # Calculate failure rate for monthly habits
                    elif habit[4] == 'monthly':
                        try:
                            current_year = current_date.year
                            current_month = current_date.month
                            failed_months = current_month - sum(1 for date_str in habit_dates if int(date_str.split('-')[0]) == current_year and int(date_str.split('-')[1]) == current_month)
                            total_months += 1
                            total_failed_months += failed_months
                        except Exception as e:
                            print(f"An error occurred while calculating failure rate for habit '{habit[1]}': {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Calculate overall failure rates
            overall_failure_rate_daily = (total_failed_days / total_days) * 100 if total_days > 0 else 0
            overall_failure_rate_weekly = (total_failed_weeks / total_weeks) * 100 if total_weeks > 0 else 0
            overall_failure_rate_monthly = (total_failed_months / total_months) * 100 if total_months > 0 else 0

            # Display overall failure rates
            print("\nOverall Failure Rates:")
            print(f"Daily habits: {overall_failure_rate_daily:.2f}% failure rate")
            print(f"Weekly habits: {overall_failure_rate_weekly:.2f}% failure rate")
            print(f"Monthly habits: {overall_failure_rate_monthly:.2f}% failure rate")
            
            # Create a list to store habit names and their failure rates
            habit_failure_data = []
            for habit in habits:
                # Calculate failure rate for each habit
                habit_failure_rate = 0
                if habit[4] == 'daily' and total_days > 0:
                    habit_failure_rate = (total_failed_days / total_days) * 100
                elif habit[4] == 'weekly' and total_weeks > 0:
                    habit_failure_rate = (total_failed_weeks / total_weeks) * 100
                elif habit[4] == 'monthly' and total_months > 0:
                    habit_failure_rate = (total_failed_months / total_months) * 100

                habit_failure_data.append([habit[1], f"{habit_failure_rate:.2f}%"])

            # Display habit failure rates in tabulated format
            print(tabulate(habit_failure_data, headers=["Habit Name", "Failure Rate"]))
            
            # Check if any habit has a failure rate over 50%, provide helpful suggestion
            for habit_data in habit_failure_data:
                habit_name = habit_data[0]
                failure_rate = float(habit_data[1].strip('%'))
                if failure_rate > 50:
                    print(f"Your Habit, {habit_name}, is not very successful. You may want to google additional techniques to reinforce this habit!")

            # Prompt the user to return to Statistics
            while True:
                choice = input("Type 'back to statistics' when you're ready to return: ").strip().lower()
                if choice == 'back to statistics':
                    # Add a delay before returning to the Statistics menu choices, remove if you please
                    print("Returning to Statistics menu in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Statistics menu in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rReturning to Statistics menu in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    return
                else:
                    print("Error: Please enter 'back to statistics'.")
                    # Add a delay before asking the user to enter the return prompt again, remove if you please
                    print("Please try again in 3...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 2...", end='', flush=True)
                    time.sleep(1)
                    print("\rPlease try again in 1...", end='', flush=True)
                    time.sleep(1)
                    print("\r")
                    continue