import sqlite3

# Task 3: Insert functions
def add_publisher(connection, name):
    try:
        connection.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.Error as e:
        print(f"Error adding publisher: {e}")

def add_magazine(connection, name, publisher_name):
    try:
        publisher = connection.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,)).fetchone()
        if publisher is None:
            print(f"Publisher '{publisher_name}' not found.")
            return
        connection.execute("INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher[0]))
    except sqlite3.Error as e:
        print(f"Error adding magazine: {e}")

def add_subscriber(connection, name, address):
    try:
        existing = connection.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (name, address)).fetchone()
        if existing is None:
            connection.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")

def add_subscription(connection, subscriber_name, magazine_name, expiration_date):
    try:
        subscriber = connection.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,)).fetchone()
        magazine = connection.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,)).fetchone()
        if subscriber is None or magazine is None:
            print("Subscriber or magazine not found.")
            return
        existing = connection.execute("SELECT 1 FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber[0], magazine[0])).fetchone()
        if existing is None:
            connection.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber[0], magazine[0], expiration_date))
    except sqlite3.Error as e:
        print(f"Error adding subscription: {e}")

# Task 1: Create and connect to database
try:
    with sqlite3.connect('../db/magazines.db') as connection:
        print("Database created and connected successfully.")
        connection.execute("PRAGMA foreign_keys = 1")

        # Task 2: Database structure
        connection.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
            )
        """)
        connection.commit()
        print("Tables created successfully.")

        # Task 3: Populate tables
        add_publisher(connection, "Conde Nast")
        add_publisher(connection, "Hearst")
        add_publisher(connection, "Time Inc")

        add_magazine(connection, "Vogue", "Conde Nast")
        add_magazine(connection, "Wired", "Conde Nast")
        add_magazine(connection, "Popular Mechanics", "Hearst")
        add_magazine(connection, "Car and Driver", "Hearst")
        add_magazine(connection, "Time", "Time Inc")
        add_magazine(connection, "Sports Illustrated", "Time Inc")

        add_subscriber(connection, "Alice Smith", "123 Main St")
        add_subscriber(connection, "Bob Jones", "456 Oak Ave")
        add_subscriber(connection, "Carol White", "789 Pine Rd")

        add_subscription(connection, "Alice Smith", "Vogue", "2025-12-31")
        add_subscription(connection, "Bob Jones", "Time", "2026-01-31")
        add_subscription(connection, "Carol White", "Sports Illustrated", "2025-11-30")

        connection.commit()
        print("Data inserted successfully.")

        # Task 4: SQL Queries
        print("\n--- All Subscribers ---")
        rows = connection.execute("SELECT * FROM subscribers").fetchall()
        for row in rows:
            print(row)

        print("\n--- All Magazines (sorted by name) ---")
        rows = connection.execute("SELECT * FROM magazines ORDER BY name").fetchall()
        for row in rows:
            print(row)

        print("\n--- Magazines by Conde Nast ---")
        rows = connection.execute("""
            SELECT magazines.name, publishers.name
            FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.publisher_id
            WHERE publishers.name = 'Conde Nast'
        """).fetchall()
        for row in rows:
            print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")