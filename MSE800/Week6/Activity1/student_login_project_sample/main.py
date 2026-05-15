#import student login submit assigment and view grades from the users.py
from users import (
    student_login,
    submit_assignment,
    view_grades
)

#student login project main function
def main():
    """Initiate the student login"""
    student_login("Mohammad")
    """After login the student can submit the assignemnt"""
    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )
    #The view grades argument should be match the student logged in
    """After submission of the assignment the student can view the grades"""
    view_grades("Alex")


if __name__ == "__main__":
    main()
