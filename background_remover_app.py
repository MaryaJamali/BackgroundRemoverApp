import tkinter as tk  # Import the tkinter library to create a graphical user interface
from tkinter import filedialog, messagebox, Radiobutton, StringVar  # Importing utilities from tkinter
from PIL import Image, ImageTk, ImageOps  # Import image processing tools from PIL
from rembg import remove  # Import the rembg library to remove the image background
import os  # Import the os library to work with the file system


class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
