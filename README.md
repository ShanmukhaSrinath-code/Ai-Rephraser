Perfect 👍
Here is a **clean, copy-paste ready `README.md`** you can directly use for your project or share with anyone starting fresh.

---

# 🚀 System-Wide AI Rephraser & Writer (Ctrl + Alt + R)

This project provides a **system-wide AI-powered writing assistant** that works across **any application** on Windows.

👉 Highlight any text
👉 Press **Ctrl + Alt + R**
👉 The text is **instantly replaced** with a professional, creative, and polished version (with emojis when appropriate).

It can:

* ✨ Rephrase sentences professionally
* ✍️ Write full emails, messages, announcements
* 🎉 Generate creative content (e.g., New Year wishes)
* 🌍 Work in **Notepad, Browser, VS Code, Email, Chat apps**
* 🧠 Run fully in the background using Docker + AutoHotkey

---

## 🧠 How It Works (High Level)

```
Highlighted Text
      ↓
Ctrl + Alt + R (AutoHotkey)
      ↓
Docker (FastAPI + OpenAI)
      ↓
AI-generated response
      ↓
Replaces selected text
```

---

## 📦 Project Structure

```
AutoHotKey/
│
├── Dockerfile
├── docker-compose.yml
├── app.py
├── rephrase.py
├── answer_web.py   (optional)
├── rephrase.ahk
├── config.env
└── README.md
```

---

## 🔧 Prerequisites

Make sure you have the following installed:

* **Docker Desktop (Windows)**
* **AutoHotkey v1**
* **Internet connection**
* **OpenAI API key**

---

## 🔑 Configuration (`config.env`)

Create or edit `config.env` (single-line values only):

```env
OPENAI_API_KEY=your_openai_api_key_here
PERPLEXITY_API_KEY=

SYSTEM_PROMPT="You are a professional and creative writing assistant who produces polished, engaging, and expressive content. If the input is a sentence or paragraph, rewrite it using refined, articulate language with enhanced flow and elevated vocabulary. If the input asks to write content such as an email, message, greeting, or announcement, generate a complete, well-structured, and engaging piece that feels warm, human, and thoughtfully crafted. Use creativity, tasteful humor, expressive phrasing, and emojis when appropriate, while keeping the overall tone professional. Do not ask questions, do not add explanations, and output only the final written content."
```

⚠️ Important:

* No spaces around `=`
* Prompt must be **one single line**
* Use straight quotes `" "`

---

## 🐳 Start the Backend (Docker)

From the project folder:

```bash
docker compose up --build -d
```

Verify it’s running:

```bash
docker ps
```

You should see:

```
autohotkey-ai-rephraser   Up   0.0.0.0:8000->8000
```

---

## ⌨️ AutoHotkey Script (`rephrase.ahk`)

This script listens for **Ctrl + Alt + R** and replaces highlighted text.

Make sure this file exists and contains the working script (already configured).

---

## ▶️ Run AutoHotkey (One Time)

1. Go to the project folder
2. Right-click `rephrase.ahk`
3. Click **Show more options → Run Script**
4. Confirm **green “H” icon** appears in the system tray

---

## 🔁 Auto-Start on System Boot (Recommended)

To make it work **automatically whenever Windows starts**:

1. Press **Win + R**
2. Type:

   ```
   shell:startup
   ```
3. Press Enter
4. Copy `rephrase.ahk` into this Startup folder

✅ Now the shortcut works **every time you turn on your laptop**

---

## 🧪 How to Use (Daily Workflow)

### 🔹 Rephrase text

1. Type any sentence:

   ```
   this sentence need improve
   ```
2. Highlight it
3. Press **Ctrl + Alt + R**

➡️ It is replaced with a polished version.

---

### 🔹 Write full content

1. Type:

   ```
   Write a fun, engaging New Year message to my team with emojis and a warm professional tone.
   ```
2. Highlight it
3. Press **Ctrl + Alt + R**

➡️ A complete, well-written message is generated and replaces the text.

---

## ✅ Works Everywhere

* Notepad
* Browser text boxes
* VS Code
* Emails
* Chat applications
* Documents

Anywhere text can be selected.

---

## 🔍 Troubleshooting

### ❌ Shortcut not working

* Check if **green “H” icon** is visible
* If not, run `rephrase.ahk`

---

### ❌ Docker not responding

Run:

```bash
docker compose up -d
```

---

### ❌ Emojis look broken (`��`)

* Ensure `app.py` returns **plain text**
* Ensure `rephrase.ahk` is running with UTF-8 support
* Restart AutoHotkey script

---

## 🧠 Golden Rule

> **Highlight text → Ctrl + Alt + R → Done**

No need to:

* Open VS Code
* Run Python manually
* Restart Docker daily

---

## 🎉 Final Result

You now have:

* ✅ System-wide AI writer
* ✅ Auto-start on boot
* ✅ Creative + professional writing
* ✅ Zero manual effort

---

## 📌 Future Enhancements (Optional)

* Multiple shortcuts (formal / fun / technical)
* Emoji on/off toggle
* HTML email output
* Tray menu UI
* Linux / macOS version

---

**Enjoy your personal AI writing assistant 🚀**
