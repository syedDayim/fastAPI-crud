
from app.main import posts
# Find the post with id 2


def updateById(id, new_data):
    for index, content in enumerate(posts):
        if( content["id"] == id):
            new_dict = {}
            new_dict['id'] = id
            new_dict['title'] = new_data['title']
            new_dict['content'] = new_data['content']
            posts[index] = new_dict
            print(content, new_dict, posts)

new_data = {
    "title" : "Updated Title",
    "content": "Updated Content"
}
updateById(2, new_data)
