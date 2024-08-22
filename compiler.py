class EALCompiler:
    def __init__(self, code):
        """
        Initializes the compiler with the provided code.
        
        Args:
            code (str): The source code to be compiled.
        """
        self.code = code
        self.bytecode = []

    def compile(self):
        """
        Compiles the code into bytecode or another intermediate form.
        
        Returns:
            list: The compiled bytecode representation of the code.
        """
        lines = self.code.split('\n')
        self.bytecode = []  # Reset bytecode list
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Handle variable declaration
            if line.startswith('declare'):
                self._compile_declaration(line)
            
            # Handle assembly-like operations
            elif re.match(r'^[a-zA-Z]+\s+[a-zA-Z]+\s*$', line):
                self.bytecode.append(('assembly', line))
            
            # Handle English-like commands
            elif re.match(r'if .* then', line):
                self.bytecode.append(('if', line))
            
            elif line.startswith('print'):
                self.bytecode.append(('print', line))
            
            else:
                print(f"Warning: Unrecognized line: {line}")

        return self.bytecode

    def _compile_declaration(self, line):
        """
        Compiles variable declarations into bytecode.
        
        Args:
            line (str): The line containing the declaration.
        
        Returns:
            None
        """
        import re
        
        match = re.match(r'declare (\w+) (\w+) = (.+);', line)
        if match:
            var_type, var_name, var_value = match.groups()
            value = self._parse_value(var_value)
            self.bytecode.append(('declare', var_name, value))
        else:
            print(f"Error: Invalid declaration syntax: {line}")

    def _parse_value(self, value):
        """
        Parses a value to the correct type.
        
        Args:
            value (str): The value to be parsed.
        
        Returns:
            The parsed value.
        """
        if value.isdigit():
            return int(value)
        elif value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        else:
            return value.strip('"')

# Example usage:
if __name__ == "__main__":
    sample_code = """
    declare int x = 10;
    mov eax, 5
    add eax, x
    if x is greater than 5 then
        print "x is greater than 5";
    print "End of program";
    """
    
    compiler = EALCompiler(sample_code)
    bytecode = compiler.compile()
    print("Compiled bytecode:\n", bytecode)
