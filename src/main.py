from fastapi import FastAPI
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import contact_crud, models, schemas
from src.configuration import database

app = FastAPI()


@app.post("/contacts/", response_model=schemas.Contact)
async def create_contact(contact: schemas.ContactCreate, db: Session = Depends(database.get_db)):
    return await contact_crud.create_contact(db=db, contact=contact)

@app.get("/contacts/", response_model=list[schemas.Contact])
async def read_contacts(db: Session = Depends(database.get_db)):
    contacts = await contact_crud.get_contacts(db=db)
    return contacts

@app.get("/contacts/{contact_id}")
async def read_contact(contact_id: int, db: Session = Depends(database.get_db)):
    db_contact = await contact_crud.get_contact(db=db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.put("/contacts/{contact_id}", response_model=schemas.Contact)
async def update_contact(contact_id: int, contact: schemas.ContactUpdate, db: Session = Depends(database.get_db)):
    db_contact = await contact_crud.update_contact(db=db, contact_id=contact_id, contact=contact)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.delete("/contacts/{contact_id}", response_model=schemas.Contact)
async def delete_contact(contact_id: int, db: Session = Depends(database.get_db)):
    db_contact = await contact_crud.delete_contact(db=db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact