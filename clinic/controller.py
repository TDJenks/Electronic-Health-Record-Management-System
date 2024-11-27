from clinic.patient import Patient
from clinic.note import Note
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.dao.patient_dao_json import PatientDAOJSON

class Controller:
   def __init__(self, autosave=False):
      self.users = []
      self.users.append( User(name='user',passw='123456') )
      self.users.append( User(name='ali', passw='@G00dPassw0rd') )
      self.users.append( User(name='kala', passw= 'J&0p@rd!z&'))
      self.current_patient = None
      self.current_user = None
      self.autosave = autosave
      self.patientsDAO = PatientDAOJSON(autosave =self.autosave )


   def isLoggedIn(self):
      if self.current_user is not None:
         return
      else:
         raise IllegalAccessException()


   # Sets current_user if valid credentials are passed -> returns true if successful
   def login(self, username, password):
      try:
         self.isLoggedIn()
         raise DuplicateLoginException()
      except IllegalAccessException as e:
         x = User(name=username, passw=password)
         for i in self.users:
            if i == x and i.password == x.password:
               self.current_user = i
               return True
         raise InvalidLoginException()

   # Sets current_user to None if current_user is not None -> returns true if successful
   def logout(self):
      try:
         self.isLoggedIn()
         self.current_user = None
         return True
      except IllegalAccessException as e:
         raise InvalidLogoutException()


   # Retrieves a Patient from phn -> returns Patient if successful
   def search_patient(self, phn):
      self.isLoggedIn()
      return self.patientsDAO.search_patient(phn)
      

   # Creates a Patient based on parameters -> returns Patient if successful (patients cannot share the same phn)
   def create_patient(self,phn, name, dob, phone, email, address):
      self.isLoggedIn()
      return self.patientsDAO.create_patient(Patient(phn=phn, name=name, dob=dob, phone=phone, email=email, address=address, autosave=self.autosave))

   # Retrieves Patients that share the same name -> returns a list of Patients
   def retrieve_patients(self, name_to_search):
      self.isLoggedIn()
      return self.patientsDAO.retrieve_patients(name_to_search)
         
   # Updates Patient attributes if Patient is not None -> returns true if successful
   def update_patient(self, cur_phn, new_phn, name, dob, phone, email, address):
      self.isLoggedIn()
      if self.search_patient(cur_phn) is None or self.current_patient is not None or (self.search_patient(new_phn) is not None and (cur_phn != new_phn)):
         raise IllegalOperationException()
      else:
         x = Patient(phn=new_phn, name=name, dob=dob, phone=phone, email=email, address=address, autosave=self.autosave)
         return self.patientsDAO.update_patient(key = cur_phn, patient = x)
         

   # Deletes a Patient -> returns true if successful
   def delete_patient(self, phn):
      self.isLoggedIn()
      if self.current_patient is not None:
         raise IllegalOperationException
      return self.patientsDAO.delete_patient(phn)

   
   # Returns all Patients currently initialized if logged in
   def list_patients(self):
      self.isLoggedIn()
      return self.patientsDAO.list_patients()


   # Returns current_patient if logged in
   def get_current_patient(self):
      self.isLoggedIn()
      if self.current_patient is not None:
         return self.current_patient
      else:
         return None

   # Assigns current_patient based on phn
   def set_current_patient(self, phn):
      self.isLoggedIn()
      x = self.search_patient(phn)
      if x is not None:
         self.current_patient = x
         return
      else:
         raise IllegalOperationException

   # Reverts current_patient to None -> returns true if successful
   def unset_current_patient(self):
      self.isLoggedIn()
      self.current_patient = None
      return True

   def hasCurrentPatient(self):
      self.isLoggedIn()
      if self.current_patient is not None:
         return 
      else:
         raise NoCurrentPatientException()


#---------------------Note Functions---------------------------#

   
   # Creates a Note in current_patient's PatientRecord -> returns the created Note if successful
   def create_note(self, details):
      self.hasCurrentPatient()
      return self.current_patient.records.create_note(details=details)
      

   # Retrives a Note in current_patient's PatientRecord identified with code -> returns the found Note if successful
   def search_note(self, code):
      self.hasCurrentPatient()
      return self.current_patient.records.search_note(code = code)
       

   # Retrieves all Notes from current_patient's PatientRecord containing the substring passed in "text" -> returns a list of Notes if successful
   def retrieve_notes(self, text):
      self.hasCurrentPatient()
      x = self.current_patient.records.retrieve_notes(text = text)
      return x
      
   # Updates Note details identified with code -> returns updated Note if successful
   def update_note(self, code, details):
      self.hasCurrentPatient()
      return self.current_patient.records.update_note(code = code, details = details)

   # Deletes Note from current_patient's PatientRecord identified with code -> returns the deleted Note
   def delete_note(self, code):
      self.hasCurrentPatient()
      return self.current_patient.records.delete_note(code = code)
    
   # Returns a list of all Notes in current_patient's PatientRecord
   def list_notes(self):
      self.hasCurrentPatient()
      return self.current_patient.records.list_all()


class User:
   def __init__(self, name=None, passw=None):
      self.username = name
      self.password = passw

   def __eq__(self, other):
      if self.username == other.username:
         return True
      else:
         return False
