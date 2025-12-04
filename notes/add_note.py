from pydantic import BaseModel
from typing import Optional

class AddNote(BaseModel):
    title: str
    content: str
    tag: Optional[str] = None

class Note(AddNote):
    id: int

notes_db: list[Note] = []
next_id: int = 1

def adding_Note(note: AddNote) -> Note:
    global next_id

    new_note = Note(id=next_id,**note.model_dump())
    notes_db.append(new_note)
    next_id += 1

    return new_note

