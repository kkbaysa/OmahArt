from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import date


class SubmissionForm(App):  # create app class
    def build(self):  # build method
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.window.add_widget(Image(source="img.png"))

        self.greeting = Label(
            text="What is your name?",
            font_size=36,
            color="#FF0000")

        self.window.add_widget(self.greeting)

        self.user = TextInput(multiline=False,
                              padding_y=(20, 20),
                              size_hint=(1, .5))
        self.window.add_widget(self.user)

        self.buttonSpace = GridLayout()
        self.buttonSpace.cols = 2
        self.button1 = Button(text="Say Howdy",
                             size_hint=(1, 0.5),
                             bold=True,
                             background_color='#FF0000')
                             # background_normal="")
        self.button1.bind(on_press=self.callback1)
        self.button2 = Button(text="Clear",
                              size_hint=(1, 0.5),
                              bold=True,
                              background_color='#000000')
        # background_normal="")
        self.button2.bind(on_press=self.callback2)
        self.buttonSpace.add_widget(self.button1)
        self.buttonSpace.add_widget(self.button2)
        self.window.add_widget(self.buttonSpace)

        return self.window

    def callback1(self, instance):
        self.greeting.text = "Submitted " + date.today().isoformat() + "!"

    def callback2(self, instance):
        self.greeting.text = ""


submissionForm = SubmissionForm()
SubmissionForm.run()
