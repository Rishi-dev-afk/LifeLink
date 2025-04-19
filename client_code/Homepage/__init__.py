from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if anvil.users.get_user():
      self.button_5.visible = False

    # Any code you write here will run before the form opens.
  def button_5_click(self,**event_args):
    user = anvil.users.login_with_form(show_signup_option=True ,allow_cancel=True)
    if user:
      open_form('Homepage')
    
  def button_3_click(self,**event_args):
    open_form('Hospitals')

  def button_7_click(self, **event_args):
    anvil.users.logout()
    self.button_5.visible = True
    self.button_7.visible = False
    
  def Donors_click(self,**event_args):
    open_form('Donors')