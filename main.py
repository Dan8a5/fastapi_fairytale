import uvicorn  
from fastapi import FastAPI, HTTPException, Depends  
from sqlmodel import Session, select  
from typing import List  
from models import House, Wolf, Pig, HouseCreate, WolfCreate, PigCreate  
from db import get_session, init_db  

# Initialize FastAPI app
app = FastAPI()

# Initialize the database
init_db()  # Run database initialization function to set up the tables

# Root endpoint to welcome users to the API
@app.get("/")
def read_root():
    return {"message": "Welcome to the 3 Little Pigs Fairytale API"}

# House routes

# Create a new house record
@app.post("/houses/", response_model=House)
def create_house(house: HouseCreate, session: Session = Depends(get_session)):
    db_house = House.model_validate(house)  # Validate and create a House object from the input
    session.add(db_house)  # Add the house object to the database session
    session.commit()  # Commit the transaction to save the house in the database
    session.refresh(db_house)  # Refresh the house object with the latest data from the database
    return db_house  # Return the newly created house

# Retrieve all houses
@app.get("/houses/", response_model=List[House])
def read_houses(session: Session = Depends(get_session)):
    houses = session.exec(select(House)).all()  # Query all houses from the database
    return houses  # Return the list of houses

# Retrieve a specific house by ID
@app.get("/houses/{house_id}", response_model=House)
def read_house(house_id: int, session: Session = Depends(get_session)):
    house = session.get(House, house_id)  # Get the house by its ID
    if not house:
        raise HTTPException(status_code=404, detail="House not found")  # If not found, raise 404 error
    return house  # Return the house object

# Update a specific house by ID
@app.put("/houses/{house_id}", response_model=House)
def update_house(house_id: int, house: HouseCreate, session: Session = Depends(get_session)):
    db_house = session.get(House, house_id)  # Retrieve the house by its ID
    if not db_house:
        raise HTTPException(status_code=404, detail="House not found")  # Raise 404 if not found
    house_data = house.model_dump(exclude_unset=True)  # Get data from the request, excluding unset fields
    for key, value in house_data.items():
        setattr(db_house, key, value)  # Update the house fields with the new data
    session.add(db_house)  # Add the updated house to the session
    session.commit()  # Commit the changes to the database
    session.refresh(db_house)  # Refresh the house object to reflect updates
    return db_house  # Return the updated house

# Delete a house by ID
@app.delete("/houses/{house_id}")
def delete_house(house_id: int, session: Session = Depends(get_session)):
    house = session.get(House, house_id)  # Retrieve the house by its ID
    if not house:
        raise HTTPException(status_code=404, detail="House not found")  # Raise 404 if not found
    session.delete(house)  # Delete the house from the database
    session.commit()  # Commit the changes
    return {"ok": True}  # Return success response

# Wolf routes

# Create a new wolf record
@app.post("/wolves/", response_model=Wolf)
def create_wolf(wolf: WolfCreate, session: Session = Depends(get_session)):
    db_wolf = Wolf.model_validate(wolf)  # Validate and create a Wolf object from the input
    session.add(db_wolf)  # Add the wolf object to the database session
    session.commit()  # Commit the transaction to save the wolf in the database
    session.refresh(db_wolf)  # Refresh the wolf object with the latest data from the database
    return db_wolf  # Return the newly created wolf

# Retrieve all wolves
@app.get("/wolves/", response_model=List[Wolf])
def read_wolves(session: Session = Depends(get_session)):
    wolves = session.exec(select(Wolf)).all()  # Query all wolves from the database
    return wolves  # Return the list of wolves

# Retrieve a specific wolf by ID
@app.get("/wolves/{wolf_id}", response_model=Wolf)
def read_wolf(wolf_id: int, session: Session = Depends(get_session)):
    wolf = session.get(Wolf, wolf_id)  # Get the wolf by its ID
    if not wolf:
        raise HTTPException(status_code=404, detail="Wolf not found")  # If not found, raise 404 error
    return wolf  # Return the wolf object

# Update a specific wolf by ID
@app.put("/wolves/{wolf_id}", response_model=Wolf)
def update_wolf(wolf_id: int, wolf: WolfCreate, session: Session = Depends(get_session)):
    db_wolf = session.get(Wolf, wolf_id)  # Retrieve the wolf by its ID
    if not db_wolf:
        raise HTTPException(status_code=404, detail="Wolf not found")  # Raise 404 if not found
    wolf_data = wolf.model_dump(exclude_unset=True)  # Get data from the request, excluding unset fields
    for key, value in wolf_data.items():
        setattr(db_wolf, key, value)  # Update the wolf fields with the new data
    session.add(db_wolf)  # Add the updated wolf to the session
    session.commit()  # Commit the changes to the database
    session.refresh(db_wolf)  # Refresh the wolf object to reflect updates
    return db_wolf  # Return the updated wolf

# Delete a wolf by ID
@app.delete("/wolves/{wolf_id}")
def delete_wolf(wolf_id: int, session: Session = Depends(get_session)):
    wolf = session.get(Wolf, wolf_id)  # Retrieve the wolf by its ID
    if not wolf:
        raise HTTPException(status_code=404, detail="Wolf not found")  # Raise 404 if not found
    session.delete(wolf)  # Delete the wolf from the database
    session.commit()  # Commit the changes
    return {"ok": True}  # Return success response

# Pig routes

# Create a new pig record
@app.post("/pigs/", response_model=Pig)
def create_pig(pig: PigCreate, session: Session = Depends(get_session)):
    db_pig = Pig.model_validate(pig)  # Validate and create a Pig object from the input
    session.add(db_pig)  # Add the pig object to the database session
    session.commit()  # Commit the transaction to save the pig in the database
    session.refresh(db_pig)  # Refresh the pig object with the latest data from the database
    return db_pig  # Return the newly created pig

# Retrieve all pigs
@app.get("/pigs/", response_model=List[Pig])
def read_pigs(session: Session = Depends(get_session)):
    pigs = session.exec(select(Pig)).all()  # Query all pigs from the database
    return pigs  # Return the list of pigs

# Retrieve a specific pig by ID
@app.get("/pigs/{pig_id}", response_model=Pig)
def read_pig(pig_id: int, session: Session = Depends(get_session)):
    pig = session.get(Pig, pig_id)  # Get the pig by its ID
    if not pig:
        raise HTTPException(status_code=404, detail="Pig not found")  # If not found, raise 404 error
    return pig  # Return the pig object

# Update a specific pig by ID
@app.put("/pigs/{pig_id}", response_model=Pig)
def update_pig(pig_id: int, pig: PigCreate, session: Session = Depends(get_session)):
    db_pig = session.get(Pig, pig_id)  # Retrieve the pig by its ID
    if not db_pig:
        raise HTTPException(status_code=404, detail="Pig not found")  # Raise 404 if not found
    pig_data = pig.model_dump(exclude_unset=True)  # Get data from the request, excluding unset fields
    for key, value in pig_data.items():
        setattr(db_pig, key, value)  # Update the pig fields with the new data
    session.add(db_pig)  # Add the updated pig to the session
    session.commit()  # Commit the changes to the database
    session.refresh(db_pig)  # Refresh the pig object to reflect updates
    return db_pig  # Return the updated pig

# Delete a pig by ID
@app.delete("/pigs/{pig_id}")
def delete_pig(pig_id: int, session: Session = Depends(get_session)):
    pig = session.get(Pig, pig_id)  # Retrieve the pig by its ID
    if not pig:
        raise HTTPException(status_code=404, detail="Pig not found")  # Raise 404 if not found
    session.delete(pig)  # Delete the pig from the database
    session.commit()  # Commit the changes
    return {"ok": True}  # Return success response