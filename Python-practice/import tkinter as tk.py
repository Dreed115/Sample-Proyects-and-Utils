import tkinter as tk
from tkinter import ttk

class Tab:
    def __init__(self, master, text):
        self.master = master
        self.tab = ttk.Frame(master)
        self.text = text

    def add_to_notebook(self, notebook):
        notebook.add(self.tab, text=self.text)

root = tk.Tk()
root.title("Dynamic Tabs Example")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tabs = []

def tab_changed(event):
    global notebook
    global tabs
    current_tab_index = notebook.index("current")
    print("Current Tab Index:", current_tab_index)
    print("Current Tab Text:", tabs[current_tab_index].text)

def add_tab():
    global notebook
    global tabs
    new_tab = Tab(root, f"Tab {len(tabs) + 1}")
    new_tab.add_to_notebook(notebook)
    tabs.append(new_tab)

add_button = tk.Button(root, text="Add Tab", command=add_tab)
add_button.pack()

notebook.bind("<<NotebookTabChanged>>", tab_changed)

root.mainloop()
