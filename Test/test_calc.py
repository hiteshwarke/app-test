from calc import add

def test_add_two_numbers():
    # Arragement
    num1 = 5
    num2 = 3
    
    # Action
    result = add(num1, num2)
    
    # Assertion
    assert result == 8, f"Expected 8 but got {result}"