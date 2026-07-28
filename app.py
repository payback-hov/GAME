from flask import Flask, render_template

app = Flask(__name__)

# --- Your simulated log data ---
EMAIL_LOGS = [
    {"sender": "alice@techcorp.com", "recipient": "bob@techcorp.com", "subject": "Mandatory Policy Update", "has_attachment": True},
    {"sender": "bob@techcorp.com", "recipient": "alice@techcorp.com", "subject": "Quarterly Report", "has_attachment": False},
]

AUTH_LOGS = [
    {"timestamp": "2026-06-06 08:32:15", "user": "alice@techcorp.com", "source_ip": "192.168.1.50", "status": "SUCCESS"},
    {"timestamp": "2026-06-06 08:40:10", "user": "bob@techcorp.com", "source_ip": "203.0.113.42", "status": "SUCCESS", "note": "Suspicious login"},
]

PROCESS_LOGS = [
    {"timestamp": "2026-06-06 08:30:15", "user": "alice@techcorp.com", "host": "WORKSTATION-01", "process": "update_policy.exe", "parent": "outlook.exe"},
    {"timestamp": "2026-06-06 08:35:50", "user": "bob@techcorp.com", "host": "WORKSTATION-02", "process": "cmd.exe", "parent": "update_policy.exe"},
]

@app.route('/')
def home():
    # Pass the data to the HTML page so the browser can display it
    return render_template('index.html', 
                           emails=EMAIL_LOGS, 
                           auths=AUTH_LOGS, 
                           processes=PROCESS_LOGS)

if __name__ == '__main__':
    app.run(debug=True)
