from calculator import Calculator
import sys


def main(args, output=sys.stdout):
    calculator = Calculator()
    calculator.expression = " ".join(args)
    try:
        result = calculator.compute_result()
        print(result, file=output)
    except ValueError as e:
        print(e, file=output)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python -m calculator.ui.cli <expression>")
        sys.exit(1)
    main(sys.argv[1:])
