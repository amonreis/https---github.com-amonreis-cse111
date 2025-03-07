
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry

import math

def main():
    # Create the TK root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of circle")
    frm_main.pack(padx=26, pady=25, fill=tk.BOTH, expand= 15)

    # Calculate the populate_main function, wich will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.
    
    
    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Diameter: (meters)"
    lbl_diameter = Label(frm_main, text="Diameter: (meters)")

    # Create a float entry box where the user will enter the
    # diameter of the circle in meters.
    ent_diameter = FloatEntry(frm_main, width=8)

    # Create a label that displays "meters"
    lbl_units = Label(frm_main, text="meters")

    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:")

    # Creat a lebel that displays "Radius:"
    lbl_radius_txt = Label(frm_main, text="Radius:")

    # Create labels that will display the results.
    lbl_radius = Label(frm_main, width=15)
    lbl_radius_units = Label(frm_main, text="m")
    lbl_result = Label(frm_main, width=15)
    lbl_area_units = Label(frm_main, text="m2")
    

    # Create the Clear Button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry_boxes, and buttons in a grid.
    lbl_diameter.grid(    row=0, column=0, padx=3, pady=3)
    ent_diameter.grid(    row=0, column=1, padx=3, pady=3)
    lbl_units.grid(       row=0, column=2, padx=0, pady=3)

    lbl_radius_txt.grid(  row=1, column=0, padx=(30,3), pady=3)
    lbl_radius.grid(      row=1, column=1, padx=3, pady=3)
    lbl_radius_units.grid(row=1, column=2, padx=0, pady=3)
    lbl_area.grid(        row=2, column=0, padx=(30,3), pady=3)
    lbl_result.grid(      row=2, column=1, padx=3, pady=3)
    lbl_area_units.grid(  row=2, column=2, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    def calculate(event):
        """Compute and display the area of 
        a circle in meters squared.
        """
        try:
            # Get the user's diameter.
            diameter = ent_diameter.get()

            # Convert diameter to radius
            radius = diameter / 2

            # Compute the area squared of the circle
            area = math.pi * (radius **2)

            # Display the area of the circle in meters squared
            lbl_result.config(text=f"{area:.2f}")
            lbl_radius.config(text=f"{radius:.2f}")

        except ValueError:
            # When the user deletes all the digits in the diameter
            # entry box, clear the result label.
            lbl_result.config(text="")
            lbl_radius.config(text="")

        
    def clear():
        """Clear all the inputs and outputs"""
        btn_clear.focus()
        ent_diameter.clear()
        lbl_result.config(text="")
        lbl_radius.config(text="")
        ent_diameter.focus()

    # Bind the calculate function to the diameter entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_diameter.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the diameter entry box.
    ent_diameter.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
