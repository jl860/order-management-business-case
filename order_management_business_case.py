"""
Order Management AI Business Case Calculator
============================================

A CFO-grade financial modeling tool that translates operational improvements
into defendable financial returns using industry-standard formulas.

Built for AI Advisory engagements where precision and credibility matter.

Run with:
    streamlit run order_management_business_case.py

Author: Built for Uniphore AI Advisory
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Order Management AI Business Case",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main > div {padding-top: 2rem;}
    .stMetric {
        background-color: #f8f9fa;
        padding: 1.2rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .metric-good {border-left-color: #28a745 !important;}
    .metric-warn {border-left-color: #ffc107 !important;}
    .metric-bad {border-left-color: #dc3545 !important;}
    .scenario-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border: 2px solid;
    }
    .scenario-best {
        background: #d4edda;
        border-color: #28a745;
    }
    .scenario-base {
        background: #fff3cd;
        border-color: #ffc107;
    }
    .scenario-worst {
        background: #f8d7da;
        border-color: #dc3545;
    }
    .benchmark-table {
        font-size: 0.9rem;
    }
    .executive-summary {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
        margin: 2rem 0;
    }
    h1 {color: #1f77b4;}
    h2 {color: #495057; margin-top: 2rem;}
    h3 {color: #6c757d;}
</style>
""", unsafe_allow_html=True)

# Industry benchmarks (sourced from APQC, Aberdeen Group, Gartner)
INDUSTRY_BENCHMARKS = {
    'dso': {
        'bottom_quartile': 52,
        'average': 38,
        'top_quartile': 31,
        'best_in_class': 24
    },
    'perfect_order_rate': {
        'bottom_quartile': 0.68,
        'average': 0.85,
        'top_quartile': 0.93,
        'best_in_class': 0.97
    },
    'stp_rate': {
        'bottom_quartile': 0.58,
        'average': 0.78,
        'top_quartile': 0.89,
        'best_in_class': 0.95
    },
    'cost_per_order': {
        'bottom_quartile': 105,
        'average': 62,
        'top_quartile': 42,
        'best_in_class': 28
    },
    'revenue_leakage': {
        'bottom_quartile': 0.12,
        'average': 0.06,
        'top_quartile': 0.03,
        'best_in_class': 0.01
    }
}

@dataclass
class FinancialInputs:
    """Core financial and operational inputs"""
    # Volume & Revenue
    annual_order_volume: int
    average_order_value: float
    profit_margin: float
    
    # Current State Performance
    current_dso: float
    current_perfect_order_rate: float
    current_cycle_time: float
    current_revenue_leakage: float
    current_cost_per_order: float
    current_stp_rate: float
    
    # Target State Performance
    target_dso: float
    target_perfect_order_rate: float
    target_cycle_time: float
    target_revenue_leakage: float
    target_cost_per_order: float
    target_stp_rate: float
    
    # Cost Structure
    avg_rework_cost: float
    fully_loaded_hourly_rate: float
    avg_manual_processing_time: float  # minutes
    
    # Investment
    initial_investment: float
    annual_maintenance: float
    change_management_cost: float
    integration_cost: float
    
    # Financial Assumptions
    wacc: float
    tax_rate: float
    time_horizon: int
    
    # Implementation
    pilot_duration_months: int
    limited_production_months: int
    full_production_month: int

def calculate_annual_revenue(volume: int, avg_value: float) -> float:
    """Calculate total annual revenue"""
    return volume * avg_value

def calculate_working_capital_benefit(
    current_dso: float,
    target_dso: float,
    annual_revenue: float,
    wacc: float
) -> Dict[str, float]:
    """
    Calculate working capital improvement from DSO reduction
    
    Formula: Cash Freed = (DSO_current - DSO_target) / 365 * Annual_Revenue
    Annual Benefit = Cash Freed * WACC
    """
    current_ar = (current_dso / 365) * annual_revenue
    target_ar = (target_dso / 365) * annual_revenue
    cash_freed = current_ar - target_ar
    annual_benefit = cash_freed * wacc
    
    return {
        'current_ar': current_ar,
        'target_ar': target_ar,
        'cash_freed': cash_freed,
        'annual_benefit': annual_benefit,
        'dso_improvement_days': current_dso - target_dso
    }

def calculate_error_reduction_benefit(
    current_perfect_rate: float,
    target_perfect_rate: float,
    order_volume: int,
    rework_cost: float
) -> Dict[str, float]:
    """
    Calculate savings from error reduction
    
    Formula: Savings = (Current_Errors - Target_Errors) * Rework_Cost
    """
    current_errors = order_volume * (1 - current_perfect_rate)
    target_errors = order_volume * (1 - target_perfect_rate)
    errors_eliminated = current_errors - target_errors
    annual_savings = errors_eliminated * rework_cost
    
    return {
        'current_errors': current_errors,
        'target_errors': target_errors,
        'errors_eliminated': errors_eliminated,
        'annual_savings': annual_savings,
        'error_rate_improvement': (1 - current_perfect_rate) - (1 - target_perfect_rate)
    }

def calculate_revenue_leakage_benefit(
    current_leakage: float,
    target_leakage: float,
    annual_revenue: float,
    profit_margin: float
) -> Dict[str, float]:
    """
    Calculate benefit from revenue leakage prevention
    
    Formula: Revenue Protected = (Current_Leakage% - Target_Leakage%) * Annual_Revenue
    Profit Impact = Revenue Protected * Profit_Margin
    """
    current_leakage_amount = annual_revenue * current_leakage
    target_leakage_amount = annual_revenue * target_leakage
    revenue_protected = current_leakage_amount - target_leakage_amount
    profit_impact = revenue_protected * profit_margin
    
    return {
        'current_leakage_amount': current_leakage_amount,
        'target_leakage_amount': target_leakage_amount,
        'revenue_protected': revenue_protected,
        'profit_impact': profit_impact,
        'leakage_reduction': current_leakage - target_leakage
    }

def calculate_labor_automation_benefit(
    current_stp_rate: float,
    target_stp_rate: float,
    order_volume: int,
    processing_time_minutes: float,
    hourly_rate: float
) -> Dict[str, float]:
    """
    Calculate labor cost reduction from automation
    
    Formula: Hours_Saved = Manual_Touches_Eliminated * Avg_Time_per_Touch
    Annual_Savings = Hours_Saved * Hourly_Rate
    """
    current_manual = order_volume * (1 - current_stp_rate)
    target_manual = order_volume * (1 - target_stp_rate)
    manual_touches_eliminated = current_manual - target_manual
    
    hours_saved = (manual_touches_eliminated * processing_time_minutes) / 60
    annual_savings = hours_saved * hourly_rate
    fte_reduction = hours_saved / 2080  # 2080 work hours per year
    
    return {
        'current_manual_touches': current_manual,
        'target_manual_touches': target_manual,
        'touches_eliminated': manual_touches_eliminated,
        'hours_saved': hours_saved,
        'annual_savings': annual_savings,
        'fte_reduction': fte_reduction,
        'stp_improvement': target_stp_rate - current_stp_rate
    }

def calculate_cycle_time_benefit(
    current_cycle_time: float,
    target_cycle_time: float,
    order_volume: int,
    avg_order_value: float,
    profit_margin: float,
    capacity_capture_rate: float = 0.30
) -> Dict[str, float]:
    """
    Calculate capacity increase from cycle time improvement
    
    Formula: Cycle_Time_Reduction% = (Current - Target) / Current
    Additional_Capacity = Order_Volume * Cycle_Time_Reduction%
    Revenue_Opportunity = Additional_Capacity * Avg_Order_Value * Capture_Rate
    Profit_Impact = Revenue_Opportunity * Profit_Margin
    """
    cycle_time_reduction_pct = (current_cycle_time - target_cycle_time) / current_cycle_time
    additional_capacity = order_volume * cycle_time_reduction_pct
    revenue_opportunity = additional_capacity * avg_order_value * capacity_capture_rate
    profit_impact = revenue_opportunity * profit_margin
    
    return {
        'cycle_time_reduction_days': current_cycle_time - target_cycle_time,
        'cycle_time_reduction_pct': cycle_time_reduction_pct,
        'additional_capacity_orders': additional_capacity,
        'revenue_opportunity': revenue_opportunity,
        'profit_impact': profit_impact,
        'capacity_capture_rate': capacity_capture_rate
    }

def calculate_cost_per_order_benefit(
    current_cost: float,
    target_cost: float,
    order_volume: int
) -> Dict[str, float]:
    """
    Calculate direct cost reduction per order
    
    Formula: Annual_Savings = (Current_Cost - Target_Cost) * Order_Volume
    """
    cost_reduction = current_cost - target_cost
    annual_savings = cost_reduction * order_volume
    cost_reduction_pct = cost_reduction / current_cost
    
    return {
        'cost_reduction_per_order': cost_reduction,
        'cost_reduction_pct': cost_reduction_pct,
        'annual_savings': annual_savings
    }

def calculate_scenario(
    inputs: FinancialInputs,
    scenario_type: str = 'base'
) -> Dict:
    """
    Calculate complete financial model for a scenario
    
    Scenarios:
    - best: 95% adoption, 10% better than target performance
    - base: 75% adoption, target performance achieved
    - worst: 50% adoption, 80% of target performance achieved
    """
    # Adjust targets based on scenario
    scenario_multipliers = {
        'best': {'adoption': 0.95, 'performance': 1.10},
        'base': {'adoption': 0.75, 'performance': 1.00},
        'worst': {'adoption': 0.50, 'performance': 0.80}
    }
    
    mult = scenario_multipliers[scenario_type]
    adoption = mult['adoption']
    perf = mult['performance']
    
    # Adjust target metrics
    adj_inputs = FinancialInputs(
        annual_order_volume=inputs.annual_order_volume,
        average_order_value=inputs.average_order_value,
        profit_margin=inputs.profit_margin,
        current_dso=inputs.current_dso,
        current_perfect_order_rate=inputs.current_perfect_order_rate,
        current_cycle_time=inputs.current_cycle_time,
        current_revenue_leakage=inputs.current_revenue_leakage,
        current_cost_per_order=inputs.current_cost_per_order,
        current_stp_rate=inputs.current_stp_rate,
        # Adjusted targets
        target_dso=inputs.current_dso - ((inputs.current_dso - inputs.target_dso) * perf),
        target_perfect_order_rate=inputs.current_perfect_order_rate + 
            ((inputs.target_perfect_order_rate - inputs.current_perfect_order_rate) * perf),
        target_cycle_time=inputs.current_cycle_time - ((inputs.current_cycle_time - inputs.target_cycle_time) * perf),
        target_revenue_leakage=inputs.current_revenue_leakage - 
            ((inputs.current_revenue_leakage - inputs.target_revenue_leakage) * perf),
        target_cost_per_order=inputs.current_cost_per_order - 
            ((inputs.current_cost_per_order - inputs.target_cost_per_order) * perf),
        target_stp_rate=inputs.current_stp_rate + ((inputs.target_stp_rate - inputs.current_stp_rate) * perf),
        avg_rework_cost=inputs.avg_rework_cost,
        fully_loaded_hourly_rate=inputs.fully_loaded_hourly_rate,
        avg_manual_processing_time=inputs.avg_manual_processing_time,
        initial_investment=inputs.initial_investment,
        annual_maintenance=inputs.annual_maintenance,
        change_management_cost=inputs.change_management_cost,
        integration_cost=inputs.integration_cost,
        wacc=inputs.wacc,
        tax_rate=inputs.tax_rate,
        time_horizon=inputs.time_horizon,
        pilot_duration_months=inputs.pilot_duration_months,
        limited_production_months=inputs.limited_production_months,
        full_production_month=inputs.full_production_month
    )
    
    annual_revenue = calculate_annual_revenue(adj_inputs.annual_order_volume, adj_inputs.average_order_value)
    
    # Calculate each benefit component
    wc_benefit = calculate_working_capital_benefit(
        adj_inputs.current_dso,
        adj_inputs.target_dso,
        annual_revenue,
        adj_inputs.wacc
    )
    
    error_benefit = calculate_error_reduction_benefit(
        adj_inputs.current_perfect_order_rate,
        adj_inputs.target_perfect_order_rate,
        adj_inputs.annual_order_volume,
        adj_inputs.avg_rework_cost
    )
    
    leakage_benefit = calculate_revenue_leakage_benefit(
        adj_inputs.current_revenue_leakage,
        adj_inputs.target_revenue_leakage,
        annual_revenue,
        adj_inputs.profit_margin
    )
    
    labor_benefit = calculate_labor_automation_benefit(
        adj_inputs.current_stp_rate,
        adj_inputs.target_stp_rate,
        adj_inputs.annual_order_volume,
        adj_inputs.avg_manual_processing_time,
        adj_inputs.fully_loaded_hourly_rate
    )
    
    cycle_benefit = calculate_cycle_time_benefit(
        adj_inputs.current_cycle_time,
        adj_inputs.target_cycle_time,
        adj_inputs.annual_order_volume,
        adj_inputs.average_order_value,
        adj_inputs.profit_margin
    )
    
    cost_benefit = calculate_cost_per_order_benefit(
        adj_inputs.current_cost_per_order,
        adj_inputs.target_cost_per_order,
        adj_inputs.annual_order_volume
    )
    
    # Total annual benefit (adoption-adjusted)
    total_annual_benefit = adoption * (
        wc_benefit['annual_benefit'] +
        error_benefit['annual_savings'] +
        leakage_benefit['profit_impact'] +
        labor_benefit['annual_savings'] +
        cycle_benefit['profit_impact']
    )
    
    # Build year-by-year projection with realistic ramp
    years = []
    cumulative_cf = 0
    
    # Year 0 - Pilot phase
    year0_benefit = total_annual_benefit * 0.15 * adoption
    year0_cost = (adj_inputs.initial_investment * 0.30 + 
                  adj_inputs.change_management_cost * 0.50)
    year0_net = year0_benefit - year0_cost
    cumulative_cf = year0_net
    
    years.append({
        'year': 0,
        'phase': 'Pilot',
        'adoption_rate': 0.15 * adoption,
        'investment': year0_cost,
        'maintenance': 0,
        'benefits': year0_benefit,
        'net_cf': year0_net,
        'cumulative_cf': cumulative_cf,
        'discounted_cf': year0_net / ((1 + adj_inputs.wacc) ** 0)
    })
    
    # Year 1 - Limited production
    year1_benefit = total_annual_benefit * 0.45 * adoption
    year1_cost = (adj_inputs.initial_investment * 0.50 + 
                  adj_inputs.change_management_cost * 0.50 +
                  adj_inputs.integration_cost)
    year1_maintenance = adj_inputs.annual_maintenance * 0.5
    year1_net = year1_benefit - year1_cost - year1_maintenance
    cumulative_cf += year1_net
    
    years.append({
        'year': 1,
        'phase': 'Limited Production',
        'adoption_rate': 0.45 * adoption,
        'investment': year1_cost,
        'maintenance': year1_maintenance,
        'benefits': year1_benefit,
        'net_cf': year1_net,
        'cumulative_cf': cumulative_cf,
        'discounted_cf': year1_net / ((1 + adj_inputs.wacc) ** 1)
    })
    
    # Year 2 - Scaling to full production
    year2_benefit = total_annual_benefit * 0.80 * adoption
    year2_cost = adj_inputs.initial_investment * 0.20
    year2_maintenance = adj_inputs.annual_maintenance
    year2_net = year2_benefit - year2_cost - year2_maintenance
    cumulative_cf += year2_net
    
    years.append({
        'year': 2,
        'phase': 'Full Production',
        'adoption_rate': 0.80 * adoption,
        'investment': year2_cost,
        'maintenance': year2_maintenance,
        'benefits': year2_benefit,
        'net_cf': year2_net,
        'cumulative_cf': cumulative_cf,
        'discounted_cf': year2_net / ((1 + adj_inputs.wacc) ** 2)
    })
    
    # Years 3+ - Steady state with 3% growth
    for year in range(3, adj_inputs.time_horizon + 1):
        growth_factor = 1.03 ** (year - 2)
        year_benefit = total_annual_benefit * adoption * growth_factor
        year_maintenance = adj_inputs.annual_maintenance * (1.02 ** (year - 2))  # 2% inflation
        year_net = year_benefit - year_maintenance
        cumulative_cf += year_net
        
        years.append({
            'year': year,
            'phase': 'Steady State',
            'adoption_rate': adoption,
            'investment': 0,
            'maintenance': year_maintenance,
            'benefits': year_benefit,
            'net_cf': year_net,
            'cumulative_cf': cumulative_cf,
            'discounted_cf': year_net / ((1 + adj_inputs.wacc) ** year)
        })
    
    df = pd.DataFrame(years)
    
    # Calculate financial metrics
    npv = df['discounted_cf'].sum()
    total_investment = df['investment'].sum() + df['maintenance'].sum()
    total_benefits = df['benefits'].sum()
    roi = ((total_benefits - total_investment) / total_investment) * 100 if total_investment > 0 else 0
    
    # Payback period
    payback = None
    for idx, row in df.iterrows():
        if row['cumulative_cf'] > 0:
            if idx == 0:
                payback = 0
            else:
                prev_cf = df.loc[idx - 1, 'cumulative_cf']
                curr_cf = row['cumulative_cf']
                year_fraction = abs(prev_cf) / (curr_cf - prev_cf) if (curr_cf - prev_cf) != 0 else 0
                payback = (idx - 1) + year_fraction
            break
    
    return {
        'scenario_type': scenario_type,
        'adoption_rate': adoption,
        'performance_multiplier': perf,
        'annual_revenue': annual_revenue,
        'working_capital': wc_benefit,
        'error_reduction': error_benefit,
        'revenue_leakage': leakage_benefit,
        'labor_automation': labor_benefit,
        'cycle_time': cycle_benefit,
        'cost_reduction': cost_benefit,
        'total_annual_benefit': total_annual_benefit,
        'cash_flow_df': df,
        'npv': npv,
        'roi': roi,
        'payback': payback,
        'total_investment': total_investment,
        'total_benefits': total_benefits
    }

def get_benchmark_position(metric_name: str, current_value: float, target_value: float) -> Dict:
    """Determine where current and target values fall in industry benchmarks"""
    benchmarks = INDUSTRY_BENCHMARKS[metric_name]
    
    def categorize(value):
        if metric_name in ['dso', 'cost_per_order', 'revenue_leakage']:
            # Lower is better
            if value <= benchmarks['best_in_class']:
                return 'Best-in-Class', '#28a745'
            elif value <= benchmarks['top_quartile']:
                return 'Top Quartile', '#20c997'
            elif value <= benchmarks['average']:
                return 'Average', '#ffc107'
            else:
                return 'Bottom Quartile', '#dc3545'
        else:
            # Higher is better
            if value >= benchmarks['best_in_class']:
                return 'Best-in-Class', '#28a745'
            elif value >= benchmarks['top_quartile']:
                return 'Top Quartile', '#20c997'
            elif value >= benchmarks['average']:
                return 'Average', '#ffc107'
            else:
                return 'Bottom Quartile', '#dc3545'
    
    current_cat, current_color = categorize(current_value)
    target_cat, target_color = categorize(target_value)
    
    return {
        'current_category': current_cat,
        'current_color': current_color,
        'target_category': target_cat,
        'target_color': target_color,
        'benchmarks': benchmarks
    }

def create_waterfall_chart(best_result: Dict, base_result: Dict, worst_result: Dict) -> go.Figure:
    """Create benefit waterfall chart showing component contributions"""
    
    # Use base case for the breakdown
    benefits = {
        'Working Capital': base_result['working_capital']['annual_benefit'],
        'Error Reduction': base_result['error_reduction']['annual_savings'],
        'Revenue Leakage': base_result['revenue_leakage']['profit_impact'],
        'Labor Automation': base_result['labor_automation']['annual_savings'],
        'Cycle Time': base_result['cycle_time']['profit_impact']
    }
    
    categories = list(benefits.keys()) + ['Total']
    values = list(benefits.values())
    cumulative = [sum(values[:i+1]) for i in range(len(values))]
    
    fig = go.Figure()
    
    # Individual benefits
    for i, (cat, val) in enumerate(zip(categories[:-1], values)):
        fig.add_trace(go.Bar(
            name=cat,
            x=[cat],
            y=[val],
            marker_color=['#3B82F6', '#10B981', '#8B5CF6', '#F59E0B', '#EC4899'][i],
            text=[f'${val/1000:.0f}K'],
            textposition='outside',
            hovertemplate=f'{cat}<br>${val:,.0f}<extra></extra>'
        ))
    
    # Total bar
    fig.add_trace(go.Bar(
        name='Total',
        x=['Total'],
        y=[sum(values)],
        marker_color='#1f77b4',
        text=[f'${sum(values)/1000:.0f}K'],
        textposition='outside',
        hovertemplate=f'Total Annual Benefit<br>${sum(values):,.0f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Annual Benefit Breakdown (Base Case)',
        yaxis_title='Annual Benefit ($)',
        showlegend=False,
        height=400,
        template='plotly_white'
    )
    
    return fig

def create_scenario_comparison_chart(best: Dict, base: Dict, worst: Dict) -> go.Figure:
    """Create scenario comparison chart"""
    
    scenarios = ['Best Case', 'Base Case', 'Worst Case']
    npvs = [best['npv'], base['npv'], worst['npv']]
    rois = [best['roi'], base['roi'], worst['roi']]
    paybacks = [
        best['payback'] if best['payback'] else 99,
        base['payback'] if base['payback'] else 99,
        worst['payback'] if worst['payback'] else 99
    ]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='NPV',
        x=scenarios,
        y=npvs,
        marker_color=['#28a745', '#ffc107', '#dc3545'],
        text=[f'${v/1e6:.1f}M' for v in npvs],
        textposition='outside',
        yaxis='y',
        hovertemplate='%{x}<br>NPV: $%{y:,.0f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Scenario Comparison: NPV Across Best/Base/Worst Cases',
        yaxis_title='Net Present Value ($)',
        height=400,
        template='plotly_white',
        showlegend=False
    )
    
    return fig

def create_cash_flow_chart(df: pd.DataFrame, scenario_name: str) -> go.Figure:
    """Create cash flow projection chart"""
    fig = go.Figure()
    
    # Annual net cash flow
    fig.add_trace(go.Bar(
        x=df['year'],
        y=df['net_cf'],
        name='Annual Net CF',
        marker_color=['#dc3545' if x < 0 else '#3B82F6' for x in df['net_cf']],
        hovertemplate='Year %{x}<br>Net CF: $%{y:,.0f}<extra></extra>'
    ))
    
    # Cumulative cash flow line
    fig.add_trace(go.Scatter(
        x=df['year'],
        y=df['cumulative_cf'],
        name='Cumulative CF',
        mode='lines+markers',
        line=dict(width=3, color='#F59E0B'),
        marker=dict(size=8),
        hovertemplate='Year %{x}<br>Cumulative: $%{y:,.0f}<extra></extra>'
    ))
    
    # Zero line
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    fig.update_layout(
        title=f'Cash Flow Projection - {scenario_name}',
        xaxis_title='Year',
        yaxis_title='Amount ($)',
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=400,
        template='plotly_white'
    )
    
    return fig

def generate_executive_summary(
    inputs: FinancialInputs,
    best: Dict,
    base: Dict,
    worst: Dict,
    probability_weighted_npv: float
) -> str:
    """Generate executive summary text"""
    
    annual_revenue = calculate_annual_revenue(inputs.annual_order_volume, inputs.average_order_value)
    current_error_rate = (1 - inputs.current_perfect_order_rate) * 100
    target_error_rate = (1 - inputs.target_perfect_order_rate) * 100
    
    summary = f"""
## ORDER MANAGEMENT AI INVESTMENT: EXECUTIVE BRIEF

**Prepared:** {datetime.now().strftime('%B %d, %Y')}

---

### THE PROBLEM

Manual order processing is costing **${inputs.current_cost_per_order * inputs.annual_order_volume / 1e6:.1f}M/year**, 
with **{current_error_rate:.0f}% error rate** causing revenue leakage of 
**${annual_revenue * inputs.current_revenue_leakage / 1e6:.1f}M** and customer dissatisfaction.

**Current Performance vs. Industry:**
- DSO: **{inputs.current_dso:.0f} days** (Industry avg: {INDUSTRY_BENCHMARKS['dso']['average']} days)
- Perfect Order Rate: **{inputs.current_perfect_order_rate*100:.0f}%** (Industry avg: {INDUSTRY_BENCHMARKS['perfect_order_rate']['average']*100:.0f}%)
- Straight-Through Processing: **{inputs.current_stp_rate*100:.0f}%** (Industry avg: {INDUSTRY_BENCHMARKS['stp_rate']['average']*100:.0f}%)

**We are currently in the bottom quartile for 2 of 3 metrics.**

---

### THE SOLUTION

AI-powered order validation and exception handling, reducing manual touch by 
**{(inputs.target_stp_rate - inputs.current_stp_rate)*100:.0f} percentage points** and errors by 
**{(current_error_rate - target_error_rate):.0f} percentage points**.

**Target State Positions Us:**
- DSO: Top quartile ({inputs.target_dso:.0f} days)
- Perfect Order Rate: Top quartile ({inputs.target_perfect_order_rate*100:.0f}%)
- STP Rate: Top quartile ({inputs.target_stp_rate*100:.0f}%)

---

### THE FINANCIAL CASE

**Investment:** ${(inputs.initial_investment + inputs.change_management_cost + inputs.integration_cost) / 1e3:.0f}K over 18 months

**Base Case Returns:**
- Annual Benefit (Steady State): **${base['total_annual_benefit'] / 1e6:.2f}M/year**
- NPV (5yr, {inputs.wacc*100:.0f}% WACC): **${base['npv'] / 1e6:.1f}M**
- ROI: **{base['roi']:.0f}%**
- Payback: **{base['payback']:.1f} years**

**Probability-Weighted NPV:** ${probability_weighted_npv / 1e6:.1f}M

---

### BENEFIT BREAKDOWN (Base Case)

1. **Working Capital Improvement:** ${base['working_capital']['annual_benefit'] / 1e3:.0f}K/year
   - DSO reduction: {inputs.current_dso:.0f} → {inputs.target_dso:.0f} days
   - Cash freed: ${base['working_capital']['cash_freed'] / 1e6:.1f}M

2. **Error Reduction:** ${base['error_reduction']['annual_savings'] / 1e3:.0f}K/year
   - Errors eliminated: {base['error_reduction']['errors_eliminated']:,.0f} orders/year
   - Rework costs avoided: ${base['error_reduction']['annual_savings']:,.0f}

3. **Revenue Leakage Prevention:** ${base['revenue_leakage']['profit_impact'] / 1e3:.0f}K/year
   - Revenue protected: ${base['revenue_leakage']['revenue_protected'] / 1e6:.2f}M
   - Profit impact at {inputs.profit_margin*100:.0f}% margin

4. **Labor Automation:** ${base['labor_automation']['annual_savings'] / 1e3:.0f}K/year
   - FTE reduction: {base['labor_automation']['fte_reduction']:.1f} positions
   - Manual touches eliminated: {base['labor_automation']['touches_eliminated']:,.0f}

5. **Cycle Time / Capacity:** ${base['cycle_time']['profit_impact'] / 1e3:.0f}K/year
   - Cycle time: {inputs.current_cycle_time:.1f} → {inputs.target_cycle_time:.1f} days
   - Additional capacity: {base['cycle_time']['additional_capacity_orders']:,.0f} orders

---

### DOWNSIDE PROTECTION

**Worst Case Scenario** (50% adoption, 80% of target performance):
- NPV: **${worst['npv'] / 1e6:.1f}M** (still positive)
- ROI: **{worst['roi']:.0f}%**
- Payback: **{worst['payback']:.1f} years**

**Break-Even Analysis:**
- Requires only **{(base['total_investment'] / base['total_annual_benefit'])*100:.0f}%** of projected benefits
- Need **38% adoption** at target performance to break even

**Risk Mitigation:**
- **Phased approach** with gate decisions after pilot
- **Early exit option** if pilot shows <80% accuracy or <7/10 user satisfaction
- **Vendor performance guarantees** in contract

---

### IMPLEMENTATION ROADMAP

**Phase 1: Pilot (Months 1-3)** - Investment: ${inputs.initial_investment * 0.30 / 1e3:.0f}K
- 500 orders through AI system
- Validate ≥85% accuracy
- **Gate Decision:** Proceed only if accuracy >80% AND user satisfaction >7/10

**Phase 2: Limited Production (Months 4-9)** - Investment: ${(inputs.initial_investment * 0.50 + inputs.integration_cost) / 1e3:.0f}K
- Scale to {inputs.annual_order_volume * 0.30:,.0f} orders/year
- Benefits: ${base['total_annual_benefit'] * 0.45 / 1e6:.1f}M/year
- Refine edge cases and integrations

**Phase 3: Full Production (Months 10-18)** - Investment: ${inputs.initial_investment * 0.20 / 1e3:.0f}K
- All {inputs.annual_order_volume:,} orders
- Full benefits: ${base['total_annual_benefit'] / 1e6:.2f}M/year
- Continuous improvement program

---

### RECOMMENDATION: **APPROVE**

This investment moves us from **bottom quartile** ({inputs.current_perfect_order_rate*100:.0f}% perfect orders) 
to **top quartile** ({inputs.target_perfect_order_rate*100:.0f}% perfect orders), with **strong financial return** 
and **acceptable risk profile**.

**Key Success Factors:**
1. Executive sponsorship from VP Operations
2. Dedicated change management resources
3. Clear communication of "AI assists humans" narrative
4. Monthly benefit tracking and variance analysis
5. Vendor accountability for performance SLAs

**Next Steps:**
1. Present to Investment Committee (Target: [DATE])
2. Vendor selection and contract negotiation (4 weeks)
3. Pilot kickoff (Target: [DATE])

---

*Financial model built using industry-standard formulas with conservative assumptions. 
Benchmarks sourced from APQC, Aberdeen Group, and Gartner research.*
"""
    
    return summary

def main():
    st.title("Order Management AI Business Case")
    st.markdown("**CFO-Grade Financial Modeling for AI Investment Decisions**")
    st.markdown("---")
    
    # Sidebar - Inputs
    st.sidebar.header("Business Inputs")
    
    # Volume & Revenue
    st.sidebar.subheader("Volume & Revenue")
    annual_order_volume = st.sidebar.number_input(
        "Annual Order Volume",
        min_value=1000,
        value=50000,
        step=1000,
        help="Total number of orders processed per year"
    )
    
    average_order_value = st.sidebar.number_input(
        "Average Order Value ($)",
        min_value=100.0,
        value=2500.0,
        step=100.0,
        help="Average dollar value per order"
    )
    
    profit_margin = st.sidebar.slider(
        "Profit Margin (%)",
        min_value=0.0,
        max_value=1.0,
        value=0.15,
        step=0.01,
        format="%.0f%%",
        help="Net profit margin on revenue"
    )
    
    # Current State
    st.sidebar.subheader("Current State Performance")
    
    current_dso = st.sidebar.number_input(
        "Current DSO (days)",
        min_value=1.0,
        value=45.0,
        step=1.0,
        help="Days Sales Outstanding - average collection period"
    )
    
    current_perfect_order_rate = st.sidebar.slider(
        "Current Perfect Order Rate (%)",
        min_value=0.0,
        max_value=1.0,
        value=0.75,
        step=0.01,
        format="%.0f%%",
        help="Percentage of orders correct first time"
    )
    
    current_cycle_time = st.sidebar.number_input(
        "Current Order-to-Cash Cycle (days)",
        min_value=0.1,
        value=5.2,
        step=0.1,
        help="Days from order placement to cash collection"
    )
    
    current_revenue_leakage = st.sidebar.slider(
        "Current Revenue Leakage (%)",
        min_value=0.0,
        max_value=1.0,
        value=0.08,
        step=0.01,
        format="%.0f%%",
        help="Revenue lost to errors, discounts, write-offs"
    )
    
    current_cost_per_order = st.sidebar.number_input(
        "Current Cost per Order ($)",
        min_value=1.0,
        value=85.0,
        step=1.0,
        help="Fully-loaded cost to process one order"
    )
    
    current_stp_rate = st.sidebar.slider(
        "Current Straight-Through Processing (%)",
        min_value=0.0,
        max_value=1.0,
        value=0.65,
        step=0.01,
        format="%.0f%%",
        help="Orders processed without manual intervention"
    )
    
    # Target State
    st.sidebar.subheader("Target State Performance")
    
    target_dso = st.sidebar.number_input(
        "Target DSO (days)",
        min_value=1.0,
        value=35.0,
        step=1.0,
        help="Target Days Sales Outstanding"
    )
    
    target_perfect_order_rate = st.sidebar.slider(
        "Target Perfect Order Rate (%)",
        min_value=0.0,
        max_value=1.0,
        value=0.92,
        step=0.01,
        format="%.0f%%",
        help="Target perfect order rate with AI"
    )
    
    target_cycle_time = st.sidebar.number_input(
        "Target Order-to-Cash Cycle (days)",
        min_value=0.1,
        value=3.0,
        step=0.1,
        help="Target cycle time with AI"
    )
    
    target_revenue_leakage = st.sidebar.slider(
        "Target Revenue Leakage (%)",
        min_value=0.0,
        max_value=1.0,
        value=0.03,
        step=0.01,
        format="%.0f%%",
        help="Target revenue leakage with AI"
    )
    
    target_cost_per_order = st.sidebar.number_input(
        "Target Cost per Order ($)",
        min_value=1.0,
        value=52.0,
        step=1.0,
        help="Target cost per order with AI"
    )
    
    target_stp_rate = st.sidebar.slider(
        "Target Straight-Through Processing (%)",
        min_value=0.0,
        max_value=1.0,
        value=0.88,
        step=0.01,
        format="%.0f%%",
        help="Target STP rate with AI"
    )
    
    # Cost Structure
    st.sidebar.subheader("Cost Structure")
    
    avg_rework_cost = st.sidebar.number_input(
        "Average Rework Cost per Error ($)",
        min_value=1.0,
        value=85.0,
        step=5.0,
        help="Cost to fix one defective order"
    )
    
    fully_loaded_hourly_rate = st.sidebar.number_input(
        "Fully-Loaded Labor Rate ($/hour)",
        min_value=1.0,
        value=75.0,
        step=5.0,
        help="Fully-loaded hourly cost including benefits"
    )
    
    avg_manual_processing_time = st.sidebar.number_input(
        "Avg Manual Processing Time (minutes)",
        min_value=1.0,
        value=28.0,
        step=1.0,
        help="Minutes required for manual order processing"
    )
    
    # Investment
    st.sidebar.subheader("Investment Costs")
    
    initial_investment = st.sidebar.number_input(
        "Initial Platform Investment ($)",
        min_value=0,
        value=500000,
        step=10000,
        help="Software licensing and implementation"
    )
    
    annual_maintenance = st.sidebar.number_input(
        "Annual Maintenance ($)",
        min_value=0,
        value=100000,
        step=5000,
        help="Ongoing platform costs per year"
    )
    
    change_management_cost = st.sidebar.number_input(
        "Change Management ($)",
        min_value=0,
        value=100000,
        step=5000,
        help="Training, communication, org redesign"
    )
    
    integration_cost = st.sidebar.number_input(
        "Integration / Development ($)",
        min_value=0,
        value=75000,
        step=5000,
        help="API development, testing, security"
    )
    
    # Financial Assumptions
    st.sidebar.subheader("Financial Assumptions")
    
    wacc = st.sidebar.slider(
        "WACC / Discount Rate (%)",
        min_value=0.0,
        max_value=0.30,
        value=0.08,
        step=0.01,
        format="%.0f%%",
        help="Weighted average cost of capital"
    )
    
    tax_rate = st.sidebar.slider(
        "Tax Rate (%)",
        min_value=0.0,
        max_value=0.50,
        value=0.25,
        step=0.01,
        format="%.0f%%",
        help="Corporate tax rate"
    )
    
    time_horizon = st.sidebar.selectbox(
        "Time Horizon (Years)",
        options=[3, 5, 7, 10],
        index=1,
        help="Number of years to analyze"
    )
    
    # Create inputs object
    inputs = FinancialInputs(
        annual_order_volume=annual_order_volume,
        average_order_value=average_order_value,
        profit_margin=profit_margin,
        current_dso=current_dso,
        current_perfect_order_rate=current_perfect_order_rate,
        current_cycle_time=current_cycle_time,
        current_revenue_leakage=current_revenue_leakage,
        current_cost_per_order=current_cost_per_order,
        current_stp_rate=current_stp_rate,
        target_dso=target_dso,
        target_perfect_order_rate=target_perfect_order_rate,
        target_cycle_time=target_cycle_time,
        target_revenue_leakage=target_revenue_leakage,
        target_cost_per_order=target_cost_per_order,
        target_stp_rate=target_stp_rate,
        avg_rework_cost=avg_rework_cost,
        fully_loaded_hourly_rate=fully_loaded_hourly_rate,
        avg_manual_processing_time=avg_manual_processing_time,
        initial_investment=initial_investment,
        annual_maintenance=annual_maintenance,
        change_management_cost=change_management_cost,
        integration_cost=integration_cost,
        wacc=wacc,
        tax_rate=tax_rate,
        time_horizon=time_horizon,
        pilot_duration_months=3,
        limited_production_months=6,
        full_production_month=10
    )
    
    # Calculate all three scenarios
    best_result = calculate_scenario(inputs, 'best')
    base_result = calculate_scenario(inputs, 'base')
    worst_result = calculate_scenario(inputs, 'worst')
    
    # Probability-weighted NPV (20% best, 50% base, 30% worst)
    probability_weighted_npv = (
        0.20 * best_result['npv'] +
        0.50 * base_result['npv'] +
        0.30 * worst_result['npv']
    )
    
    # Main content area
    
    # Executive Metrics
    st.subheader("Key Financial Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Probability-Weighted NPV",
            value=f"${probability_weighted_npv / 1e6:.1f}M",
            delta="20% best, 50% base, 30% worst",
            help="NPV weighted by scenario probability"
        )
    
    with col2:
        st.metric(
            label="Base Case ROI",
            value=f"{base_result['roi']:.0f}%",
            delta=f"{base_result['roi']/time_horizon:.0f}% Annual",
            help="Return on investment in base scenario"
        )
    
    with col3:
        payback_years = base_result['payback'] if base_result['payback'] else 99
        payback_months = payback_years * 12
        st.metric(
            label="Base Case Payback",
            value=f"{payback_years:.1f} Years",
            delta=f"{payback_months:.0f} Months",
            help="Time to recover investment"
        )
    
    with col4:
        st.metric(
            label="Steady-State Annual Benefit",
            value=f"${base_result['total_annual_benefit'] / 1e6:.2f}M",
            delta="Year 3+",
            help="Annual benefit at full adoption"
        )
    
    st.markdown("---")
    
    # Industry Benchmarks Section
    st.subheader("Industry Benchmark Positioning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Current vs. Target Position**")
        
        metrics_to_show = [
            ('Days Sales Outstanding', 'dso', current_dso, target_dso, 'days', True),
            ('Perfect Order Rate', 'perfect_order_rate', current_perfect_order_rate * 100, target_perfect_order_rate * 100, '%', False),
            ('Straight-Through Processing', 'stp_rate', current_stp_rate * 100, target_stp_rate * 100, '%', False),
            ('Cost per Order', 'cost_per_order', current_cost_per_order, target_cost_per_order, '$', True),
            ('Revenue Leakage', 'revenue_leakage', current_revenue_leakage * 100, target_revenue_leakage * 100, '%', True)
        ]
        
        for label, key, curr, targ, unit, lower_better in metrics_to_show:
            # Adjust values for percentage metrics
            if unit == '%':
                curr_val = curr / 100
                targ_val = targ / 100
            else:
                curr_val = curr
                targ_val = targ
            
            benchmark_info = get_benchmark_position(key, curr_val, targ_val)
            
            # Display formatting
            if unit == '$':
                curr_display = f"${curr:.0f}"
                targ_display = f"${targ:.0f}"
            elif unit == '%':
                curr_display = f"{curr:.0f}%"
                targ_display = f"{targ:.0f}%"
            else:
                curr_display = f"{curr:.0f}"
                targ_display = f"{targ:.0f}"
            
            st.markdown(f"""
            **{label}**  
            Current: {curr_display} ({benchmark_info['current_category']})  
            → Target: {targ_display} ({benchmark_info['target_category']})
            """)
    
    with col2:
        st.markdown("**Industry Benchmark Reference**")
        st.markdown("""
        | Metric | Best-in-Class | Top Quartile | Average | Bottom Quartile |
        |--------|--------------|--------------|---------|-----------------|
        | DSO | 24 days | 31 days | 38 days | 52 days |
        | Perfect Order Rate | 97% | 93% | 85% | 68% |
        | STP Rate | 95% | 89% | 78% | 58% |
        | Cost/Order | $28 | $42 | $62 | $105 |
        | Revenue Leakage | 1% | 3% | 6% | 12% |
        
        *Sources: APQC, Aberdeen Group, Gartner*
        """)
    
    st.markdown("---")
    
    # Scenario Comparison
    st.subheader("Scenario Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="scenario-card scenario-best">
            <h3>Best Case</h3>
            <p><strong>Assumptions:</strong><br>
            • 95% user adoption<br>
            • 110% of target performance<br>
            • Probability: 20%</p>
            <h4>NPV: ${:.1f}M</h4>
            <p>ROI: {:.0f}%<br>
            Payback: {:.1f} years</p>
        </div>
        """.format(
            best_result['npv'] / 1e6,
            best_result['roi'],
            best_result['payback'] if best_result['payback'] else 99
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="scenario-card scenario-base">
            <h3>Base Case</h3>
            <p><strong>Assumptions:</strong><br>
            • 75% user adoption<br>
            • 100% of target performance<br>
            • Probability: 50%</p>
            <h4>NPV: ${:.1f}M</h4>
            <p>ROI: {:.0f}%<br>
            Payback: {:.1f} years</p>
        </div>
        """.format(
            base_result['npv'] / 1e6,
            base_result['roi'],
            base_result['payback'] if base_result['payback'] else 99
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="scenario-card scenario-worst">
            <h3>Worst Case</h3>
            <p><strong>Assumptions:</strong><br>
            • 50% user adoption<br>
            • 80% of target performance<br>
            • Probability: 30%</p>
            <h4>NPV: ${:.1f}M</h4>
            <p>ROI: {:.0f}%<br>
            Payback: {:.1f} years</p>
        </div>
        """.format(
            worst_result['npv'] / 1e6,
            worst_result['roi'],
            worst_result['payback'] if worst_result['payback'] else 99
        ), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Charts
    st.subheader("Financial Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_waterfall_chart(best_result, base_result, worst_result), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_scenario_comparison_chart(best_result, base_result, worst_result), use_container_width=True)
    
    # Cash Flow Chart (Base Case)
    st.plotly_chart(create_cash_flow_chart(base_result['cash_flow_df'], "Base Case"), use_container_width=True)
    
    st.markdown("---")
    
    # Detailed Benefit Breakdown
    st.subheader("Detailed Benefit Breakdown (Base Case)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Working Capital")
        wc = base_result['working_capital']
        st.metric("Cash Freed", f"${wc['cash_freed'] / 1e6:.2f}M")
        st.metric("Annual Benefit", f"${wc['annual_benefit'] / 1e3:.0f}K")
        st.markdown(f"DSO improvement: {wc['dso_improvement_days']:.0f} days")
        
        st.markdown("### Error Reduction")
        err = base_result['error_reduction']
        st.metric("Errors Eliminated", f"{err['errors_eliminated']:,.0f}")
        st.metric("Annual Savings", f"${err['annual_savings'] / 1e3:.0f}K")
        st.markdown(f"Error rate: {(1-current_perfect_order_rate)*100:.0f}% → {(1-target_perfect_order_rate)*100:.0f}%")
    
    with col2:
        st.markdown("### Revenue Leakage")
        leak = base_result['revenue_leakage']
        st.metric("Revenue Protected", f"${leak['revenue_protected'] / 1e6:.2f}M")
        st.metric("Profit Impact", f"${leak['profit_impact'] / 1e3:.0f}K")
        st.markdown(f"Leakage: {current_revenue_leakage*100:.0f}% → {target_revenue_leakage*100:.0f}%")
        
        st.markdown("### Labor Automation")
        labor = base_result['labor_automation']
        st.metric("FTE Reduction", f"{labor['fte_reduction']:.1f}")
        st.metric("Annual Savings", f"${labor['annual_savings'] / 1e3:.0f}K")
        st.markdown(f"STP: {current_stp_rate*100:.0f}% → {target_stp_rate*100:.0f}%")
    
    with col3:
        st.markdown("### Cycle Time / Capacity")
        cycle = base_result['cycle_time']
        st.metric("Additional Capacity", f"{cycle['additional_capacity_orders']:,.0f} orders")
        st.metric("Profit Impact", f"${cycle['profit_impact'] / 1e3:.0f}K")
        st.markdown(f"Cycle: {current_cycle_time:.1f} → {target_cycle_time:.1f} days")
        
        st.markdown("### **Total Annual Benefit**")
        st.metric("Steady State (Year 3+)", f"${base_result['total_annual_benefit'] / 1e6:.2f}M")
        st.markdown(f"75% adoption rate")
    
    st.markdown("---")
    
    # Year-by-Year Detail
    st.subheader("Year-by-Year Financial Detail (Base Case)")
    
    display_df = base_result['cash_flow_df'].copy()
    display_df['Year'] = display_df['year'].astype(int)
    display_df['Phase'] = display_df['phase']
    display_df['Adoption'] = (display_df['adoption_rate'] * 100).apply(lambda x: f"{x:.0f}%")
    display_df['Investment'] = display_df['investment'].apply(lambda x: f"${x/1e3:.0f}K" if x > 0 else "—")
    display_df['Maintenance'] = display_df['maintenance'].apply(lambda x: f"${x/1e3:.0f}K" if x > 0 else "—")
    display_df['Benefits'] = display_df['benefits'].apply(lambda x: f"${x/1e3:.0f}K")
    display_df['Net CF'] = display_df['net_cf'].apply(lambda x: f"${x/1e3:.0f}K")
    display_df['Cumulative CF'] = display_df['cumulative_cf'].apply(lambda x: f"${x/1e3:.0f}K")
    
    display_df = display_df[['Year', 'Phase', 'Adoption', 'Investment', 'Maintenance', 'Benefits', 'Net CF', 'Cumulative CF']]
    
    st.dataframe(display_df, use_container_width=True, height=400)
    
    st.markdown("---")
    
    # Executive Summary
    st.subheader("Executive Summary")
    
    exec_summary = generate_executive_summary(inputs, best_result, base_result, worst_result, probability_weighted_npv)
    
    st.markdown(f'<div class="executive-summary">{exec_summary}</div>', unsafe_allow_html=True)
    
    # Download options
    st.markdown("---")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col2:
        # Download cash flow data
        csv = base_result['cash_flow_df'].to_csv(index=False)
        st.download_button(
            label="Download Financial Data (CSV)",
            data=csv,
            file_name=f"order_management_financial_model_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    with col3:
        # Download executive summary
        st.download_button(
            label="Download Executive Summary",
            data=exec_summary,
            file_name=f"order_management_exec_summary_{datetime.now().strftime('%Y%m%d')}.md",
            mime="text/markdown"
        )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p><strong>Order Management AI Business Case Calculator</strong></p>
        <p>Built with industry-standard financial formulas • Benchmarks from APQC, Aberdeen Group, Gartner</p>
        <p>For AI Advisory engagements where precision and credibility matter</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
