import pickle
import os
from clinic.note import Note
from clinic.dao.note_dao_pickle import NoteDAOPickle


class PatientRecord:
    def __init__(self, file_path, autosave=False):
        self.auto_counter = 0
        self.autosave = autosave
        if self.autosave:
            try:
                with open(file_path, "a") as file:
                    pass
                with open(file_path, "rb") as file:
                    temp = pickle.load(file)
                    if temp:
                        self.auto_counter = max(temp.keys())
            except EOFError:
                pass
            except pickle.UnpicklingError:
                pass
        self.notesDAO = NoteDAOPickle(file_path, autosave)


    # Creates a Note in PatientRecord -> returns created Note if successful
    def create_note(self, details=None):
        self.auto_counter += 1
        return self.notesDAO.create_note(note=Note(code=self.auto_counter, details= details ))
        

    # Retrives a Note from PatientRecord identified with code -> returns found Note if successful
    def search_note(self, code=None):
        return self.notesDAO.search_note(code)

    # Retrieves all Notes from PatientRecord containing the substring passed in "text" -> returns list of Notes if successful
    def retrieve_notes(self, text = None):
        if text is None:
            return None
        return self.notesDAO.retrieve_notes(text)
                
    # Updates Note deatils from PatientRecord identified with code -> returns true if successful
    def update_note(self, code = None, details = None):
        return self.notesDAO.update_note(note = Note(code = code, details = details))
        
    # Deletes a Note from PatientRecord identified with code -> returns true if successful
    def delete_note(self, code = None):
        return self.notesDAO.delete_note(key = code)

    
    # Returns a list of all Notes in PatientRecord
    def list_all(self):
        return self.notesDAO.list_notes()
    
    

