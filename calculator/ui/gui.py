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


class CalculatorApp(App):
    def build(self):
        self._calc = Calculator()

        grid = BoxLayout(orientation='vertical')

        self._display = Label(text="0", font_size=24, size_hint=(1, 0.75))
        grid.add_widget(self._display)

        for button_names_row in BUTTONS_NAMES:
            grid_row = BoxLayout()
            for button_name in button_names_row:
                button = Button(text=button_name, font_size=24, on_press=self.on_button_press)
                grid_row.add_widget(button)
            grid.add_widget(grid_row)

        return grid

    def on_button_press(self, button):
        match button.text:
            case "=":
                try:
                    result = self._calc.compute_result()
                    self._display.text = str(result)
                except ValueError as e:
                    self._display.text = "Error"
            case "+":
                self._calc.plus()
                self._display.text = self._calc.expression
            case "-":
                self._calc.minus()
                self._display.text = self._calc.expression
            case "*":
                self._calc.multiply()
                self._display.text = self._calc.expression
            case "/":
                self._calc.divide()
                self._display.text = self._calc.expression
            case ".":
                self._calc.dot()
                self._display.text = self._calc.expression
            case _:
                self._calc.digit(button.text)
                self._display.text = self._calc.expression


if __name__ == '__main__':
    CalculatorApp().run()
