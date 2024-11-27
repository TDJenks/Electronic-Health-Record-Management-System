import datetime
from clinic.patient_record import PatientRecord
from clinic.note import Note


class Patient:
    def __init__(self, phn=None, name = None, dob=None, phone = None, email=None, address= None, autosave=False):
        self.phn = str(phn)
        self.name = str(name)
        self.dob = str(dob)
        self.phone = str(phone)
        self.email = str(email)
        self.address = str(address)
        self.autosave = bool(autosave)
        self.records = PatientRecord("clinic/records/" + str(phn) + ".dat", self.autosave)

    # Returns true if the Patients have identical attributes
    def __eq__(self, other):
        if other is None:
            return False
        else:
            return ((self.phn == other.phn) and (self.name == other.name) 
                and (self.dob == other.dob) and (self.address == other.address) 
                and (self.email == other.email) and (self.phone == other.phone))
    
    # Patient can be passed as a string
    def __str__(self):
        return str(self.name) + ' : ' + str(self.phn) +" : " + str(self.dob) + " : " +str(self.phone)








    