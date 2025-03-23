Play Predictor Application
Overview
The Play Predictor is a powerful tool designed to help analyze and predict football plays based on historical data. It allows users to create coach profiles, record plays, and get statistical predictions for future plays.

Features
1. Coach Management
Create new coach profiles
Each coach has their own database of plays
Track play history for each coach

2. Play Recording
Record new plays with detailed information:
Quarter
Down
Distance
Yard Line
Personnel
Formation
Play Type
Automatic game date and play number tracking
Easy-to-use form interface

3. Play Prediction
Get statistical predictions based on historical data
Filter predictions by:
Quarter
Down
Distance (Short/Medium/Long)
Yard Line
Formation
Personnel
View percentage chances for different play types

4. Settings
Configure distance thresholds:
Short Distance Threshold
Medium Distance Threshold
Long Distance Threshold
Real-time validation to ensure proper order of thresholds

Technical Requirements
Python 3.x
PyQt6 for the graphical user interface
SQLite3 for data storage

How to Use
Getting Started
Run PlayPredictorGUIV3.py
Create a new coach profile using the "Create Coach" tab
Record plays using the "Add Play" tab
Get predictions using the "Get Play" tab
Customize distance thresholds using the "Settings" tab

Recording Plays
Select a coach from the dropdown
Fill in all required fields:
Quarter (1-4)
Down (1-4)
Distance (yards)
Yard Line (0-100)
Personnel (number of players)
Formation
Play Type
Click "Add Play" to save

Getting Predictions
Select a coach from the dropdown
Choose filter criteria:
Quarter
Down
Distance (Short/Medium/Long)
Yard Line
Formation
Personnel
Click "Get Play" to see predictions

Configuring Settings
Go to the "Settings" tab
Adjust the distance thresholds:
Short Distance Threshold (default: 3)
Medium Distance Threshold (default: 7)
Long Distance Threshold (default: 10)
Click "Apply Settings" to save changes

Data Storage
Each coach's plays are stored in a separate SQLite database
Database files are stored in the coaches directory
File names follow the format: COACH_NAME.db

Troubleshooting
Ensure all required fields are filled before adding a play
Check that distance thresholds are in proper order (Short < Medium < Long)
Verify that the coach exists before trying to get predictions

Version History
v3.0: Added settings tab for configurable distance thresholds
v2.0: Improved user interface and data management
v1.0: Initial release with basic play prediction functionality