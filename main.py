# imports the class LogLine
from parse import parse

# user input log line
log_line_input = input("Enter log line: ")

# LogLine object is stored in a variable
log_line_object = parse(log_line_input)
# calls the function in the object to display table with enriched log data
log_line_object.display_enriched_log()
