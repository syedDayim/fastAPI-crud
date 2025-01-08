import psycopg2
from app.data import posts
from app.dbconnect import dbConnection


connection, cursor = dbConnection()

#Finds post by id and deletes it
def find_by_id_and_delete(id):
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (str(id), ))
    post = cursor.fetchone()
    connection.commit()
    return post

def find_post_by_id(id):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s""", (str(id),) )
    post = cursor.fetchone()
    print(post)
    return post

def update_post_by_id(id, new_data):
    cursor.execute(""" UPDATE posts SET title = (%s), content = (%s), published = (%s) WHERE id = (%s) RETURNING *;""", ((new_data.title, new_data.content, new_data.published, str(id) )))       
    post = cursor.fetchone()
    connection.commit()
    return post     


