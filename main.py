#!/usr/bin/env python3
import tkinter
import calculator

class Calc:
    def __init__(self):
        self.calc = calculator.Calculator()
        self.first = 0
        self.second = 0
        self.operation = ""
        self.second_input = False

    def evaluate(self, option):
        self.calc.x = self.first
        self.calc.y = self.second
        if (option == "multiply" or option == "divide" or 
            option == "add" or option == "subtract"):
            if self.operation != option:
                self.operation = option
                print("no operation yet")
                return
            if self.second_input == False:
                print("second input not detected!")
                return

        match option:
            case "multiply":
                self.first = self.calc.multiply()
            case "divide":
                self.first = self.calc.divide()
            case "add":
                self.first = self.calc.add()
            case "subtract":
                self.first = self.calc.subtract()
            case "percent":
                self.first = self.calc.percent()
            case "plusminus":
                self.first = self.calc.plusminus()
            case _:
                raise ValueError
            
        self.operation = ""
        self.second = 0 # Reset the second part to zero
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

frame_row_one = tkinter.Frame(window, 
                              padx = 0,
                              pady = 0,
                              width = 20,
                              height = 5,
                              bd = 0)
frame_row_one.grid(row = 1, column = 0)

multiply_button = tkinter.Button(frame_row_one,
                                 text = "X",
                                 relief = "solid",
                                 command = lambda: c.evaluate("multiply"),
                                 bd = 0,
                                 font = ("Kozuka Mincho Pro M", 60)
                                 )
#multiply_button.pack()
multiply_button.pack(side = "right", expand = "True")

divide_button = tkinter.Button(frame_row_one,
                                 text = "÷",
                                 relief = "solid",
                                 command = lambda: c.evaluate("divide"),
                                 bd = 0,
                                 font = ("Kozuka Mincho Pro M", 60)
                                 )
divide_button.pack(side = "right")

percent_button = tkinter.Button(frame_row_one,
                                 text = "%",
                                 relief = "solid",
                                 command = lambda: c.evaluate("percent"),
                                 bd = 0,
                                 font = ("Kozuka Mincho Pro M", 60)
                                 )
percent_button.pack(side = "right")

del_button = tkinter.Button(frame_row_one,
                                 text = "C",
                                 relief = "solid",
                                 command = c.clear,
                                 bd = 0,
                                 font = ("Kozuka Mincho Pro M", 60)
                                 )
del_button.pack(side = "left")



window.mainloop()