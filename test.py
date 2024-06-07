#!/usr/bin/env python3
import calculator

calc = calculator.Calculator()

calc.x = 5
calc.y = 3
calc.operation = "multiply"

print(calc.evaluate()) # prints 15
calc.operation = ""
print(calc.evaluate()) # prints None