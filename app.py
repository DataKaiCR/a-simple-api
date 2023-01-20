from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from typing import Optional

from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Templates
templates = Jinja2Templates(directory="templates")

# Application
app = FastAPI()



# Dictionary gets converted into json response
@app.get('/') 
async def home(request: Request, db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return templates.TemplateResponse('base.html', {
        'request': request, 'item_list': items
    })
    
@app.post('/add')
async def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.Item(title=title)
    db.add(new_todo)
    db.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url = url, status_code=status.HTTP_303_SEE_OTHER)

@app.get('/update/{todo_id}')
async def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Item).filter(models.Item.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url = url, status_code = status.HTTP_302_FOUND)

@app.get('/delete/{todo_id}')
async def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Item).filter(models.Item.id == todo_id).first()
    db.delete(todo)
    db.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url = url, status_code = status.HTTP_302_FOUND)