# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

> As a user
> So that I can keep track of my tasks
> I want to check if a text includes the string #TODO


## 2. Design the Function Signature


```python
def test_check_for_todo():
    # 'text' (string): The inpput text in which we want to check for the presence of "#TODO"
    #  has_todo (bool): a boolean value indicating whether the text includes "#TODO"
```

## 3. Create Examples as Tests


```python
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
```
## 4. Implement the Behaviour



```python
# EXAMPLE


"""
Check if the text contains the string "#TODO"
"""
def check_for_todo(text):
    has_todo = "#TODO" in text.upper()
    return has_todo

"""
Run the tests
"""
test_check_for_todo()

```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
