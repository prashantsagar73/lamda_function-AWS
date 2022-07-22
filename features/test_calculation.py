"""
Example BDD test steps
"""
from pytest_bdd import scenario, given, when, then

context = {}

@scenario('calculation.feature', 'One plus one')
def test_calculation():
    """test method to link steps with scenario"""
    pass


@given('I have one')
def step_i_have_one():
    """Store one in the context"""
    context['one'] = 1


@given('I have another one')
def step_i_have_another():
    """Store another in the context"""
    context['another'] = 1


@when('I add them')
def step_i_add_them():
    """Add one and another and store the result in the context"""
    context['result'] = context['one'] + context['another']


@then('I get two')
def step_i_get_two():
    """Confirm calculation result"""
    assert context['result'] == 2
