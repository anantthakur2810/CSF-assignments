from typing import List, Tuple


class Calculator:
    def __init__(self):
        self.history: List[Tuple[str, float]] = []

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def save_history(self, expression: str, result: float) -> None:
        self.history.append((expression, result))
        # Keep last 10
        if len(self.history) > 10:
            self.history.pop(0)

    def show_history(self) -> None:
        if not self.history:
            print("No history yet.")
            return
        print("\nLast calculations:")
        for expr, res in self.history:
            print(f"  {expr} = {res}")


def get_number(prompt: str) -> float:
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def main():
    calc = Calculator()
    menu = (
        "\nSimple Calculator - choose an option:\n"
        "1) Addition\n"
        "2) Subtraction\n"
        "3) Multiplication\n"
        "4) Division\n"
        "5) History\n"
        "6) Exit\n"
    )

    while True:
        print(menu)
        choice = input("Enter choice (1-6): ").strip()
        if choice == '6':
            print("Goodbye!")
            break
        elif choice == '5':
            calc.show_history()
            continue
        elif choice in ('1', '2', '3', '4'):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            try:
                if choice == '1':
                    r = calc.add(a, b)
                    expr = f"{a} + {b}"
                elif choice == '2':
                    r = calc.subtract(a, b)
                    expr = f"{a} - {b}"
                elif choice == '3':
                    r = calc.multiply(a, b)
                    expr = f"{a} * {b}"
                elif choice == '4':
                    r = calc.divide(a, b)
                    expr = f"{a} / {b}"
                print(f"Result: {r}")
                calc.save_history(expr, r)
            except ZeroDivisionError as e:
                print(e)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    main()