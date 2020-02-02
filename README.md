# Algorithms-and-Data-Structures
Python implementation of the most important sorting algorithms (with computational analisys)


LICENSE INFORMATIONS 

Copyright 2018, Alessandro Placido Luise, All rights reserved

You can download, modify and improve this code as you prefer. 

---------------------------------------------------------------

HOW IT WORKS

This Python 3 code was written in few days for a college exam but most importantly for learning purposes. 
I know that some parts of the code could be improved (I have not used object-oriented paradigm) but for now I have no time to do this.

Smart Tester tests a sorting alghoritm (in this case InsertionSort,CountingSort,MergeSort,HeapSort), calculates the execution times and confronts
complexity with n, n^2, nlog2n.  (linear, quadratic, logaritmic)

On the left, you can generate a random array of input lenght, insert an array manually or read it form .txt file. Note that you can do your 
operations also for an input of strings, not also integers.
Once you have your input array, you can sort it with the algorithm you prefer by clicking the button on the right.
On the bottom, you can test your algorithm by giving it some random, ascendent or descendent input for N numbers of times.
For example :

Input random
Initial Lenght : 2000 // Initial array lenght
Multiplication factor : 3 // for each loop, multiplicates 2000*3 and generate an array of 2000 + 6000, 8000 + 6000, 14000 + 6000 elements etc.. 
Loops : 10 // Numbers of loops. Tests the selected algorithm 10 times each time with an input of different size (8000, 14000, 20000 ....)

Once finished, you can show a graph that confronts the calculated samples with n, n^2, nlogn (Show results button). The execution time is in microseconds.

The tree subprogram was written in C++ and allows you to do some operations on binary trees. It can test only the insert operation.

EXECUTABLE : 
I have included the executable, so you can use this program without installing python libraries or c++ libraries (folder "dist", click on "english-ver" application to run it).

IMPORTANT : There is no loading screen, so it can take a while to start due to loading modules and stuff.

IDE : Intellij Idea
