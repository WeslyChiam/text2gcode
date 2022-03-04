# text2gcode

A python script to convert words and number to gcode for gravier. 

Requirements:
  1. Python 3.10 or above(This .py script use match case statement, which is newly introduce in Python version 3.10)
  
Notes: 
  If no Python 3.10 or higher installed, it is recommended to use .exe 
  
Steps:
  1. Run main.py or main.exe from dist folder 
  2. Fill in requirements for each text field,<br>
    'Text' holds the words or number user wish to convert into G code, <br>
    'Z' represent as the depth for gravier cut through a board,<br> 
    'F' represent as the feedrate or speed,<br>
    'Spacing' means the space between each charater. <br>
  3. After finish fill up, proceed by press 'Convert' button 
  4. The script run convert the input by character and show info box when done 
  5. There will be two output from the script:<br>
    'Output.txt' is a text field holds the g code command,<br>
    'Command.nc' is a file ready to be execute 
    
Any issues or bug found, please inform and I will try to correct it. 
Thanks. 
