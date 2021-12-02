from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.resources import resource_add_path
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
import csv

class Form(App):  # create app class
    def build(self):  # build method
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1000, 1000)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (.8, 1)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Header
        self.headerSpace = GridLayout()
        self.headerSpace.cols = 1
        self.appPhoto = Image(source="OmahaArt.png")
        self.headerSpace.add_widget(self.appPhoto)

        self.greeting = Label(
            text="Sign your business up to be on OmahArt!",
            font_size=36,
            color="#100000")
        self.headerSpace.add_widget(self.greeting)

        self.window.add_widget(self.headerSpace)

        ## Form
        self.form = GridLayout(spacing=20)
        self.form.cols = 2

        # First Name
        self.firstNameLabel = Label(
            text="First Name",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle")
        self.form.add_widget(self.firstNameLabel)

        self.firstName = TextInput(multiline=False,
                                   padding_y=(1, 1),
                                   size_hint=(3, 3))
        self.form.add_widget(self.firstName)

        ## Last Name
        self.lastNameLabel = Label(
            text="Last Name",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.lastNameLabel)

        self.lastName = TextInput(multiline=False,
                              padding_y=(1, 1),
                              size_hint=(3, 3))
        self.form.add_widget(self.lastName)

        ## Company Name
        self.companyNameLabel = Label(
            text="Company Name",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyNameLabel)

        self.companyName = TextInput(multiline=False,
                                     padding_y=(1, 1),
                                     size_hint=(3, 3))
        self.form.add_widget(self.companyName)


        ## Company Phone
        self.companyPhoneLabel = Label(
            text="Phone Number",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyPhoneLabel)

        self.companyPhone = TextInput(multiline=False,
                                      padding_y=(1, 1),
                                      size_hint=(3, 3))
        self.form.add_widget(self.companyPhone)

        ## Company Street
        self.companyStreetLabel = Label(
            text="Street",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyStreetLabel)

        self.companyStreet = TextInput(multiline=False,
                                       padding_y=(1, 1),
                                       size_hint=(3, 3))
        self.form.add_widget(self.companyStreet)

        ## Company City
        self.companyCityLabel = Label(
            text="City",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyCityLabel)

        self.companyCity = TextInput(multiline=False,
                                     padding_y=(1, 1),
                                     size_hint=(3, 3))
        self.form.add_widget(self.companyCity)

        ## Company City
        self.companyStateLabel = Label(
            text="State",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyStateLabel)

        self.companyState = TextInput(multiline=False,
                                      padding_y=(1, 1),
                                      size_hint=(3, 3))
        self.form.add_widget(self.companyState)

        ## Company Zip
        self.companyZipLabel = Label(
            text="Zip",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle")
        self.form.add_widget(self.companyZipLabel)

        self.companyZip = TextInput(multiline=False,
                                    padding_y=(1, 1),
                                    size_hint=(3, 3))
        self.form.add_widget(self.companyZip)

        ## Company Bio
        self.companyBioLabel = Label(
            text="Information about your business",
            font_size=36,
            color="#100000",
            text_size=(300, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyBioLabel)

        self.companyBio = TextInput(multiline=True,
                                    padding_y=(1, 1),
                                    size_hint=(1, 10))
        self.form.add_widget(self.companyBio)

        self.window.add_widget(self.form)


############ Buttons ############
        ## Submit Buttons
        self.buttonSpace = GridLayout(padding=25)
        self.buttonSpace.cols = 2
        self.buttonSpace.size_hint = (.25, .25)

        self.button1 = Button(text="Go Back",
                             size_hint=(.25, 0.25),
                             bold=True,
                             background_color='#FF0000')
                             # background_normal="")
        self.button1.bind(on_press=self.callback1)

        ## Submit Button
        self.button2 = Button(text="Submit Form",
                              size_hint=(.25, 0.25),
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
        with open("companyBios.csv", "at") as csvOut:
            entry = [self.firstName.text, self.lastName.text, self.companyName.text]
            csvWriter = csv.writer(csvOut)
            csvWriter.writerow(entry)
            csvOut.close()

form = Form()
form.run()
