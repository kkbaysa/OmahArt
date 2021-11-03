from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import csv

class Form(App):  # create app class
    def build(self):  # build method
        Window.clearcolor = (1, 1, 1, 1)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.appPhoto = Image(source="OmahaArt.png")
        self.window.add_widget(self.appPhoto)

        # self.window.add_widget(Image(source="OmahaArt.png"))

        self.greeting = Label(
            text="What is your name?",
            font_size=36,
            color="#100000")
        self.window.add_widget(self.greeting)


        # First Name
        self.firstNameLabel = Label(
            text="First Name",
            font_size=36,
            color="#100000")
        self.window.add_widget(self.firstNameLabel)

        self.firstName = TextInput(multiline=False,
                              padding_y=(20, 20),
                              size_hint=(1, .5))
        self.window.add_widget(self.firstName)

        ## Last Name
        self.lastNameLabel = Label(
            text="Last Name",
            font_size=36,
            color="#100000")
        self.window.add_widget(self.lastNameLabel)

        self.lastName = TextInput(multiline=False,
                              padding_y=(20, 20),
                              size_hint=(1, .5))
        self.window.add_widget(self.lastName)

        ## Company Name
        self.companyNameLabel = Label(
            text="Company Name",
            font_size=36,
            color="#100000")
        self.window.add_widget(self.companyNameLabel)

        self.companyName = TextInput(multiline=False,
                                  padding_y=(20, 20),
                                  size_hint=(1, .5))
        self.window.add_widget(self.companyName)


        ## Submit Buttons
        self.buttonSpace = GridLayout()
        self.buttonSpace.cols = 2
        self.button1 = Button(text="Go Back",
                             size_hint=(1, 0.5),
                             bold=True,
                             background_color='#FF0000')
                             # background_normal="")
        self.button1.bind(on_press=self.callback1)

        ## Submit Button
        self.button2 = Button(text="Submit Form",
                              size_hint=(1, 0.5),
                              bold=True,
                              background_color='#100000')
        self.button2.bind(on_press=self.callback2)

        ## Add buttons to a row
        self.buttonSpace.add_widget(self.button1)
        self.buttonSpace.add_widget(self.button2)

        ## Add Button Space to Window
        self.window.add_widget(self.buttonSpace)

        return self.window

    def callback1(self, instance):
        self.greeting.text = ""

    def callback2(self, instance):
        self.greeting.text = "Submitted. We will get back to you shortly, " + self.firstName.text + "!"
        # with open("companyBios.csv", "at") as csvOut:
        #     entry = [firstName, lastName, companyName]
        #     csvWriter = csv.writer(csvOut)
        #     csvWriter.writerow(entry)
        #     csvOut.close()




form = Form()
form.run()
