# Exception handling allows Python programs to gracefully handle runtime errors without crashing.
# The try-except block is used to catch and respond to exceptions.

# try: Code that might raise an error.
# except: Code that handles the error.
# else: Executes if no exception occurs.
# finally: Always executes, error or not.
# You can catch specific errors like ZeroDivisionError, ValueError.

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by Zero!")
    else:
        print("Result is:", result)
    finally:
        print("Execution completed.")

divide(10, 2)

divide(5, 0)
