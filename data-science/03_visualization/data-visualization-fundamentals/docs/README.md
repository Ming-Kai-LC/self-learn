# Data Visualization Fundamentals - Documentation

This directory contains additional documentation and resources for the Data Visualization Fundamentals project.

## Contents

- **This File**: Documentation index and quick reference
- **Learning Resources**: Additional materials and references
- **Troubleshooting Guide**: Solutions to common issues
- **Quick Reference**: Cheat sheets and syntax guides

---

## Quick Start Guide

### 1. Installation
```bash
# Navigate to project directory
cd projects/data-visualization-fundamentals

# Install dependencies
pip install -r requirements.txt

# Generate sample datasets
python scripts/download_datasets.py
```

### 2. Launch Jupyter
```bash
jupyter notebook
```

### 3. Start Learning
Open `notebooks/00_setup_introduction.ipynb` and begin your journey!

---

## Module Overview

| Module | Title | Time | Difficulty | Focus |
|--------|-------|------|------------|-------|
| 00 | Setup & Introduction | 45 min | Beginner | Environment setup, library overview |
| 01 | Matplotlib Fundamentals | 90 min | Beginner | Line, scatter, bar, histogram plots |
| 02 | Customizing Plots | 90 min | Beginner | Colors, styles, subplots, annotations |
| 03 | Seaborn Statistical Viz | 90 min | Beginner-Int | Distributions, relationships, statistics |
| 04 | Time Series Visualization | 90 min | Intermediate | Temporal data, trends, seasonality |
| 05 | Interactive Plotly | 90 min | Intermediate | Interactive charts, animations, dashboards |
| 06 | Scientific Best Practices | 60 min | Intermediate | Publication quality, accessibility |
| 07 | Capstone Project | 120 min | Intermediate | Complete end-to-end analysis |

**Total Time**: 8-12 hours

---

## Quick Reference Cheat Sheets

### Matplotlib Essentials

```python
import matplotlib.pyplot as plt

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot types
ax.plot(x, y)                    # Line plot
ax.scatter(x, y)                 # Scatter plot
ax.bar(categories, values)       # Bar chart
ax.hist(data, bins=30)           # Histogram

# Customization
ax.set_title('Title')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.legend()
ax.grid(True)

# Save figure
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

### Seaborn Quick Commands

```python
import seaborn as sns

# Distribution plots
sns.histplot(data, x='column')
sns.kdeplot(data, x='column')
sns.violinplot(data, x='category', y='value')

# Categorical plots
sns.boxplot(data, x='category', y='value')
sns.barplot(data, x='category', y='value')

# Relationship plots
sns.scatterplot(data, x='var1', y='var2')
sns.regplot(data, x='var1', y='var2')

# Multi-plot grids
sns.pairplot(data)
sns.heatmap(correlation_matrix, annot=True)
```

### Plotly Express Basics

```python
import plotly.express as px

# Interactive plots
fig = px.line(df, x='date', y='value', title='Title')
fig = px.scatter(df, x='x', y='y', color='category')
fig = px.bar(df, x='category', y='value')

# Show plot
fig.show()

# Save to HTML
fig.write_html('plot.html')
```

---

## Choosing the Right Chart Type

### Comparison
- **Bar Chart**: Comparing quantities across categories
- **Grouped Bar Chart**: Comparing multiple series across categories
- **Horizontal Bar Chart**: When category names are long

### Distribution
- **Histogram**: Single variable distribution
- **Box Plot**: Distribution with quartiles and outliers
- **Violin Plot**: Distribution with density
- **KDE Plot**: Smooth distribution estimate

### Relationship
- **Scatter Plot**: Relationship between two continuous variables
- **Line Plot**: Trend over continuous variable (often time)
- **Regression Plot**: Relationship with fitted line

### Part-to-Whole
- **Stacked Bar Chart**: Components of a total
- **Area Chart**: Cumulative totals over time
- **Pie Chart**: Use sparingly, only for simple proportions

### Time Series
- **Line Plot**: Trends over time
- **Area Chart**: Cumulative or filled regions
- **Heatmap**: Time on one axis, categories on another

---

## Color Palettes Reference

### Matplotlib Named Colors
- Basic: 'red', 'blue', 'green', 'orange', 'purple'
- Extended: 'steelblue', 'coral', 'crimson', 'darkgreen'
- Grayscale: 'black', 'gray', 'silver', 'white'

### Colormaps (Sequential)
- 'viridis' - Default, colorblind-friendly
- 'plasma', 'inferno', 'magma' - Perceptually uniform
- 'Blues', 'Greens', 'Reds' - Single hue

### Colormaps (Diverging)
- 'RdBu' - Red to Blue (temperature, correlations)
- 'RdYlGn' - Red-Yellow-Green (bad-neutral-good)
- 'coolwarm' - Cool to warm

### Seaborn Palettes
```python
sns.set_palette('deep')        # Default
sns.set_palette('pastel')      # Light colors
sns.set_palette('colorblind')  # Colorblind-safe
```

---

## Common Issues and Solutions

### Issue: Plots not displaying in Jupyter
**Solution**: Add `%matplotlib inline` to first code cell

### Issue: Figures look pixelated
**Solution**: Save with higher DPI: `plt.savefig('plot.png', dpi=300)`

### Issue: Text overlapping in plots
**Solution**: Use `plt.tight_layout()` before saving/showing

### Issue: Legend covering data
**Solution**: Change legend location: `ax.legend(loc='upper right')` or `loc='best'`

### Issue: Import errors
**Solution**: Verify installation: `pip install -r requirements.txt --upgrade`

### Issue: Jupyter kernel crashes
**Solution**:
1. Restart kernel: Kernel → Restart
2. Clear outputs: Cell → All Output → Clear
3. Check memory usage

---

## File Format Guide

### When to Use Each Format

**PNG** (Raster)
- ✓ Presentations, web, general use
- ✓ Universal support
- ✗ Can pixelate when scaled
- Recommended DPI: 300

**PDF** (Vector)
- ✓ Academic papers, print
- ✓ Scalable without quality loss
- ✗ Larger file sizes
- Best for: Publications

**SVG** (Vector)
- ✓ Web graphics, design tools
- ✓ Editable in vector software
- ✗ Limited software support
- Best for: Web embedding

**JPG** (Raster)
- ✗ Not recommended for plots
- Compression artifacts on charts

---

## Keyboard Shortcuts (Jupyter)

### Navigation
- `Esc` - Enter command mode
- `Enter` - Enter edit mode
- `A` - Insert cell above
- `B` - Insert cell below
- `DD` - Delete cell
- `Z` - Undo delete

### Execution
- `Shift + Enter` - Run cell and move to next
- `Ctrl + Enter` - Run cell and stay
- `Alt + Enter` - Run cell and insert below

### Editing
- `M` - Change to markdown
- `Y` - Change to code
- `Ctrl + S` - Save notebook

---

## Dataset Descriptions

### stock_prices.csv
- **Size**: 366 days × 5 stocks
- **Columns**: Date (index), TECH, FINANCE, ENERGY, HEALTH, RETAIL
- **Use**: Time series visualization, financial analysis
- **Module**: 04, 07

### climate_data.csv
- **Size**: 408 months (1990-2024)
- **Columns**: Date, Temperature_C, CO2_ppm, SeaLevel_mm
- **Use**: Time series, trends, correlations
- **Module**: 04, 06, 07

### sales_data.csv
- **Size**: 365 days × 4 products × 4 regions
- **Columns**: Date, Product, Region, Units_Sold, Revenue
- **Use**: Categorical analysis, business intelligence
- **Module**: 01, 02, 03

### survey_data.csv
- **Size**: 500 responses
- **Columns**: Age_Group, Education, Income, Satisfaction, Hours_Per_Week, Recommend
- **Use**: Statistical visualization, distributions
- **Module**: 03, 06

### experiment_data.csv
- **Size**: 300 measurements (3 groups)
- **Columns**: Group, Measurement
- **Use**: Scientific plots, statistical comparisons
- **Module**: 03, 06

### correlation_data.csv
- **Size**: 200 samples × 5 variables
- **Columns**: Variable_1 through Variable_5
- **Use**: Correlation analysis, pair plots
- **Module**: 03, 06

---

## Additional Learning Resources

### Official Documentation
- [Matplotlib Docs](https://matplotlib.org/stable/contents.html)
- [Seaborn Docs](https://seaborn.pydata.org/)
- [Plotly Python Docs](https://plotly.com/python/)
- [Pandas Visualization](https://pandas.pydata.org/docs/user_guide/visualization.html)

### Books
- **"Storytelling with Data"** by Cole Nussbaumer Knaflic
- **"The Visual Display of Quantitative Information"** by Edward Tufte
- **"Fundamentals of Data Visualization"** by Claus O. Wilke

### Online Galleries
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Example Gallery](https://seaborn.pydata.org/examples/index.html)
- [Plotly Chart Studio](https://plotly.com/chart-studio/)
- [Python Graph Gallery](https://python-graph-gallery.com/)

### Inspiration
- [r/dataisbeautiful](https://reddit.com/r/dataisbeautiful)
- [Information is Beautiful](https://informationisbeautiful.net/)
- [FlowingData](https://flowingdata.com/)
- [The Pudding](https://pudding.cool/)

---

## Project Structure Explained

```
data-visualization-fundamentals/
│
├── README.md                    # Main project documentation
├── requirements.txt             # Python package dependencies
│
├── notebooks/                   # All learning modules
│   ├── 00_*.ipynb              # Module files (00-07)
│   └── outputs/                # Generated plots and figures
│
├── data/                        # Sample datasets (generated)
│   ├── .gitkeep
│   └── *.csv                   # Various sample datasets
│
├── scripts/                     # Utility scripts
│   └── download_datasets.py    # Generate sample data
│
└── docs/                        # Additional documentation
    └── README.md               # This file
```

---

## Contributing

Want to improve this project?

1. **Report Issues**: Found a bug or typo? Open an issue
2. **Suggest Improvements**: Have ideas for better examples?
3. **Add Examples**: Created a great visualization? Share it!
4. **Fix Errors**: Submit a pull request with corrections

---

## Support

### Getting Help
1. **Check documentation**: README.md and this file
2. **Review troubleshooting**: See "Common Issues" above
3. **Search online**: Stack Overflow, documentation sites
4. **Ask community**: Post in relevant forums

### Useful Communities
- Stack Overflow ([matplotlib tag](https://stackoverflow.com/questions/tagged/matplotlib))
- [Matplotlib Discourse](https://discourse.matplotlib.org/)
- Reddit: r/datascience, r/python, r/learnpython

---

## Version History

**v1.0** (Current)
- Initial release with 8 complete modules
- Coverage of Matplotlib, Seaborn, and Plotly
- Focus on scientific/statistical visualization and time series
- Beginner-friendly with comprehensive examples
- 8-12 hours of learning content

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Happy Visualizing!** 📊📈📉

Remember: The goal is not just to make plots, but to communicate insights effectively. Choose clarity over complexity, and always consider your audience.
