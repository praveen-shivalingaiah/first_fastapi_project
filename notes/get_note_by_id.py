from fastapi import HTTPException
from notes.add_note import Note,notes_db


def get_note_by_id(id: int) -> Note:
    for note in notes_db:
        if note.id == id:
            return note
    raise HTTPException(status_code=404,detail="Not Found") 