"""
Example code file to test pytest, pylint and code coverage
"""


def pass_me():
    """
    This method returns 1
    """
    i = 1
    return i


def fail_me():
    """
    This method returns 0
    """
    i = 0
    print("Another line of code")
    return i
