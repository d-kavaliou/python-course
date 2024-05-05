from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)

Base = declarative_base()

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    parent_id = Column(Integer, ForeignKey("parents.id"))

class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    children = relationship("Child", back_populates="parent")

Child.parent = relationship("Parent", back_populates="children")

Base.metadata.create_all(bind=engine)

class ChildCreate(BaseModel):
    name: str
    age: int
    parent_id: int

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/children/")
async def create_child(child: ChildCreate):
    query = Child.insert().values(name=child.name, age=child.age, parent_id=child.parent_id)
    child_id = await database.execute(query)
    return {"id": child_id, **child.dict()}

@app.get("/children/{child_id}")
async def get_child(child_id: int):
    query = Child.select().where(Child.c.id == child_id)
    child = await database.fetch_one(query)
    if not child:
        raise HTTPException(status_code=404, detail="Child not found")
    return child