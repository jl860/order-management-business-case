# GitHub Deployment Checklist

## ✅ Pre-Deployment Checklist

### Files Ready
- [ ] `order_management_business_case.py` (main application)
- [ ] `requirements.txt` (rename from `requirements_business_case.txt`)
- [ ] `README.md` (rename from `README_BUSINESS_CASE.md`)
- [ ] `DEPLOYMENT_GUIDE.md` (rename from `DEPLOYMENT_GUIDE_BUSINESS_CASE.md`)
- [ ] `WHAT_CHANGED.md` (optional, documents evolution)

### Content Review
- [ ] Update repository URL in README.md (line 6)
- [ ] Add screenshot/demo GIF to README.md (optional)
- [ ] Review default values in calculator match your typical use case
- [ ] Verify industry benchmarks are current (lines 75-103 in .py file)

---

## 🚀 GitHub Deployment Steps

### Step 1: Create Repository

1. Go to https://github.com
2. Click "+" in top right → "New repository"
3. **Repository name:** `order-management-business-case`
4. **Description:** "CFO-grade financial modeling tool for Order Management AI investments"
5. **Public repository** (required for free Streamlit hosting)
6. ✅ Check "Add a README file" (we'll replace it)
7. Click "Create repository"

**Result:** You're now on your repository page

---

### Step 2: Upload Files

#### Option A: Web Upload (Easiest)

1. Click "Add file" → "Upload files"

2. Upload these files:
   - `order_management_business_case.py` (keep name)
   - `requirements_business_case.txt` → **Rename to `requirements.txt`**
   - `README_BUSINESS_CASE.md` → **Rename to `README.md`** (replaces default)
   - `DEPLOYMENT_GUIDE_BUSINESS_CASE.md` → **Rename to `DEPLOYMENT_GUIDE.md`**
   - `WHAT_CHANGED.md` (optional)

3. Scroll down to "Commit changes"
4. Commit message: "Initial commit - CFO-grade Order Management calculator"
5. Click "Commit changes"

**Wait 10 seconds for upload to complete**

#### Option B: Git Command Line (Advanced)

```bash
# Clone your empty repository
git clone https://github.com/YOUR_USERNAME/order-management-business-case.git
cd order-management-business-case

# Copy files (adjust paths as needed)
cp /path/to/order_management_business_case.py .
cp /path/to/requirements_business_case.txt requirements.txt
cp /path/to/README_BUSINESS_CASE.md README.md
cp /path/to/DEPLOYMENT_GUIDE_BUSINESS_CASE.md DEPLOYMENT_GUIDE.md
cp /path/to/WHAT_CHANGED.md .

# Commit and push
git add .
git commit -m "Initial commit - CFO-grade Order Management calculator"
git push origin main
```

---

### Step 3: Verify Upload

On your GitHub repository page, you should see:

```
order-management-business-case/
├── order_management_business_case.py
├── requirements.txt
├── README.md
├── DEPLOYMENT_GUIDE.md
└── WHAT_CHANGED.md
```

**If files are missing:** Repeat Step 2

**If filenames are wrong:** Click on file → Click pencil icon (Edit) → Rename

---

### Step 4: Test Locally (Optional but Recommended)

Before deploying to cloud, test locally:

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/order-management-business-case.git
cd order-management-business-case

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run order_management_business_case.py
```

**Open browser to http://localhost:8501**

**Test checklist:**
- [ ] App loads without errors
- [ ] Can adjust all sliders
- [ ] Charts display properly
- [ ] Can download CSV
- [ ] Can download Executive Summary
- [ ] Scenario cards show Best/Base/Worst
- [ ] Industry benchmark table displays

**If any issues:** Fix the code, commit, push to GitHub

```bash
git add .
git commit -m "Fix: [describe what you fixed]"
git push
```

---

## ☁️ Streamlit Cloud Deployment

### Step 5: Connect to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "Sign in" (top right)
3. Click "Continue with GitHub"
4. Click "Authorize streamlit"

**You're now on the Streamlit Cloud dashboard**

---

### Step 6: Deploy App

1. Click "New app" (big button in center)

2. Fill in the deployment form:

   **Repository:**
   - Click dropdown
   - Select: `YOUR_USERNAME/order-management-business-case`
   - If you don't see it, click "Reload repositories"

   **Branch:**
   - Leave as: `main`

   **Main file path:**
   - Type: `order_management_business_case.py`
   - Make sure this is exact (case-sensitive)

3. **Advanced settings** (click to expand):
   - Python version: 3.11 (recommended)
   - Leave other settings as default

4. Click "Deploy!" button

---

### Step 7: Wait for Deployment

**What you'll see:**

```
🍳 Your app is in the oven!
   Installing Python dependencies...
   ✅ streamlit
   ✅ pandas
   ✅ numpy
   ✅ plotly
   Starting application...
```

**Timeline:**
- First deployment: 2-4 minutes
- Subsequent deployments: 30-60 seconds

**Do not close the browser window during deployment**

---

### Step 8: App is Live! 🎉

**When deployment completes, you'll see:**

```
✅ Your app is live!
   https://YOUR_USERNAME-order-management-business-case-abc123.streamlit.app
```

**Copy this URL** - this is your permanent link

---

### Step 9: Test Deployed App

1. Click on the URL to open your app
2. Run through test checklist again:
   - [ ] App loads (no errors)
   - [ ] Sidebar inputs work
   - [ ] All charts display
   - [ ] Downloads work
   - [ ] Try on mobile device

**Common first-deploy issues:**

| Problem | Solution |
|---------|----------|
| "Module not found" | Check requirements.txt exists and has all packages |
| "File not found" | Main file path must be exact: `order_management_business_case.py` |
| App crashes immediately | Check Python version (3.11 recommended) |
| Charts don't display | Usually fixes itself after page refresh |

**If errors persist:**
- Click "Manage app" → "Reboot app"
- Check logs for specific error messages
- Verify files uploaded correctly on GitHub

---

## 🎯 Post-Deployment Steps

### Step 10: Update README with Live Link

1. Go to your GitHub repository
2. Click on `README.md`
3. Click pencil icon (Edit)
4. Find line 6: `[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url-here.streamlit.app)`
5. Replace `https://your-app-url-here.streamlit.app` with your actual URL
6. Scroll down, click "Commit changes"

**Now your README has a live demo button** ✨

---

### Step 11: Share Your App

**Your permanent URL format:**
```
https://YOUR_USERNAME-order-management-business-case-RANDOM_ID.streamlit.app
```

**Share with:**
- ✉️ Email to colleagues
- 💼 Include in LinkedIn posts
- 📊 Add to presentation slides
- 🔗 Paste in Slack/Teams
- 📱 Works on any device (mobile-friendly)

**No login required for viewers** - anyone with the link can access it

---

### Step 12: Enable Analytics (Optional)

In Streamlit Cloud:

1. Click "Manage app"
2. Go to "Analytics" tab
3. See:
   - Number of visits
   - Active users
   - Most used features

**Use this to:**
- Track adoption
- Identify popular features
- Justify future enhancements

---

## 🔄 Making Updates

### After Initial Deployment

**To update the app:**

1. **Edit on GitHub directly:**
   - Go to repository
   - Click on file to edit
   - Click pencil icon
   - Make changes
   - Commit changes
   
   **OR**

2. **Edit locally and push:**
   ```bash
   # Make your changes to files
   git add .
   git commit -m "Update: [what you changed]"
   git push
   ```

**Streamlit Cloud auto-detects changes and redeploys** (takes ~1 minute)

**No need to manually redeploy** ✨

---

## 📋 Common Customizations After Deployment

### Update Default Values

**Most common request:** "Can we change the defaults to match our typical client?"

**To update:**

1. Open `order_management_business_case.py` on GitHub
2. Click pencil icon (Edit)
3. Find the input section (search for "st.sidebar.number_input")
4. Change `value=` parameters

Example:
```python
# Change DSO default from 45 to 38
current_dso = st.sidebar.number_input(
    "Current DSO (days)",
    min_value=1.0,
    value=38.0,  # ← Changed from 45.0
    step=1.0
)
```

5. Commit changes
6. App auto-redeploys with new defaults

---

### Add Company Branding

**To add your logo and colors:**

1. Edit lines 22-60 (CSS section)
2. Change colors:
   ```python
   h1 {color: #YOUR_BRAND_COLOR;}
   .stMetric {border-left: 4px solid #YOUR_BRAND_COLOR;}
   ```

3. To add logo, add before `st.title()`:
   ```python
   col1, col2, col3 = st.columns([1, 2, 1])
   with col2:
       st.image("https://your-logo-url.com/logo.png", width=300)
   ```

---

### Update Industry Benchmarks

**If you have proprietary research:**

1. Edit lines 75-103
2. Update the `INDUSTRY_BENCHMARKS` dictionary
3. Add source citation in footer

---

## 🐛 Troubleshooting

### App Won't Deploy

**"Module not found" error:**
```bash
# Solution: Check requirements.txt has all packages
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
```

**"File not found" error:**
- Main file path must be exact: `order_management_business_case.py`
- Case-sensitive!
- Check file exists on GitHub

---

### App Crashes After Deployment

1. Click "Manage app" → "Logs"
2. Look for error message
3. Common causes:
   - Missing package in requirements.txt
   - Typo in Python code
   - Incorrect file reference

**To fix:**
1. Make changes on GitHub
2. Commit
3. Wait for auto-redeploy (1 minute)

---

### Charts Not Displaying

**Usually fixes itself:**
1. Refresh the page
2. Try different browser
3. Clear cache

**If persists:**
- Check Plotly version in requirements.txt: `plotly>=5.17.0`
- Reboot app in Streamlit dashboard

---

### Slow Performance

**If app is sluggish:**

**Causes:**
- Too many users at once (free tier limit)
- Large dataset calculations
- Complex charts

**Solutions:**
1. Upgrade to Streamlit paid tier ($20/month)
2. Cache calculations with `@st.cache_data`
3. Optimize chart rendering

---

## 📊 Success Metrics

**You'll know deployment succeeded when:**

✅ App loads without errors  
✅ All inputs adjust smoothly  
✅ Charts render properly  
✅ Downloads work  
✅ Works on mobile  
✅ URL is shareable  
✅ No login required for viewers  
✅ Auto-updates when you push to GitHub  

---

## 🎓 Learning Resources

**Streamlit Documentation:**
- Docs: https://docs.streamlit.io
- Gallery: https://streamlit.io/gallery
- Forum: https://discuss.streamlit.io

**GitHub Help:**
- Basics: https://docs.github.com/en/get-started/quickstart
- Uploading files: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

**Troubleshooting:**
- Streamlit community forum (very responsive)
- GitHub Discussions on your repository
- Stack Overflow (tag: [streamlit])

---

## 🎯 Final Checklist

Before sharing with stakeholders:

- [ ] App deployed and accessible
- [ ] Tested on desktop browser
- [ ] Tested on mobile device
- [ ] All charts display correctly
- [ ] Download buttons work
- [ ] Executive summary generates properly
- [ ] Default values make sense
- [ ] README updated with live link
- [ ] Shared URL with at least one colleague for feedback

---

## 🚀 You're Ready!

**Your CFO-grade calculator is live and ready for serious business cases.**

**Next steps:**
1. Share the URL with your team
2. Gather feedback on default values
3. Customize for your most common use case
4. Use it in your next client engagement

**When you close your first deal using this tool, that's the best payment.**

---

**Questions?** Create a GitHub issue on your repository or reach out for support.

**Good luck crushing those CFO meetings!** 💼📊💰
