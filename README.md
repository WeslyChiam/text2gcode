# text2gcode

A python script to convert words and number to gcode for gravier. 

Requirements:
  1. Python 3.10 or above(This .py script use match case statement, which is newly introduce in Python version 3.10)
  
Notes: 
  If no Python 3.10 or higher installed, it is recommended to use .exe from folder dist 
  
Steps:
  1. Run main.py or main.exe from dist folder 
  2. Fill in requirements for each text field 
    2.1 'Text' holds the words or number user wish to convert into G code 
    2.2 'Z' represent as the depth for gravier cut through a board 
    2.3 'F' represent as the feedrate or speed
    2.4 'Spacing' means the space between each charater 
  3. After finish fill up, proceed by press 'Convert' button 
  4. The script run convert the input by character and show info box when done 
  5. There will be two output from the script:
    5.1 'Output.txt' is a text field holds the g code command 
    5.2 'Command.nc' is a file ready to be execute 
    
Any issues or bug found, please inform and I will try to correct it. 
Thanks. 
