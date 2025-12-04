from fastapi import HTTPException
from notes.add_note import notes_db,Note
from pydantic import BaseModel
from typing import Optional

class UpdateNote(BaseModel):
    title: str
    content: str

def update_note_by_id(id: int,updateNote: UpdateNote) -> Note:
    for note in notes_db:
        if note.id == id:
            note.title = updateNote.title
            note.content = updateNote.content
            return note
    raise HTTPException(status_code=403,detail="Cannot update the field")