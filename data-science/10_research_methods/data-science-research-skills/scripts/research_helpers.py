"""
Research Helper Functions
==========================

Utility functions to support your research projects.
"""

import os
from datetime import datetime

import numpy as np
import pandas as pd


def create_paper_tracker():
    """
    Create a DataFrame template for tracking papers.

    Returns:
        pd.DataFrame: Empty paper tracking template
    """
    return pd.DataFrame(
        {
            "Title": [],
            "Authors": [],
            "Year": [],
            "Type": [],
            "Pass_Level": [],
            "Key_Finding": [],
            "Relevance": [],
            "Status": [],
            "Date_Read": [],
            "Notes": [],
        }
    )


def add_paper(
    tracker,
    title,
    authors,
    year,
    paper_type="Original Research",
    pass_level="Pass 1",
    key_finding="",
    relevance=3,
    status="To Read",
    notes="",
):
    """
    Add a paper to your tracking system.

    Args:
        tracker (pd.DataFrame): Paper tracker DataFrame
        title (str): Paper title
        authors (str): Paper authors
        year (int): Publication year
        paper_type (str): Type of paper
        pass_level (str): Reading level completed
        key_finding (str): Main finding
        relevance (int): Relevance score (1-5)
        status (str): Reading status
        notes (str): Additional notes

    Returns:
        pd.DataFrame: Updated tracker
    """
    new_paper = pd.DataFrame(
        [
            {
                "Title": title,
                "Authors": authors,
                "Year": year,
                "Type": paper_type,
                "Pass_Level": pass_level,
                "Key_Finding": key_finding,
                "Relevance": relevance,
                "Status": status,
                "Date_Read": datetime.now().strftime("%Y-%m-%d"),
                "Notes": notes,
            }
        ]
    )

    return pd.concat([tracker, new_paper], ignore_index=True)


def search_query_builder(keywords, year_start=None, year_end=None, author=None, intitle=False):
    """
    Build a Google Scholar search query.

    Args:
        keywords (list): List of keywords
        year_start (int): Start year for range
        year_end (int): End year for range
        author (str): Author name
        intitle (bool): Search in title only

    Returns:
        str: Formatted search query
    """
    query_parts = []

    # Add keywords
    for keyword in keywords:
        if " " in keyword:
            query_parts.append(f'"{keyword}"')
        else:
            query_parts.append(keyword)

    query = " ".join(query_parts)

    # Add year range
    if year_start and year_end:
        query += f" {year_start}..{year_end}"

    # Add author
    if author:
        query += f' author:"{author}"'

    # Add title search
    if intitle:
        query = f"intitle:{query}"

    return query


def calculate_sample_size(effect_size, power=0.8, alpha=0.05):
    """
    Calculate required sample size for research.

    Args:
        effect_size (float): Expected effect size (Cohen's d)
        power (float): Statistical power (default 0.8)
        alpha (float): Significance level (default 0.05)

    Returns:
        int: Required sample size per group
    """
    from scipy import stats

    # This is a simplified calculation
    # For precise calculations, use statistical software

    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)

    n = ((z_alpha + z_beta) / effect_size) ** 2 * 2

    return int(np.ceil(n))


def create_research_timeline(start_date, total_weeks, phases):
    """
    Create a research project timeline.

    Args:
        start_date (str): Start date (YYYY-MM-DD)
        total_weeks (int): Total project duration in weeks
        phases (dict): Dictionary of phase names and durations in weeks

    Returns:
        pd.DataFrame: Timeline with phases and dates
    """
    from datetime import timedelta

    start = pd.to_datetime(start_date)
    timeline = []
    current_date = start

    for phase, weeks in phases.items():
        end_date = current_date + timedelta(weeks=weeks)
        timeline.append(
            {
                "Phase": phase,
                "Start": current_date.strftime("%Y-%m-%d"),
                "End": end_date.strftime("%Y-%m-%d"),
                "Weeks": weeks,
            }
        )
        current_date = end_date

    return pd.DataFrame(timeline)


def validate_data_quality(df, required_columns=None, max_missing_pct=0.1):
    """
    Perform basic data quality checks.

    Args:
        df (pd.DataFrame): Data to validate
        required_columns (list): Columns that must exist
        max_missing_pct (float): Maximum allowed missing percentage

    Returns:
        dict: Data quality report
    """
    report = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": {},
        "duplicates": df.duplicated().sum(),
        "quality_issues": [],
    }

    # Check required columns
    if required_columns:
        missing_cols = set(required_columns) - set(df.columns)
        if missing_cols:
            report["quality_issues"].append(f"Missing required columns: {missing_cols}")

    # Check missing values
    for col in df.columns:
        missing = df[col].isnull().sum()
        missing_pct = missing / len(df)
        report["missing_values"][col] = {"count": missing, "percentage": missing_pct}

        if missing_pct > max_missing_pct:
            report["quality_issues"].append(
                f"{col}: {missing_pct*100:.1f}% missing (> {max_missing_pct*100}%)"
            )

    # Overall quality score
    if len(report["quality_issues"]) == 0:
        report["overall_quality"] = "Excellent"
    elif len(report["quality_issues"]) <= 2:
        report["overall_quality"] = "Good"
    elif len(report["quality_issues"]) <= 5:
        report["overall_quality"] = "Fair"
    else:
        report["overall_quality"] = "Poor"

    return report


def generate_citation(authors, year, title, venue, citation_style="apa"):
    """
    Generate a citation in specified format.

    Args:
        authors (str): Authors (e.g., "Smith, J., & Jones, K.")
        year (int): Publication year
        title (str): Paper title
        venue (str): Journal or conference
        citation_style (str): Citation style ('apa', 'mla', 'chicago')

    Returns:
        str: Formatted citation
    """
    if citation_style.lower() == "apa":
        return f"{authors} ({year}). {title}. {venue}."
    elif citation_style.lower() == "mla":
        return f'{authors}. "{title}." {venue}, {year}.'
    elif citation_style.lower() == "chicago":
        return f'{authors}. "{title}." {venue} ({year}).'
    else:
        return f"{authors} ({year}). {title}. {venue}."


def create_project_structure(project_name, base_path="."):
    """
    Create a standard research project structure.

    Args:
        project_name (str): Name of the project
        base_path (str): Base path where to create project
    """
    project_path = os.path.join(base_path, project_name)

    folders = [
        "data/raw",
        "data/processed",
        "notebooks",
        "src",
        "outputs/figures",
        "outputs/tables",
        "outputs/models",
        "docs",
        "tests",
    ]

    for folder in folders:
        os.makedirs(os.path.join(project_path, folder), exist_ok=True)

        # Create .gitkeep files
        gitkeep_path = os.path.join(project_path, folder, ".gitkeep")
        with open(gitkeep_path, "w") as f:
            pass

    print(f"✅ Project structure created at: {project_path}")
    print("\nFolders created:")
    for folder in folders:
        print(f"  - {folder}")


# Example usage
if __name__ == "__main__":
    print("Research Helper Functions")
    print("=" * 50)
    print("\nAvailable functions:")
    print("  - create_paper_tracker()")
    print("  - add_paper()")
    print("  - search_query_builder()")
    print("  - calculate_sample_size()")
    print("  - create_research_timeline()")
    print("  - validate_data_quality()")
    print("  - generate_citation()")
    print("  - create_project_structure()")
    print("\nImport this module in your notebooks:")
    print("  from scripts.research_helpers import *")
