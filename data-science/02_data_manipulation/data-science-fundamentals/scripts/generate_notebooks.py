"""
Script to generate Jupyter notebook templates for the Data Science Fundamentals project.
"""

import json
import os

# Notebook templates
NOTEBOOKS = {
    "03_pandas_basics.ipynb": {
        "title": "Module 03: Pandas Basics",
        "time": "60 minutes",
        "topics": [
            "Introduction to Pandas",
            "Series and DataFrames",
            "Loading data (CSV, Excel, JSON)",
            "Selecting and filtering data",
            "Group-by operations",
            "Data aggregation",
            "Date/time handling",
            "Exporting data",
        ],
        "next_module": "04_data_cleaning.ipynb",
    },
    "04_data_cleaning.ipynb": {
        "title": "Module 04: Data Cleaning",
        "time": "60 minutes",
        "topics": [
            "Identifying missing data",
            "Handling missing values",
            "Removing duplicates",
            "Data type conversions",
            "String cleaning",
            "Outlier detection",
            "Data validation",
        ],
        "next_module": "05_exploratory_data_analysis.ipynb",
    },
    "05_exploratory_data_analysis.ipynb": {
        "title": "Module 05: Exploratory Data Analysis (EDA)",
        "time": "60 minutes",
        "topics": [
            "Summary statistics",
            "Distribution analysis",
            "Correlation analysis",
            "Cross-tabulation",
            "Pivot tables",
            "Data profiling",
            "Insights extraction",
        ],
        "next_module": "06_data_visualization_matplotlib.ipynb",
    },
    "06_data_visualization_matplotlib.ipynb": {
        "title": "Module 06: Data Visualization with Matplotlib",
        "time": "60 minutes",
        "topics": [
            "Introduction to Matplotlib",
            "Line plots",
            "Bar charts",
            "Scatter plots",
            "Histograms",
            "Subplots and layouts",
            "Customization (colors, labels, legends)",
            "Saving figures",
        ],
        "next_module": "07_advanced_visualization.ipynb",
    },
    "07_advanced_visualization.ipynb": {
        "title": "Module 07: Advanced Visualization",
        "time": "60 minutes",
        "topics": [
            "Seaborn statistical plots",
            "Heatmaps and correlation matrices",
            "Distribution plots",
            "Categorical plots",
            "Plotly interactive charts",
            "Dashboards",
            "Best practices",
        ],
        "next_module": "08_statistical_analysis.ipynb",
    },
    "08_statistical_analysis.ipynb": {
        "title": "Module 08: Statistical Analysis",
        "time": "75 minutes",
        "topics": [
            "Probability distributions",
            "Hypothesis testing",
            "T-tests",
            "Chi-square tests",
            "ANOVA",
            "P-values and significance",
            "Confidence intervals",
            "Statistical inference",
        ],
        "next_module": "09_introduction_to_machine_learning.ipynb",
    },
    "09_introduction_to_machine_learning.ipynb": {
        "title": "Module 09: Introduction to Machine Learning",
        "time": "60 minutes",
        "topics": [
            "What is machine learning?",
            "Supervised vs unsupervised learning",
            "Train-test split",
            "Feature engineering basics",
            "Model evaluation metrics",
            "Cross-validation",
            "Scikit-learn basics",
            "Your first ML model",
        ],
        "next_module": "10_supervised_learning.ipynb",
    },
    "10_supervised_learning.ipynb": {
        "title": "Module 10: Supervised Learning",
        "time": "75 minutes",
        "topics": [
            "Linear regression",
            "Logistic regression",
            "Decision trees",
            "Random forests",
            "K-nearest neighbors",
            "Model evaluation",
            "Feature importance",
            "Hyperparameter tuning",
        ],
        "next_module": "11_final_project.ipynb",
    },
    "11_final_project.ipynb": {
        "title": "Module 11: Final Capstone Project",
        "time": "90 minutes",
        "topics": [
            "Project overview",
            "Data loading and exploration",
            "Data cleaning",
            "Exploratory data analysis",
            "Visualization",
            "Statistical analysis",
            "Machine learning modeling",
            "Results interpretation",
            "Conclusion and next steps",
        ],
        "next_module": None,
    },
}


def create_notebook_template(filename, config):
    """Create a Jupyter notebook template."""

    cells = []

    # Title cell
    title_content = f"# {config['title']}\\n\\n"
    title_content += f"**Estimated Time**: {config['time']}\\n\\n"
    title_content += "## Learning Objectives\\n\\n"
    title_content += "By the end of this module, you will understand:\\n\\n"
    for topic in config["topics"]:
        title_content += f"- {topic}\\n"
    title_content += "\\n## Prerequisites\\n\\n"
    title_content += "- Previous modules completed\\n"
    title_content += "- Python and NumPy basics\\n\\n---"

    cells.append({"cell_type": "markdown", "metadata": {}, "source": title_content.split("\\n")})

    # Introduction cell
    intro_content = f"## 1. Introduction\\n\\n"
    intro_content += f"Welcome to {config['title']}!\\n\\n"
    intro_content += "In this module, you'll learn:\\n\\n"
    for i, topic in enumerate(config["topics"][:3], 1):
        intro_content += f"{i}. **{topic}**\\n"
    intro_content += f"\\nAnd {len(config['topics']) - 3} more important topics!"

    cells.append({"cell_type": "markdown", "metadata": {}, "source": intro_content.split("\\n")})

    # Setup cell
    cells.append(
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Import required libraries\\n",
                "import pandas as pd\\n",
                "import numpy as np\\n",
                "import matplotlib.pyplot as plt\\n",
                "import seaborn as sns\\n",
                "\\n",
                "# Set visualization defaults\\n",
                "%matplotlib inline\\n",
                "plt.style.use('default')\\n",
                "\\n",
                "print('Libraries imported successfully!')",
            ],
        }
    )

    # Content sections (placeholders)
    for i, topic in enumerate(config["topics"], 2):
        cells.append(
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"## {i}. {topic}\\n\\nContent coming soon! This section will cover:\\n- Key concepts\\n- Practical examples\\n- Hands-on exercises"
                ],
            }
        )

        cells.append(
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    f"# {topic} - Example code\\n",
                    "# TODO: Add comprehensive examples and exercises\\n",
                    "\\n",
                    "print(f'Learning about: {topic}')",
                ],
            }
        )

    # Exercises cell
    exercises_num = len(config["topics"]) + 2
    cells.append(
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"## {exercises_num}. Practice Exercises\\n\\nApply what you've learned with these hands-on exercises!"
            ],
        }
    )

    cells.append(
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Exercise 1\\n",
                "# TODO: Complete the exercises below\\n",
                "\\n",
                "# Your code here\\n",
            ],
        }
    )

    # Key takeaways cell
    takeaways_num = exercises_num + 1
    takeaway_content = f"## {takeaways_num}. Key Takeaways\\n\\n"
    takeaway_content += "Congratulations on completing this module! You've learned:\\n\\n"
    for topic in config["topics"]:
        takeaway_content += f"✓ **{topic}**\\n"

    takeaway_content += "\\n## Next Steps\\n\\n"
    if config["next_module"]:
        takeaway_content += f"**Next Module**: `{config['next_module']}`\\n\\n"
        takeaway_content += "Continue your learning journey!\\n\\n---"
    else:
        takeaway_content += "**Congratulations!** You've completed all modules!\\n\\n"
        takeaway_content += "You now have the fundamentals of data science. Keep practicing and building projects!\\n\\n"
        takeaway_content += "**Next steps**:\\n"
        takeaway_content += "- Build portfolio projects\\n"
        takeaway_content += "- Join Kaggle competitions\\n"
        takeaway_content += "- Explore advanced topics\\n"
        takeaway_content += "- Share your knowledge\\n\\n---"

    cells.append({"cell_type": "markdown", "metadata": {}, "source": takeaway_content.split("\\n")})

    # Create notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    return notebook


def main():
    """Generate all notebook templates."""
    # Get the notebooks directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    notebooks_dir = os.path.join(os.path.dirname(script_dir), "notebooks")

    print(f"Generating notebooks in: {notebooks_dir}")

    for filename, config in NOTEBOOKS.items():
        filepath = os.path.join(notebooks_dir, filename)

        # Skip if exists
        if os.path.exists(filepath):
            print(f"  Skipping {filename} (already exists)")
            continue

        # Generate notebook
        notebook = create_notebook_template(filename, config)

        # Write to file
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)

        print(f"  Created {filename}")

    print("\\nNotebook generation complete!")


if __name__ == "__main__":
    main()
