import datetime
import shutil
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
	pass


class RegistrationWindow(Screen):
	def register_user(self):
		fname = self.ids.fname.text.strip()
		lname = self.ids.lname.text.strip()
		phone = self.ids.phone.text.strip()
		idnumber = self.ids.idnumber.text.strip()
		password = self.ids.password.text.strip()

		# validation of the user inputs

		if fname == "" or lname == "" or phone == "" or idnumber == "" or password == "":
			self.ids.error.text = "[color=ff3333] The fields with * sign are required! [/color]"
		else:
			if "09" in phone:
				self.ids.fname.text = ""
				self.ids.lname.text = ""
				self.ids.phone.text = ""
				self.ids.email.text = ""
				self.ids.gender.text = ""
				self.ids.idnumber.text = ""
				self.ids.address.text = ""
				self.ids.password.text = ""

				self.ids.error.text = "[color=11ff33] You have successfully Registered![/color]"

			else:
				self.ids.error.text = "[color=ff3333] Enter a valid Phone Number![/color]"


class ManagementSystem(App):
	@staticmethod
	def build(**kwargs):
		return WindowManager()


if __name__ == "__main__":
	ManagementSystem().run()
