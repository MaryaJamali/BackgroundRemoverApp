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

        # Create a frame to display the image
        self.image_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.SUNKEN)
        self.image_frame.pack(pady=20)  # Pack the frame with a distance of 20 pixels from the top

        # Create a label for the image selection command
        self.label = tk.Label(self.root, text="Please select your input image:", font=("Arial", 14), bg="white")
        self.label.pack()  # Label packing

        # Create a button to select an image
        self.select_button = tk.Button(self.root, text="Select Image", command=self.select_image, font=("Arial", 12),
                                       bg="#4CAF50", fg="black")
        self.select_button.pack(pady=10)  # Pack the button 10 pixels from the top

        # Create radio button for color mode
        self.color_radio = Radiobutton(self.root, text="Remove the background and display the image in color",
                                       variable=self.mode_var, value="color", font=("Arial", 12), bg="white")
        self.color_radio.pack(anchor="center", padx=20)  # Align to center with 20 pixels from left and right

        self.gray_radio = Radiobutton(self.root, text="Remove background and display black and white image",
                                      variable=self.mode_var, value="gray", font=("Arial", 12), bg="white")
        self.gray_radio.pack(anchor="center", padx=20)  # Align to center with 20 pixels from left and right

        # Create button to perform background removal operation
        self.remove_button = tk.Button(self.root, text="Run the program", command=self.remove_and_display,
                                       font=("Arial", 12), bg="#4CAF50", fg="black")
        self.remove_button.pack(pady=20)  # pack the button with a distance of 20 pixels from the top

        # Create labels to display messages and status
        self.output_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue", bg="white")
        self.output_label.pack()  # Pack the label
        
    # Function to select the input image
    def select_image(self):
        # Open the file selection window
        self.input_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
        if self.input_image_path:  # If a path is selected
            # Display the name of the selected file
            self.output_label.config(text=f"Selected image: {os.path.basename(self.input_image_path)}")
                # Function to remove the background and display the image
    def remove_and_display(self):
        if self.input_image_path:  # If an image is selected
            try:
                with open(self.input_image_path, "rb") as f_in:
                    image_data = f_in.read()  # Read selected image data
                output_data = remove(image_data)  # Remove image background

                self.output_image_path = "output_image.png"  # Save the output image to a file
                with open(self.output_image_path, "wb") as f_out:
                    f_out.write(output_data)

                # Save the output image to a file
                img = Image.open(self.output_image_path)
                if self.mode_var.get() == "gray":  # If black and white mode is selected
                    img = ImageOps.grayscale(img)  # Convert the image to black and white

                # Change the size of the image to display in the window
                img = img.resize((400, 300), Image.ANTIALIAS)

                # Change the size of the image to display in the window
                img = ImageTk.PhotoImage(img)
                if hasattr(self, "img_label"):  # If the image label exists
                    self.img_label.config(image=img)  # Set the label image
                    self.img_label.image = img  # Save the image reference
                else:
                    self.img_label = tk.Label(self.image_frame, image=img, bg="white")  # create new label with image
                    self.img_label.image = img  # Save the image reference
                    self.img_label.pack()  # Pack the label

            except Exception as e:  # If an error occurs
                # Show error message
                messagebox.showerror("Error", f"Error removing image background:\n{str(e)}")
        else:
            # Display warning message if no image is selected
            messagebox.showwarning("Warning", "Please select an image first.")

if __name__ == "__main__":
    root = tk.Tk()  # Create the root tkinter object
    app = BackgroundRemoverApp(root)  # Create the app object with the root window
    root.mainloop()   # Start the tkinter main loop
