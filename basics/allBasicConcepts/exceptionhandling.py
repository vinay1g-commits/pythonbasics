#python handles errors using try except block
try:
    results = 10/0
except ZeroDivisionError:
    print("Divisional error")

"""
try-except helps handle exceptions gracefully, ensuring that the 
program doesn’t crash unexpectedly. This is crucial in automation 
testing to manage errors during script execution.
"""