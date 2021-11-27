'''

From Tkinter Tutorial Python 3.4
https://www.youtube.com/watch?v=JQ7QP5rPvjU&index=7&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk



'''

import matplotlib
matplotlib.use("TkAgg")     # Backend of matplotlib
#   This allows you to push a matplotlib graph to canvas and use a toolbar to navigate:
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk     # CSS for Tkinter
from matplotlib import style


# Global Variables

LARGE_FONT = ("Verdana", 12)



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs): # args = arguments/ Key Word Arguments (Dictionaries).

        print("Initializing the TK class and creating a container")
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default=None)   # must be properly formatted ".ico" at 16x16 px

        tk.Tk.wm_title(self, "Sea of BTC Client")

        container = tk.Frame(self)  # Frame is edge of window
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        print("Generating the frames")
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            print("Generating " + str(F))
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        print(self.frames)

        print("Initializing the Start Page")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        print("Showing the frame " + str(cont))
        frame = self.frames[cont]
        frame.tkraise()     # Raise to front

    def test(self, statement):
        print("Test Statement " + str(statement))


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Test Statement",
                            command=lambda: controller.test('hello'))
        button2.pack()

        button3 = ttk.Button(self, text="Visit Page 3",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)



        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="To Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Back Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Don't you dare press this button!!!",
                                 command=lambda: controller.show_frame(StartPage))
        button1.pack()

        '''
        Add canvas, show canvas, place things in Canvas and add navigation bars
        '''
        print("Creating the figure")
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)      # 1 x 1...plot number 1.  ("111")
        a.plot([1,2,3,4,5,6,7,8], [3,2,3,4,6,5,4,7])    # Dummy plot

        print("Putting the canvas to the frame")

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        print("Creating the toolbar for the canvas")

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH,  expand=True)




# This is why SeaofBTCapp is passed on as "controller" in subsequent class __init__ calls.  This is the main class.
print("Running the application")
if __name__ == "__main__":
    app = SeaofBTCapp()
    app.mainloop()