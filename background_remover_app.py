import tkinter as tk  # Import the tkinter library to create a graphical user interface
from tkinter import filedialog, messagebox, Radiobutton, StringVar  # Importing utilities from tkinter
from PIL import Image, ImageTk, ImageOps  # Import image processing tools from PIL
from rembg import remove  # Import the rembg library to remove the image background
import os  # Import the os library to work with the file system


class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Remove image background")  # Set the title of the main window
        self.root.geometry("600x400")  # Set window size
        self.root.configure(background='white')  # Set the background color of the window to white

        self.input_image_path = None  # Stores the input image path
        self.output_image_path = None  # Stores the output image path

        self.mode_var = StringVar()  # Create a StringVar variable to store the selected mode (color or black and white)
        self.mode_var.set("color")  # Set the default mode to color
