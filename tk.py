from tkinter import *
from tkinter import ttk
import random
from sort_gui import bubble, insertion, selection, heap, merge, quick, quick_tm

root = Tk()
root.title("Sort Visualizer")

root.maxsize(900, 600)
root.config(bg="Black")
select_alg = StringVar()
data = []
values = ["Bubble Sort",
          "Selection Sort",
          "Insertion Sort",
          "Heap Sort",
          "Merge Sort",
          "Quick Sort",
          "Quick 3 Medians"]


def generate():
    global data
    sizeval = int(size_entry.get())
    data = []
    for _ in range(sizeval):
        data.append(random.randrange(0, sizeval))

    drawData(data, ['Red' for x in range(len(data))])



# funtion to create the data bars by creating a canvas in Tkinter
def drawData(data, colorlist):
    canvas.grid(row=1, column=0, padx=10, pady=5)
    canvas.delete("all")
    can_height = 380
    can_width = 550
    x_width = can_width / (len(data) + 1)
    offset = 30
    spacing = 10

    normalized_data = [i / max(data) for i in data]
    Label(Mainframe, text="                                          ", bg='Grey').grid(row=1, column=4, padx=5, pady=5,
                                                                                        sticky=W)
    for i, height in enumerate(normalized_data):
        # top left corner
        x0 = i * x_width + offset + spacing
        y0 = can_height - height * 340

        # bottom right corner
        x1 = ((i + 1) * x_width) + offset
        y1 = can_height

        # data bars are generated as Red colored vertical rectangles
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        canvas.create_text(x0 + 2, y0, anchor=SE, text=str(data[i]))
    root.update_idletasks()


def start_algorithm():
    global data
    time_taken = 0
    if clicked.get() == "Bubble Sort":
        time_taken = bubble(data)
        drawData(data, ['Green' for x in range(len(data))])
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
    if clicked.get() == "Selection Sort":
        time_taken = selection(data)
        drawData(data, ['Green' for x in range(len(data))])
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
    if clicked.get() == "Insertion Sort":
        time_taken = insertion(data)
        drawData(data, ['Green' for x in range(len(data))])
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
    if clicked.get() == "Heap Sort":
        time_taken = heap(data)
        drawData(data, ['Green' for x in range(len(data))])
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
    if clicked.get() == "Merge Sort":
        time_taken = merge(data)
        drawData(data, ['Green' for x in range(len(data))])
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
    if clicked.get() == "Quick Sort":
        time_taken = quick(data, drawData)
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
    if clicked.get() == "Quick 3 Medians":
        time_taken = quick_tm(data)
        drawData(data, ['Green' for x in range(len(data))])
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)


Mainframe = Frame(root, width=600, height=200, bg="Grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="Grey")
canvas.grid(row=1, column=0, padx=10, pady=5)

clicked = StringVar()
clicked.set("Select Algorithm")
alg_menu = ttk.OptionMenu(Mainframe, clicked, "Select Algorithm", "Bubble Sort", "Selection Sort", "Insertion Sort",
                          "Heap Sort", "Merge Sort", "Quick Sort", "Quick 3 Medians")
alg_menu.grid(row=0, column=0, padx=5, pady=5)

size_entry = Entry(Mainframe)
size_entry.grid(row=0, column=4, padx=5, pady=5)
size_entry.get()
size_entry.insert(0, "Enter Data Size:")

Button(Mainframe, text="Data", bg="Red", command=generate).grid(row=0, column=5, padx=5, pady=5)

Button(Mainframe, text="START", bg="Blue", command=start_algorithm).grid(row=0, column=6, padx=5, pady=5)

Label(Mainframe, text="Time_taken", bg='Grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)


root.mainloop()
