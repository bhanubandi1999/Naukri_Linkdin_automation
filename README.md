# 🤖 Automated Naukri & LinkedIn Profile Updater

This project automates the process of updating **Naukri** and **LinkedIn** profiles using Python & Playwright.
It rotates **resume headlines**, deletes and re-uploads resumes, and even updates **LinkedIn remote service descriptions** — saving time and keeping your profiles fresh.

---

## ✨ Features
- 🔄 Auto-rotates **resume headlines** from a pre-defined list.  
- 📄 Deletes old resume and uploads a new one on **Naukri**.  
- 📝 Updates **LinkedIn profile headline** automatically.  
- 🌍 Updates **LinkedIn remote service descriptions** with rotating messages.  
- 🖥 Runs in **Chrome (persistent session)** to avoid re-login every time.  
- 🪟 Minimizes browser window for clean background execution.  

---

## 📋 Requirements

### 1. Install Python
Make sure Python **3.8+** is installed. Check with:
```bash
python3 --version
```

### 2. Install Playwright
Install Playwright and required browsers:
```bash
pip install playwright
playwright install
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, create one with:
```txt
playwright
```

### 4. Google Chrome Path
Update the Chrome path in the script if needed:
```python
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # For Mac
```
- **Windows example:** `"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"`  
- **Linux example:** `"/usr/bin/google-chrome"`

### 5. Resume File
Update the resume path:
```python
resume_path = "/Users/username/Downloads/Resume.pdf"
```

### 6. Credentials
Store your Naukri credentials in **environment variables** (recommended):
```bash
export NAUKRI_EMAIL="your_email@example.com"
export NAUKRI_PASS="your_password"
```

Inside Python, they are accessed as:
```python
os.getenv("NAUKRI_EMAIL")
os.getenv("NAUKRI_PASS")
```

---

## 🚀 How to Run
Run the script directly:
```bash
python main.py
```

The script will:
1. Log in (session is persisted, so login is usually skipped after the first run).  
2. Navigate to your **Naukri profile** → update headline → delete and upload resume.  
3. Navigate to **LinkedIn** → update headline and remote description.  
4. Sleep for 1 hour (configurable) → repeat.  

---

## ⚙️ Configuration

### Headline Rotation
Edit these arrays in the script:
```python
HEADLINES = ["DevOps Engineer | ...", "AWS DevOps Engineer | ...", ...]
LINKDIN_HEADLINES = ["DevOps Engineer | 3.5+ yrs ...", ...]
LINKDIN_REMOTE_HEADLINES = ["I specialize in automation...", ...]
```

### Sleep Interval
At the bottom of the script:
```python
time.sleep(3600)  # 1 hour
```
Change as needed (value is in seconds).

---

## 🛠 Troubleshooting

- **Chrome not launching?**  
  Update the `CHROME_PATH` to your system’s Chrome executable.

- **Playwright errors?**  
  Make sure you ran:
  ```bash
  playwright install
  ```

- **Selectors not working?**  
  Inspect Naukri/LinkedIn pages, as selectors may change over time. Update the `page.locator(...)` or `page.click(...)` accordingly.

---

## ⚠️ Disclaimer
This script is for **educational purposes** only.  
Automating interactions with LinkedIn or Naukri may violate their **Terms of Service**. Use responsibly at your own risk.

---

## 👨‍💻 Author
**Bhanuprakash Reddy**  
🚀 DevOps Engineer | AWS | Kubernetes | CI/CD | Cloud Automation  
📫 DM me on [LinkedIn](https://www.linkedin.com/in/bandi-bhanu-prakash-reddy/)
