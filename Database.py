# This is the Database for the Habit Tracker app

import sqlite3
from sqlite3 import Error
from datetime import date

class DatabaseManager:
    def __init__(self, db_file):
        """
        Initialize the DatabaseManager with the specified database file.
        """
        self.db_file = db_file

    def create_connection(self):
        """
        Create a database connection to the SQLite database specified by the db_file.
        """
        try:
            connection = sqlite3.connect(self.db_file)
            return connection
        except Error as e:
            print(e)
            return None

    def create_tables(self):
        """
        Create the tables in the database if they do not exist.

        This method creates two tables:
        - habits: stores information about habits
        - check_ins: stores check-in dates for habits
        
        The tables are related through the id!
        """
        # SQL statement to create the habits table
        create_habits_table = """
        CREATE TABLE IF NOT EXISTS habits (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Details TEXT,
            Category TEXT NOT NULL,
            Periodicity TEXT NOT NULL,
            Date_Added DATE NOT NULL
        )
        """

        # SQL statement to create the check_ins table
        create_check_ins_table = """
        CREATE TABLE IF NOT EXISTS check_ins (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Habit_ID INTEGER NOT NULL,
            Check_In_Date DATE,
            FOREIGN KEY (Habit_ID) REFERENCES habits (ID)
        )
        """

        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # Create the habits table
            cursor.execute(create_habits_table)

            # Create the check_ins table
            cursor.execute(create_check_ins_table)

            connection.commit()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def add_habit(self, name, details, category, periodicity):
        """
        Add a new habit to the database.

        This method is called when the user adds a new habit through the Actions Menu.
        It takes the habit details provided by the user, including the habit's name, details,
        category, and periodicity, and inserts them into the database. Additionally, it records
        the current date as the date the habit was added.
        """
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # Get the current date
            current_date = date.today()

            # SQL statement to insert a new habit
            insert_habit_query = """
            INSERT INTO habits (Name, Details, Category, Periodicity, Date_Added)
            VALUES (?, ?, ?, ?, ?)
            """

            # Execute the SQL statement to insert the new habit
            cursor.execute(insert_habit_query, (name, details, category, periodicity, current_date))

            # Get the ID of the newly added habit
            habit_id = cursor.lastrowid

            # SQL statement to insert the first check-in date for the habit
            insert_check_in_query = """
            INSERT INTO check_ins (Habit_ID, Check_In_Date)
            VALUES (?, ?)
            """

            # Execute the SQL statement to insert the first check-in date
            cursor.execute(insert_check_in_query, (habit_id, current_date))

            # Commit the changes
            connection.commit()

            return habit_id
        except Error as e:
            print(e)
            return None
        finally:
            if connection:
                connection.close()
                
    def get_habits_basics(self):
        """
        Retrieve basic habit data from the database.

        This method fetches basic information about all habit records from the 'habits' table in the database
        and returns them as a list of tuples, where each tuple represents a habit record.
        The tuple contains the habit ID, name, details, category, periodicity, and date added.
        """
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # SQL statement to select basic information for all habit records
            select_habits_query = """
            SELECT ID, Name, Details, Category, Periodicity, Date_Added
            FROM habits
            """

            # Execute the SQL statement to select basic information for all habit records
            cursor.execute(select_habits_query)

            # Fetch all habit records
            habits = cursor.fetchall()

            return habits
        except Error as e:
            print(e)
            return None
        finally:
            if connection:
                connection.close()

    def edit_habit_basics(self, habit_id, name=None, details=None, category=None, periodicity=None):
        """
        Edit basic habit data in the database.

        This method updates the basic information of a habit in the 'habits' table based on the provided habit ID.
        The method allows for editing the habit's name, details, category, and periodicity.
        Any parameter set to None will not be updated.
        Data is collected by the Actions.py file in the edit_habit method
        """
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # Check if name, category, or periodicity is empty
            if not name or not category or not periodicity:
                print("Error: Name, category, and periodicity cannot be empty.")
                return False

            # SQL statement to update habit data
            update_habit_query = """
            UPDATE habits
            SET Name = COALESCE(?, Name),
                Details = COALESCE(?, Details),
                Category = COALESCE(?, Category),
                Periodicity = COALESCE(?, Periodicity)
            WHERE ID = ?
            """

            # Execute the SQL statement to update habit data
            cursor.execute(update_habit_query, (name, details, category, periodicity, habit_id))

            # Commit the changes to the database
            connection.commit()

            # Check if any rows were affected
            if cursor.rowcount > 0:
                return True
            else:
                return False

        except Error as e:
            print(e)
            return False
        finally:
            if connection:
                connection.close()
                
    def delete_habit_all(self, habit_id):
        """
        Delete a habit along with all associated data from the database.

        This method deletes a habit record from the 'habits' table along with all associated
        check-in records from the 'check_ins' table based on the provided habit ID.
        """
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # SQL statement to delete check-in records associated with the habit
            delete_check_ins_query = """
            DELETE FROM check_ins
            WHERE Habit_ID = ?
            """

            # Execute the SQL statement to delete check-in records
            cursor.execute(delete_check_ins_query, (habit_id,))

            # SQL statement to delete the habit record
            delete_habit_query = """
            DELETE FROM habits
            WHERE ID = ?
            """

            # Execute the SQL statement to delete the habit record
            cursor.execute(delete_habit_query, (habit_id,))

            # Commit the changes to the database
            connection.commit()

            return True  # Deletion successful

        except Error as e:
            print(e)
            return False  # Deletion failed

        finally:
            if connection:
                connection.close()
                
    def add_check_in(self, habit_id, check_in_date):
        """
        Add a new check-in date for a habit in the database.

        This method inserts a new record into the 'check_ins' table with the provided habit ID
        and check-in date.
        """
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # SQL statement to insert a new check-in date
            insert_check_in_query = """
            INSERT INTO check_ins (Habit_ID, Check_In_Date)
            VALUES (?, ?)
            """

            # Execute the SQL statement to insert the new check-in date
            cursor.execute(insert_check_in_query, (habit_id, check_in_date))

            # Commit the changes to the database
            connection.commit()

            return True  # Check-in date added successfully

        except Error as e:
            print(e)
            return False  # Failed to add check-in date

        finally:
            if connection:
                connection.close()
                
    def update_check_in_date(self, check_in_id, new_date):
        """
        Update a check-in date in the database.

        This method updates the check-in date associated with a specific check-in ID.
        """
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # SQL statement to update the check-in date
            update_check_in_query = """
            UPDATE check_ins
            SET Check_In_Date = ?
            WHERE ID = ?
            """

            # Execute the SQL statement to update the check-in date
            cursor.execute(update_check_in_query, (new_date, check_in_id))

            # Commit the changes to the database
            connection.commit()

            # Check if any rows were affected
            if cursor.rowcount > 0:
                return True 
            else:
                return False

        except Error as e:
            print(e)
            return False

        finally:
            if connection:
                connection.close()
                
    def get_all_dates(self):
        """
        Retrieve all dates for each habit from the database.

        This method fetches all check-in dates for each habit and returns them as a dictionary,
        where each key is the habit ID and the corresponding value is a list of dates associated
        with that habit.
        """
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # SQL statement to select habit ID and name along with all associated check-in dates
            select_dates_query = """
            SELECT habits.ID, habits.Name, check_ins.Check_In_Date
            FROM habits
            LEFT JOIN check_ins ON habits.ID = check_ins.Habit_ID
            """

            # Execute the SQL statement to select habit ID, name, and check-in dates
            cursor.execute(select_dates_query)

            # Fetch all check-in dates
            rows = cursor.fetchall()

            # Create a dictionary to store dates for each habit
            habit_dates = {}

            # Process the fetched rows
            for row in rows:
                habit_id = row[0]
                habit_name = row[1]
                check_in_date = row[2]

                # Check if the habit ID already exists in the dictionary
                if habit_id in habit_dates:
                    # Append the check-in date to the list of dates for this habit
                    habit_dates[habit_id]['dates'].append(check_in_date)
                else:
                    # Create a new entry for this habit ID in the dictionary
                    habit_dates[habit_id] = {'name': habit_name, 'dates': [check_in_date]}

            return habit_dates

        except Error as e:
            print(e)
            return None

        finally:
            if connection:
                connection.close()
                
    def get_dates_by_habit_id(self, habit_id):
        """
        Retrieve all check-in dates for a specific habit from the database.

        This method fetches all check-in dates associated with the specified habit ID
        and returns them as a list.
        """
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # SQL statement to select check-in dates for the specified habit ID
            select_dates_query = """
            SELECT Check_In_Date
            FROM check_ins
            WHERE Habit_ID = ?
            """

            # Execute the SQL statement to select check-in dates
            cursor.execute(select_dates_query, (habit_id,))

            # Fetch all check-in dates
            dates = [row[0] for row in cursor.fetchall()]

            return dates

        except Error as e:
            print(e)
            return None

        finally:
            if connection:
                connection.close()
                
    def update_habit_start_date(self, habit_id, new_start_date):
        
        """
        Update the start date of a habit in the database.
        """
        
        try:
            # Connect to the database
            connection = self.create_connection()
            cursor = connection.cursor()

            # SQL statement to update the start date of the habit
            update_start_date_query = """
            UPDATE habits
            SET Date_Added = ?
            WHERE ID = ?
            """

            # Execute the SQL statement to update the start date
            cursor.execute(update_start_date_query, (new_start_date, habit_id))

            # Commit the changes to the database
            connection.commit()
            
        except Error as e:
            print("An error occurred while updating the habit start date:", e)
        finally:
            if connection:
                connection.close()