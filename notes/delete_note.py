from fastapi import HTTPException
from notes.add_note import notes_db,Note

def delete_note_by_id(id:int) -> Note:
    for note in notes_db:
        if note.id == id:
            notes_db.remove(note)
            return
    raise HTTPException(status_code=404,detail="note not found")