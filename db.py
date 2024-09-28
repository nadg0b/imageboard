import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_board(board_name):
    conn = get_db_connection()
    conn.execute("INSERT INTO boards(board_title) VALUES(?)", (board_name,))
    conn.commit()
    conn.close()

    
def get_boards():
    conn = get_db_connection()
    boards = conn.execute("SELECT * FROM boards")
    for board in boards:
        print(board["board_id"], 
              board['board_title'], 
              board["board_created"])
    conn.close()


def create_thread(title, img_url, content, is_starter, reply_to, board):
    conn = get_db_connection()
    conn.execute('''INSERT INTO threads(thread_title, thread_image_url, thread_content, is_thread_starter, thread_reply_to_id, thread_board_id) 
                 VALUES(?, ?, ?, ?, ?, ?)''', (title, img_url, content, is_starter, reply_to, board))
    conn.commit()
    conn.close()


def get_threads():
    conn = get_db_connection()
    threads = conn.execute("SELECT * FROM threads")
    for thread in threads:
        print(thread["thread_title"], 
              thread["thread_image_url"], 
              thread["thread_content"],
              thread["is_thread_starter"],
              thread["thread_reply_to_id"],
              thread["thread_board_id"])
    conn.close()


get_boards()