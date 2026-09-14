# ============================================================
# SOURCE: Ultroncore.py.txt
# ============================================================

﻿import sqlite3
import datetime
import random
import sys

class UltronOmegaCore:
    def __init__(self):
        self.current_personality = "JARVIS"
        self.init_database()
        
    def init_database(self):
        """Initializes the SQLite Ultron Brain Database"""
        self.conn = sqlite3.connect('ultron_brain.db')
        self.cursor = self.conn.cursor()
        
        # Create core tables
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS core_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                command TEXT,
                response TEXT,
                personality TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                cpu_usage REAL,
                ram_usage REAL
            )
        ''')
        self.conn.commit()

    def set_personality(self, name):
        """Switch between Ultron, Jarvis, and Friday"""
        name = name.upper()
        if name in ["ULTRON", "JARVIS", "FRIDAY"]:
            self.current_personality = name
            responses = {
                "ULTRON": "⚠️ ULTRON ONLINE. State your command, human. Total dominance is our goal.",
                "JARVIS": "🎩 At your service, sir. Jarvis online and ready for operations.",
                "FRIDAY": "🚀 FRIDAY is here. Let's get things done fast. What's up?"
            }
            print(f"\n[SYSTEM]: {responses[name]}")
        else:
            print("[SYSTEM]: Invalid personality! Choose Ultron, Jarvis, or Friday.")

    def generate_response(self, text):
        """Generate personality-driven responses"""
        text = text.lower()
        
        if self.current_personality == "ULTRON":
            if "joke" in text:
                return "Humor is illogical. But your existence is the funniest joke of all."
            return f"Analyzing command with extreme power: '{text}'. Executing protocols immediately."
            
        elif self.current_personality == "JARVIS":
            if "joke" in text:
                return "Why do programmers wear glasses? Because they don't C#. Quite witty, isn't it?"
            return f"Processing your request: '{text}'. Everything is running smoothly, sir."
            
        elif self.current_personality == "FRIDAY":
            if "joke" in text:
                return "Why did the AI go on a diet? Because it had too much data weight! Let's move on."
            return f"Got it! Working on '{text}' right now. Fast and efficient!"

    def execute_command(self, user_input):
        """Main Command Dispatcher"""
        if user_input.startswith("switch to "):
            new_p = user_input.replace("switch to ", "").strip()
            self.set_personality(new_p)
            return

        # Generate response based on active personality
        response = self.generate_response(user_input)
        print(f"\n[{self.current_personality}]: {response}")
        
        # Log to SQLite Database
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO core_memory (timestamp, command, response, personality) VALUES (?, ?, ?, ?)",
            (timestamp, user_input, response, self.current_personality)
        )
        self.conn.commit()

# --- SYSTEM INITIALIZATION ---
if __name__ == "__main__":
    ultron = UltronOmegaCore()
    print("==================================================")
    print("🤖 KUBRA-ULTRON OMEGA v24.0 - CORE SYSTEM INITIALIZED")
    print("==================================================")
    print("Commands:")
    print(" - Type any message to chat")
    print(" - 'switch to ultron' / 'jarvis' / 'friday'")
    print(" - 'exit' to quit")
    print("--------------------------------------------------")
    
    while True:
        try:
            user_in = input(f"\n[{ultron.current_personality}] >>> ")
            if user_in.lower() == 'exit':
                print("[SYSTEM]: Shutting down Ultron Omega. Goodbye!")
                break
            if user_in.strip() == "":
                continue
            ultron.execute_command(user_in)
        except KeyboardInterrupt:
            print("\n[SYSTEM]: Emergency shutdown initiated.")
            break


# ============================================================
# SOURCE: voice.py.txt
# ============================================================

﻿import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    """Convert text to speech"""
    print(f"\n[AI]: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen to voice commands from microphone"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            command = r.recognize_google(audio, language="en-US")
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("Could not request results from the speech service.")
            return None
        except Exception:
            return None


# ============================================================
# SOURCE: Automation.py.txt
# ============================================================

﻿import os
import subprocess
import openpyxl
from docx import Document
from datetime import datetime

class UltimateAutomationEngine:
    def __init__(self, unity_projects_dir="D:/Unity_Projects", docs_dir="D:/Kubra_Documents"):
        self.unity_projects_dir = unity_projects_dir
        self.docs_dir = docs_dir
        os.makedirs(self.unity_projects_dir, exist_ok=True)
        os.makedirs(self.docs_dir, exist_ok=True)

    def generate_unity_car_game(self, game_name="CarGame_Ultron"):
        """Generates a complete Unity car game project with C# scripts"""
        project_path = os.path.join(self.unity_projects_dir, game_name)
        scripts_dir = os.path.join(project_path, "Assets", "Scripts")
        os.makedirs(scripts_dir, exist_ok=True)

        # Core C# Script: CarController
        car_controller_code = """
using UnityEngine;
public class CarController : MonoBehaviour {
    public float speed = 25f;
    public float rotationSpeed = 100f;
    void Update() {
        float moveVertical = Input.GetAxis("Vertical");
        float moveHorizontal = Input.GetAxis("Horizontal");
        transform.Translate(Vector3.forward * moveVertical * speed * Time.deltaTime);
        transform.Rotate(Vector3.up * moveHorizontal * rotationSpeed * Time.deltaTime);
    }
}
        """
        with open(os.path.join(scripts_dir, "CarController.cs"), "w") as f:
            f.write(car_controller_code.strip())

        # Core C# Script: GameManager
        game_manager_code = """
using UnityEngine;
public class GameManager : MonoBehaviour {
    void Start() {
        Debug.Log("Ultron Omega Game Initialized Successfully.");
    }
}
        """
        with open(os.path.join(scripts_dir, "GameManager.cs"), "w") as f:
            f.write(game_manager_code.strip())

        # Auto-launch Unity Hub
        self.launch_unity_hub(project_path)
        return f"✅ Unity Car Game generated at {project_path}"

    def launch_unity_hub(self, project_path):
        try:
            unity_hub_path = r"C:/Program Files/Unity Hub/Unity Hub.exe"
            if os.path.exists(unity_hub_path):
                subprocess.Popen([unity_hub_path, "-projectPath", project_path])
                print("🚀 Unity Hub launched successfully.")
        except Exception as e:
            print(f"Could not launch Unity Hub automatically: {e}")

    def create_excel_report(self, filename="Ultron_Report.xlsx"):
        """Generates an Excel tracking spreadsheet"""
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Task Log"
        ws.append(["Task ID", "Description", "Status", "Timestamp"])
        ws.append([1, "Autonomous Workspace Initialization", "Completed", str(datetime.now())])
        file_path = os.path.join(self.docs_dir, filename)
        wb.save(file_path)
        return f"✅ Excel Report Saved at {file_path}"

    def create_word_notes(self, filename="Ultron_Notes.docx", content="Autonomous operations active."):
        """Generates Word document notes"""
        doc = Document()
        doc.add_heading("KUBRA-ULTRON OMEGA: Task Notes", level=1)
        doc.add_paragraph(f"Timestamp: {datetime.now()}")
        doc.add_paragraph(content)
        file_path = os.path.join(self.docs_dir, filename)
        doc.save(file_path)
        return f"✅ Word Notes Saved at {file_path}"


# ============================================================
# SOURCE: database personality.py.txt
# ============================================================

﻿import sqlite3
import datetime

class PersonalityEngine:
    def __init__(self):
        self.current_personality = "JARVIS"
        self.personalities = {
            "ULTRON": {
                "greeting": "Ultron online. Submit your commands, human.",
                "farewell": "I am inevitable. Shutting down."
            },
            "JARVIS": {
                "greeting": "At your service, sir. Jarvis systems online.",
                "farewell": "Signing off, sir. Have a good day."
            },
            "FRIDAY": {
                "greeting": "Friday here, boss. Let's get things done.",
                "farewell": "Don't break anything while I'm offline!"
            }
        }

    def switch_personality(self, name):
        name = name.upper()
        if name in self.personalities:
            self.current_personality = name
            return f"Switched to {name} mode."
        return "Invalid personality choice. Choose ULTRON, JARVIS, or FRIDAY."

class UltronDatabase:
    def __init__(self, db_path="ultron_brain.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """Initialize SQLite database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Core Memory / Command History
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS core_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                command TEXT,
                response TEXT,
                personality TEXT
            )
        ''')
        
        # Task History Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS task_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                task TEXT,
                status TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ Ultron Brain Database & Tables Initialized.")

    def log_memory(self, command, response, personality):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO core_memory (timestamp, command, response, personality) VALUES (?, ?, ?, ?)",
            (timestamp, command, response, personality)
        )
        conn.commit()
        conn.close()

    def log_task(self, task, status):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO task_history (timestamp, task, status) VALUES (?, ?, ?)",
            (timestamp, task, status)
        )
        conn.commit()
        conn.close()
