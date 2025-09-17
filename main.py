import tkinter as tk
from tkinter import filedialog
from watermarker import WaterMarker
import os

WATERMARK = "@LAR"

input_file = ""
output_file = ""

def select_input(label: tk.Label, btn_to_hide: tk.Button, btn_to_show: tk.Button):
    global input_file
    filename = filedialog.askopenfilename(
        title="Select input file",
        filetypes=(("Images", "*.jpg;*.jpeg;"),)
    )
    if filename:
        input_file = filename
        label.config(text=f"File: {os.path.basename(filename)}")
        btn_to_hide.pack_forget()
        btn_to_show.pack(pady=5)


def select_output():
    global output_file
    filename = filedialog.asksaveasfilename(
        title="Save output file",
        defaultextension=".jpg",
        filetypes=(("Images", "*.jpg;*.jpeg;"),)
    )
    if filename:
        output_file = filename

def add_watermark(label: tk.Label):
    if input_file:
        select_output()
        if output_file:
            watermarker = WaterMarker(input_file, output_file, WATERMARK)
            watermarker.add_watermark()
            label.config(text=f"Watermark added to: {os.path.basename(output_file)}")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Watermarker")
    root.geometry("300x120")
    root.resizable(False, False)

    label_input_filename = tk.Label(root, text="")
    label_input_filename.pack(pady=10)

    btn_watermark = tk.Button(root, text="Add Watermark", command=lambda: add_watermark(label_input_filename))

    btn_upload = tk.Button(root, text="Upload image", command=lambda: select_input(label_input_filename, btn_upload, btn_watermark))
    btn_upload.pack(pady=5)

    root.mainloop()
