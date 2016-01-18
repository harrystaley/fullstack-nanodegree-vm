'''Database access functions for the web forum.'''

# imports Postgres SQL
import psycopg2
import bleach


# Get posts from database.
def get_all_posts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")
    C = DB.cursor()

    # get all posts from the database
    C.execute("SELECT time, content \
               FROM posts \
               ORDER BY time ASC")
    all_posts = ({'content': str(row[1]),
                 'time': str(row[0])}
                 for row in C.fetchall())
    DB.close()
    return all_posts


# Add a post to the database.
def add_post(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum")
    C = DB.cursor()
    post_content = bleach.clean(content, strip=True)
    # insert a post into the posts table time is left off
    # because it is automatically generated
    # the content parameter is passed into SQL using string substitution
    C.execute("INSERT INTO posts (content) \
               VALUES (%s)", (post_content,))
    DB.commit()
    DB.close()
