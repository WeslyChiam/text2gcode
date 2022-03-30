# text2gcode

A python script to convert words and number to gcode for gravier. 

Requirements:
  <ol>
  <li>Python 3.10 or above(This .py script use match case statement, which is newly introduce in Python version 3.10)</li>
  <ul>
  <li>Best way to know which version Python install in your machine, open console or terminal and type "Python", it will show the version it install once enterd</li>
  <li><a href="https://www.python.org/downloads/release/python-3100/"> Click this link if Python 3.10 is not install</a></li>
  </ul>
  <li>a cnc machine(Not necessary if you only want to test the output)</li>
  <li>cnc machine control software (grbl)<li>
  <ul>
    <li>There are few software that can run gcode file, I would recommend <a href="https://github.com/Denvi/Candle">Candle</a>
  </ul>
  </ol>
  
Notes: 
  <ul>
  <li>If no Python 3.10 or higher installed and you prefer to not install, it is recommended to use .exe </li>
  </ul>
  
  
Steps:
<ol>
<li>Run main.py(by console) or main.exe</li>
<li>Fill in requirements for each text field,</li>
  <ul>
  <li>'Text' holds the words or number user wish to convert into G code.</li>
  <li>'Z' represent as the depth for gravier cut through a board.</li>
  <li>'F' represent as the feedrate or speed.</li>
  <li>'Font Size' means size of the Text, each character is measured by width x height in cm unit.</li>
  <li>'Unit' offers to choose whether the text will be done in mm unit or cm unit</li>
  <li>'Drill Speed' holds the value to tell the machine how fast the drill will be run</li>
  <li>The checkbox "Include Box Surround" will cover the text in a rectangle box.</li>
  </ul>
<li>After finish fill up, proceed by press 'Convert' button</li>
<li>The script run convert the input by character and show info box when done</li>
<li>There will be two output from the script:</li>
  <ul>
  <li>'Command.nc' is a file ready to be execute by cnc machine</li>
  </ul>
</ol>
  
Any issues or bug found, please inform and I will try to correct it. 
Thanks. 
