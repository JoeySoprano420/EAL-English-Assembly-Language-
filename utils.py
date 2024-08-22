import traceback

def handle_error(error):
    """
    Handles errors by logging them and providing a user-friendly message.
    
    Args:
        error (Exception): The error or exception to be handled.
        
    Returns:
        None
    """
    # Log the full traceback of the error
    print("An error occurred:")
    traceback.print_exception(type(error), error, error.__traceback__)
    
    # Provide a user-friendly message
    print("Oops! Something went wrong. Please check the error details above.")

def format_code(code):
    """
    Formats code to ensure proper indentation and syntax.

    Args:
        code (str): The code to be formatted.

    Returns:
        str: The formatted code.
    """
    import re
    
    # Basic formatting rules:
    # - Ensure single spaces after keywords
    # - Indent code properly
    formatted_code = code
    
    # Normalize newlines
    formatted_code = re.sub(r'\r\n', '\n', formatted_code)
    formatted_code = re.sub(r'\r', '\n', formatted_code)
    
    # Replace multiple newlines with a single newline
    formatted_code = re.sub(r'\n\s*\n', '\n\n', formatted_code)
    
    # Basic indentation rules for common constructs (Python-like)
    # This is a simplified example and may need to be extended
    lines = formatted_code.split('\n')
    indented_lines = []
    indentation_level = 0
    indent_size = 4  # Use 4 spaces for indentation
    
    for line in lines:
        stripped_line = line.strip()
        
        # Adjust indentation based on keywords
        if stripped_line.endswith(':') and not stripped_line.startswith('#'):
            indented_lines.append(' ' * (indent_size * indentation_level) + stripped_line)
            indentation_level += 1
        elif stripped_line.startswith('}') or stripped_line.startswith('end'):
            indentation_level -= 1
            indented_lines.append(' ' * (indent_size * indentation_level) + stripped_line)
        else:
            indented_lines.append(' ' * (indent_size * indentation_level) + stripped_line)
    
    formatted_code = '\n'.join(indented_lines)
    
    return formatted_code

# Example usage:
if __name__ == "__main__":
    sample_code = """
    def example_function(param):
    print("Hello, world!")
    if param > 10:
        print("Param is greater than 10")
        else:
    print("Param is 10 or less")
    """
    
    try:
        formatted_code = format_code(sample_code)
        print("Formatted code:\n", formatted_code)
    except Exception as e:
        handle_error(e)
