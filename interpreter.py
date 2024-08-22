import json
import re

class EALInterpreter:
    def __init__(self, code):
        """
        Initializes the interpreter with the provided code.
        
        Args:
            code (str): The source code to be interpreted.
        """
        self.code = code
        self.variables = {}
        self.instructions = []

    def interpret(self):
        """
        Parses and interprets the code to convert it into executable instructions.
        
        Returns:
            None
        """
        lines = self.code.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Handle variable declaration
            if line.startswith('declare'):
                self._handle_declaration(line)
            
            # Handle assembly-like operations
            elif re.match(r'^[a-zA-Z]+\s+[a-zA-Z]+\s*$', line):
                self.instructions.append(('assembly', line))
            
            # Handle English-like commands
            elif re.match(r'if .* then', line):
                self.instructions.append(('if', line))
            
            elif line.startswith('print'):
                self.instructions.append(('print', line))
            
            else:
                print(f"Warning: Unrecognized line: {line}")

    def execute(self):
        """
        Executes the interpreted instructions.
        
        Returns:
            None
        """
        for instruction_type, instruction in self.instructions:
            if instruction_type == 'assembly':
                self._execute_assembly(instruction)
            elif instruction_type == 'if':
                self._execute_if(instruction)
            elif instruction_type == 'print':
                self._execute_print(instruction)
            else:
                print(f"Error: Unrecognized instruction type: {instruction_type}")

    def _handle_declaration(self, line):
        """
        Handles variable declarations.
        
        Args:
            line (str): The line containing the declaration.
        
        Returns:
            None
        """
        match = re.match(r'declare (\w+) (\w+) = (.+);', line)
        if match:
            var_type, var_name, var_value = match.groups()
            self.variables[var_name] = self._parse_value(var_value)
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

    def _execute_assembly(self, instruction):
        """
        Executes assembly-like instructions.
        
        Args:
            instruction (str): The assembly-like instruction.
        
        Returns:
            None
        """
        print(f"Executing assembly instruction: {instruction}")

    def _execute_if(self, instruction):
        """
        Executes conditional statements.
        
        Args:
            instruction (str): The conditional statement.
        
        Returns:
            None
        """
        # Simplified example: Just prints the condition for now
        print(f"Evaluating if statement: {instruction}")

    def _execute_print(self, instruction):
        """
        Executes print statements.
        
        Args:
            instruction (str): The print statement.
        
        Returns:
            None
        """
        match = re.match(r'print "(.*)";', instruction)
        if match:
            print(match.group(1))
        else:
            print(f"Error: Invalid print syntax: {instruction}")

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
    
    interpreter = EALInterpreter(sample_code)
    interpreter.interpret()
    interpreter.execute()
