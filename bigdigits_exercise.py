#!python3
# bigdigits.py

import sys


Zero =  ["  ***  ",
         " *   * ",
         "*     *",
         "*     *",
         "*     *",
         " *   * ",
         "  ***  "]
One =   [" * ",
         "** ",
         " * ",
         " * ",
         " * ",
         " * ",
         "***"]
Two =   [" *** ",
         "*   *",
         "*  * ",
         "  *  ",
         " *   ",
         "*    ",
         "*****"]
Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four =  ["   *  ",
         "  **  ",
         " * *  ",
         "*  *  ",
         "******",
         "   *  ",
         "   *  "]
Five =  ["*****",
         "*    ",
         "*    ",
         " *** ",
         "    *",
         "*   *",
         " *** "]
Six =   [" *** ",
         "*    ",
         "*    ",
         "**** ",
         "*   *",
         "*   *",
         " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine =  [" ****",
         "*   *",
         "*   *",
         " ****",
         "    *",
         "    *",
         "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    if len(sys.argv) > 1:
      digits = sys.argv[1]
    else:
      digits = input("Enter number: ")
    row = 0
    while row < 7:
        line = " | "
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for c in digit[row]:
                if c == '*':
                    c = str(number)
                line += c
            line += " | "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
