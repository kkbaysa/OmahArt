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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from functools import partial
import csv


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)


class Form(Screen):  # create screen
    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1000, 1000)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (.8, 1)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Header
        self.headerSpace = GridLayout(minimum_height=300, spacing=-150)
        self.headerSpace.cols = 1
        self.appPhoto = Image(source="OmahaArt.png")
        self.headerSpace.add_widget(self.appPhoto)
        self.greeting = Label(
            text="Sign your business up to be on OmahArt!",
            font_size=42,
            color="#100000"
        )
        self.headerSpace.add_widget(self.greeting)

        self.window.add_widget(self.headerSpace)

        ## Form
        self.form = GridLayout(spacing=(10, 10))
        self.form.cols = 2

        # First Name
        self.firstNameLabel = Label(
            text="First Name",
            font_size=30,
            color="#100000",
            text_size=(500, None),
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
            font_size=30,
            color="#100000",
            text_size=(500, None),
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
            font_size=30,
            color="#100000",
            text_size=(500, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyNameLabel)

        self.companyName = TextInput(multiline=False,
                                     padding_y=(1, 1),
                                     size_hint=(3, 3))
        self.form.add_widget(self.companyName)

        ## Company Email
        self.companyEmailLabel = Label(
            text="Company Email",
            font_size=30,
            color="#100000",
            text_size=(500, None),
            halign="left",
            valign="middle")
        self.form.add_widget(self.companyEmailLabel)

        self.companyEmail = TextInput(multiline=False,
                                      padding_y=(1, 1),
                                      size_hint=(3, 3))
        self.form.add_widget(self.companyEmail)

        ## Company Website URL
        self.companyWebsiteLabel = Label(
            text="Company Website URL",
            font_size=30,
            color="#100000",
            text_size=(500, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyWebsiteLabel)

        self.companyWebsite = TextInput(multiline=False,
                                        padding_y=(1, 1),
                                        size_hint=(3, 3))
        self.form.add_widget(self.companyWebsite)

        ## Company Street
        self.companySocialMediaLabel = Label(
            text="Social Media Handle",
            font_size=30,
            color="#100000",
            text_size=(500, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companySocialMediaLabel)

        self.companySocialMedia = TextInput(multiline=False,
                                            padding_y=(1, 1),
                                            size_hint=(3, 3))
        self.form.add_widget(self.companySocialMedia)

        ## Company City
        self.companyPhoneNumberLabel = Label(
            text="Company Phone Number",
            font_size=30,
            color="#100000",
            text_size=(500, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyPhoneNumberLabel)

        self.companyPhoneNumber = TextInput(multiline=False,
                                            padding_y=(1, 1),
                                            size_hint=(3, 3))
        self.form.add_widget(self.companyPhoneNumber)

        ## Company Category
        self.companyCategoryLabel = Label(
            text="Company Product Category (ex: pottery, oil paint, embroidery)",
            font_size=30,
            color="#100000",
            text_size=(500, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyCategoryLabel)

        self.companyCategory = TextInput(multiline=False,
                                         padding_y=(1, 1),
                                         size_hint=(3, 3))
        self.form.add_widget(self.companyCategory)

        ## Company Bio
        self.companyBioLabel = Label(
            text="Information about your business",
            font_size=30,
            color="#100000",
            text_size=(500, None),
            halign="left",
            valign="middle"
        )
        self.form.add_widget(self.companyBioLabel)

        self.companyBio = TextInput(multiline=True,
                                    padding_y=(1, 1),
                                    size_hint=(1, 10))
        self.form.add_widget(self.companyBio)

        self.window.add_widget(self.form)

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

        self.add_widget(self.window)

    def callback1(self, pop, instance):
        pop.dismiss()
        self.manager.current = 'homescreen'

    def callback2(self, instance):
        pop = Popup(title='Submission Received', size_hint=(None, None), size=(1100,800))
        self.contents = GridLayout()
        self.contents.cols = 1
        self.message = Label(text="Submitted. We will get back to you shortly, " + self.firstName.text + "!")
        self.returnButton = Button(text='Return to Home Page')
        # self.returnButton.bind(on_press=pop.close())
        self.returnButton.bind(on_press=partial(self.callback1, pop))
        self.contents.add_widget(self.message)
        self.contents.add_widget(self.returnButton)

        pop.content = self.contents
        pop.open()

        # self.manager.current = 'popup'
        with open("companyBios.csv", "at") as csvOut:
            entry = [self.firstName.text, self.lastName.text, self.companyName.text,
                     self.companyEmail.text, self.companyWebsite.text, self.companySocialMedia.text,
                     self.companyPhoneNumber.text, self.companyCategory.text, self.companyBio.text]
            csvWriter = csv.writer(csvOut)
            csvWriter.writerow(entry)
            csvOut.close()

# class SubmitPopup(Widget):
#     def __init__(self, **kwargs):
#         super(SubmitPopup, self).__init__(**kwargs)
#         self.content = GridLayout()
#         self.content.cols = 1
#         self.message = Label(text="Submitted. We will get back to you shortly, " + self.firstName.text + "!")
#         self.returnButton = Button(text='Return to Home Page')
#         self.returnButton.bind(on_press=self.callback1)
#         self.content.add_widget(self.message)
#         self.content.add_widget(self.returnButton)
#         pop = Popup(title='Submission Received',
#                     content=self.content,
#                     size_hint=(None, None), size=(1100, 800))
#         pop.open()

##########

class HomeScreen(Screen):  # create app class
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1000, 1000)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (.8, 1)
        self.window.pos_hint = {"center_x": 0.5, "center_y": .75}

        self.header = BoxLayout(orientation='horizontal')
        self.homeButton = Button(text="Home Page",
                           size_hint=(.25, .12),
                           bold=True,
                           background_color="#0000FF")
        self.formButtom = Button(text="Sign Up Page",
                                 size_hint=(.25, .12),
                                 bold=True,
                                 on_press=partial(self.screen_transition))
        self.header.add_widget(self.homeButton)
        self.header.add_widget(self.formButtom)

        self.window.add_widget(self.header)

        self.space = GridLayout()
        self.space.cols = 1
        self.space.size_hint = (.1, .1)
        self.window.add_widget(self.space)

        self.cardScroller = ScrollView()
        self.cards = GridLayout()
        self.cards.cols = 2
        # self.cards.size_hint = (0.6, 0.7)

        for i in range(10):
            self.card1 = Button(text="Company " + str(i),
                                size_hint=(.5, .25),
                                bold=True,
                                background_color='#99FFFF')
            self.card1.size_hint = (.75, .25)
            self.card1.bind(on_press=partial(self.callback1, i))
            self.cards.add_widget(self.card1)

        self.cardScroller.add_widget(self.cards)

        self.window.add_widget(self.cardScroller)

        self.add_widget(self.window)

    def callback1(self, i, instance):
        popHome = Popup(title='Company Name' + str(i),
                    content=Label(text='Company Name Information'),
                    size_hint=(None, None), size=(1100, 800))
        popHome.open()

    def screen_transition(self, *args):
        self.manager.current = 'form'


class Application(App):
    def build(self):
        sm = ScreenManagement()
        sm.add_widget(HomeScreen(name='homescreen'))
        sm.add_widget(Form(name='form'))
        # sm.add_widget(SubmitPopup(name='popup'))
        return sm


if __name__ == "__main__":
    Application().run()
