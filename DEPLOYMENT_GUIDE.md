# Deployment Guide - Streamlit Cloud

## Quick Start: Get Your Calculator Live in 15 Minutes

### Prerequisites
- GitHub account (free)
- Files ready: `order_management_enhanced.py`, `requirements.txt`, `README.md`

---

## Step 1: Create GitHub Repository

1. Go to https://github.com and sign in
2. Click **"+"** (top right) → **"New repository"**
3. **Repository name**: `order-management-calculator`
4. **Description**: "CFO-grade Order Management AI business case calculator"
5. **Visibility**: Public (required for free Streamlit hosting)
6. ✅ Check **"Add a README file"**
7. Click **"Create repository"**

---

## Step 2: Upload Files

### Option A: Web Upload (Easiest)

1. In your new repository, click **"Add file"** → **"Upload files"**
2. Upload these files:
   - `order_management_enhanced.py`
   - `requirements.txt`
   - `README.md` (will replace the default)
3. Add commit message: "Initial commit - Enhanced Order Management calculator"
4. Click **"Commit changes"**

### Option B: Git Command Line

```bash
git clone https://github.com/YOUR_USERNAME/order-management-calculator.git
cd order-management-calculator

# Copy your files
cp order_management_enhanced.py .
cp requirements.txt .
cp README.md .

# Commit and push
git add .
git commit -m "Initial commit - Enhanced calculator"
git push origin main
```

---

## Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click **"Sign in"** (top right)
3. Choose **"Continue with GitHub"**
4. Authorize Streamlit to access your repositories
5. Click **"New app"**

### Configuration:

**Repository**: Select `YOUR_USERNAME/order-management-calculator`

**Branch**: `main`

**Main file path**: `order_management_enhanced.py`

**App URL (optional)**: Choose a custom subdomain like `mycompany-om-calculator`

6. Click **"Deploy!"**

---

## Step 4: Wait for Deployment

**Deployment takes 2-3 minutes**

You'll see:
1. "Preparing your app..."
2. "Installing dependencies..."
3. "Running your app..."
4. ✅ "Your app is live!"

**Your URL will be**: `https://your-app-name.streamlit.app`

---

## Step 5: Test Your Live App

Once deployed, test the following:

**Functionality Checklist:**
- [ ] Currency selector works (USD ↔ EUR)
- [ ] All three case scenarios display correctly
- [ ] Color-coded case banner shows correct color
- [ ] All sliders and inputs function
- [ ] Numbers display with commas
- [ ] All charts render properly:
  - [ ] Waterfall chart
  - [ ] 3-year projection
  - [ ] Scenario comparison
  - [ ] Sensitivity tornado
- [ ] All tables display correctly
- [ ] CSV export downloads
- [ ] Executive summary exports

**If something doesn't work:**
- Check Streamlit Cloud logs (click "Manage app" → "Logs")
- Fix the issue in your local code
- Commit and push to GitHub
- Streamlit auto-redeploys in ~1 minute

---

## Step 6: Share with Clients

**Your app is now live and public!**

Share the URL: `https://your-app-name.streamlit.app`

### Professional Sharing Tips:

**1. Email Template:**
```
Subject: Order Management AI - Interactive Business Case

Hi [Client Name],

I've prepared an interactive business case calculator for our 
Order Management AI discussion. You can:

• Adjust assumptions to match your environment
• Compare Best/Base/Worst case scenarios
• See sensitivity analysis on key variables
• Switch between USD and EUR
• Download detailed analysis

Access here: https://your-app-name.streamlit.app

Let's schedule time to walk through the results together.

Best regards,
[Your Name]
```

**2. In Presentations:**
- Screen share the live calculator during meetings
- Let clients adjust inputs in real-time
- Export summary for their internal review

**3. Proposal Documents:**
- Include QR code linking to calculator
- Reference URL in executive summary
- Use exported CSV for detailed appendix

---

## Managing Your App

### View App Status
https://share.streamlit.io/YOUR_USERNAME/order-management-calculator

### Update Your App
Just push changes to GitHub - Streamlit auto-redeploys:
```bash
git add .
git commit -m "Update: [describe changes]"
git push
```

### View Logs (for troubleshooting)
Manage app → Logs → See real-time error messages

### App Settings
- Manage app → Settings
- Secrets: Add API keys or sensitive config
- Resources: See usage stats
- Reboot: Restart if app freezes

---

## Troubleshooting

### "Module not found" error
- Check `requirements.txt` has all dependencies
- Ensure package names are spelled correctly
- Verify versions are compatible

### "App is not loading"
- Check for Python syntax errors in logs
- Verify main file name matches deployment config
- Ensure all imports are available

### "Changes not showing"
- Wait 60 seconds for auto-redeploy
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
- Check GitHub repository has latest commit

### Charts not rendering
- Verify plotly is in requirements.txt
- Check browser console for JavaScript errors
- Try different browser

---

## Advanced: Custom Domain

### Option 1: Streamlit Subdomain
Free custom subdomain like `mycompany-calculator.streamlit.app`
- Configure during deployment or in Settings

### Option 2: Your Own Domain
Requires paid Streamlit plan:
1. Purchase domain (e.g., calculator.mycompany.com)
2. Upgrade to Streamlit Teams or Enterprise
3. Configure DNS CNAME record
4. Add custom domain in Streamlit settings

---

## Security & Privacy

### Data Privacy
- Streamlit Cloud apps are public by default
- User inputs are NOT saved or logged
- No data persists between sessions
- Each user has isolated session state

### Making App Private
Requires paid Streamlit plan:
1. Upgrade to Teams or Enterprise
2. Enable authentication
3. Control access with email whitelist or SSO

### Client Data Concerns
If handling sensitive client data:
1. Run locally instead of cloud
2. Deploy to client's private cloud
3. Use Streamlit Enterprise with authentication

---

## Cost Structure

### Free Tier
✅ Perfect for client demos
- Unlimited public apps
- 1GB resources per app
- Community support
- Streamlit.app domain

### Paid Tiers (optional)
**Teams** ($28/month per editor):
- Private apps
- Custom domains
- Priority support
- More resources

**Enterprise** (custom pricing):
- SSO authentication
- Dedicated resources
- SLA guarantees
- White-label options

**For most use cases, FREE tier is sufficient.**

---

## Maintenance & Updates

### Regular Updates
Recommended schedule:
- **Monthly**: Review exchange rates, update if needed
- **Quarterly**: Validate scenario assumptions against outcomes
- **Annually**: Refresh industry benchmarks

### Version Control
Use Git tags for major releases:
```bash
git tag -a v2.0 -m "Enhanced calculator with sensitivity analysis"
git push origin v2.0
```

### Backup
Your GitHub repository IS your backup. To create local backup:
```bash
git clone https://github.com/YOUR_USERNAME/order-management-calculator.git
cd order-management-calculator
zip -r backup-$(date +%Y%m%d).zip .
```

---

## Next Steps

1. ✅ Deploy to Streamlit Cloud
2. ✅ Test all functionality
3. ✅ Customize for your first client
4. ✅ Share URL and gather feedback
5. ✅ Iterate based on client needs

**Your calculator is now a competitive differentiator.**

Use it to:
- Lead with value in sales conversations
- Qualify opportunities based on financial potential
- Support business case development in SOWs
- Enable clients to self-serve ROI modeling

---

## Support Resources

**Streamlit Documentation**: https://docs.streamlit.io
**Streamlit Community**: https://discuss.streamlit.io
**GitHub Issues**: Create issues in your repository

**Questions about this calculator?**
Refer to README.md for detailed feature documentation.

---

**You're now live! Start closing deals with CFO-grade analysis.** 🚀
