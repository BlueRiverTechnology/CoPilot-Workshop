# Setup Instructions for GitHub Copilot Workshop
## Complete Environment Setup Guide

---

## Prerequisites Checklist

Before the workshop, ensure you have:

- [ ] GitHub account with Copilot access
- [ ] VS Code (latest version)
- [ ] Python 3.10+ installed
- [ ] Git installed
- [ ] Stable internet connection

---

## Step 1: GitHub Copilot Subscription

### Organization Access

Deere provides Copilot access:

1. Check your GitHub settings → Copilot
2. You should see "Enabled by your organization"
3. If not visible, Follow these Steps to Get John Deere Github Account. To gain access you must request to become a member of the `github_user_access` AD security group. Request access to `github_user_access` using
ServiceNow (direct link to security request form). https://johndeere.service-now.com/ep?id=sc_cat_item_guide&sys_id=9bf898fa13f2cb000f315d622244b0b5

Next, to login to GitHub Enterprise Cloud first go to github.com and click on sign in. Next type in your
RACF followed by _deere  (e.g BNG4N4_deere). You will see an button for sign in with your identity provider. Click that button to be redirected to OKTA and finish the sign in process. If you see an error with OKTA while signing in you are most likely missing access to the required AD group `github_user_access` . Follow the process above again or contact IT support.

---

## Step 2: Get Co-pilot License
REQUEST/RENEW LICENSE at https://devportal.deere.com/license-management

---

## Step 3: Download the latest Version of Git
Install Git from Company Portal:

1. Click Windows Button/Icon then Type Company Portal
2. In the Top Search Bar, type... "Git"
3. Click "Install"

---

## Step 4: Install Visual Studio Code:

1. Click Windows Button/Icon then Type Company Portal
2. In the Top Search Bar, type... "Visual Studio Code"
3. Click "Install"

## Step 5: Sign into VSCode using your Github Account

---

## Step 6 & 7: Add Python Extension to VSCODE:

Install Python Extension and Configure Interpreter in VSCode (See Below)

1. Click the Extensions Marketplace on the left of the screen then search for Python . You
want to install the official Microsoft extension (generally the very first one). This will take
about a minute to install.
2. Press Ctrl+Shift+P and type "Python: Select Interpreter"
3. Look for your Python interpreter or create a venv 

---

## Step 8:Verify Installation

Open terminal and run:
```bash
code --version
```

---

## Step 9: Install GitHub Copilot Extensions

### Required Extensions

Open VS Code and install these extensions:

1. **GitHub Copilot** (Required)
   - Extension ID: `GitHub.copilot`
   - Provides code completions

2. **GitHub Copilot Chat** (Required)
   - Extension ID: `GitHub.copilot-chat`
   - Provides chat interface

### Installation Steps

**VS Code Marketplace**

1. Open VS Code
2. Click Extensions icon (sidebar) or press `Cmd+Shift+X`
3. Search "GitHub Copilot"
4. Click "Install" on both extensions

### Verify Copilot is Working

1. Open any code file (e.g., create `test.py`)
2. Start typing: `def hello_world():`
3. You should see Copilot suggestions (gray text)
4. Press `Tab` to accept

If you see suggestions, Copilot is working! ✅

---

## Step 10: Download Class Materials

### Get Project

Navigate to your OneDrive and Download copilot-workshop-student folder then Open Folder in VSCode

https://deere-my.sharepoint.com/:f:/g/personal/graylawrence_johndeere_com/IgDR9so2DtJNQ6dIE4gJEhk1AeCRclInwoTWzkti8E-t-wk?e=YRAFkg