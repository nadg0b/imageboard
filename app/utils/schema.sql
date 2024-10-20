DROP TABLE IF EXISTS boards;
DROP TABLE IF EXISTS threads;

CREATE TABLE boards (
    board_id INTEGER PRIMARY KEY AUTOINCREMENT,
    board_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    board_title TEXT NOT NULL
);

CREATE TABLE threads (
    thread_id INTEGER PRIMARY KEY AUTOINCREMENT,
    thread_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    thread_title TEXT NOT NULL,
    thread_image_url TEXT NOT NULL,
    thread_content TEXT NOT NULL,
    is_thread_starter BOOLEAN NOT NULL,
    thread_reply_to_id INTEGER,
    thread_board_id INTEGER, 
    FOREIGN KEY (thread_reply_to_id) REFERENCES threads(thread_id),
    FOREIGN KEY (thread_board_id) REFERENCES boards(board_id)
);