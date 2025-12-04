from fastapi import FastAPI
from notes.add_note import AddNote , Note , adding_Note
from notes.get_notes import get_all_notes
from notes.get_note_by_id import get_note_by_id
from notes.update_note import update_note_by_id,UpdateNote
from notes.delete_note import delete_note_by_id
from fastapi import status


app = FastAPI()

@app.post("/add_note",status_code=status.HTTP_201_CREATED)
def addNote(note: AddNote):
    return adding_Note(note)

@app.get("/get_notes",status_code=status.HTTP_200_OK)
def getNotes():
    return get_all_notes()

@app.get("/get_note/{id}",response_model=Note,status_code=status.HTTP_200_OK)
def getNoteByID(id:int):
    return get_note_by_id(id)

@app.patch("/get_note/{id}",response_model=Note,status_code=status.HTTP_200_OK)
def updateNoteByID(id:int,note:UpdateNote):
    return update_note_by_id(id,note)

@app.delete("/delete_note/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deleteNoteByID(id:int):
    return delete_note_by_id(id)