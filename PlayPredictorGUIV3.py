from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                            QLabel, QLineEdit, QPushButton, QTabWidget, QComboBox,
                            QTextEdit, QFormLayout, QMessageBox, QSpinBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sqlite3
import os
from datetime import datetime

class PlayPredictorGUI(QWidget):
    """
    Main window for the play predictor application.
    """
    def __init__(self):
        """
        Initialize the main window and set up the user interface.
        """
        super().__init__()
        self.current_coach = None
        self.SHORT = 3
        self.MEDIUM = 7
        self.LONG = 10
        self.initUI()
    
    def initUI(self):
        """
        Set up the main user interface with tabs for creating coaches,
        getting plays, and adding plays.
        """
        # Set window properties
        self.setWindowTitle('Play Predictor')
        self.setGeometry(100, 100, 800, 600)
        
        # Create main layout with spacing
        layout = QVBoxLayout()
        layout.setSpacing(20)
        
        # Create tabs with enhanced style
        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #333;
                background: white;
                padding: 15px;
            }
            QTabBar::tab {
                background: #f8f9fa;
                padding: 12px 24px;
                border: 1px solid #333;
                border-bottom: none;
                margin-right: 2px;
                color: #333;
                font-weight: bold;
            }
            QTabBar::tab:hover {
                background: #e9ecef;
            }
            QTabBar::tab:selected {
                background: white;
                border-bottom: 2px solid #007AFF;
                color: #007AFF;
            }
            QTabBar::tab:!selected {
                margin-top: 2px;
            }
        """)
        
        # Create Coach tab
        create_coach_tab = QWidget()
        create_coach_layout = QVBoxLayout()
        create_coach_layout.setSpacing(15)
        
        # Coach name input with proper spacing
        coach_name_layout = QHBoxLayout()
        coach_name_layout.setSpacing(10)
        
        coach_name_label = QLabel('Coach Name:')
        coach_name_label.setStyleSheet("font-weight: bold;")
        self.coach_name_entry = QLineEdit()
        self.coach_name_entry.setMinimumWidth(200)
        
        coach_name_layout.addWidget(coach_name_label)
        coach_name_layout.addWidget(self.coach_name_entry)
        
        # Create button with proper size
        create_coach_button = QPushButton('Create Coach')
        create_coach_button.setFixedHeight(40)
        create_coach_button.clicked.connect(self.create_coach)
        
        create_coach_layout.addLayout(coach_name_layout)
        create_coach_layout.addWidget(create_coach_button)
        create_coach_tab.setLayout(create_coach_layout)
        
        # Get Play tab
        get_play_tab = QWidget()
        get_play_layout = QVBoxLayout()
        get_play_layout.setSpacing(15)
        
        # Coach selection with proper spacing
        coach_select_layout = QHBoxLayout()
        coach_select_layout.setSpacing(10)
        
        coach_select_label = QLabel('Select Coach:')
        coach_select_label.setStyleSheet("font-weight: bold;")
        self.coach_select_combo = QComboBox()
        self.coach_select_combo.setMinimumWidth(200)
        
        coach_select_layout.addWidget(coach_select_label)
        coach_select_layout.addWidget(self.coach_select_combo)
        
        # Get play form with proper spacing
        get_play_form = QFormLayout()
        get_play_form.setSpacing(10)
        get_play_form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        
        # Create combo boxes for quarter and down
        self.quarter_combo = QComboBox()
        self.down_combo = QComboBox()
        
        # Create line edits for numeric inputs
        self.distance_spin = QLineEdit()
        self.yard_line_spin = QLineEdit()
        self.personnel_spin = QLineEdit()
        
        # Create line edits for text inputs
        self.formation_text = QLineEdit()
        
        # Add form fields
        get_play_form.addRow('Quarter:', self.quarter_combo)
        get_play_form.addRow('Down:', self.down_combo)
        get_play_form.addRow('Distance:', self.distance_spin)
        get_play_form.addRow('Yard Line:', self.yard_line_spin)
        get_play_form.addRow('Formation:', self.formation_text)  
        get_play_form.addRow('Personnel:', self.personnel_spin)
        
        # Get play button with proper size
        get_play_button = QPushButton('Get Play')
        get_play_button.setFixedHeight(40)
        get_play_button.clicked.connect(self.get_play)
        
        get_play_layout.addLayout(coach_select_layout)
        get_play_layout.addLayout(get_play_form)
        get_play_layout.addWidget(get_play_button)
        get_play_tab.setLayout(get_play_layout)
        
        # Add Play tab
        add_play_tab = QWidget()
        add_play_layout = QVBoxLayout()
        add_play_layout.setSpacing(15)
        
        # Coach selection with proper spacing
        add_coach_select_layout = QHBoxLayout()
        add_coach_select_layout.setSpacing(10)
        
        add_coach_select_label = QLabel('Select Coach:')
        add_coach_select_label.setStyleSheet("font-weight: bold;")
        self.add_coach_select_combo = QComboBox()
        self.add_coach_select_combo.setMinimumWidth(200)
        
        add_coach_select_layout.addWidget(add_coach_select_label)
        add_coach_select_layout.addWidget(self.add_coach_select_combo)
        
        # Add play form with proper spacing
        add_play_form = QFormLayout()
        add_play_form.setSpacing(10)
        add_play_form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        
        # Create input fields for play data
        self.game_date = QLineEdit()
        self.game_date.setPlaceholderText("Last used date")
        self.play_number = QLineEdit()
        self.play_number.setPlaceholderText("Auto-incremented")
        self.quarter = QLineEdit()
        self.down = QLineEdit()
        self.distance = QLineEdit()
        self.yard_line = QLineEdit()
        self.personnel = QLineEdit()
        self.formation = QLineEdit()
        self.play = QLineEdit()
        
        # Add form fields
        add_play_form.addRow('Game Date (YYYY-MM-DD):', self.game_date)
        add_play_form.addRow('Play Number:', self.play_number)
        add_play_form.addRow('Quarter:', self.quarter)
        add_play_form.addRow('Down:', self.down)
        add_play_form.addRow('Distance:', self.distance)
        add_play_form.addRow('Yard Line:', self.yard_line)
        add_play_form.addRow('Personnel:', self.personnel)
        add_play_form.addRow('Formation:', self.formation)
        add_play_form.addRow('Play:', self.play)
        
        # Add play button with proper size
        add_play_button = QPushButton('Add Play')
        add_play_button.setFixedHeight(40)
        add_play_button.clicked.connect(self.add_play)
        
        add_play_layout.addLayout(add_coach_select_layout)
        add_play_layout.addLayout(add_play_form)
        add_play_layout.addWidget(add_play_button)
        add_play_tab.setLayout(add_play_layout)
        
        # Create Settings tab
        settings_tab = QWidget()
        settings_layout = QVBoxLayout()
        settings_layout.setSpacing(25)  # Increased spacing
        
        # Create form layout for settings
        settings_form = QFormLayout()
        settings_form.setSpacing(20)  # Increased spacing
        
        # Style for labels and spin boxes
        label_style = """
            QLabel {
                font-weight: bold;
                color: #333;
                font-size: 20px;  /* Increased font size */
            }
        """
        spinbox_style = """
            QSpinBox {
                padding: 12px;  /* Increased padding */
                font-size: 18px;  /* Increased font size */
                border: 1px solid #ccc;
                border-radius: 6px;
                color: #333;
                background-color: white;
                min-width: 120px;  /* Increased width */
            }
        """
        
        # Short distance setting
        self.short_spin = QSpinBox()
        self.short_spin.setMinimum(1)
        self.short_spin.setMaximum(99)
        self.short_spin.setValue(self.SHORT)
        self.short_spin.setStyleSheet(spinbox_style)
        settings_form.addRow(QLabel('Short Distance Threshold:'), self.short_spin)
        
        # Medium distance setting
        self.medium_spin = QSpinBox()
        self.medium_spin.setMinimum(1)
        self.medium_spin.setMaximum(99)
        self.medium_spin.setValue(self.MEDIUM)
        self.medium_spin.setStyleSheet(spinbox_style)
        settings_form.addRow(QLabel('Medium Distance Threshold:'), self.medium_spin)
        
        # Long distance setting
        self.long_spin = QSpinBox()
        self.long_spin.setMinimum(1)
        self.long_spin.setMaximum(99)
        self.long_spin.setValue(self.LONG)
        self.long_spin.setStyleSheet(spinbox_style)
        settings_form.addRow(QLabel('Long Distance Threshold:'), self.long_spin)
        
        # Apply button
        apply_button = QPushButton('Apply Settings')
        apply_button.setFixedHeight(50)  # Increased height
        apply_button.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 18px;  /* Increased font size */
                padding: 12px 24px;
                border-radius: 6px;
                background-color: #007AFF;
                color: white;
            }
            QPushButton:hover {
                background-color: #0062cc;
            }
        """)
        apply_button.clicked.connect(self.apply_settings)
        
        settings_layout.addLayout(settings_form)
        settings_layout.addWidget(apply_button)
        settings_tab.setLayout(settings_layout)
        
        # Add tabs to the tab widget
        tabs.addTab(create_coach_tab, 'Create Coach')
        tabs.addTab(get_play_tab, 'Get Play')
        tabs.addTab(add_play_tab, 'Add Play')
        tabs.addTab(settings_tab, 'Settings')
        
        # Add tabs to main layout
        layout.addWidget(tabs)
        
        # Set window layout
        self.setLayout(layout)
        
        # Style the window
        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
            QLabel {
                color: #333;
                font-size: 12px;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: white;
                color: #333;
                font-size: 12px;
                min-width: 200px;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #007AFF;
            }
            QPushButton {
                padding: 12px 24px;
                background-color: #007AFF;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        
        # Initialize combo boxes
        self.init_combo_boxes()
        
        # Connect coach selection change to update date and play number
        self.add_coach_select_combo.currentTextChanged.connect(self.update_date_and_play_number)
        
        # Update coach list after all widgets are created
        self.update_coach_list()
    
    def init_combo_boxes(self):
        self.quarter_combo.addItems([''] + [str(i) for i in range(1, 5)] + ['OT'])  
        self.down_combo.addItems([''] + [str(i) for i in range(1, 5)])  

    def get_coach_db_path(self, coach_name):
        """
        Get the full path to the coach's database file.
        
        Args:
            coach_name (str): Name of the coach (will be converted to uppercase and spaces replaced with underscores)
            
        Returns:
            str: Full path to the coach's database file
        """
        # Create coaches directory if it doesn't exist
        coaches_dir = os.path.join(os.getcwd(), 'coaches')
        if not os.path.exists(coaches_dir):
            os.makedirs(coaches_dir)
        
        # Return the full path to the coach's database
        return os.path.join(coaches_dir, f"{coach_name}.db")
    
    def update_coach_list(self):
        """
        Update the coach selection combo boxes with available coaches.
        Coaches are detected by looking for .db files in the coaches directory.
        """
        # Clear existing items and add empty option
        self.coach_select_combo.clear()
        self.coach_select_combo.addItem('')
        self.add_coach_select_combo.clear()
        self.add_coach_select_combo.addItem('')
        
        # Get list of coach databases
        coaches_dir = os.path.join(os.getcwd(), 'coaches')
        if os.path.exists(coaches_dir):
            for file in os.listdir(coaches_dir):
                if file.endswith('.db'):
                    # Convert filename back to human-readable coach name
                    coach_name = file[:-3].replace('_', ' ')
                    self.coach_select_combo.addItem(coach_name)
                    self.add_coach_select_combo.addItem(coach_name)
    
    def update_date_and_play_number(self):
        """
        Update the game date and play number fields based on the selected coach.
        Automatically fills in the last used date and calculates the next play number.
        """
        coach_name = self.add_coach_select_combo.currentText()
        if coach_name:
            last_date, last_play_number = self.get_last_play_info(coach_name)
            
            # Set game date to last date or today if no plays exist
            if not self.game_date.text().strip():
                if last_date:
                    self.game_date.setText(last_date)
                else:
                    today = datetime.now().strftime('%Y-%m-%d')
                    self.game_date.setText(today)
            
            # Set play number to next number for the current date
            if not self.play_number.text().strip():
                current_date = self.game_date.text()
                if current_date == last_date and last_play_number is not None:
                    self.play_number.setText(str(last_play_number + 1))
                else:
                    self.play_number.setText("1")
    
    def create_coach(self):
        """
        Create a new coach database.
        The database will be created in the coaches directory with a table for storing play schemes.
        """
        coach_name = self.coach_name_entry.text().strip().replace(" ", "_").upper()
        if not coach_name:
            QMessageBox.warning(self, "Error", "Please enter a coach name")
            return
            
        db_path = self.get_coach_db_path(coach_name)
        if os.path.exists(db_path):
            QMessageBox.warning(self, "Error", f"Database for {coach_name} already exists")
            return
            
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Create table for storing play schemes
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
            
            QMessageBox.information(self, "Success", f"Database for {coach_name} created successfully")
            self.update_coach_list()
            self.coach_name_entry.clear()
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error creating coach database: {str(e)}")
    
    def get_last_play_info(self, coach_name):
        """
        Get the last used date and highest play number for a coach.
        
        Args:
            coach_name (str): Name of the coach
            
        Returns:
            tuple: (last_date, last_play_number) or (None, None) if no plays exist
        """
        db_path = self.get_coach_db_path(coach_name)
        if not os.path.exists(db_path):
            return None, None
            
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Get the most recent date and its corresponding highest play number
            cursor.execute("""
                SELECT Game_Date, MAX(Play_Number) as Last_Play_Number
                FROM Coach_Scheme
                GROUP BY Game_Date
                ORDER BY Game_Date DESC
                LIMIT 1
            """)
            result = cursor.fetchone()
            
            if not result:
                conn.close()
                return None, None
                
            last_date, last_play_number = result
            
            conn.close()
            
            return last_date, last_play_number if last_play_number else 0
            
        except Exception as e:
            print(f"Error getting last play info: {str(e)}")
            return None, None
    
    def get_play(self):
        """
        Get play predictions based on user-selected criteria.
        Uses a SQL query with a Common Table Expression to calculate percentages.
        """
        coach_name = self.coach_select_combo.currentText().replace(" ", "_").upper()
        if not coach_name:
            QMessageBox.warning(self, "Error", "Please select a coach")
            return
            
        db_path = self.get_coach_db_path(coach_name)
        if not os.path.exists(db_path):
            QMessageBox.warning(self, "Error", f"Database for {coach_name} does not exist")
            return
            
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Use instance variables for constants
            SHORT = self.SHORT
            MEDIUM = self.MEDIUM
            LONG = self.LONG
            
            # Build the query with conditions
            query = """
            WITH TotalPlays AS (
                SELECT COUNT(*) AS Total_Play
                FROM Coach_Scheme
                WHERE 1=1
            """
            
            params = []
            
            # Add quarter condition if selected
            if self.quarter_combo.currentText() and self.quarter_combo.currentText() != '':
                query += " AND Quarter = ?"
                params.append(int(self.quarter_combo.currentText()))
            
            # Add down condition if selected
            if self.down_combo.currentText() and self.down_combo.currentText() != '':
                query += " AND Down = ?"
                params.append(int(self.down_combo.currentText()))
            
            # Add numeric conditions if values are provided
            if self.distance_spin.text():
                if int(self.distance_spin.text()) <= SHORT:
                    query += " AND Distance <= " + str(SHORT)
                elif int(self.distance_spin.text()) <= MEDIUM:
                    query += " AND Distance <= " + str(MEDIUM) + " AND Distance > " + str(SHORT)
                elif int(self.distance_spin.text()) <= LONG:
                    query += " AND Distance <= " + str(LONG) + " AND Distance > " + str(MEDIUM)
                elif int(self.distance_spin.text()) > LONG:
                    query += " AND Distance > " + str(LONG)
                params.append(int(self.distance_spin.text()))
            
            # Add yard line condition if provided
            if self.yard_line_spin.text():
                query += " AND Yard_Line = ?"
                params.append(int(self.yard_line_spin.text()))
            
            # Add text conditions if values are provided
            if self.formation_text.text():
                query += " AND Formation = ?"
                params.append(self.formation_text.text())
            
            if self.personnel_spin.text():
                query += " AND Personel = ?"
                params.append(int(self.personnel_spin.text()))
            
            query += """
            )
            SELECT 
                Formation, 
                Play, 
                (COUNT(*) * 100.0) / (SELECT Total_Play FROM TotalPlays) AS Percent_Chance
            FROM Coach_Scheme
            WHERE 1=1
            """
            
            # Add quarter condition if selected
            if self.quarter_combo.currentText() and self.quarter_combo.currentText() != '':
                query += " AND Quarter = ?"
                params.append(int(self.quarter_combo.currentText()))
            
            # Add down condition if selected
            if self.down_combo.currentText() and self.down_combo.currentText() != '':
                query += " AND Down = ?"
                params.append(int(self.down_combo.currentText()))
            
            # Add numeric conditions if values are provided
            if self.distance_spin.text():
                if int(self.distance_spin.text()) <= SHORT:
                    query += " AND Distance <= " + str(SHORT)
                elif int(self.distance_spin.text()) <= MEDIUM:
                    query += " AND Distance <= " + str(MEDIUM) + " AND Distance > " + str(SHORT)
                elif int(self.distance_spin.text()) <= LONG:
                    query += " AND Distance <= " + str(LONG) + " AND Distance > " + str(MEDIUM)
                elif int(self.distance_spin.text()) > LONG:
                    query += " AND Distance > " + str(LONG)
                params.append(int(self.distance_spin.text()))
            
            if self.yard_line_spin.text():
                query += " AND Yard_Line = ?"
                params.append(int(self.yard_line_spin.text()))
            
            # Add text conditions if values are provided
            if self.formation_text.text():
                query += " AND Formation = ?"
                params.append(self.formation_text.text())
            
            if self.personnel_spin.text():
                query += " AND Personel = ?"
                params.append(int(self.personnel_spin.text()))
            
            query += " GROUP BY Formation, Play ORDER BY Percent_Chance DESC"
            
            cursor.execute(query, params)
            results = cursor.fetchall()
            
            if not results:
                QMessageBox.information(self, "Results", "No plays found matching the criteria")
                return
                
            # Format results for display
            result_text = "Play Prediction Results:\n\n"
            for formation, play, chance in results:
                result_text += f"Formation: {formation}, Play: {play}, Chance: {chance:.1f}%\n"
            
            QMessageBox.information(self, "Results", result_text)
            
            conn.close()
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error getting play: {str(e)}")
            print(f"Error details: {str(e)}")
    
    def add_play(self):
        """
        Add a new play to the selected coach's database.
        Automatically fills in the game date and play number if not provided.
        """
        coach_name = self.add_coach_select_combo.currentText().replace(" ", "_").upper()
        if not coach_name:
            QMessageBox.warning(self, "Error", "Please select a coach")
            return
            
        db_path = self.get_coach_db_path(coach_name)
        if not os.path.exists(db_path):
            QMessageBox.warning(self, "Error", f"Database for {coach_name} does not exist")
            return
            
        try:
            # Get last play info before connecting to database
            last_date, last_play_number = self.get_last_play_info(coach_name)
            
            # Debug output
            print(f"Last date: {last_date}, Last play number: {last_play_number}")
            
            # If no date is provided, use last date or today's date
            if not self.game_date.text().strip():
                if last_date:
                    self.game_date.setText(last_date)
                else:
                    today = datetime.now().strftime('%Y-%m-%d')
                    self.game_date.setText(today)
                    
                # Debug output
                print(f"Set game date to: {self.game_date.text()}")
            
            # If no play number is provided, use next number for the date
            if not self.play_number.text().strip():
                current_date = self.game_date.text()
                if current_date == last_date and last_play_number is not None:
                    self.play_number.setText(str(last_play_number + 1))
                else:
                    self.play_number.setText("1")
                
                # Debug output
                print(f"Set play number to: {self.play_number.text()}")
            
            # Now connect to database and validate
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Validate required fields
            required_fields = {
                'Game_Date': self.game_date.text(),
                'Play_Number': self.play_number.text(),
                'Quarter': self.quarter.text(),
                'Down': self.down.text(),
                'Distance': self.distance.text(),
                'Yard_Line': self.yard_line.text(),
                'Personel': self.personnel.text(),
                'Formation': self.formation.text(),
                'Play': self.play.text()
            }
            
            missing_fields = [field for field, value in required_fields.items() if not value.strip()]
            if missing_fields:
                QMessageBox.warning(self, "Error", f"Please fill in the following fields: {', '.join(missing_fields)}")
                return
            
            # Insert the play
            cursor.execute("""
                INSERT INTO Coach_Scheme (Game_Date, Play_Number, Quarter, Down, Distance, Yard_Line, Personel, Formation, Play)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.game_date.text(),
                int(self.play_number.text()),
                self.quarter.text(),
                self.down.text(),
                self.distance.text(),
                self.yard_line.text(),
                self.personnel.text(),
                self.formation.text(),
                self.play.text()
            ))
            
            conn.commit()
            conn.close()
            
            QMessageBox.information(self, "Success", "Play added successfully!")
            
            # Clear the form
            self.game_date.clear()
            self.play_number.clear()
            self.quarter.clear()
            self.down.clear()
            self.distance.clear()
            self.yard_line.clear()
            self.personnel.clear()
            self.formation.clear()
            self.play.clear()
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error adding play: {str(e)}")
            print(f"Error details: {str(e)}")

    def apply_settings(self):
        """
        Apply the new settings values.
        """
        try:
            self.SHORT = self.short_spin.value()
            self.MEDIUM = self.medium_spin.value()
            self.LONG = self.long_spin.value()
            
            # Ensure values are in proper order
            if self.SHORT >= self.MEDIUM or self.MEDIUM >= self.LONG:
                QMessageBox.warning(self, "Error", "Short must be less than Medium, and Medium must be less than Long")
                return
                
            QMessageBox.information(self, "Success", "Settings have been updated successfully")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error applying settings: {str(e)}")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = PlayPredictorGUI()
    window.show()
    sys.exit(app.exec())