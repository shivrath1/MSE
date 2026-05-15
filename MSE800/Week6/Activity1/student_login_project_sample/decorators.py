from datetime import datetime


#Decorator function used to log activity details
def log_activity(func):
#Wrapper function with arguments
    def wrapper(*args, **kwargs):
        print("===================================")
        #Prints the function name being executed
        print(f"Function: {func.__name__}")
        #Print current date and time
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        #Execute the original function
        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper
