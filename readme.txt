"""
Pruthvik Kakadiya
Design & Analysis of algorithms project
Id : 1001861545
Project 1 : Sorting Algorithms
language : python 
"""

1: install matplotlib library
2: install tkinter library for GUI
3: run main.py for normal execution 


--->  (on terminal)python3 main.py
-----------------------------------------------------------------
      (enter your choice..)
1: Compare time complexities of all algorithms using user given different Dataset sizes 
2: Run sorting algorithm and provide Sorted Dataset using User Given Dataset 
3:GUI to visualize sort
4:GUI to compare time complexity of algorithms
5: exit

--->  1 (....choice 1....)

	(enter no of how many different sizes of dataset you want to      	 compare, eg.1, 2, 3, 4, 5..)

--->	Enter no of how many different Dataset sizes you want to be compared: 2

	(enter different sizes of dataset, eg.500, 1000, 2000, 	 	 5000...)

--->	Enter different Dataset sizes (followed by enter): 
	1000
	2000
--->	Dataset sizes are:  [1000, 2000]
	1000 Data_size Sorted by BubbleSort   0.05189323425292969
	2000 ...
	...
	...
	...
	1000 ...
	2000 Data_size Sorted by QuickSort with three medians   	  		0.004981517791748047

--->	Dataset sizes are:  [1000, 2000]
	Bubble sort    :  [0.05189323425292969, 0.30518102645874023]
	Selection sort :  [0.027926206588745117,0.11369037628173828]
	Insertion sort :  [0.032911062240600586, 0.1366422176361084]
	Heap sort      :  [.003995895385742187,0.007978439331054688]
	Merge sort     :  [0.002992153167724609,0.00498461723327636]
	Quick sort     :  [0.00099778175354003,0.003988981246948242]
	Quick 3 medians:  [0.002992153167724609,0.00498151779174804]

	(matplotlib will show a graph of time complexities for give 	 dataset sizes)

---> 2   (...choice 2...)

		(select one algorithm..)
Choose from following sorting algorithm
1:Bubble sort ... 2 .. 3 .. 4 .. 5 .. 6 .. 7:Quick 3 medians sort
8: exit
---> 1    (.... 1 for bubble sort...)
--->	Enter the list of numbers separated by spaces: 
	10 25 150 1 0 24 35 1 47 60 2
  
		(...will show unsoted and sorted datasets...)
---> [10, 25, 150, 1, 0, 24, 35, 1, 47, 60, 2]
	[0, 1, 1, 2, 10, 24, 25, 35, 47, 60, 150]
-----------------------------------------------------------------

5: run tk.py and tk_compare.py for GUI
  (....choice 3 or 4....)

-----------------------------------------------------------------
For Gui
-----------------------------------------------------------------
--->  (on terminal)python3 tk.py
--->  (on terminal)python3 tk_compare.py
-----------------------------------------------------------------