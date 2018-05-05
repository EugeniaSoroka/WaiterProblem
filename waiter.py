import Tkinter
import tkMessageBox
from Tkinter import *
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Button as mButton
import numpy as np
import random
from math import sqrt, pi
import wx
from scipy.spatial import ConvexHull
import tkFont


LIM = 1.05
R = 1.0
PAUSE = 0.5
STOP = False

area = pi * pow(R, 2)

x_pts = []
y_pts = []
xc_r = 0
yc_r = 0
LEN = 0

class GUI:

    def __init__(self, master):
        self.master = master
        master.title("Waiter Problem")

        self.label = Label(master, text="Select a method for inputting points")
        self.label.config(font=("Helvetica", 22), padx = 150, pady = 50)
        self.label.pack()

        photo = PhotoImage(file="waiter.gif")
        w = Label(master, image=photo)
        w.photo = photo
        w.pack()
        self.label = Label(master)
        self.label.config(pady = 10)
        self.label.pack()

        helv = tkFont.Font(family='Helvetica', size=16)

        self.rand_button = Button(master, text="Random input", command=self.rand_input)
        self.rand_button.config(font=helv)
        self.rand_button.config(bg='white', fg='black', activebackground='lightblue', activeforeground='darkblue')
        self.rand_button.pack(pady=20)

        self.import_button = Button(master, text="Import a file", command=self.import_file)
        self.import_button.config(font=helv)
        self.import_button.config(bg='white', fg='black', activebackground='lightblue', activeforeground='darkblue')
        self.import_button.pack(pady=20)

        self.manual_button = Button(master, text="Input manually", command=self.manual_input)
        self.manual_button.config(font=helv)
        self.manual_button.config(bg='white', fg='black', activebackground='lightblue', activeforeground='darkblue')
        self.manual_button.pack(pady=20)
        self.label = Label(master)
        self.label.config(pady = 20)
        self.label.pack()


        global x_pts
        x_pts = []
        global y_pts
        y_pts = []


    def alg(self):
        def nearest(x, y, xt, yt):
            a_vector = np.asarray([np.asarray([x[k], y[k]]) for k in range(len(x))])
            b = np.asarray([xt, yt])
            idx = np.array([np.linalg.norm(a-b) for a in a_vector]).argmin()
            #k = x_pts.index(float(a_vector[idx][0]))
            k = notvisited[idx]
            return k

        x = []
        y = []
        notvisited = [k for k in range(LEN)]
        visited = []
        for i in range(LEN-1):
            if i == 0:
                k = nearest(x_pts, y_pts, xc_r, yc_r)
            else:
                k = nearest([x_pts[notvisited[k]] for k in range(len(notvisited))],\
                    [y_pts[notvisited[k]] for k in range(len(notvisited))],\
                    (i+2)*xc_r - sum([x_pts[visited[k]] for k in range(len(visited))]),\
                    (i+2)*yc_r - sum([y_pts[visited[k]] for k in range(len(visited))]) )
            x.append(x_pts[k])
            y.append(y_pts[k])
            visited.append(k)
            notvisited.remove(k)
        i = LEN - 1
        k = notvisited[0]
        x.append(x_pts[k])
        y.append(y_pts[k])
        visited.append(k)
        notvisited.remove(k)

        return x, y



    def solve_click(self, event):
        plt.close()

        global LEN
        LEN = len(x_pts)
        global xc_r
        xc_r = sum(x_pts) / LEN
        global yc_r
        yc_r = sum(y_pts) / LEN
        
        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        fig.canvas.set_window_title('Solution to your problem') 
        ax1.set_xlim([-LIM, LIM])
        ax1.set_ylim([-LIM, LIM])
        ax2.set_xlim([-LIM, LIM])
        ax2.set_ylim([-LIM, LIM])
        ax1.set(adjustable='box-forced', aspect='equal')
        ax2.set(adjustable='box-forced', aspect='equal')
        ax1.set_title('Initial '+str(len(x_pts))+' points')
        ax2.set_title('Solution', fontsize=14)

        ax1.plot(x_pts, y_pts, "o", color='steelblue')
        circ1 = plt.Circle((0, 0), 1, color='blue', fill=False)
        ax1.add_artist(circ1)
        #ax2.plot(x_pts, y_pts, "o")
        circ2 = plt.Circle((0, 0), 1, color='blue', fill=False)
        ax2.add_artist(circ2)

        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())

        plt.show(block=False)
        if STOP == False: plt.pause(PAUSE)
        
        out = self.alg()
        x = out[0]
        y = out[1]
        xc = []
        yc = []
        path_area = 0
        t = ax1.text(LIM-0.45, LIM+0.2, 'Area of a convex hull = '\
            +str(round(path_area, 6))+' = '+str(round((100*path_area)/area, 2))+'%'+" of total area", fontsize=12)
        #path_len = 0
        #t = ax1.text(LIM-0.2, LIM+0.1, 'Total length of path = '+str(round(path_len, 2)), fontsize=11)
        for i in range(len(x)):
            if i == 0:
                ax2.plot(xc_r, yc_r, "o", color='red')
                plt.show(block=False)
                if STOP == False: plt.pause(1)
                else: raw_input("pause")
                ax2.plot(x[i], y[i], "o", color='darkorange')
                ax2.annotate(i+1, xy = (x[i], y[i]), textcoords = 'data', fontsize = 11)
                xc.append(x[i])
                yc.append(y[i])
            else:
                ax2.plot(x[i-1], y[i-1], "o", color='steelblue')
                ax2.plot(x[i], y[i], "o", color='darkorange')
                ax2.annotate(i+1, xy = (x[i], y[i]), textcoords = 'data', fontsize = 11)
                xc.append(sum(x[:(i+1)])/(i+1))
                yc.append(sum(y[:(i+1)])/(i+1))
                ax2.plot(xc, yc, ".", color = 'limegreen')
                #ax2.plot(xc, yc, "r.-")
                if (i >= 2): 
                    points = np.asarray([[xc[k], yc[k]] for k in range(i+1)])
                    hull = ConvexHull(points)
                    plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], 'lightgreen', alpha=0.15)
                    ax2.plot(xc_r, yc_r, "o", color='red')
                    #for simplex in hull.simplices:
                    #    ax2.plot([points[simplex[0]][0], points[simplex[1]][0]], \
                    #        [points[simplex[0]][1], points[simplex[1]][1]], 'r--')
                    path_area = hull.volume
                    t.set_text('Area of a convex hull = '\
                        +str(round(path_area, 6))+' = '+str(round((100*path_area)/area, 2))+'%'+" of total area")
                #path_len += sqrt(pow(x[len(x)-2] - x[len(x)-1], 2) + pow(y[len(x)-2] - y[len(x)-1], 2))
                #t.set_text('Total length of path = '+str(round(path_len, 2)))
            plt.show(block=False)
            if STOP == False: plt.pause(PAUSE)
            else: raw_input("pause")
        ax2.plot(x[len(x)-1], y[len(x)-1], "o", color='steelblue')
        for simplex in hull.simplices:
            ax2.plot([points[simplex[0]][0], points[simplex[1]][0]], \
            [points[simplex[0]][1], points[simplex[1]][1]], 'g--')
        plt.show(block=False)
        

    def show_input(self):

        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Input points') 
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        ax = plt.gca()
        ax.set_xlim([-LIM, LIM])
        ax.set_ylim([-LIM, LIM])
        ax.set(adjustable='box-forced', aspect='equal')

        l, = ax.plot(x_pts, y_pts, "o")
        circ = plt.Circle((0, 0), 1, color='blue', fill=False)
        ax.add_artist(circ)
        ax.set_title(str(len(x_pts))+" input points", fontsize=14)

        def onpick(event):
            m_x, m_y = event.x, event.y
            x, y = ax.transData.inverted().transform([m_x, m_y])
            if (-LIM <= x and x <= LIM and -LIM <= y and y <= LIM):
                if (pow(x, 2) + pow(y, 2) >= pow(R, 2)):
                    tkMessageBox.showerror("Error","Point must be INSIDE a circle")
                elif ((x in x_pts) and (y in y_pts)):
                    tkMessageBox.showerror("Error","Points can't COINCIDE")
                else:
                    x_pts.append(x)
                    y_pts.append(y)
                    l.set_xdata(x_pts)
                    l.set_ydata(y_pts)
                    ax.set_title(str(len(x_pts))+" input points", fontsize=14)
                    fig.canvas.draw()
                    #print(x,y)

        fig.canvas.mpl_connect('button_press_event', onpick)


        axcut = plt.axes([0.75, 0.5, 0.1, 0.075])
        bcut = mButton(axcut, 'Solve it!', color='white', hovercolor='lightblue')
        bcut.label.set_fontsize(12)
        bcut.on_clicked(self.solve_click)

        plt.show()



    def rand_input(self):
        x = []
        y = []
        global x_pts
        x_pts = []
        global y_pts
        y_pts = []

        LEN = int(round(np.random.uniform(10.0, 20.0)))
        for i in range(LEN):
            x = np.random.uniform(-R, R)
            y = np.random.uniform(-R, R)
            if (pow(x, 2) + pow(y, 2) < pow(R, 2) and not((x in x_pts) and (y in y_pts))):
                x_pts.append(x)
                y_pts.append(y)

        self.show_input()


    def import_file(self):
        global x_pts
        x_pts = []
        global y_pts
        y_pts = []

        pullData = open("files/f0.txt", "r").read()
        dataList = pullData.split('\n')
        for eachLine in dataList:
            if len(eachLine) > 1:
                xstr, ystr = eachLine.split(',')
                x = float(xstr)
                y = float(ystr)
                x_pts.append(x)
                y_pts.append(y)
        self.show_input()


    def manual_input(self):
        global x_pts
        x_pts = []
        global y_pts
        y_pts = []
        self.show_input()



root = Tk()
my_gui = GUI(root)
root.mainloop()