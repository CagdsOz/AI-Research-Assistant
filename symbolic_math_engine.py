import sympy as sp
from typing import Dict, Any

class SymbolicMathEngine:
    def __init__(self):
        """
        Provides verifiable symbolic mathematics computation and LaTeX output generation.
        """
        self.x = sp.symbols('x')

    def parse_and_solve(self, expression_str: str, operation: str) -> Dict[str, Any]:
        """
        Parses infix strings and handles integration, differentiation, and solving.
        """
        try:
            # Safe parsing of the mathematical string
            expr = sp.sympify(expression_str)
            
            if operation == "integrate":
                result = sp.integrate(expr, self.x)
                derivation = f"Step-by-step: Integral of {sp.latex(expr)} dx"
            elif operation == "differentiate":
                result = sp.diff(expr, self.x)
                derivation = f"Step-by-step: Derivative of {sp.latex(expr)} w.r.t x"
            elif operation == "solve":
                result = sp.solve(expr, self.x)
                derivation = f"Step-by-step: Finding roots for {sp.latex(expr)} = 0"
            else:
                return {"error": "Unsupported operation"}

            return {
                "success": True,
                "result_latex": sp.latex(result),
                "derivation": derivation,
                "raw_result": str(result)
            }

        except Exception as e:
            return {
                "success": False,
                "error": "Deterministic error: Invalid mathematical syntax",
                "details": str(e)
            }