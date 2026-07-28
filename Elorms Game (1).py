import sys
import time

# Simulated Log Database
EMAIL_LOGS = [
    {"id": "E01", "sender": "hr@techcorp-updates.com", "recipient": "alice@techcorp.com", "subject": "Mandatory Policy Update", "has_attachment": True, "attachment_name": "update_policy.iso"},
    {"id": "E02", "sender": "boss@techcorp.com", "recipient": "bob@techcorp.com", "subject": "Quarterly Report", "has_attachment": False, "attachment_name": "None"},
    {"id": "E03", "sender": "it-support@techcorp-help.com", "recipient": "charlie@techcorp.com", "subject": "Password Reset Required", "has_attachment": True, "attachment_name": "reset_tool.exe"}
]

AUTH_LOGS = [
    {"timestamp": "2026-06-06 08:15:22", "user": "alice@techcorp.com", "source_ip": "192.168.1.50", "status": "SUCCESS"},
    {"timestamp": "2026-06-06 09:30:10", "user": "alice@techcorp.com", "source_ip": "203.0.113.42", "status": "SUCCESS"}, # Suspicious login
    {"timestamp": "2026-06-06 10:11:05", "user": "bob@techcorp.com", "source_ip": "192.168.1.55", "status": "SUCCESS"},
    {"timestamp": "2026-06-06 11:00:19", "user": "charlie@techcorp.com", "source_ip": "198.51.100.99", "status": "FAILED"}
]

PROCESS_LOGS = [
    {"timestamp": "2026-06-06 09:32:00", "user": "alice@techcorp.com", "host": "WORKSTATION-01", "process": "update_policy.iso", "parent": "outlook.exe"},
    {"timestamp": "2026-06-06 09:35:12", "user": "alice@techcorp.com", "host": "WORKSTATION-01", "process": "cmd.exe", "parent": "update_policy.iso"},
    {"timestamp": "2026-06-06 10:00:00", "user": "bob@techcorp.com", "host": "WORKSTATION-02", "process": "excel.exe", "parent": "explorer.exe"}
]

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def clear_screen():
    print("\n" + "="*60 + "\n")

def display_help():
    print("Available Commands:")
    print("  emails     - View corporate email logs (check for phishing)")
    print("  auth       - View authentication / login logs")
    print("  process    - View endpoint process execution logs")
    print("  solve      - Submit your findings to close the case")
    print("  exit       - Quit the game")

def show_emails():
    clear_screen()
    print("--- EMAIL LOGS ---")
    for e in EMAIL_LOGS:
        print(f"ID: {e['id']} | From: {e['sender']} | To: {e['recipient']} | Subject: {e['subject']} | Attachment: {e['attachment_name']}")

def show_auth():
    clear_screen()
    print("--- AUTHENTICATION LOGS ---")
    for a in AUTH_LOGS:
        print(f"Time: {a['timestamp']} | User: {a['user']} | IP: {a['source_ip']} | Status: {a['status']}")

def show_process():
    clear_screen()
    print("--- PROCESS EXECUTION LOGS ---")
    for p in PROCESS_LOGS:
        print(f"Time: {p['timestamp']} | Host: {p['host']} | User: {p['user']} | Process: {p['process']} | Parent: {p['parent']}")

def solve_case():
    clear_screen()
    print("=== INCIDENT RESPONSE DEBRIEF ===")
    print("Answer the following questions to secure TechCorp and catch the attacker:\n")
    
    q1 = input("1. Which user account was successfully compromised by the attacker? ").strip().lower()
    q2 = input("2. What is the malicious external IP address used by the attacker for access? ").strip()
    q3 = input("3. What was the name of the malicious file attached to the phishing email? ").strip().lower()

    # Evaluation
    correct_user = "alice@techcorp.com"
    correct_ip = "203.0.113.42"
    correct_file = "update_policy.iso"

    score = 0
    if correct_user in q1: score += 1
    if correct_ip in q2: score += 1
    if correct_file in q3: score += 1

    print("\n" + "-"*40)
    if score == 3:
        print("🏆 SUCCESS! You solved the case like a pro KC7 Analyst!")
        print("FLAG: KC7{pyth0n_thr34t_hunt3r_2026}")
    else:
        print(f"❌ Investigation Incomplete. You got {score}/3 correct. Review the logs and try again!")
    print("-"*40)

def main():
    clear_screen()
    print_slow("raccoon 🦝 [Casey's CTI Agency]: Welcome, Analyst!")
    print_slow("TechCorp has suffered a security breach. Your mission is to inspect logs, find anomalies, and pivot through the evidence.")
    print_slow("Type 'help' to see available investigative tools.\n")

    while True:
        command = input("investigator@kc7:~# ").strip().lower()
        
        if command == "help":
            display_help()
        elif command == "emails":
            show_emails()
        elif command == "auth":
            show_auth()
        elif command == "process":
            show_process()
        elif command == "solve":
            solve_case()
        elif command == "exit":
            print("Exiting investigation. Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()