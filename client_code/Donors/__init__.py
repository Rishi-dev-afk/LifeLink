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
      self.button_7.visible = False

    # Any code you write here will run before the form opens.
  def button_6_click(self, **event_args):
    anvil.users.logout()
    self.button_7.visible = True
    self.button_6.visible = False