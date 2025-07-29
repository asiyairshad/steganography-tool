import tkinter as tk
from tkinter import filedialog, messagebox
from steg_utils import encode_message, decode_message

def open_file():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.bmp")])
    entry_image.delete(0, tk.END)
    entry_image.insert(0, path)

def save_encoded():
    input_image = entry_image.get()
    message = text_message.get("1.0", tk.END).strip()
    password = entry_password.get().strip()
    output_path = filedialog.asksaveasfilename(defaultextension=".png")
    if input_image and message and password:
        encode_message(input_image, message, password, output_path)
        messagebox.showinfo("Success", "Encrypted message embedded successfully!")

def decode():
    input_image = entry_image.get()
    password = entry_password.get().strip()
    if input_image and password:
        message = decode_message(input_image, password)
        text_message.delete("1.0", tk.END)
        text_message.insert(tk.END, message)

# GUI Window
app = tk.Tk()
app.title("Steganography Tool (Encrypted)")

tk.Label(app, text="Image File:").pack()
entry_image = tk.Entry(app, width=50)
entry_image.pack()
tk.Button(app, text="Browse", command=open_file).pack()

tk.Label(app, text="Password:").pack()
entry_password = tk.Entry(app, show="*", width=50)
entry_password.pack()

tk.Label(app, text="Message:").pack()
text_message = tk.Text(app, height=10, width=50)
text_message.pack()

tk.Button(app, text="Encode and Save Image", command=save_encoded).pack()
tk.Button(app, text="Decode from Image", command=decode).pack()

app.mainloop()
