import sqlite3
def build_query():
    params = []

    # Base query
    query = """
    WITH TotalPlays AS (
        SELECT COUNT(*) AS Total_Play
        FROM Coach_Scheme
        WHERE 1 = 1 """
    
    # Asking for required inputs
    quarter = input("Enter Quarter (or press Enter to skip): ").strip()
    if quarter:
        query += " AND quarter = ?"
        params.append(int(quarter))

    down = input("Enter Down (or press Enter to skip): ").strip()
    if down:
        query += " AND Down = ?"
        params.append(int(down))

    distance = input("Enter Distance (or press Enter to skip): ").strip()
    if distance:
        query += " AND Distance = ?"
        params.append(int(distance))

    yard_line = input("Enter Yard Line (or press Enter to skip): ").strip()
    if yard_line:
        query += " AND Yard_Line = ?"
        params.append(int(yard_line))

    # Optional inputs
    formation = input("Enter Formation (optional, press Enter to skip): ").strip()
    if formation:
        query += " AND Formation = ?"
        params.append(formation)

    personnel = input("Enter Personnel (optional, press Enter to skip): ").strip()
    if personnel:
        query += " AND Personel = ?"
        params.append(int(personnel))
    
    #Finish Query
    query += """)
    SELECT 
        Formation, 
        Play, 
        (COUNT(*) * 100.0) / (SELECT Total_Play FROM TotalPlays) AS Percent_Chance
    FROM Coach_Scheme
    WHERE 1=1
    """
    if quarter:
        query += " AND quarter = ?"
        params.append(int(quarter))

    if down:
        query += " AND Down = ?"
        params.append(int(down))

    if distance:
        query += " AND Distance = ?"
        params.append(int(distance))

    if yard_line:
        query += " AND Yard_Line = ?"
        params.append(int(yard_line))

    # Optional inputs
    if formation:
        query += " AND Formation = ?"
        params.append(formation)

    if personnel:
        query += " AND Personel = ?"
        params.append(int(personnel))
    
    
    query += ";"

    return query, params

def execute_query(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query, params = build_query()

 #   print("\nExecuting Query:\n", query, "\nWith Parameters:", params)
    cursor.execute(query, params)
    
    results = cursor.fetchall()
    
    if results:
        print("\nResults:")
        for row in results:
            print(row)
    else:
        print("\nNo results found matching the criteria.")

    conn.close()

if __name__ == "__main__":
    coach_name = input("Enter the coach's name to access the database: ").strip().replace(" ", "_")
    coach_name = coach_name.upper()
    db_name = f"{coach_name}.db"
    
    execute_query(db_name)