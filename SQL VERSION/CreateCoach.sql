CREATE TABLE Coach_Scheme (
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