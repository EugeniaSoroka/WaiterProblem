## WAITER PROBLEM: Placing glasses on a tray

The problem can be formulated as follows:
You serve drinks in a restaurant and must carry a tray with one hand. As you load glasses onto the tray, the tray can become unstable – your hand must stay under the center of mass of the glasses. There are particular spots on the tray where the glasses must be placed, but you are free to place the glasses in any order you want.
- How should you do it to make sure the tray stays balanced?

Formally, we can model this problem as follows, thinking of the glasses as “points” in the plane.
Let S = {P1, ... , Pn} be a set of n points in the plane. Let C(X) denote the center of mass of the set X ⊆ S of points. Our goal is to ﬁnd a “good” ordering (permutation π) of the points S, (Pπ1 , Pπ2 , ... , Pπn), so that the center of mass, Cj = C({Pπ1 , Pπ2 , ... , Pπj}), of the ﬁrst j points (j = 1, 2, . . . , n) in the order does not “move around” too much. The “score” for a given ordering π might be defined in several ways, but here I am trying to minimize the total area of the convex hull of the centers of mass.



### Running Instructions
(checked for Ubuntu 16.04 and Windows 10)

To run the program, first make sure that you have Python 2.7+ installed on your system, as well as all the packages listed in Prerequisites (below). Then simply run the command:
```
python waiter.py
```
There are three input options:
1. Random input
2. Import a file
3. Input manually

When 2. Import a file is selected, program automatically selects file f0.txt. To import another file, you can change the name of the file in line 264 of waiter.py - simply specify your path and file name instead of "files/f0.txt". When using your own file, make sure that you comply with the format:

Each line contains a pair of x and y coordinates of a point, separated by "," - without any spaces



### Prerequisites
1. wx

To intall wx, run:
```
pip install wxPython
```
2. matplotlib
3. numpy
4. random
5. math
6. scipy

For 2-6, run command:
```
pip install package-name
```
having replaced package-name with the corresponding package name (e.g. matplotlib) to install it.



### Copyright and attribution
Created by Eugenia Soroka

Ph.D. Student

Stony Brook University, NY

CSE555 / AMS545 (Computational Geometry)

Spring 2018