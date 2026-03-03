from kivymd.app import MDApp # Imports the base class for a KivyMD application
from kivy.lang import Builder # Imports the tool used to load the .kv design file
from kivy.uix.screenmanager import ScreenManager # Imports the manager that handles switching between screens
import sqlite3 # Imports the database engine to store user information
import logic # Imports your custom logic.py file where screen classes are defined

class MainApp(MDApp): # Defines the main class of the app, inheriting from MDApp
    is_admin = 0 # A global variable to track if the logged-in user is an admin

    def build(self): # The main function that initializes and returns the app UI
        self.init_db() # Calls the function to set up the database
        self.theme_cls.primary_palette = "Indigo" # Sets the main color theme of the app to Indigo
        Builder.load_file('layout.kv') # Tells Python to read the design rules from layout.kv
        
        sm = ScreenManager() # Creates an instance of the ScreenManager to hold our screens
        
        # Adding the different screens (Login, Signup, Calculator, Admin) to the manager:
        sm.add_widget(logic.LoginScreen(name='login')) # Adds the Login screen
        sm.add_widget(logic.SignUpScreen(name='signup')) # Adds the Signup screen
        sm.add_widget(logic.CalcScreen(name='calc')) # Adds the Calculator screen
        sm.add_widget(logic.AdminScreen(name='admin')) # Adds the Admin dashboard screen
        
        return sm # Returns the manager as the root of the application

    def init_db(self): # Function to initialize the SQLite database
        conn = sqlite3.connect('users.db') # Connects to (or creates) a file named users.db
        cur = conn.cursor() # Creates a "cursor" to execute SQL commands
        
        # Creates a table for users if it doesn't exist, with columns for name, password, and admin status:
        cur.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, is_admin INTEGER)')
        
        conn.commit() # Saves the changes to the database
        conn.close() # Closes the connection to the database file

    def go_back(self): 
        self.root.current = 'calc' # A helper function to switch the view back to the calculator screen

if __name__ == '__main__': # Standard Python check to see if this file is being run directly
    MainApp().run() # Starts the application