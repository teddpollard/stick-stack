import json
import sys
import os

FILE = os.path.join(os.path.dirname(__file__), "self_reminder_data.json")

def load_reminders():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_reminders(reminders):
    with open(FILE, "w") as f:
        json.dump(reminders, f, indent=2)

def list_reminders():
    reminders = load_reminders()
    if not reminders:
        print("No active reminders.")
    for idx, r in enumerate(reminders, 1):
        status = "✅" if r["done"] else "🔁"
        print(f"{idx}. {status} {r['text']}")

def add_reminder(text):
    reminders = load_reminders()
    reminders.append({"text": text, "done": False})
    save_reminders(reminders)
    print(f"Added reminder: {text}")

def mark_done(index):
    reminders = load_reminders()
    if 0 < index <= len(reminders):
        reminders[index - 1]["done"] = True
        save_reminders(reminders)
        print(f"Marked as done: {reminders[index - 1]['text']}")
    else:
        print("Invalid reminder index.")

def clear_done():
    reminders = [r for r in load_reminders() if not r["done"]]
    save_reminders(reminders)
    print("Cleared all completed reminders.")

def help():
    print("""
USAGE:
  python self_reminder.py add "Remember to breathe"
  python self_reminder.py list
  python self_reminder.py done 2
  python self_reminder.py clear
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    else:
        command = sys.argv[1]
        if command == "add":
            add_reminder(" ".join(sys.argv[2:]))
        elif command == "list":
            list_reminders()
        elif command == "done":
            try:
                mark_done(int(sys.argv[2]))
            except:
                print("Please provide a valid reminder number.")
        elif command == "clear":
            clear_done()
        else:
            help()
