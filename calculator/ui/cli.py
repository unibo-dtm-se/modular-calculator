from calculator import Calculator
import sys


class CalculatorCLI:
    def __init__(self, args):
        self._args = args
        self._calc = Calculator()

    def run(self):
        if not self._args:
            print("Usage: python -m calculator.ui.cli <expression>")
            return
        self._calc.expression = " ".join(self._args)
        try:
            result = self._calc.compute_result()
            print(result)
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    CalculatorCLI(sys.argv[1:]).run()
