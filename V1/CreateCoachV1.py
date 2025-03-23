import sqlite3

def create_database(coach_name = None):
    # Get coach's name and format it for the database filename
    if not coach_name:
        coach_name = input("Enter the coach's name: ").strip().replace(" ", "_")
        coach_name = coach_name.upper()
    db_name = f"{coach_name}.db"
    
    # Connect to SQLite database (creates if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create the Coach_Scheme table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Coach_Scheme (
        Game_Date DATE,
        Play_Number INTEGER,
        Quarter INTEGER,
        Down INTEGER,
        Distance INTEGER,
        Yard_Line INTEGER,
        Personel INTEGER,
        Formation TEXT NOT NULL, 
        Play TEXT NOT NULL,
        PRIMARY KEY (Game_Date, Play_Number)
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
    
    print(f"Database '{db_name}' created successfully with table 'Coach_Scheme'.")

if __name__ == "__main__":
    create_database()