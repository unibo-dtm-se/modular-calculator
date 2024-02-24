from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from calculator import Calculator


BUTTONS_NAMES = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+'],
]


def browse_children(widget):
    yield widget
    if hasattr(widget, 'children'):
        for child in widget.children:
            yield from browse_children(child)


class CalculatorApp(App):
    def build(self):
        self.calculator = Calculator()

        grid = BoxLayout(orientation='vertical')

        self.display = Label(text="0", font_size=24, size_hint=(1, 0.75))
        grid.add_widget(self.display)

        for button_names_row in BUTTONS_NAMES:
            grid_row = BoxLayout()
            for button_name in button_names_row:
                button = Button(text=button_name, font_size=24, on_press=self.on_button_press)
                grid_row.add_widget(button)
            grid.add_widget(grid_row)

        return grid
    
    def button(self, text) -> Button:
        for widget in browse_children(self.root):
            if isinstance(widget, Button) and widget.text == text:
                return widget

    def on_button_press(self, instance):
        match instance.text:
            case "=":
                try:
                    result = self.calculator.compute_result()
                    self.display.text = str(result)
                except ValueError as e:
                    self.display.text = "Error"
            case "+":
                self.calculator.plus()
                self.display.text = self.calculator.expression
            case "-":
                self.calculator.minus()
                self.display.text = self.calculator.expression
            case "*":
                self.calculator.multiply()
                self.display.text = self.calculator.expression
            case "/":
                self.calculator.divide()
                self.display.text = self.calculator.expression
            case _:
                self.calculator.digit(instance.text)
                self.display.text = self.calculator.expression


if __name__ == '__main__':
    CalculatorApp().run()
