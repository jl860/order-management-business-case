# Order Management AI Business Case Calculator - Deployment Guide

## 🎯 What This Tool Does

A **CFO-grade financial modeling tool** that translates Order Management operational improvements into defendable financial returns using industry-standard formulas.

**Key Differentiators:**
- Real financial calculations (not handwavy percentages)
- Industry benchmarks built-in (APQC, Aberdeen, Gartner)
- Three-scenario analysis (Best/Base/Worst)
- Probability-weighted NPV
- Phased implementation modeling
- Auto-generated executive summary

---

## 📋 Quick Start

### Local Deployment (5 minutes)

1. **Install Python** (if needed)
   - Download from: https://www.python.org/downloads/
   - Version 3.8+ required
   - ✅ Check "Add Python to PATH" during install

2. **Put files in folder**
   ```
   order-management-calculator/
   ├── order_management_business_case.py
   └── requirements_business_case.txt
   ```

3. **Open terminal in folder**
   - Windows: Type `cmd` in folder address bar
   - Mac: Terminal → `cd path/to/folder`

4. **Install dependencies**
   ```bash
   pip install -r requirements_business_case.txt
   ```

5. **Run the app**
   ```bash
   streamlit run order_management_business_case.py
   ```

6. **Opens automatically** at http://localhost:8501

---

## ☁️ GitHub + Streamlit Cloud Deployment (15 minutes)

### Step 1: Create GitHub Repository

1. Go to https://github.com
2. Click "+" → "New repository"
3. Name: `order-management-business-case`
4. Public repository
5. Add README ✅
6. Click "Create repository"

### Step 2: Upload Files

1. Click "Add file" → "Upload files"
2. Upload:
   - `order_management_business_case.py`
   - `requirements_business_case.txt` (rename to `requirements.txt`)
3. Commit message: "Initial upload - CFO-grade business case calculator"
4. Click "Commit changes"

### Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "Sign in" → "Continue with GitHub"
3. Authorize Streamlit Cloud
4. Click "New app"
5. Fill in:
   - **Repository:** your-username/order-management-business-case
   - **Branch:** main
   - **Main file:** order_management_business_case.py
6. Click "Deploy!"

### Step 4: App Goes Live

- Deployment takes 2-3 minutes
- You'll get a permanent URL like:
  `https://your-username-order-management-business-case.streamlit.app`
- Share this URL with anyone

---

## 🔑 Key Features

### 1. Real Financial Formulas

**Working Capital Benefit:**
```
Cash Freed = (DSO_current - DSO_target) / 365 * Annual_Revenue
Annual Benefit = Cash Freed * WACC
```

**Error Reduction Benefit:**
```
Errors Eliminated = (Current_Error_Rate - Target_Error_Rate) * Order_Volume
Annual Savings = Errors_Eliminated * Rework_Cost
```

**Revenue Leakage Prevention:**
```
Revenue Protected = (Current_Leakage% - Target_Leakage%) * Annual_Revenue
Profit Impact = Revenue Protected * Profit_Margin
```

**Labor Automation:**
```
Manual Touches Eliminated = (Current_STP - Target_STP) * Order_Volume
Hours Saved = Touches * Avg_Time_Minutes / 60
Annual Savings = Hours_Saved * Hourly_Rate
FTE Reduction = Hours_Saved / 2080
```

**Cycle Time / Capacity:**
```
Cycle_Reduction% = (Current_Cycle - Target_Cycle) / Current_Cycle
Additional_Capacity = Order_Volume * Cycle_Reduction%
Revenue_Opportunity = Additional_Capacity * Avg_Order_Value * Capture_Rate
Profit_Impact = Revenue_Opportunity * Profit_Margin
```

### 2. Industry Benchmarks (Hardcoded)

| Metric | Best-in-Class | Top Quartile | Average | Bottom Quartile |
|--------|--------------|--------------|---------|-----------------|
| DSO | 24 days | 31 days | 38 days | 52 days |
| Perfect Order Rate | 97% | 93% | 85% | 68% |
| STP Rate | 95% | 89% | 78% | 58% |
| Cost/Order | $28 | $42 | $62 | $105 |
| Revenue Leakage | 1% | 3% | 6% | 12% |

*Sources: APQC, Aberdeen Group, Gartner*

### 3. Three-Scenario Analysis

**Automatically calculated:**

| Scenario | Adoption | Performance | Probability | Use Case |
|----------|----------|-------------|-------------|----------|
| Best Case | 95% | 110% of target | 20% | Everything goes right |
| Base Case | 75% | 100% of target | 50% | Realistic expectations |
| Worst Case | 50% | 80% of target | 30% | Partial success |

**Probability-Weighted NPV = (0.20 × Best) + (0.50 × Base) + (0.30 × Worst)**

### 4. Phased Implementation

**Year 0: Pilot (Months 1-3)**
- 15% adoption
- 30% of investment
- Gate decision: Proceed if accuracy >80% AND satisfaction >7/10

**Year 1: Limited Production (Months 4-9)**
- 45% adoption
- 50% of investment + change management + integration
- Refine edge cases

**Year 2: Full Production (Months 10-18)**
- 80% adoption
- 20% remaining investment
- Continuous improvement

**Year 3+: Steady State**
- Full adoption
- 3% annual benefit growth
- 2% maintenance inflation

### 5. Auto-Generated Executive Summary

**Includes:**
- Problem statement with current vs. industry comparison
- Solution description
- Financial case (NPV, ROI, payback)
- Benefit breakdown by category
- Downside protection analysis
- Implementation roadmap with gate decisions
- Recommendation with key success factors
- Next steps with timeline

**Downloadable as Markdown file** for inclusion in presentations.

---

## 📊 What You'll See in the UI

### Top Metrics (4 cards)
1. **Probability-Weighted NPV** - Risk-adjusted value
2. **Base Case ROI** - Return on investment
3. **Base Case Payback** - Time to recover investment
4. **Steady-State Annual Benefit** - Year 3+ recurring benefit

### Industry Benchmark Positioning
- Current vs. Target position for each metric
- Color-coded by quartile (Red/Yellow/Green)
- Full benchmark table showing where you stand

### Scenario Comparison Cards
- Three colored cards (Green/Yellow/Red)
- Shows NPV, ROI, Payback for each scenario
- Explains assumptions and probability

### Charts (3 total)
1. **Waterfall Chart** - Shows how each benefit component adds up
2. **Scenario Comparison** - Bar chart comparing NPV across scenarios
3. **Cash Flow Projection** - Annual bars + cumulative line

### Detailed Benefit Breakdown
- 5 benefit categories with specific calculations
- Shows exact numbers (cash freed, errors eliminated, FTE reduction)
- Transparent about assumptions

### Year-by-Year Financial Table
- Shows phase, adoption rate, investment, benefits, cash flow
- Tracks cumulative cash flow to identify payback point

### Executive Summary
- Complete board-ready brief
- Formatted for copy-paste into documents
- Downloadable as separate file

---

## 💼 How to Use This Tool

### For Internal Business Case Development

1. **Gather Current State Data**
   - Pull DSO from finance system
   - Calculate perfect order rate from quality data
   - Determine cost per order from activity-based costing
   - Measure STP rate from exception logs
   - Quantify revenue leakage from write-off reports

2. **Set Realistic Targets**
   - Use industry benchmarks as guide
   - Top quartile is achievable with AI
   - Best-in-class requires mature processes
   - Don't set targets beyond best-in-class

3. **Input Investment Costs**
   - Get quotes from 2-3 vendors for platform cost
   - Add 15-20% for change management
   - Budget $50-100K for integration
   - Maintenance typically 15-25% of initial investment

4. **Review All Three Scenarios**
   - Present base case as primary
   - Use worst case to show downside protection
   - Don't oversell best case

5. **Download Outputs**
   - Export financial data to Excel for detailed analysis
   - Include executive summary in slide deck
   - Share Streamlit link with stakeholders for exploration

### For Client Engagements

1. **Workshop Preparation**
   - Pre-populate with client's industry benchmarks
   - Use their actual cost structure
   - Bring laptop for live modeling

2. **Discovery Session**
   - Walk through current state inputs together
   - Let client see industry comparison real-time
   - Adjust targets collaboratively

3. **Financial Review**
   - Show all three scenarios upfront
   - Emphasize probability-weighted NPV
   - Highlight worst-case still positive

4. **Executive Presentation**
   - Use auto-generated summary as baseline
   - Customize recommendations section
   - Print PDF of full output

---

## 🎨 Customization Options

### Update Industry Benchmarks

Edit lines 75-103 in `order_management_business_case.py`:

```python
INDUSTRY_BENCHMARKS = {
    'dso': {
        'bottom_quartile': 52,
        'average': 38,
        'top_quartile': 31,
        'best_in_class': 24
    },
    # ... update other metrics
}
```

### Adjust Default Values

Find the input sections (lines 800+) and change `value=` parameter:

```python
current_dso = st.sidebar.number_input(
    "Current DSO (days)",
    min_value=1.0,
    value=45.0,  # ← Change this default
    step=1.0
)
```

### Modify Scenario Assumptions

Edit lines 463-469:

```python
scenario_multipliers = {
    'best': {'adoption': 0.95, 'performance': 1.10},
    'base': {'adoption': 0.75, 'performance': 1.00},  # ← Adjust these
    'worst': {'adoption': 0.50, 'performance': 0.80}
}
```

### Change Probability Weights

Edit line 973:

```python
probability_weighted_npv = (
    0.20 * best_result['npv'] +  # ← Change probabilities
    0.50 * base_result['npv'] +
    0.30 * worst_result['npv']
)
```

### Add Company Branding

Edit lines 22-60 for custom CSS:

```python
st.markdown("""
<style>
    h1 {color: #YOUR_BRAND_COLOR;}  # ← Change colors
    .stMetric {
        border-left: 4px solid #YOUR_BRAND_COLOR;
    }
</style>
""", unsafe_allow_html=True)
```

---

## 🔧 Troubleshooting

### "Module not found" error
```bash
pip install --upgrade streamlit pandas numpy plotly
```

### Port 8501 already in use
```bash
streamlit run order_management_business_case.py --server.port=8502
```

### Charts not displaying
- Clear browser cache
- Try different browser (Chrome recommended)
- Restart Streamlit app

### Calculations seem wrong
- Verify all inputs have reasonable values
- Check that current > target for metrics where lower is better
- Ensure profit margin is entered as decimal (0.15 = 15%)

### Deployment to Streamlit Cloud fails
- Ensure `requirements.txt` exists (not `requirements_business_case.txt`)
- Check that file name is exactly `order_management_business_case.py`
- Wait 5 minutes and try "Reboot app" in Streamlit dashboard

---

## 📈 Best Practices

### Data Gathering

**DO:**
- Use trailing 12-month averages for operational metrics
- Get finance approval on cost assumptions
- Validate industry benchmarks with third-party research
- Document all assumptions with sources

**DON'T:**
- Use peak period data (Q4, month-end) as baseline
- Inflate targets beyond industry best-in-class
- Mix different time periods (fiscal vs calendar year)
- Present only best case scenario

### Stakeholder Communication

**CFO/Finance:**
- Lead with probability-weighted NPV
- Show sensitivity to key assumptions
- Emphasize phased investment with gates
- Compare to alternative investments

**Operations Leadership:**
- Focus on FTE impact and redeployment strategy
- Highlight quality improvements (perfect order rate)
- Show customer satisfaction benefits
- Address change management plan

**Executive Committee:**
- Start with industry benchmark positioning
- Use three-scenario framing
- Emphasize downside protection
- Include competitive intelligence ("peers are moving")

### Model Validation

Before presenting, verify:

1. **Sanity Check Total Benefits**
   - Should be 15-30% of revenue for most Order Management improvements
   - If >30%, assumptions likely aggressive
   - If <5%, may not be worth doing

2. **Benchmark Against Similar Projects**
   - Typical payback: 1.5-3.0 years
   - Typical ROI: 150-300%
   - If wildly different, explain why

3. **Stress Test Scenarios**
   - What if adoption is only 25%?
   - What if targets take 2x longer to achieve?
   - At what point does NPV go negative?

4. **Get Finance Sign-Off**
   - CFO should approve WACC assumption
   - Controller should validate cost structure
   - FP&A should review benefit calculations

---

## 📚 Technical Details

### Calculation Methodology

**NPV Formula:**
```
NPV = Σ (CF_t / (1 + WACC)^t)
Where: CF_t = cash flow in year t
       WACC = weighted average cost of capital
```

**Benefit Ramp-Up:**
- Year 0: 15% of full benefit
- Year 1: 45% of full benefit
- Year 2: 80% of full benefit
- Year 3+: 100% of full benefit × 1.03^(year-2) growth

**Cost Structure:**
- Year 0: 30% investment + 50% change mgmt
- Year 1: 50% investment + 50% change mgmt + integration + 50% maintenance
- Year 2: 20% investment + full maintenance
- Year 3+: Maintenance with 2% annual inflation

### Data Flow

```
User Inputs
    ↓
Current State Metrics → Industry Benchmark Comparison
    ↓
Target State Metrics → Gap Analysis
    ↓
Financial Formulas → Benefit Calculations
    ↓
Scenario Adjustments → Best/Base/Worst Cases
    ↓
Probability Weighting → Risk-Adjusted NPV
    ↓
Charts + Summary → Executive Outputs
```

### File Structure

```
order_management_business_case.py
├── Imports & Configuration (lines 1-75)
├── Industry Benchmarks (lines 75-103)
├── FinancialInputs dataclass (lines 105-138)
├── Financial Calculation Functions (lines 140-422)
│   ├── calculate_working_capital_benefit()
│   ├── calculate_error_reduction_benefit()
│   ├── calculate_revenue_leakage_benefit()
│   ├── calculate_labor_automation_benefit()
│   ├── calculate_cycle_time_benefit()
│   └── calculate_cost_per_order_benefit()
├── Scenario Calculation (lines 424-609)
│   └── calculate_scenario() - builds year-by-year model
├── Benchmark Positioning (lines 611-647)
├── Visualization Functions (lines 649-795)
│   ├── create_waterfall_chart()
│   ├── create_scenario_comparison_chart()
│   └── create_cash_flow_chart()
├── Executive Summary Generator (lines 797-973)
└── Main UI (lines 975-end)
    ├── Sidebar inputs
    ├── Metric cards
    ├── Benchmark table
    ├── Scenario cards
    ├── Charts
    ├── Detail tables
    └── Downloads
```

---

## 🎯 Success Metrics

After deploying, you'll know it's working when:

✅ **CFO says:** "This is the most credible AI business case I've seen"  
✅ **You can answer:** "How did you calculate that?" for every number  
✅ **You present:** Three scenarios, not just one  
✅ **You show:** Downside protection, not just upside potential  
✅ **You compare:** Client's current state to industry benchmarks  
✅ **You defend:** Every assumption with a source or rationale  

This tool is built for **precision and credibility** over flashiness.

---

## 📞 Support

**Documentation:**
- Streamlit: https://docs.streamlit.io
- Plotly: https://plotly.com/python/
- Pandas: https://pandas.pydata.org/docs/

**Community:**
- Streamlit Forum: https://discuss.streamlit.io
- Stack Overflow: Tag with [streamlit]

**Customization Help:**
- Python functions are well-documented with docstrings
- Variable names are descriptive
- Comments explain complex calculations

---

## 🚀 Next Steps After Deployment

1. **Test with Sample Data**
   - Use the defaults to see a complete example
   - Try extreme values to verify error handling
   - Export all outputs to review formatting

2. **Customize for Your Organization**
   - Update industry benchmarks if you have proprietary research
   - Adjust default values to your typical client profile
   - Add company branding to CSS

3. **Create Client Templates**
   - Save common industry configurations
   - Document assumption sources
   - Prepare talking points for each scenario

4. **Train Your Team**
   - Walk through each calculation
   - Practice live demo with stakeholders
   - Role-play CFO objections

5. **Gather Feedback**
   - What questions does it not answer?
   - What calculations are unclear?
   - What would make it more credible?

---

**You now have a CFO-grade business case tool. Make it your signature asset.**
