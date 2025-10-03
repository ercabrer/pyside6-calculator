"""
Calculator Backend Logic
Handles all calculator operations and state management
"""

class CalculatorEngine:
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset calculator to initial state"""
        self.current_input = ""
        self.operation = ""
        self.operand1 = 0
        self.operand2 = 0
        self.result = 0
        self.just_calculated = False
        self.has_decimal = False
    
    def add_digit(self, digit):
        """Add a digit to current input"""
        if self.just_calculated:
            self.current_input = ""
            self.just_calculated = False
            self.has_decimal = False
            
        if self.current_input == "0" and digit != "0":
            self.current_input = digit
        elif not (self.current_input == "0" and digit == "0"):
            self.current_input += digit
            
        return self.current_input if self.current_input else "0"
    
    def add_decimal(self):
        """Add decimal point to current input"""
        if self.just_calculated:
            self.current_input = "0"
            self.just_calculated = False
            self.has_decimal = False
            
        if not self.has_decimal:
            if not self.current_input:
                self.current_input = "0"
            self.current_input += "."
            self.has_decimal = True
            
        return self.current_input
    
    def set_operation(self, op):
        """Set the operation to perform"""
        if self.current_input:
            if self.operation and not self.just_calculated:
                # Chain operations
                result = self.calculate()
                if result is not None:
                    self.operand1 = result
                else:
                    return None
            else:
                try:
                    self.operand1 = float(self.current_input)
                except ValueError:
                    return None
                    
            self.operation = op
            self.current_input = ""
            self.just_calculated = False
            self.has_decimal = False
            
        return self.format_number(self.operand1)
    
    def calculate(self):
        """Perform the calculation"""
        if not self.operation or not self.current_input:
            return None
            
        try:
            self.operand2 = float(self.current_input)
        except ValueError:
            return "Error"
            
        try:
            if self.operation == '+':
                self.result = self.operand1 + self.operand2
            elif self.operation == '-':
                self.result = self.operand1 - self.operand2
            elif self.operation == '*':
                self.result = self.operand1 * self.operand2
            elif self.operation == '/':
                if self.operand2 == 0:
                    return "Error"
                self.result = self.operand1 / self.operand2
            else:
                return "Error"
                
            # Reset for next calculation
            self.operation = ""
            self.current_input = ""
            self.just_calculated = True
            self.has_decimal = False
            
            return self.result
            
        except Exception:
            return "Error"
    
    def toggle_sign(self, current_display):
        """Toggle the sign of current number"""
        if current_display == "0" or current_display == "Error":
            return current_display
            
        if current_display.startswith('-'):
            new_value = current_display[1:]
        else:
            new_value = '-' + current_display
            
        self.current_input = new_value
        return new_value
    
    def calculate_percentage(self, current_display):
        """Calculate percentage of current number"""
        if current_display == "Error":
            return current_display
            
        try:
            value = float(current_display)
            result = value / 100
            self.current_input = str(result)
            return self.format_number(result)
        except ValueError:
            return "Error"
    
    def calculate_square(self, current_display):
        """Calculate square of current number"""
        if current_display == "Error":
            return current_display
            
        try:
            value = float(current_display)
            result = value ** 2
            self.current_input = str(result)
            self.just_calculated = True
            return self.format_number(result)
        except (ValueError, OverflowError):
            return "Error"
    
    def clear(self):
        """Clear calculator completely"""
        self.reset()
        return "0"
    
    def format_number(self, number):
        """Format number for display"""
        if number == int(number):
            return str(int(number))
        else:
            # Remove trailing zeros and unnecessary decimal point
            formatted = f"{number:.10g}"
            return formatted
    
    def get_current_display(self):
        """Get what should be displayed"""
        if self.current_input:
            return self.current_input
        elif self.just_calculated:
            return self.format_number(self.result)
        else:
            return "0"