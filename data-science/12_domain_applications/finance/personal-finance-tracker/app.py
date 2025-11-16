"""
Personal Finance Tracker - Streamlit Web Application

A modern web interface for tracking income, expenses, budgets, and financial goals.
Built with Streamlit for an interactive user experience.

Run with: streamlit run app.py
"""

import json
import os
from datetime import datetime, timedelta

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Personal Finance Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown(
    """
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Initialize session state for data persistence
if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=["date", "category", "amount", "description"])
if "income" not in st.session_state:
    st.session_state.income = pd.DataFrame(columns=["date", "category", "amount", "description"])
if "budgets" not in st.session_state:
    st.session_state.budgets = {
        "Food": 350.00,
        "Transport": 100.00,
        "Entertainment": 150.00,
        "Shopping": 200.00,
        "Utilities": 250.00,
    }


# Load data on startup
def load_data():
    """Load expenses and income from CSV files if they exist."""
    if os.path.exists("data/expenses.csv"):
        df = pd.read_csv("data/expenses.csv", parse_dates=["date"])
        st.session_state.expenses = df
    if os.path.exists("data/income.csv"):
        df = pd.read_csv("data/income.csv", parse_dates=["date"])
        st.session_state.income = df


# Save data
def save_data():
    """Save expenses and income to CSV files."""
    os.makedirs("data", exist_ok=True)
    st.session_state.expenses.to_csv("data/expenses.csv", index=False)
    st.session_state.income.to_csv("data/income.csv", index=False)


# Load data on app start
load_data()

# Header
st.markdown('<h1 class="main-header">💰 Personal Finance Tracker</h1>', unsafe_allow_html=True)
st.markdown("Track your income and expenses with powerful analytics and insights")

# Sidebar Navigation
with st.sidebar:
    st.image(
        "https://via.placeholder.com/150x50/1E88E5/FFFFFF?text=Finance+Tracker",
        use_container_width=True,
    )
    st.markdown("## Navigation")

    page = st.radio(
        "Go to:",
        [
            "📊 Dashboard",
            "➕ Add Transaction",
            "💵 Income",
            "💸 Expenses",
            "📈 Analytics",
            "🎯 Budgets",
            "⚙️ Settings",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")

    # Quick Stats in Sidebar
    st.markdown("### Quick Stats")
    total_expenses = (
        st.session_state.expenses["amount"].sum() if len(st.session_state.expenses) > 0 else 0
    )
    total_income = (
        st.session_state.income["amount"].sum() if len(st.session_state.income) > 0 else 0
    )
    net_savings = total_income - total_expenses

    st.metric("Total Income", f"${total_income:,.2f}")
    st.metric("Total Expenses", f"${total_expenses:,.2f}")
    st.metric(
        "Net Savings",
        f"${net_savings:,.2f}",
        delta=f"{(net_savings/total_income*100):.1f}%" if total_income > 0 else "0%",
    )

# Main Content Area
if page == "📊 Dashboard":
    st.header("Dashboard Overview")

    # Top Metrics Row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("💰 Total Income", f"${total_income:,.2f}")

    with col2:
        st.metric("💸 Total Expenses", f"${total_expenses:,.2f}")

    with col3:
        savings_rate = (net_savings / total_income * 100) if total_income > 0 else 0
        st.metric("📊 Savings Rate", f"{savings_rate:.1f}%")

    with col4:
        transaction_count = len(st.session_state.expenses) + len(st.session_state.income)
        st.metric("📝 Total Transactions", transaction_count)

    st.markdown("---")

    # Charts Row
    if len(st.session_state.expenses) > 0:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Spending by Category")
            category_totals = st.session_state.expenses.groupby("category")["amount"].sum()
            fig = px.pie(values=category_totals.values, names=category_totals.index, hole=0.4)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Income vs Expenses")
            # Prepare monthly data
            if len(st.session_state.income) > 0:
                expenses_monthly = st.session_state.expenses.copy()
                expenses_monthly["month"] = expenses_monthly["date"].dt.to_period("M").astype(str)
                exp_by_month = expenses_monthly.groupby("month")["amount"].sum()

                income_monthly = st.session_state.income.copy()
                income_monthly["month"] = income_monthly["date"].dt.to_period("M").astype(str)
                inc_by_month = income_monthly.groupby("month")["amount"].sum()

                fig = go.Figure()
                fig.add_trace(
                    go.Bar(
                        x=inc_by_month.index,
                        y=inc_by_month.values,
                        name="Income",
                        marker_color="green",
                    )
                )
                fig.add_trace(
                    go.Bar(
                        x=exp_by_month.index,
                        y=exp_by_month.values,
                        name="Expenses",
                        marker_color="red",
                    )
                )
                fig.update_layout(barmode="group", xaxis_title="Month", yaxis_title="Amount ($)")
                st.plotly_chart(fig, use_container_width=True)

        # Recent Transactions
        st.subheader("Recent Transactions")
        recent_expenses = st.session_state.expenses.sort_values("date", ascending=False).head(5)
        if len(recent_expenses) > 0:
            st.dataframe(
                recent_expenses[["date", "category", "amount", "description"]],
                use_container_width=True,
            )
    else:
        st.info("No data yet! Add your first transaction to get started.")

elif page == "➕ Add Transaction":
    st.header("Add New Transaction")

    tab1, tab2 = st.tabs(["💸 Add Expense", "💵 Add Income"])

    with tab1:
        with st.form("expense_form"):
            col1, col2 = st.columns(2)

            with col1:
                exp_date = st.date_input("Date", value=datetime.now())
                exp_category = st.selectbox(
                    "Category",
                    [
                        "Food",
                        "Transport",
                        "Entertainment",
                        "Shopping",
                        "Utilities",
                        "Healthcare",
                        "Other",
                    ],
                )

            with col2:
                exp_amount = st.number_input("Amount ($)", min_value=0.01, value=10.00, step=0.01)
                exp_description = st.text_input("Description")

            submitted = st.form_submit_button("Add Expense", use_container_width=True)

            if submitted:
                new_expense = pd.DataFrame(
                    [
                        {
                            "date": pd.to_datetime(exp_date),
                            "category": exp_category,
                            "amount": float(exp_amount),
                            "description": exp_description,
                        }
                    ]
                )
                st.session_state.expenses = pd.concat(
                    [st.session_state.expenses, new_expense], ignore_index=True
                )
                save_data()
                st.success(f"✅ Added expense: ${exp_amount:.2f} for {exp_category}")
                st.rerun()

    with tab2:
        with st.form("income_form"):
            col1, col2 = st.columns(2)

            with col1:
                inc_date = st.date_input("Date", value=datetime.now(), key="inc_date")
                inc_category = st.selectbox(
                    "Category",
                    ["Salary", "Freelance", "Investment", "Business", "Gift", "Other"],
                    key="inc_cat",
                )

            with col2:
                inc_amount = st.number_input(
                    "Amount ($)", min_value=0.01, value=100.00, step=0.01, key="inc_amt"
                )
                inc_description = st.text_input("Description", key="inc_desc")

            submitted = st.form_submit_button("Add Income", use_container_width=True)

            if submitted:
                new_income = pd.DataFrame(
                    [
                        {
                            "date": pd.to_datetime(inc_date),
                            "category": inc_category,
                            "amount": float(inc_amount),
                            "description": inc_description,
                        }
                    ]
                )
                st.session_state.income = pd.concat(
                    [st.session_state.income, new_income], ignore_index=True
                )
                save_data()
                st.success(f"✅ Added income: ${inc_amount:.2f} from {inc_category}")
                st.rerun()

elif page == "💸 Expenses":
    st.header("Expense Management")

    if len(st.session_state.expenses) > 0:
        # Filters
        col1, col2, col3 = st.columns(3)

        with col1:
            categories = ["All"] + list(st.session_state.expenses["category"].unique())
            selected_category = st.selectbox("Filter by Category", categories)

        with col2:
            min_date = st.session_state.expenses["date"].min().date()
            start_date = st.date_input("Start Date", value=min_date)

        with col3:
            max_date = st.session_state.expenses["date"].max().date()
            end_date = st.date_input("End Date", value=max_date)

        # Filter data
        filtered_df = st.session_state.expenses.copy()
        if selected_category != "All":
            filtered_df = filtered_df[filtered_df["category"] == selected_category]
        filtered_df = filtered_df[
            (filtered_df["date"].dt.date >= start_date) & (filtered_df["date"].dt.date <= end_date)
        ]

        # Display summary
        st.metric("Total in Selection", f"${filtered_df['amount'].sum():,.2f}")

        # Display table
        st.dataframe(filtered_df.sort_values("date", ascending=False), use_container_width=True)

        # Category breakdown
        st.subheader("Category Breakdown")
        category_summary = (
            filtered_df.groupby("category")["amount"].agg(["sum", "count", "mean"]).round(2)
        )
        category_summary.columns = ["Total", "Count", "Average"]
        st.dataframe(category_summary, use_container_width=True)
    else:
        st.info("No expenses recorded yet.")

elif page == "💵 Income":
    st.header("Income Management")

    if len(st.session_state.income) > 0:
        # Display summary
        st.metric("Total Income", f"${st.session_state.income['amount'].sum():,.2f}")

        # Display table
        st.dataframe(
            st.session_state.income.sort_values("date", ascending=False), use_container_width=True
        )

        # Category breakdown
        st.subheader("Income by Source")
        income_summary = (
            st.session_state.income.groupby("category")["amount"]
            .agg(["sum", "count", "mean"])
            .round(2)
        )
        income_summary.columns = ["Total", "Count", "Average"]
        st.dataframe(income_summary, use_container_width=True)
    else:
        st.info("No income recorded yet.")

elif page == "📈 Analytics":
    st.header("Financial Analytics")

    if len(st.session_state.expenses) > 0:
        tab1, tab2, tab3 = st.tabs(["Trends", "Insights", "Forecast"])

        with tab1:
            st.subheader("Spending Trends")

            # Monthly trend
            df_monthly = st.session_state.expenses.copy()
            df_monthly["month"] = df_monthly["date"].dt.to_period("M").astype(str)
            monthly_totals = df_monthly.groupby("month")["amount"].sum()

            fig = px.line(
                x=monthly_totals.index,
                y=monthly_totals.values,
                title="Monthly Spending Trend",
                labels={"x": "Month", "y": "Amount ($)"},
            )
            fig.update_traces(mode="lines+markers")
            st.plotly_chart(fig, use_container_width=True)

            # Day of week analysis
            df_dow = st.session_state.expenses.copy()
            df_dow["day_of_week"] = df_dow["date"].dt.day_name()
            dow_spending = (
                df_dow.groupby("day_of_week")["amount"]
                .sum()
                .reindex(
                    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                )
            )

            fig = px.bar(
                x=dow_spending.index,
                y=dow_spending.values,
                title="Spending by Day of Week",
                labels={"x": "Day", "y": "Amount ($)"},
                color=dow_spending.values,
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.subheader("Spending Insights")

            # Top spending days
            top_days = st.session_state.expenses.nlargest(5, "amount")
            st.write("**Top 5 Largest Expenses:**")
            for idx, row in top_days.iterrows():
                st.write(
                    f"- ${row['amount']:.2f} on {row['date'].strftime('%Y-%m-%d')}: {row['description']} ({row['category']})"
                )

            # Average by category
            st.write("\n**Average Spending by Category:**")
            avg_by_cat = (
                st.session_state.expenses.groupby("category")["amount"]
                .mean()
                .sort_values(ascending=False)
            )
            for cat, avg in avg_by_cat.items():
                st.write(f"- {cat}: ${avg:.2f}")

        with tab3:
            st.subheader("Spending Forecast")
            st.info("Simple linear forecast based on historical trends")

            # Prepare monthly data
            df_monthly = st.session_state.expenses.copy()
            df_monthly["month"] = df_monthly["date"].dt.to_period("M")
            monthly_totals = df_monthly.groupby("month")["amount"].sum().reset_index()
            monthly_totals["month_num"] = range(len(monthly_totals))

            if len(monthly_totals) >= 3:
                import numpy as np
                from sklearn.linear_model import LinearRegression

                X = monthly_totals[["month_num"]].values
                y = monthly_totals["amount"].values

                model = LinearRegression()
                model.fit(X, y)

                # Forecast next 3 months
                future_months = np.array([[len(monthly_totals) + i] for i in range(1, 4)])
                predictions = model.predict(future_months)

                forecast_df = pd.DataFrame(
                    {
                        "Month": ["Next Month", "Month +2", "Month +3"],
                        "Predicted Spending": predictions,
                    }
                )

                st.dataframe(forecast_df, use_container_width=True)

                trend = "increasing" if model.coef_[0] > 0 else "decreasing"
                st.write(
                    f"**Trend:** Spending is {trend} by approximately ${abs(model.coef_[0]):.2f} per month"
                )
            else:
                st.warning("Need at least 3 months of data for forecasting")
    else:
        st.info("Add some transactions to see analytics!")

elif page == "🎯 Budgets":
    st.header("Budget Management")

    st.subheader("Set Monthly Budgets")

    col1, col2 = st.columns([2, 1])

    with col1:
        # Budget setting
        with st.form("budget_form"):
            for category in list(st.session_state.budgets.keys()):
                st.session_state.budgets[category] = st.number_input(
                    f"{category} Budget",
                    min_value=0.0,
                    value=float(st.session_state.budgets.get(category, 0.0)),
                    step=10.0,
                    key=f"budget_{category}",
                )

            if st.form_submit_button("Save Budgets"):
                st.success("✅ Budgets updated!")

    with col2:
        st.metric("Total Budget", f"${sum(st.session_state.budgets.values()):,.2f}")

    # Budget vs Actual
    if len(st.session_state.expenses) > 0:
        st.subheader("Budget Status (Current Month)")

        current_date = datetime.now()
        current_month_expenses = st.session_state.expenses[
            (st.session_state.expenses["date"].dt.year == current_date.year)
            & (st.session_state.expenses["date"].dt.month == current_date.month)
        ]

        actual_spending = current_month_expenses.groupby("category")["amount"].sum()

        budget_data = []
        for category, budget in st.session_state.budgets.items():
            actual = actual_spending.get(category, 0)
            remaining = budget - actual
            pct_used = (actual / budget * 100) if budget > 0 else 0

            budget_data.append(
                {
                    "Category": category,
                    "Budget": f"${budget:.2f}",
                    "Spent": f"${actual:.2f}",
                    "Remaining": f"${remaining:.2f}",
                    "Used": f"{pct_used:.1f}%",
                    "Status": "✅" if remaining >= 0 else "⚠️",
                }
            )

        budget_df = pd.DataFrame(budget_data)
        st.dataframe(budget_df, use_container_width=True)

elif page == "⚙️ Settings":
    st.header("Settings")

    tab1, tab2, tab3 = st.tabs(["Import/Export", "Data Management", "About"])

    with tab1:
        st.subheader("Import Data")
        uploaded_file = st.file_uploader("Upload Expenses CSV", type=["csv"])
        if uploaded_file:
            try:
                df_import = pd.read_csv(uploaded_file, parse_dates=["date"])
                st.session_state.expenses = pd.concat(
                    [st.session_state.expenses, df_import], ignore_index=True
                )
                save_data()
                st.success(f"✅ Imported {len(df_import)} expenses")
            except Exception as e:
                st.error(f"Error importing: {e}")

        st.markdown("---")
        st.subheader("Export Data")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📥 Download Expenses as CSV"):
                csv = st.session_state.expenses.to_csv(index=False)
                st.download_button("Download", csv, "expenses.csv", "text/csv")

        with col2:
            if st.button("📥 Download Income as CSV"):
                csv = st.session_state.income.to_csv(index=False)
                st.download_button("Download", csv, "income.csv", "text/csv")

    with tab2:
        st.subheader("Data Management")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Expenses", len(st.session_state.expenses))
            if st.button("🗑️ Clear All Expenses", type="secondary"):
                if st.checkbox("Confirm deletion"):
                    st.session_state.expenses = pd.DataFrame(
                        columns=["date", "category", "amount", "description"]
                    )
                    save_data()
                    st.success("Expenses cleared")

        with col2:
            st.metric("Total Income Records", len(st.session_state.income))
            if st.button("🗑️ Clear All Income", type="secondary"):
                if st.checkbox("Confirm deletion", key="confirm_income"):
                    st.session_state.income = pd.DataFrame(
                        columns=["date", "category", "amount", "description"]
                    )
                    save_data()
                    st.success("Income records cleared")

    with tab3:
        st.subheader("About Personal Finance Tracker")
        st.markdown(
            """
        **Version:** 2.0.0 (Enhanced)

        **Features:**
        - Income and expense tracking
        - Budget management
        - Interactive visualizations
        - Spending analytics and forecasts
        - Data import/export

        **Built with:**
        - Python
        - Streamlit
        - Pandas
        - Plotly
        - Scikit-learn

        **Created as part of the Python Projects Portfolio**
        """
        )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Personal Finance Tracker © 2025 | Built with Streamlit"
    "</div>",
    unsafe_allow_html=True,
)
