from flask import Flask, render_template, request

app = Flask(__name__)

# --- Your simulated log data ---
EMAIL_LOGS = [
    {"sender": "alice@techcorp.com", "recipient": "bob@techcorp.com", "subject": "Mandatory Policy Update", "has_attachment": True},
    {"sender": "bob@techcorp.com", "recipient": "alice@techcorp.com", "subject": "Quarterly Report", "has_attachment": False},
]

AUTH_LOGS = [
    {"timestamp": "2026-06-06 08:32:15", "user": "alice@techcorp.com", "source_ip": "192.168.1.50", "status": "SUCCESS"},
    {"timestamp": "2026-06-06 08:40:10", "user": "bob@techcorp.com", "source_ip": "203.0.113.42", "status": "SUCCESS", "note": "Suspicious login"},
    {"timestamp": "2026-06-06 11:05:15", "user": "charlie@techcorp.com", "source_ip": "198.51.100.99", "status": "FAILED"},
]

PROCESS_LOGS = [
    {"timestamp": "2026-06-06 08:30:15", "user": "alice@techcorp.com", "host": "WORKSTATION-01", "process": "update_policy.exe", "parent": "outlook.exe"},
    {"timestamp": "2026-06-06 08:35:50", "user": "bob@techcorp.com", "host": "WORKSTATION-02", "process": "cmd.exe", "parent": "update_policy.exe"},
]

@app.route('/')
def home():
    return render_template('index.html', 
                           emails=EMAIL_LOGS, 
                           auths=AUTH_LOGS, 
                           processes=PROCESS_LOGS,
                           result=None)

@app.route('/investigate', methods=['POST'])
def investigate():
    suspect = request.form.get('suspect')
    if suspect == "alice":
        result = "✅ Alice sent a legitimate policy update. She has a clean record. Keep looking!"
    elif suspect == "bob":
        result = "🚨 CRITICAL ALERT! You have identified the insider threat! \n\nBob had a 'Suspicious login' flagged from an unusual IP (203.0.113.42) and a bizarre process execution. \n\n**You solved the case!**"
    elif suspect == "charlie":
        result = "❌ Charlie had a failed login, but it's an old IP address. He's a red herring. Investigate the other users."
    else:
        result = "Unknown target. Stay sharp."
    
    return render_template('index.html', 
                           emails=EMAIL_LOGS, 
                           auths=AUTH_LOGS, 
                           processes=PROCESS_LOGS,
                           result=result)

@app.route('/reset')
def reset():
    return home()

if __name__ == '__main__':
    app.run(debug=True)
