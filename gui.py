import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Wiki Search")

url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(root)
url_entry.grid(row=0, column=1, padx=5, pady=5)

search_label = tk.Label(root, text="Search:")
search_label.grid(row=1, column=0, padx=5, pady=5)

search_entry = tk.Entry(root)
search_entry.grid(row=1, column=1, padx=5, pady=5)

def search_wiki():
    url = url_entry.get()
    search = search_entry.get()

    command = f"python wiki.py --url {url} --search '{search}'"
    subprocess.call(command, shell=True)

search_button = tk.Button(root, text="Search", command=search_wiki)
search_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
