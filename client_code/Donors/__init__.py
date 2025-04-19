from ._anvil_designer import DonorsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Donors(DonorsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if anvil.users.get_user():
      self.signup_signin.visible = False

    # Any code you write here will run before the form opens.
  def Logout_click(self, **event_args):
    anvil.users.logout()
    self.signup_signin.visible = True
    self.button_6.visible = False


  def signup_signin_click(self, **event_args):
    user = anvil.users.login_with_form(show_signup_option=True ,allow_cancel=True)
    if user:
      open_form('Donors')
   

