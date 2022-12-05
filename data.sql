CREATE TABLE IF NOT EXISTS Users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT,
  email TEXT NOT NULL UNIQUE,
  hashed_password TEXT,
  city TEXT,
  state TEXT,
  administrator TEXT,
  active TEXT,
  date_created TEXT
  );
