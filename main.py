#!/usr/bin/env python3
import tkinter
import calculator

class Calc:
    def __init__(self):
        self.calc = calculator.Calculator()
        self.first = 0
        self.second = 0

    def evaluate(self, option):
        self.calc.x = self.first
        self.calc.y = self.second
        if self.calc.operation == "":
            self.calc.operation = option
            print("no operation yet")
            return
        

        self.first = self.calc.evaluate()
        self.second = 0
        
        result_window.configure(text = self.first)

    def test(self):
        self.first = 5
        self.second = 3
        result_window.configure(text = self.first)

    def clear(self):
        self.calc.operation = ""
        self.first = 0
        self.second = 0
        

c = Calc()


window = tkinter.Tk()
window.title("calculator")
window.geometry('300x500')
window.resizable(False, False)

result_window = tkinter.Label(window,
                              text= "result window",
                              fg= "white", 
                              relief="solid",
                              anchor = "e",
                              width = 20,
                              height = 3,
                              pady = 0,
                              padx = 20,
                              font = ("Kozuka Mincho Pro M", 20))
#result_window.pack(side = "top", expand = "False")
result_window.grid(row = 0, column = 0)

frame_row_one = tkinter.Frame(window)
frame_row_one.grid(row = 1, column = 0)

multiply_button = tkinter.Button(frame_row_one,
                                 text = "X",
                                 relief = "solid",
                                 command = lambda: c.evaluate("multiply"),
                                 width = 3,
                                 height = 3,
                                 bd = 0,
                                 font = ("Kozuka Mincho Pro M", 20),
                                 repeatdelay=1000,
                                 repeatinterval=100
                                 )
#multiply_button.pack()
multiply_button.pack(side = "right")

divide_button = tkinter.Button(frame_row_one,
                                 text = "÷",
                                 relief = "solid",
                                 command = lambda: c.evaluate("divide"),
                                 width = 3,
                                 height = 3,
                                 bd = 0,
                                 font = ("Kozuka Mincho Pro M", 20)
                                 )
divide_button.pack(side = "right")

test_button = tkinter.Button(frame_row_one,
                                 text = "test",
                                 relief = "solid",
                                 command = c.test,
                                 width = 3,
                                 height = 3,
                                 bd = 0,
                                 font = ("Kozuka Mincho Pro M", 20)
                                 )
test_button.pack(side = "right")

del_button = tkinter.Button(frame_row_one,
                                 text = "C",
                                 relief = "solid",
                                 command = c.clear,
                                 width = 3,
                                 height = 3,
                                 bd = 0,
                                 font = ("Kozuka Mincho Pro M", 20)
                                 )
del_button.pack(side = "left")



window.mainloop()