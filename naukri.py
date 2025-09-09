import time
import os
from playwright.sync_api import sync_playwright
import random
from dotenv import load_dotenv

load_dotenv()

# ====== CONFIG ======
# CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Replace with your actual credentials
NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASS = os.getenv("NAUKRI_PASS")
resume_path = "/Users/bhanubandi/Downloads/Bhanuprakash_EXP-3+yrs.pdf"


NAUKRI_LOGIN_URL = "https://www.naukri.com/nlogin/login"
NAUKRI_PROFILE_URL = "https://www.naukri.com/mnjuser/profile"

HEADLINE_CLICK= "https://www.naukri.com/mnjuser/profile#:~:text=upto%202%20MB-,Resume%20headline,editOneTheme,-AWS%20DevOps%20Engineer"
RESUME="https://www.naukri.com/mnjuser/profile?id=&altresid&action=modalOpen#:~:text=Resume-,Update,-Resume%20headline"
RESUME_DELETE= "https://www.naukri.com/mnjuser/profile?id=&altresid#:~:text=downloadOneTheme-,deleteOneTheme,-Choose%20File"


HEADLINES = ["DevOps Engineer | 4 yrs automating CI/CD, IaC & Kubernetes on AWS | Cut infra costs by 40% - Boosted deployment speed 65% | AWS | Kubernetes | Terraform | Jenkins | Prometheus | Docker | DevSecOps | Eks | Azure Devops | GCP |",
             "AWS DevOps Engineer | 4 yrs automating CI/CD, IaC & Kubernetes on AWS | Cut infra by costs 40% - Boosted deployment speed 65% | AWS | Kubernetes | Terraform | Jenkins | Prometheus | Docker | DevSecOps | Eks | Azure Devops | GCP |",
             "AWS DevOps Engineer | 4 yrs automating CI/CD, IaC & Kubernetes on AWS | Cut infra by costs 40% - Boosted deployment speed 65% | AWS | Kubernetes | Terraform | Jenkins | Prometheus | Docker | DevSecOps | Eks |",
             "DevOps Engineer | 4 yrs automating CI/CD, IaC & Kubernetes on AWS | Cut infra costs by 40% - Boosted deployment speed 65% | AWS | Kubernetes | Terraform | Jenkins | Prometheus | Docker | DevSecOps | Eks | Azure Devops |",
             "DevOps Engineer | 4 yrs automating CI/CD, IaC & Kubernetes on AWS | Cut infra costs by 40% - Boosted deployment speed 65% | AWS | Kubernetes | Terraform | Jenkins | Prometheus | Docker | DevSecOps |",
             ]

# keep a global index
current_index = 0

def get_next_headline():
    global current_index
    headline = HEADLINES[current_index]
    current_index = (current_index + 1) % len(HEADLINES)  # loop back to 0
    return headline


# def update_naukri():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(executable_path=CHROME_PATH, headless=False)
#         context = browser.new_context()
#         page = context.new_page()

def update_naukri():
    with sync_playwright() as p:
        # Path to your Chrome executable (Mac M1)
        CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        
        # Create a dedicated Chrome user-data directory for Naukri automation
        USER_DATA_DIR = "/Users/bhanubandi/chrome-naukri"

        # Use persistent context (keeps cookies, login sessions, etc.)
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            executable_path=CHROME_PATH,
            headless=False,
        )
        page = context.new_page()

        page.wait_for_timeout(1000)

        # Minimize the browser window
        try:
            session = context.new_cdp_session(page)
            window_info = session.send("Browser.getWindowForTarget")
            window_id = window_info["windowId"]

            session.send("Browser.setWindowBounds", {
                "windowId": window_id,
                "bounds": {"windowState": "minimized"}
            })
            print("🪟 Browser minimized successfully")
        except Exception as e:
            print("⚠️ Could not minimize browser:", e)

        # # Open Naukri login page
        # page.goto(NAUKRI_LOGIN_URL)
        # page.wait_for_timeout(3000)

        # # Enter credentials
        # try:
        #     page.fill("input#usernameField", NAUKRI_EMAIL)
        #     page.fill("input#passwordField", NAUKRI_PASS)
        #     page.click("button:has-text('Login')")
        #     page.wait_for_timeout(3000)
        #     print("✅ Logged in successfully")
        # except Exception as e:
        #     print("⚠️ Could not log in:", e)

        # Go to profile page
        try:
            page.goto(NAUKRI_PROFILE_URL)
            page.wait_for_timeout(3000)

            print("✅ navigated to profile page")
        except Exception as e:
            print("⚠️ failed to navigate to profile page", e)


        # Go to headline page
        try:
            page.goto(HEADLINE_CLICK)
            page.wait_for_timeout(3000)

            print("✅ navigated to headline")
        except Exception as e:
            print("⚠️ failed to navigate to headline", e)
        
        # Click edit button
        try:
            page.click("//span[normalize-space(text())='Resume headline']/ancestor::div[contains(@class,'widget')]//span[@class='edit icon']")
            page.wait_for_timeout(3000)

            print("✅ clicked on edit button")
        except Exception as e:
            print("⚠️ failed to click on edit button", e)

        # Fill headline
        try:
            textarea = page.locator("#resumeHeadlineTxt")   # by ID
            textarea.wait_for(state="visible", timeout=3000)
            #HEADLINE_TEXT = random.choice(HEADLINES)
            HEADLINE_TEXT = get_next_headline()

            print(f"Selected headline: {HEADLINE_TEXT}")
            textarea.fill(HEADLINE_TEXT)
            print("✅ Filled headline")
        except Exception as e:
            print("⚠️ Could not fill headline:", e)

        # Click Save button
        try:
            save_btn = page.locator("button.btn-dark-ot[type='submit']").first  
            save_btn.wait_for(state="visible", timeout=7000)
            save_btn.click()
            print("✅ Clicked on Resume Headline save button")
        except Exception as e:
            print("⚠️ Could not click save button:", e)
        page.wait_for_timeout(7000)


         # Go to Resume Update page
        try:
            page.goto(RESUME_DELETE)
            page.wait_for_timeout(3000)

            print("✅ navigated to Resume Update page")
        except Exception as e:
            print("⚠️ failed to navigate to Update page", e)

        
        # Click Resume delete button
        try:
            page.click("//i[@class='icon' and @title='Click here to delete your resume']")
            page.wait_for_timeout(2000)

            delete_btn = page.locator("button.btn-dark-ot:has-text('Delete')").nth(1)  # Select the second button with this class
            delete_btn.wait_for(state="visible", timeout=5000)
            delete_btn.click()

            print("✅ clicked on Resume delete button")
        except Exception as e:
            print("⚠️ failed to click on resume delete button", e)
        page.wait_for_timeout(15000)


        try:
           # Find the hidden input inside .attachCV
            file_input = page.locator(".attachCV input[type='file']")
            file_input.set_input_files(resume_path)
            print("✅ Resume uploaded successfully")
            page.wait_for_timeout(5000)

            
        except Exception as e:
            print("⚠️ failed to upload resume delete", e)
        page.wait_for_timeout(15000)

        context.close()
        
        # End
        print("Job done closing the browser 🎉")
        #browser.close()


if __name__ == "__main__":
    while True:
        update_naukri()
        print("⏳ Sleeping for 1 hour...")
        time.sleep(300)
       