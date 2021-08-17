from tkinter import *
import random
from sort_gui import bubble, insertion, selection, heap, merge, quicks, quick_tm


def generate_compare(size):
    data1 = []
    for _ in range(size):
        data1.append(random.randrange(0, size))
    return data1


def time_all():
    Label(Mainframe, text="                                        ", bg='Grey').grid(row=1, column=1, padx=5, pady=5, sticky=W)
    Label(Mainframe, text="                                        ", bg='Grey').grid(row=2, column=1, padx=5, pady=5, sticky=W)
    Label(Mainframe, text="                                        ", bg='Grey').grid(row=3, column=1, padx=5, pady=5, sticky=W)
    Label(Mainframe, text="                                        ", bg='Grey').grid(row=4, column=1, padx=5, pady=5, sticky=W)
    Label(Mainframe, text="                                        ", bg='Grey').grid(row=5, column=1, padx=5, pady=5, sticky=W)
    Label(Mainframe, text="                                        ", bg='Grey').grid(row=6, column=1, padx=5, pady=5, sticky=W)
    Label(Mainframe, text="                                        ", bg='Grey').grid(row=7, column=1, padx=5, pady=5, sticky=W)
    if var1.get():
        sizeval = int(size_entry.get())
        data1 = generate_compare(sizeval)
        # print("something v1", data1)
        time_taken = bubble(data1)
        # print("something v1", data1)
        l1 = Label(Mainframe, text=time_taken, bg='Grey').grid(row=1, column=1, padx=5, pady=5, sticky=W)
    if var2.get():
        sizeval = int(size_entry.get())
        data1 = generate_compare(sizeval)
        # print("something v2", data1)
        time_taken = selection(data1)
        # print("something v2", data1)
        l2 = Label(Mainframe, text=time_taken, bg='Grey').grid(row=2, column=1, padx=5, pady=5, sticky=W)
    if var3.get():
        sizeval = int(size_entry.get())
        data1 = generate_compare(sizeval)
        # print("something v3", data1)
        time_taken = insertion(data1)
        # print("something v3", data1)
        l3 = Label(Mainframe, text=time_taken, bg='Grey').grid(row=3, column=1, padx=5, pady=5, sticky=W)
    if var4.get():
        sizeval = int(size_entry.get())
        data1 = generate_compare(sizeval)
        # print("something v4", data1)
        time_taken = merge(data1)
        # print("something v4", data1)
        l4 = Label(Mainframe, text=time_taken, bg='Grey').grid(row=4, column=1, padx=5, pady=5, sticky=W)
    if var5.get():
        sizeval = int(size_entry.get())
        data1 = generate_compare(sizeval)
        # print("something v5", data1)
        time_taken = heap(data1)
        # print("something v5", data1)
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=5, column=1, padx=5, pady=5, sticky=W)
    if var6.get():
        sizeval = int(size_entry.get())
        data1 = generate_compare(sizeval)
        # print("something v6", data1)
        time_taken, sorted = quicks(data1)
        # print("something v6", sorted)
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=6, column=1, padx=5, pady=5, sticky=W)
    if var7.get():
        sizeval = int(size_entry.get())
        data1 = generate_compare(sizeval)
        # print("something v7", data1)
        time_taken = quick_tm(data1)
        # print("something v7", data1)
        Label(Mainframe, text=time_taken, bg='Grey').grid(row=7, column=1, padx=5, pady=5, sticky=W)


root = Tk()
root.title("Sort Visualizer")

root.maxsize(900, 600)
root.config(bg="Black")

Mainframe = Frame(root, width=600, height=200, bg="Grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

size_entry = Entry(Mainframe)
size_entry.grid(row=0, column=2, padx=5, pady=5)
size_entry.get()
size_entry.insert(0, "Enter Data Size:")


Label(Mainframe, text="Select algorithm", bg='Grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
var1 = IntVar()
c1 = Checkbutton(Mainframe, text="Bubble sort", variable=var1, bg='Grey').grid(row=1, column=0, padx=5, pady=5,
                                                                               sticky=W)
var2 = IntVar()
c2 = Checkbutton(Mainframe, text="Selection sort", variable=var2, bg='Grey').grid(row=2, column=0, padx=5, pady=5,
                                                                                  sticky=W)
var3 = IntVar()
c3 = Checkbutton(Mainframe, text="Insertion sort", variable=var3, bg='Grey').grid(row=3, column=0, padx=5, pady=5,
                                                                                  sticky=W)
var4 = IntVar()
c4 = Checkbutton(Mainframe, text="Merge sort", variable=var4, bg='Grey').grid(row=4, column=0, padx=5, pady=5, sticky=W)

var5 = IntVar()
c5 = Checkbutton(Mainframe, text="Heap sort", variable=var5, bg='Grey').grid(row=5, column=0, padx=5, pady=5, sticky=W)

var6 = IntVar()
c6 = Checkbutton(Mainframe, text="Quick sort", variable=var6, bg='Grey').grid(row=6, column=0, padx=5, pady=5, sticky=W)

var7 = IntVar()
c7 = Checkbutton(Mainframe, text="Quick 3 medians sort", variable=var7, bg='Grey').grid(row=7, column=0, padx=5, pady=5,
                                                                                        sticky=W)
b1 = Button(Mainframe, text="Compare_Selected", bg="Blue", command=time_all).grid(row=0, column=3, padx=5, pady=5)

root.mainloop()


