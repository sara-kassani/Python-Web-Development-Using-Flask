import os       

from flask import Flask
app= Flask(__name__)


@app.route('/')
def index():
    return "Index Page"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile based on its username
    return "User %s visited" % username
# e.g. http://0.0.0.0:5000/user/sara


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Show the post with the given id, the id must be integer
    return "Post %d" % post_id
# e.g. http://0.0.0.0:5000/post/15

if __name__ =='__main__':
    host= os.getenv('IP', '0.0.0.0')
    port= int(os.getenv('PORT', 5000))
    app.debug= True
    app.run(host=host, port=port)
