from lib.todo_checker import check_for_todo

def test_check_for_todo():

    """
    Test with a text containing "#TODO" at the beginning 
    """
    result = check_for_todo("#TODO: Finish the project")
    assert result == True 

    """
    Test with a text containing "#TODO" at the middle 
    """
    result = check_for_todo("Please #TODO: Review the report")
    assert result == True 

    """
    Test with a text containing "#TODO" at the end
    """
    result = check_for_todo("Don't forget to #TODO")
    assert result == True 

    """
    Test with a text that does not containt "#TODO"
    """
    result = check_for_todo("This is a regular text")
    assert result == False

    """
    Test with an empty text
    """
    result = check_for_todo("") 
    assert result == False

    print("All tests passed.")
