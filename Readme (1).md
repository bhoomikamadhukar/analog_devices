The projects aim was to write python code to search a directory for files that match the extension and count the number of lines in that file. 
I have accomplished this task using glob. It is a python library that helps us walk through all paths that match a pattern and find matching files. 
The code works properly and I have handles edge cases like :
1. If directory does not exist, display a message
2. If the line count is 0 in all files, the average lines is 0 and there is no Zero division error. 
3. If file does not exist, display a message. 

The code can be found in main.py, pytests in test_cases.py and I have a dummy folder to show it works. 
Here is the output sample:
![alt text](https://github.com/bhoomikamadhukar/Analog-Devices/blob/main/images/out.png)

The code passes pylint, test cases and can handle exceptions well. 


