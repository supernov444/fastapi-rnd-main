from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os

from app.database import SessionLocal, engine, Base
from app import models, crud, schemas

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up templates
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse("/users")

@app.get("/users", response_class=HTMLResponse)
async def users_page(request: Request, db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/create", response_class=HTMLResponse)
async def create_form(request: Request):
    return templates.TemplateResponse("create.html", {
        "request": request, 
        "error": None, 
        "username": "", 
        "email": "", 
        "full_name": ""
    })

@app.post("/create", response_class=HTMLResponse)
async def create_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    full_name: str = Form(None),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # Create UserCreate schema object
        user_data = schemas.UserCreate(
            username=username,
            email=email,
            full_name=full_name,
            password=password
        )
        
        crud.create_user(db, user_data)
        return RedirectResponse("/users", status_code=303)
    except ValueError as e:
        return templates.TemplateResponse("create.html", {
            "request": request,
            "error": str(e),
            "username": username,
            "email": email,
            "full_name": full_name
        })

@app.get("/edit/{user_id}", response_class=HTMLResponse)
async def edit_form(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("edit.html", {"request": request, "user": user})

@app.post("/edit/{user_id}", response_class=RedirectResponse)
async def update_user(
    user_id: int,
    username: str = Form(...),
    email: str = Form(...),
    full_name: str = Form(None),
    password: str = Form(None),
    db: Session = Depends(get_db)
):
    # Create UserUpdate schema
    user_update = schemas.UserUpdate(
        username=username,
        email=email,
        full_name=full_name,
        password=password
    )
    
    user = crud.update_user(db, user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return RedirectResponse("/users", status_code=303)

@app.get("/delete/{user_id}", response_class=RedirectResponse)
async def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return RedirectResponse("/users", status_code=303)

@app.delete("/api/users/{user_id}")
async def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}