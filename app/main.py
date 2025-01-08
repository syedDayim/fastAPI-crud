from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from app.dbconnect import dbConnection      # Logic to make connection with the database
from app.data import posts                  # Import Posts
from app.utils import find_by_id_and_delete # Delete Function
from app.utils import find_post_by_id       # Finds Posts
from app.utils import update_post_by_id     # Update Posts



app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = False


connection, cursor = dbConnection() # this connects with the database and returns the connection and cursor varaible.


# Gets All Posts
@app.get("/")
async def root():
    cursor.execute("SELECT * FROM posts;")
    all_posts = cursor.fetchall()
    return {"data": all_posts}

# Posts a Post
@app.post("/posts")
async def create_post(new_post: Post):
    cursor.execute("""INSERT INTO posts (title, content) VALUES (%s, %s)  RETURNING * ;""", (new_post.title, new_post.content))
    post = cursor.fetchone()
    connection.commit()
    return {"message": post}


# Gets a Specific Post
@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    new_post = find_post_by_id(id)
    if not new_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID: {id} Post Not Found")
    return {"post": new_post}


# Deletes Specific Post
@app.delete("/posts/{id}")
async def delete_post(id, response: Response):
    deleted_post = find_by_id_and_delete(int(id))
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post Doesn't Exist")
    return {"posts": deleted_post}


# Updated the Post by ID
@app.put("/posts/{id}")
async def update_post(id: int, respose: Response, new_data: Post):
    updated_post = update_post_by_id(id, new_data)
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post doesnt exist")
    return {"Response" : updated_post}