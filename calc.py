import kivy
from kivy.uix.label import Label
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Chibuike(App):
  def build(self):
    layout = BoxLayout(orientation='vertical')
    self.result_string = ""

    # Add buttons for the virtual keyboard
    buttons = [
      ['7', '8', '9', '/'],
      ['4', '5', '6', '*'],
      ['1', '2', '3', '-'],
      ['C', '0', '=', '+'],
      ['a', 'b', 'c']
    ]
    for row in buttons:
      h_layout = BoxLayout()
      for label in row:
        button = Button(text=label)
        button.bind(on_press=self.on_button_press)
        h_layout.add_widget(button)
      layout.add_widget(h_layout)

    # Add a label to display the result
    self.result_label = Label(text='0')
    layout.add_widget(self.result_label)
    
    # Set the window title
    Window.title = "Hey"

    # Show the minimize button
    Window.minimize = True

    # Show the close button
    Window.close = True

    # Show the maximize button
    Window.maximize = True

    # Set the window size
    Window.size = (1000, 500)

    return layout

  def on_button_press(self, instance):
    label = instance.text

    # Clear the result if the user pressed the 'C' button
    if label == 'C':
      self.result_string = ""
    # If the user pressed the '=' button, try to evaluate the result
    elif label == '=':
      try:
        result = eval(self.result_string)
        self.result_string = str(result)
      except Exception as e:
        self.result_string = "Error"
    # Otherwise, just add the button label to the result string
    else:
      self.result_string += label

    # Update the result label
    self.result_label.text = self.result_string

if __name__ == '__main__':
  Chibuike().run()
