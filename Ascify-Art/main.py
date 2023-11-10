import tkinter as tk
from PIL import Image, ImageTk
def image_to_ascii(image, new_width=100):
    image = image.convert('L')
    image = image.resize((new_width, int(new_width * image.height / image.width)))
    ascii_str = ""
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            ascii_str += ASCII_CHARS[pixel // 25]  # Adjust the range as needed
        ascii_str += "\n"
    return ascii_str
def display_ascii_in_window(image_path, new_width=100):
    root = tk.Tk()
    root.title("ASCII Art")
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    ascii_str = image_to_ascii(image, new_width)
    ascii_label = tk.Label(root, text=ascii_str, font=("Courier", 6))
    ascii_label.pack()
    root.mainloop()
if __name__ == "__main__":
    ASCII_CHARS = "@%#*+=-:. "
    input_image_path = "input_image.jpg"
    display_ascii_in_window(input_image_path)
