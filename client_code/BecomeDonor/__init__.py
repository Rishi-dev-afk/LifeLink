from ._anvil_designer import BecomeDonorTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BecomeDonor(BecomeDonorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    name = self.text_box_1.text
    blood_group = self.drop_down_1.selected_value
    contact = self.text_box_3.text
    Location = self.text_box_4.text
    Last_donation = self.date_picker_1.date

    user = anvil.users.get_user()

    app_tables.donors.add_row(User= user,
                             Name= name,
                             Blood_Group = blood_group,
                             Contact= contact,
                             Location= Location,
                             Last_donation= Last_donation)
    alert("Your details have been saved sucessfully")
    open_form('Donors')

    
    

  