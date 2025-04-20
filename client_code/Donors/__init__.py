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
    if anvil.users.get_user() is None:
      self.Donate_Blood.visible = False
      self.Logout.visible = False
      self.label_1.visible = False
      self.label_3.visible = False
      self.label_4.visible = False
      self.label_5.visible = False
      self.label_6.visible = False
    user = anvil.users.get_user()
    if user is not None:
      donor = app_tables.donors.get(User=user)
      if donor:
        self.Donate_Blood.visible = False
    if user:
      donor = app_tables.donors.get(User=user)
      if donor:
        self.Name.text = donor['Name']
        self.Blood_Group.text = donor['Blood_Group']
        self.Contact.text = donor['Contact']
        self.Location.text = donor['Location']
        self.Last_Donation.text = donor['Last_donation']
      else:
        self.Name.text = "Not registered as Donor"
        self.label_1.visible = False
        self.label_3.visible = False
        self.label_4.visible = False
        self.label_5.visible = False
        self.label_6.visible = False
    else:
        self.Name.text = "Not registered as Donor"
        

    # Any code you write here will run before the form opens.
  def Logout_click(self, **event_args):
    anvil.users.logout()
    self.signup_signin.visible = True
    open_form('Donors')


  def signup_signin_click(self, **event_args):
    user = anvil.users.login_with_form(show_signup_option=True ,allow_cancel=True)
    if user:
      open_form('Donors')

  def Homepage_click(self, **event_args):
    open_form('Homepage')

  def Donate_Blood_click(self, **event_args):
    open_form('BecomeDonor')


   

