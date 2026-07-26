#=================================================
# Math functions
#=================================================

import ast, random, math, operator
from colorama import Fore, Style

class MathFunc:
    mathset = {
        "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, 
        "tan": math.tan, "log": math.log, "log10": math.log10, 
        "abs": abs, "pi": math.pi, "e": math.e
    }
    _reserved = {"sqrt", "sin", "cos", "tan", "log", "log10", "abs", "pi", "e"}
    _allowed_operators = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod, ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}

    MATHSET_HELP = {
        "sqrt": "sqrt(x) - Returns the square root of x.",
        "sin": "sin(x) - Returns the sine of x in radians.",
        "cos": "cos(x) - Returns the cosine of x in radians.",
        "tan": "tan(x) - Returns the tangent of x in radians.",
        "log": "log(x, [base]) - Returns the natural logarithm of x (or logarithm with specified base).",
        "log10": "log10(x) - Returns the base-10 logarithm of x.",
        "abs": "abs(x) - Returns the absolute value of x.",
        "pi": "pi - Mathematical constant for π (~3.14159).",
        "e": "e - Mathematical constant for e (~2.71828)."
    }

    @staticmethod
    def help_attribute(attr: str):
        """Displays help for a specific MathSet attribute or custom variable."""
        attr = attr.lower().strip()
        if attr in MathFunc.MATHSET_HELP:
            print(f"{Fore.GREEN}=== MathSet Help: {attr} ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{MathFunc.MATHSET_HELP[attr]}{Style.RESET_ALL}")
        elif attr in MathFunc.mathset and attr not in MathFunc._reserved:
            print(f"{Fore.CYAN}{attr}{Style.RESET_ALL} is a custom user variable with current value: {Fore.GREEN}{MathFunc.mathset[attr]}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No MathSet documentation found for '{attr}'.{Style.RESET_ALL}")

    @staticmethod
    def _eval_ast_node(node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)): return node.value
            raise ValueError("Only numeric constants allowed.")
        elif hasattr(ast, "Num") and isinstance(node, getattr(ast, "Num")): return node.n
        elif isinstance(node, ast.Name):
            if node.id in MathFunc.mathset:
                val = MathFunc.mathset[node.id]
                if callable(val): raise ValueError(f"'{node.id}' is a function, not a constant or variable.")
                return val
            raise ValueError(f"Undefined variable '{node.id}'")
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type in MathFunc._allowed_operators: return MathFunc._allowed_operators[op_type](MathFunc._eval_ast_node(node.operand))
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in MathFunc._allowed_operators: return MathFunc._allowed_operators[op_type](MathFunc._eval_ast_node(node.left), MathFunc._eval_ast_node(node.right))
            raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in MathFunc.mathset and callable(MathFunc.mathset[func_name]):
                    args = [MathFunc._eval_ast_node(arg) for arg in node.args]
                    return MathFunc.mathset[func_name](*args)
                raise ValueError(f"Unknown function '{func_name}'")
            raise ValueError("Complex function calls not supported.")
        else: raise ValueError(f"Unsupported syntax expression: {type(node).__name__}")

    @staticmethod
    def evaluate(expression: str):
        try:
            print(f"Result: {Fore.GREEN}{MathFunc._eval_ast_node(ast.parse(expression, mode='eval').body)}{Style.RESET_ALL}")
        except Exception as e: print(f"{Fore.RED}Error evaluating expression: {e}{Style.RESET_ALL}")

    @staticmethod
    def getmath():
        print(f"{Fore.BLUE}MathSet{Style.RESET_ALL}:\n",
              f"{Fore.CYAN}sqrt, sin, cos, tan, log, log10, pi, e{Style.RESET_ALL}",
              f"You can use {Fore.GREEN}help <mathset>{Style.RESET_ALL} to dive deeper in MathSet usage.")
    
    @staticmethod
    def rtool(start: int = None, end: int = None):
        try:
            if start is not None and end is not None: num = random.randint(min(start, end), max(start, end))
            elif start is not None: num = random.randint(1, start)
            else: num = random.randint(1, 1000)
            print(f"Random number: {Fore.GREEN}{num}{Style.RESET_ALL}")
        except Exception as e: print(f"{Fore.RED}Error generating random number: {e}{Style.RESET_ALL}")

    @staticmethod
    def set_var(var_name: str, value: float):
        try:
            MathFunc.mathset[var_name] = float(value)
            print(f"Variable {Fore.CYAN}{var_name}{Style.RESET_ALL} assigned value {Fore.GREEN}{float(value)}{Style.RESET_ALL}.")
        except ValueError: print(f"{Fore.RED}Invalid numeric value provided.{Style.RESET_ALL}")

    @staticmethod
    def del_var(var_name: str):
        if var_name in MathFunc._reserved: print(f"{Fore.RED}Cannot delete built-in constant/function '{var_name}'.{Style.RESET_ALL}")
        elif var_name in MathFunc.mathset:
            del MathFunc.mathset[var_name]
            print(f"Variable {Fore.GREEN}{var_name}{Style.RESET_ALL} deleted.")
        else: print(f"{Fore.RED}Variable '{var_name}' not found.{Style.RESET_ALL}")

    @staticmethod
    def getvar(var_name: str):
        if var_name in MathFunc.mathset and var_name not in MathFunc._reserved:
            print(f"{Fore.CYAN}{var_name}{Style.RESET_ALL} = {Fore.GREEN}{MathFunc.mathset[var_name]}{Style.RESET_ALL}")
        elif var_name in MathFunc._reserved: print(f"{Fore.YELLOW}'{var_name}' is a built-in function/constant.{Style.RESET_ALL}")
        else: print(f"{Fore.RED}Variable '{var_name}' not found.{Style.RESET_ALL}")

    @staticmethod
    def list_vars():
        user_vars = {k: v for k, v in MathFunc.mathset.items() if k not in MathFunc._reserved}
        if user_vars:
            print(f"{Fore.BLUE}== USER VARIABLES =={Style.RESET_ALL}")
            for k, v in user_vars.items(): print(f"{Fore.CYAN}{k:<15}{Style.RESET_ALL}: {Fore.GREEN}{v}{Style.RESET_ALL}")
        else: print(f"{Fore.YELLOW}No custom variables saved yet.{Style.RESET_ALL}")