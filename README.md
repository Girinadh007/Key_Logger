# 🛡️ Simple Python Keylogger

This is a lightweight, educational keylogger written in Python. It captures keystrokes in real-time and logs them into a single file, stored locally on your machine.

> ⚠️ This tool is for educational and authorized testing purposes **only**. Do **not** run it on systems or users without explicit consent. Misuse may violate privacy laws.

---

## 📦 Features

- ✅ Captures all keystrokes silently
- ✅ Logs to a single, timestamped file
- ✅ Runs continuously in the background
- ✅ Cross-platform (Windows, macOS, Linux)

---

## 🛠 Requirements

- Python 3.6+
- [`pynput`](https://pypi.org/project/pynput/)

🙏 Disclaimer

This software is provided for educational use only. The author is not responsible for any misuse or damage caused by running this software.
🚀 How to Run 
Clone or download this repository:

    git clone https://github.com/Girinadh007/Key_Logger.git
    cd Key_Logger  

Run the script:

    python keylogger.py

Start typing in any open application (e.g., Notepad, browser, text editor). Your keystrokes will be logged

📁 Log Output

All keystrokes are saved to:

 """ keylogs/keylog_YYYY-MM-DD_HH-MM-SS.txt """

Each key is appended to the file as you type.

```bash
pip install -r requirements.txt
