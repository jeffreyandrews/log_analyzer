# log_analyzer
This is a python log analyzer that reads a file of logs and gives the user a summary of the file. After running this program you will be prompted to enter the name of the .txt file log file that you wish to get a summary of. When inputting the file's name, do not include .txt, as that is taken care of by the program. The program then runs several checks and reports back to the user with a basic summary that includes the number of entries, how many of each severity type there was, critical entries, and how many errors there were of each service type. I included several sample log files that are great for testing the program, but the program will work all the same if you create your own .txt file in the same layout as my sample files.
I did this project because I recently learned how to work on outside files from inside a python program and this was a great way to practice that skill in a cybersecurity project. I learned so much during this project. Notably, I improved my skills working with dictionaries, file I/O, writing docstrings, string parsing, and having many functions work together to consistently provide a reliable result.

----------------------------------------------------------------------------------

Example log input:

2024-03-15 14:23:05 INFO DatabaseService Connection established successfully

----------------------------------------------------------------------------------


Example summary(log2.txt):

=== LOG SUMMARY ===

Total entries: 10

INFO: 0

WARNING: 1

ERROR: 7

CRITICAL: 2


=== CRITICAL ALERTS ===

2024-04-01 09:00:15 CRITICAL SystemMonitor Database unreachable shutting down dependent services


2024-04-01 09:00:45 CRITICAL SystemMonitor All reconnect attempts exhausted manual intervention required


=== TOP ERRORS BY SERVICE ===

DatabaseService - 4 occurrence(s)

SystemMonitor - 2 occurrence(s)

AuthService - 2 occurrence(s)

APIGateway - 1 occurrence(s)
