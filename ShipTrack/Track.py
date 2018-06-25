"""
 ShipTrack by Max Lareau
 - Easily track packages from different carriers in an easy to read format

 Track Class
 - Class that handles all tracking information
 - Uses tracking api to fetch required data for tracking info
 - Formats data for presentation on table in Main Class
"""

# Import
from tkinter import *

def main():
    # Initialize window
    tk = Tk()
    tk.title('testing menubar')
    tk.geometry('400x400')

    # Define functions for menu
    def printNothing():
        print('Nothing happened')

    # Initialize menu
    menu = Menu(tk)
    menu.add_command(label='New', command=printNothing)
    menu.add_separator()
    menu.add_command(label='Exit', command=tk.quit)

    tk.config(menu=menu)
    tk.mainloop()

main()