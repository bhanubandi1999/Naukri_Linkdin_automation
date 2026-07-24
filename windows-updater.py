import time
import random
from playwright.sync_api import sync_playwright

# =====================================================
# CONFIG
# =====================================================

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

NAUKRI_LOGIN_URL = "https://www.naukri.com/nlogin/login"
NAUKRI_PROFILE_URL = "https://www.naukri.com/mnjuser/profile"

HEADLINE_CLICK = "https://www.naukri.com/mnjuser/profile#:~:text=upto%202%20MB-,Resume%20headline,editOneTheme,-AWS%20DevOps%20Engineer"

RESUME_DELETE = "https://www.naukri.com/mnjuser/profile?id=&altresid#:~:text=downloadOneTheme-,deleteOneTheme,-Choose%20File"

WAIT_MS = 5000

# =====================================================
# Headlines
# =====================================================

HEADLINES = [

"4+ Yrs Exp. DevOps Engineer | AWS | Kubernetes | Terraform | GitHub Actions | Docker | CI/CD | Platform Engineering | SRE | DevSecOps",

"4+ Yrs Exp. DevOps & Cloud Engineer | AWS | Kubernetes | Terraform | GitOps | CI/CD | Platform Engineering | Infrastructure Automation",

"4+ Yrs Exp. Platform Engineer | AWS | Kubernetes | Terraform | GitOps | Infrastructure as Code (IaC) | SRE | DevSecOps",

"4+ Yrs Exp. DevOps Engineer | AWS | Kubernetes | Terraform | Docker | Jenkins | GitHub Actions | ArgoCD | Linux",

"4+ Yrs Exp. Cloud & DevOps Engineer | AWS | Kubernetes | Terraform | Docker | GitHub Actions | CI/CD | Automation",

"4+ Yrs Exp. Site Reliability Engineer (SRE) | AWS | Kubernetes | Terraform | Monitoring | Observability | Incident Response",

"4+ Yrs Exp. Cloud Platform Engineer | AWS | Kubernetes | Terraform | Helm | ArgoCD | Platform Engineering | DevSecOps",

"4+ Yrs Exp. DevOps Engineer | Building Secure, Scalable & Reliable Cloud Platforms | AWS | Kubernetes | Terraform",

"4+ Yrs Exp. Platform & DevOps Engineer | AWS | Kubernetes | Terraform | GitHub Actions | Linux | Python | Automation",

"4+ Yrs Exp. Cloud Infrastructure Engineer | AWS | Kubernetes | Terraform | Docker | GitHub Actions | Platform Engineering",

"4+ Yrs Exp. DevOps Engineer | Cloud Native | Kubernetes | AWS | Terraform | GitOps | Observability | Automation",

"4+ Yrs Exp. DevOps Engineer | Platform Engineering | Kubernetes | AWS | Terraform | CI/CD | GitHub Actions | DevSecOps",

"4+ Yrs Exp. Platform Engineer | AWS | Kubernetes | Terraform | Docker | Helm | ArgoCD | Prometheus | Grafana",

"4+ Yrs Exp. Cloud Engineer | AWS | Kubernetes | Infrastructure Automation | Terraform | Ansible | GitOps | Linux",

"4+ Yrs Exp. DevOps & Platform Engineer | AWS | Kubernetes | Terraform | GitHub Actions | Docker | ArgoCD | Observability",

"4+ Yrs Exp. Platform Engineer | Cloud Infrastructure | AWS | Kubernetes | Terraform | GitOps | Automation | SRE",

"4+ Yrs Exp. DevOps Engineer | AWS | Azure | Kubernetes | Terraform | Multi-Cloud | GitOps | Platform Engineering",

"4+ Yrs Exp. DevOps Engineer | Cloud Infrastructure | AWS | Kubernetes | Terraform | Linux | Python | CI/CD | DevSecOps",

"4+ Yrs Exp. DevOps Engineer | Platform Engineering | Cloud Native | AWS | Kubernetes | Terraform | Reliability | Automation",

"4+ Yrs Exp. DevOps Engineer | Platform Engineer | Cloud Engineer | AWS | Kubernetes | Terraform | Docker | GitHub Actions | Jenkins | ArgoCD | Linux | Python | SRE | DevSecOps | Observability",

"4+ Yrs Exp. DevOps Engineer | Platform Engineer | SRE | AWS | Kubernetes | Terraform | GitOps | CI/CD | DevSecOps | Linux",

"4+ Yrs Exp. Cloud Platform & DevOps Engineer | AWS | Kubernetes | Terraform | Helm | GitHub Actions | ArgoCD | Security",

"4+ Yrs Exp. Platform Engineer | Kubernetes | AWS | Terraform | GitOps | Cloud Infrastructure | Automation | Reliability",

"4+ Yrs Exp. DevOps Engineer | AWS | Kubernetes | Docker | Terraform | GitHub Actions | Jenkins | Linux | Python | Automation",

"4+ Yrs Exp. Cloud Infrastructure & DevOps Engineer | AWS | Kubernetes | Terraform | IaC | GitOps | CI/CD | SRE"

]

# =====================================================
# Accounts
# =====================================================

ACCOUNTS = [

    {
        "name": "Personal Account",

        "username": "bhanureddybandi@gmail.com",

        "password": "password",

        "user_data_dir": "/Users/bhanubandi/chrome-naukri-1",

        "resume": "/Users/bhanubandi/Documents/Bandi_Bhanuprakash_Devops_Jul-2026-resume.pdf",

        "headlines": HEADLINES
    },

    {
        "name": "Second Account",

        "username": "bhanureddy.awsdevops@gmail.com",

        "password": "password",

        "user_data_dir": "/Users/bhanubandi/chrome-naukri-2",

        "resume": "/Users/bhanubandi/Documents/Bandi_Bhanuprakash_Devops_Jul-2026-resume.pdf",

        "headlines": HEADLINES
    }

]


def login(page, account):
    """
    Login only if login page is shown.
    """

    page.goto(NAUKRI_LOGIN_URL)

    page.wait_for_timeout(3000)

    try:

        if page.locator("#usernameField").count() > 0:

            print("Logging in...")

            page.fill("#usernameField", account["username"])

            page.fill("#passwordField", account["password"])

            page.click("button[type='submit']")

            page.wait_for_load_state("networkidle")

            page.wait_for_timeout(WAIT_MS)

            print("Login Successful")

    except Exception as e:

        print("Login skipped:", e)


def update_naukri(account):

    print("=" * 70)
    print("Updating :", account["name"])
    print("=" * 70)

    with sync_playwright() as p:

        context = p.chromium.launch_persistent_context(

            user_data_dir=account["user_data_dir"],

            executable_path=CHROME_PATH,

            headless=False,
    
        )

        page = context.new_page()

    # Wait a moment for the window to appear
        page.wait_for_timeout(1000)

        # Minimize Chrome
        try:
            session = context.new_cdp_session(page)

            window = session.send("Browser.getWindowForTarget")

            session.send(
                "Browser.setWindowBounds",
                {
                    "windowId": window["windowId"],
                    "bounds": {
                        "windowState": "minimized"
                    }
                }
            )

            print("✅ Chrome minimized")

        except Exception as e:
            print("❌ Failed to minimize:", e)


        # ---------------- Login ----------------

        login(page, account)

        # ---------------- Profile ----------------
        print("Navigating to Profile Page...")
        page.goto(NAUKRI_PROFILE_URL)

        page.wait_for_timeout(WAIT_MS)

        # ---------------- Resume Headline ----------------
        print("Navigating to Resume Headline Page...")
        page.goto(HEADLINE_CLICK)

        page.wait_for_timeout(WAIT_MS)

        page.click("//span[normalize-space(text())='Resume headline']/ancestor::div[contains(@class,'widget')]//span[@class='edit icon']")

        page.wait_for_timeout(WAIT_MS)

        headline = random.choice(HEADLINES)

        print("Selected Headline:", headline)


        print("Updating Resume Headline...")
        
        page.locator("#resumeHeadlineTxt").fill(headline)

        page.locator("button.btn-dark-ot[type='submit']").first.click()

        print("Headline Updated")

        page.wait_for_timeout(WAIT_MS)

        # ---------------- Resume Upload ----------------
        print("Navigating to Resume Upload Page...")
        page.goto(RESUME_DELETE)

        page.wait_for_timeout(WAIT_MS)

        try:
            print("Navigating to Resume Delete Page...")
            page.click("//i[@title='Click here to delete your resume']")

            page.wait_for_timeout(2000)
            print("Deleting Resume...")
            page.locator("button.btn-dark-ot:has-text('Delete')").nth(1).click()
            print("Resume Deleted")
            page.wait_for_timeout(10000)

        except:

            print("Delete skipped")

        print("Navigating to Resume Upload Page...")
        with page.expect_file_chooser() as fc:

            page.locator("span.dummyUploadNewCTA").click()

        fc.value.set_files(account["resume"])

        print("Resume Uploaded")

        page.wait_for_timeout(WAIT_MS)

        context.close()


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    while True:

        for account in ACCOUNTS:

            try:

                update_naukri(account)

            except Exception as e:

                print(account["name"], "Failed")

                print(e)

            print("Waiting 30 seconds before next account...")

            time.sleep(30)

        print("\nBoth accounts updated successfully.")

        print("Sleeping for 30 minutes...\n")

        time.sleep(1800)
