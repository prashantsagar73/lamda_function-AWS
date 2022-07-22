"""
Example test cases to test pytest, pylint and code coverage
"""

from example import pass_me
from example import fail_me


def test_pass_me():
    """Assert pass_me output and get code coverage for that method"""
    assert pass_me() == 1


def test_high_coverage():
    """
    Assert fail_me output and get code coverage for
    that method resulting in high code coverage
    """
    assert fail_me() == 0


# def test_low_coverage():
#    """Do not call fail_me resulting in low code coverage"""
#    i = 1
#    assert i == 1


# def test_fail_me():
#     """Failing assert to test when pytest fails"""
#     assert fail_me() == 1
