#There are two common uses of triple quotes:

#1.Single-Line Strings: You can use triple quotes to create single-line strings just like regular quotes:
single_line_string = """This is a single-line string."""

# 2.Multi-Line Strings (Docstrings):
# Triple quotes are often used to create multi-line strings
# for documenting functions, classes, or modules.
#  This is called a docstring. It's a common practice to include 
# docstrings at the beginning of these constructs to explain their 
# purpose and usage:

def my_function(arg1, arg2):
    """
    This is a docstring that explains what the function does.
    
    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.
        
    Returns:
        bool: The result of some operation.
    """
    # Function code here
