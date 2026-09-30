from calc import add

def test_add_two_numbers():
    # Arragement
    num1 = 5
    num2 = 3
    
    # Action
    result = add(num1, num2)
    
    # Assertion
    assert result == 8, f"Expected 8 but got {result}"
    
def test_add_multiple_numbers():
    # Arragement
    numbers = [1, 2, 3, 4, 5]
    
    
    # Action
    # result = add(1, 2, 3, 4, 5)  # Assuming add function can take multiple arguments
    result = add(*numbers)
    
    # Assertion
    assert result == 15, f"Expected 15 but got {result}"
    
def test_add_no_numbers_return_zero():
    # Action
    result = add()
    
    # Assertion
    assert result == 0, f"Expected 0 but got {result}"