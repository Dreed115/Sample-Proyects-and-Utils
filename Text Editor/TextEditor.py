import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk, simpledialog, messagebox
import os

#Global Variables
num_frame = 1
T1 = []
current_tab_index = 0
size = 12
last_index = "1.0"
for_search = False

class CustomNotebook(ttk.Notebook):
    __initialized = False

    def __init__(self,  *args, **kwargs):        
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__initialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(["pressed"])
            self._active = index
            return "break"
        
    def on_close_release(self, event):
        global num_frame
        global T1
        global current_tab_index

        if not self.instate(["pressed"]):
            return
        
        element = self.identify(event.x, event.y)
        if "close" not in element:
            return

        index = self.index("@%d,%d" % (event.x, event.y))

        if self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

        num_frame -= 1

        del T1[current_tab_index]
        #if num_frame < 1:
        #    window.quit

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (tk.PhotoImage("img_close", file="icons8-close-10.png"))

        style.element_create("close", "image", "img_close", border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])

class Tab:
    def __init__(self, master):
        global size
        self.master = master
        self.tab = tk.Frame(master)
        self.tab.pack(fill="both", expand=True)

        self.scroll = tk.Scrollbar(self.tab)
        self.scroll.pack(side="right", fill="y")

        self.text = tk.Text(self.tab, font=("Consolas", size), padx=10, pady=10, undo=True, autoseparators=True, maxundo=-1, yscrollcommand=self.scroll.set) 
        self.text.pack(fill="both", expand=True)
        self.scroll.config(command=self.text.yview)

        self.name = "No title"
        self.path = ""

    def add(self, notebook):
        notebook.add(self.tab, text=self.name)

    def set_text(self, name):
        self.name = name
        notebook.tab(self.tab, text=name)

    def get_path(self, path):
        self.path = path

#The event when the tab change
def tab_changed(event):
        global notebook
        global T1
        global current_tab_index
        if num_frame >= 1:
            current_tab_index = notebook.index("current")
        else:
            window.destroy()

def add_tab(notebook, window):
    global num_frame
    new_tab = Tab(window)
    new_tab.add(notebook)
    T1.append(new_tab)
    num_frame += 1

def save_as_file(window):
    global notebook
    global T1
    global current_tab_index
    T1[current_tab_index].get_path(asksaveasfilename(filetypes=[("Text File", "*.txt *.dat *.pos *.xyz")]))

    if T1[current_tab_index].path == "":
        return
    
    with open(T1[current_tab_index].path, "w") as f:
        content = T1[current_tab_index].text.get(1.0, tk.END)
        f.write(content)
    T1[current_tab_index].set_text(f"{os.path.basename(T1[current_tab_index].path)}")
    
def open_file(window):
    global notebook
    global T1
    global current_tab_index
    filepath = askopenfilename(filetypes=[("Text File", "*.txt *.dat *.pos *.xyz")])

    if not filepath:
        return

    T1[current_tab_index].text.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        T1[current_tab_index].text.insert(tk.END, content)
    T1[current_tab_index].set_text(f"{os.path.basename(filepath)}")

def save_file(window):
    global notebook
    global T1
    global current_tab_index
    
    if T1[current_tab_index].path == "":
        save_as_file(window)
    else:
        with open(T1[current_tab_index].path, "w") as f:
            content = T1[current_tab_index].text.get(1.0, tk.END)
            f.write(content)
        T1[current_tab_index].set_text(f"{os.path.basename(T1[current_tab_index].path)}")

def search_next():
    global T1
    global current_tab_index
    global last_index
    global for_search
    if for_search:
        try:
            start_index = T1[current_tab_index].text.search(for_search, last_index, tk.END)
            end_index = f"{start_index}+{len(for_search)}c"
            T1[current_tab_index].text.tag_add("sel", start_index, end_index)
            last_index = end_index
        except tk.TclError:
            messagebox.showinfo("Search",  "No more Ocurrencies") 
    else:
        search()

def search():
    global T1
    global current_tab_index
    global last_index
    global for_search
    try:
        for_search = simpledialog.askstring(title="Search", prompt="Enter word for search \t\t\t")
        start_index = T1[current_tab_index].text.search(for_search, "1.0", tk.END)
        end_index = f"{start_index}+{len(for_search)}c"
        T1[current_tab_index].text.tag_add("sel", start_index, end_index)
        last_index = end_index
    except tk.TclError:
        pass

def select_all(event=None):
    global T1
    global current_tab_index
    T1[current_tab_index].text.tag_add("sel", "1.0", "end")
    return "break"

def restore():
    global T1
    for tab in T1:
        tab.text.config(font=("Consolas", 12))

def copy():
    global T1
    global current_tab_index
    global content
    try:
        content = T1[current_tab_index].text.selection_get()
        window.clipboard_clear()
        window.clipboard_append(content)
        return "break"
    except tk.TclError:
        pass

def paste():
    global T1
    global current_tab_index
    global content
    try:
        T1[current_tab_index].text.insert(tk.END, content)
        return "break"
    except NameError:
        pass

def cut():
    global content
    global T1
    global current_tab_index
    
    try:    
        content = T1[current_tab_index].text.selection_get()
        window.clipboard_clear()
        window.clipboard_append(content)
        T1[current_tab_index].text.delete("sel.first", "sel.last")
        return "break"
    except tk.TclError: 
        pass

def zoom_in():
    global T1
    global current_tab_index
    global size
    size += 4
    for tab in T1:
        tab.text.config(font=("Consolas", size))

def zoom_out():
    global T1
    global current_tab_index
    global size
    size -= 4
    for tab in T1:
        tab.text.config(font=("Consolas", size))

def undo():
    try:
        T1[current_tab_index].text.edit_undo()
    except tk.TclError:
        pass

def redo():
    try:
        T1[current_tab_index].text.edit_redo()
    except tk.TclError:
        pass

def show_position():
    global T1
    global current_tab_index
    position = T1[current_tab_index].text.index(tk.INSERT)
    line, column = map(int, position.split("."))
    position_label.config(text=f"Row: {line}, Column: {column}")

#Parameters and declarations
window = tk.Tk()
window.title("Text Editor")

#Icons
icono_chico = tk.PhotoImage(file="icons16.png")
icono_grande = tk.PhotoImage(file="icons32.png")
window.iconphoto(False, icono_grande, icono_chico)

#Menu init
menu = tk.Menu(window, tearoff=0)
window.config(menu=menu)        

#Archive Menu
archive_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archive", menu=archive_menu)
archive_menu.add_command(label="New", command=lambda: add_tab(notebook, window))
archive_menu.add_separator()
archive_menu.add_command(label="Open", command=lambda: open_file(window))
archive_menu.add_command(label="Save", command=lambda: save_file(window))
archive_menu.add_command(label="Save As", command=lambda: save_as_file(window))
archive_menu.add_separator()
archive_menu.add_command(label="Exit", command=window.quit)

#Edit Menu
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=lambda: undo())
edit_menu.add_command(label="Redo", command=lambda: redo())
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=lambda: copy())
edit_menu.add_command(label="Cut", command=lambda: cut())
edit_menu.add_command(label="Paste", command=lambda: paste())
edit_menu.add_separator()
edit_menu.add_command(label="Search", command=lambda: search())
edit_menu.add_command(label="Search Next", command=lambda: search_next())
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: select_all())

#View Menu
view_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom in", command=lambda: zoom_in())
view_menu.add_command(label="Zoom out", command=lambda: zoom_out())
view_menu.add_command(label="Restore", command=lambda: restore())

#Notebook Init
notebook = CustomNotebook(window, width=800, height=400)
notebook.pack(side="top", fill="both", expand=True)

#Fisrt Tab
new_tab = Tab(window)
new_tab.add(notebook)
T1.append(new_tab)

#Update tab index when click in it
notebook.bind("<<NotebookTabChanged>>", tab_changed)

#Label to show the position in the text widget
position_label = tk.Label(window)
position_label.pack(fill=tk.Y, side=tk.BOTTOM)
show_position()

#Keyboard shortcuts declaration
window.bind("<Control-n>", lambda x: add_tab(notebook, window))
window.bind("<Control-N>", lambda x: add_tab(notebook, window))
window.bind("<Control-s>", lambda x: save_file(window))
window.bind("<Control-S>", lambda x: save_file(window))
window.bind("<Control-Shift-s>", lambda x: save_as_file(window))
window.bind("<Control-Shift-S>", lambda x: save_as_file(window))
window.bind("<Control-o>", lambda x: open_file(window))
window.bind("<Control-O>", lambda x: open_file(window))
window.bind("<Control-a>", lambda x: select_all())
window.bind("<Control-A>", lambda x: select_all())
window.bind("<Control-c>", lambda x: copy())
window.bind("<Control-C>", lambda x: copy())
window.bind("<Control-x>", lambda x: cut())
window.bind("<Control-X>", lambda x: cut())
window.bind("<Control-b>", lambda x: search())
window.bind("<Control-B>", lambda x: search())
window.bind("<F3>", lambda x: search_next())
window.bind("<Control-KeyPress-plus>", lambda x: zoom_in())
window.bind("<Control-KeyPress-minus>", lambda x: zoom_out())
window.bind("<Control-0>", lambda x: restore())
window.bind("<KeyRelease>", lambda x: show_position())
window.bind("<Button-1>", lambda x: show_position())

window.mainloop()


