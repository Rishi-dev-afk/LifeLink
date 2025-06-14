from ._anvil_designer import FindDonorTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class FindDonor(FindDonorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def Search_click(self, **event_args):
    bg = self.Blood_Group.selected_value
    loc = self.Location.selected_value
    results = anvil.server.call('find_donors', bg, loc)
    self.results_panel.items = results

  def Back_click(self, **event_args):
    open_form('Donors')
