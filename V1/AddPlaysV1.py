import sqlite3

def insert_play_data(db_name, game_date):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    play_number = 1
    
    while True:
        try:
            print(f"\nEntering data for Play Number {play_number}")
            quarter = int(input("Enter Quarter: "))
            down = int(input("Enter Down: "))
            distance = int(input("Enter Distance: "))
            yard_line = int(input("Enter Yard Line: "))
            personel = int(input("Enter Personnel: "))
            formation = input("Enter Formation : ")
            play = input("Enter Play : ")
            
            cursor.execute("""
                INSERT INTO Coach_Scheme (Game_Date, Play_Number, quarter, Down, Distance, Yard_Line, Personel, Formation, Play)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?,)
            """, (game_date, play_number, quarter, down, distance, yard_line, personel, formation, play))
            
            conn.commit()
            play_number += 1
            
            cont = input("Do you want to enter another play? (yes/no): ").strip().lower()
            if cont != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter numeric values where required.")
    
    conn.close()

def main():
    coach_name = input("Enter the coach's name: ").strip().replace(" ", "_")
    coach_name = coach_name.upper()
    db_name = f"{coach_name}.db"
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Coach_Scheme (
        Game_Date DATE,
        Play_Number INTEGER,
        quarter INTEGER,
        Down INTEGER,
        Distance INTEGER,
        Yard_Line INTEGER,
        Personel INTEGER,
        Play TEXT NOT NULL,
        PRIMARY KEY (Game_Date, Play_Number)
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
    
    game_date = input("Enter the game date (YYYY-MM-DD): ").strip()
    insert_play_data(db_name, game_date)
    
    print(f"Data entry complete for game date {game_date} in database '{db_name}'.")

if __name__ == "__main__":
    main()