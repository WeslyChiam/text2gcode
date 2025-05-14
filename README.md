# text2gcode

## A python script to convert words and number to gcode for gravier. 

Requirements:
1. Python 3.10 or above(This .py script use match case statement, which is newly introduce in Python version 3.10)
    - Best way to know which version Python install in your machine, open console or terminal and type `Python`, it will show the version it install once enterd
    - [Click this link if Python 3.10 is not install](https://www.python.org/downloads/release/python-3100/)
2. A cnc machine(Not necessary if you only want to test the output)
3. cnc machine control software (grbl)
    - There are few software that can run gcode file, I would recommend [Candle](https://github.com/Denvi/Candle)
## Notes:
  - If no Python 3.10 or higher installed and you prefer to not install, it is recommended to use .exe instead.
## Steps:
 1. Run `main.py`(by console) or `main.exe`
 2. Fill in requirements for each text field,
    - `Text` holds the words or number user wish to convert into G code.
    - `Z` represent as the depth for gravier cut through a board.
    - `F` represent as the feedrate or speed.
    - `Font Size` means size of the Text, each character is measured by (width x height) in mm unit.
    - `Unit` offers to choose whether the text will be done in mm unit or cm unit. 
    - `Drill Speed` holds the value to tell the machine how fast the drill will be run
    - The checkbox `Include Box Surround` will cover the text in a rectangle box.
  3. After finish fill up, proceed by press `Convert` button
  4. The script run convert the input by character and show info box when done
  5. `(Text).nc` is a file ready to be execute by cnc machine
  
Any issues or bug found, please inform and I will try to correct it. 
Thanks. 
