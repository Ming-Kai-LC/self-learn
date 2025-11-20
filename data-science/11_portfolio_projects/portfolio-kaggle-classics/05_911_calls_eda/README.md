# 911 Calls Exploratory Data Analysis

**Difficulty**: ⭐ Beginner
**Type**: Exploratory Data Analysis (EDA)
**Dataset**: Montgomery County 911 Calls (Kaggle)
**Estimated Time**: 15-20 hours

## Problem Statement

Emergency services need to optimize resource allocation based on call patterns. Understanding when, where, and why 911 calls occur helps emergency responders:
- Deploy resources efficiently
- Predict high-demand periods
- Identify geographic hotspots
- Plan staffing schedules
- Improve response times

**Goal**: Perform comprehensive exploratory data analysis to discover patterns and insights in 911 emergency calls.

## Business Impact

**Why This Matters**:
- **Resource Optimization**: Deploy ambulances, fire trucks, and police units where and when they're most needed
- **Staffing**: Schedule more personnel during peak hours/days
- **Budget Planning**: Allocate budgets based on service demand patterns
- **Public Safety**: Faster response times save lives
- **Policy Making**: Data-driven decisions for public safety infrastructure

**Potential Impact**:
- 10-15% improvement in response times through better resource allocation
- 20-30% reduction in overtime costs through optimized staffing
- Better coverage of high-risk areas identified through geographic analysis

## Dataset

- **Source**: Montgomery County 911 Calls (Kaggle)
- **Rows**: ~100,000+ emergency calls
- **Time Period**: Typically 2015-2020
- **Geographic Coverage**: Montgomery County, Pennsylvania

### Key Features

**Call Information**:
- `lat`: Latitude coordinate
- `lng`: Longitude coordinate
- `desc`: Description of emergency
- `zip`: Zip code
- `title`: Title/Category of call
- `timeStamp`: Date and time of call
- `twp`: Township
- `addr`: Address
- `e`: Dummy variable (always 1)

**Derived Features** (we'll create):
- `Reason`: Main category (EMS, Fire, Traffic)
- `Hour`: Hour of day (0-23)
- `Month`: Month of year
- `DayOfWeek`: Day of week
- `Date`: Just the date (no time)

## Analysis Approach

### 1. Data Understanding and Cleaning
- Load and inspect dataset structure
- Handle missing values
- Parse timestamp into datetime components
- Extract reason/category from title field
- Data type conversions

### 2. Temporal Analysis
- **Hourly patterns**: When do most calls occur during the day?
- **Daily patterns**: Which days of the week have more calls?
- **Monthly trends**: Seasonal variations in call volume
- **Yearly trends**: Overall growth or decline in calls
- **Heatmaps**: Hour vs Day of Week

### 3. Categorical Analysis
- **Call types distribution**: EMS vs Fire vs Traffic
- **Top emergency descriptions**: Most common emergencies
- **Category trends over time**: How categories vary by time

### 4. Geographic Analysis
- **Township distribution**: Which areas have most calls?
- **Zip code analysis**: Geographic hotspots
- **Mapping**: Visualize call locations on map (if possible)
- **Geographic patterns by category**: Where do different emergencies occur?

### 5. Advanced Insights
- **Correlation analysis**: Relationships between features
- **Peak periods identification**: Busiest times/days/locations
- **Anomaly detection**: Unusual spikes in calls
- **Comparative analysis**: EMS vs Fire vs Traffic patterns

## Expected Insights

### Temporal Patterns
- **Peak hours**: Likely 8 AM - 6 PM (working hours)
- **Peak days**: Weekdays vs weekends differences
- **Seasonal trends**: Summer (more outdoor accidents) vs Winter (weather-related)

### Geographic Patterns
- **Urban vs suburban**: Higher density areas = more calls
- **Specific hotspots**: Certain intersections, neighborhoods
- **Category geography**: Traffic calls on highways, EMS in residential

### Category Insights
- **EMS dominant**: Medical emergencies likely 60-70% of calls
- **Fire incidents**: Relatively rare but critical
- **Traffic**: Concentrated on major roads and peak hours

## Technologies Used

- **Python 3.8+**
- **Data Manipulation**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Datetime Handling**: datetime, pandas datetime
- **Environment**: Jupyter Notebook

## How to Run

### Prerequisites
```bash
pip install -r requirements.txt
```

### Download Dataset
Download the 911 Calls dataset from Kaggle:
https://www.kaggle.com/datasets/mchirico/montcoalert

Place `911.csv` in the project folder.

### Run the Notebook
```bash
jupyter notebook 911_calls_eda.ipynb
```

### Run Cells
Execute cells sequentially from top to bottom.

## Project Structure

```
05_911_calls_eda/
├── 911_calls_eda.ipynb  # Main analysis notebook
├── README.md             # This file
├── requirements.txt      # Python dependencies
└── 911.csv              # Dataset (download from Kaggle)
```

## Key Findings (Preview)

### Temporal Insights
- **Busiest Hour**: 3-5 PM (afternoon rush hour + school dismissal)
- **Busiest Day**: Fridays (heading into weekend activities)
- **Busiest Month**: January (winter weather, flu season)
- **Peak Period**: Weekday afternoons (3-6 PM)

### Geographic Insights
- **Top Township**: Lower Merion (population density)
- **Top Zip Codes**: Urban/suburban areas with higher population
- **EMS Hotspots**: Residential neighborhoods
- **Traffic Hotspots**: Major highways and intersections

### Category Insights
- **EMS**: 50-55% of all calls, peak during daytime
- **Traffic**: 35-40% of calls, peak during rush hours (7-9 AM, 4-6 PM)
- **Fire**: 5-10% of calls, relatively consistent throughout day

### Actionable Recommendations
1. **Staffing**: Increase staff 3-6 PM on weekdays
2. **EMS Deployment**: Focus on high-density residential areas
3. **Traffic Units**: Position near major intersections during rush hours
4. **Seasonal Prep**: Increase capacity in January (winter) and July (summer)
5. **Weekend Coverage**: Adjust for different patterns (late night calls increase)

## Visualizations Created

1. **Time Series Plots**:
   - Calls over time (overall trend)
   - Calls by month (seasonal patterns)
   - Calls by hour (daily patterns)
   - Calls by day of week

2. **Heatmaps**:
   - Hour vs Day of Week (peak periods)
   - Month vs Reason (category trends)

3. **Bar Charts**:
   - Top townships
   - Top zip codes
   - Call types distribution
   - Top emergency descriptions

4. **Comparative Analysis**:
   - Reason breakdown over time
   - Geographic distribution by category

## Skills Demonstrated

✅ **Data Cleaning**: Handling messy real-world data
✅ **DateTime Operations**: Extracting temporal features
✅ **Pandas Mastery**: Groupby, pivot tables, aggregations
✅ **Time Series Analysis**: Trends, seasonality, patterns
✅ **Data Visualization**: Multiple chart types, heatmaps
✅ **Statistical Analysis**: Distributions, correlations
✅ **Business Insights**: Translating data into recommendations
✅ **Professional Communication**: Clear, actionable findings

## Next Steps

### For Deeper Analysis
1. **Predictive Modeling**: Forecast call volume for next week/month
2. **Clustering**: Identify similar townships/time periods
3. **Anomaly Detection**: Detect unusual spikes (disasters, events)
4. **Interactive Dashboard**: Streamlit/Dash for stakeholder use
5. **Geospatial Visualization**: Folium maps with call density heatmaps

### For Portfolio
- [ ] Add geographic heat maps using Folium
- [ ] Create interactive dashboard
- [ ] Write blog post on EDA best practices
- [ ] Add statistical testing (hypothesis tests)
- [ ] Include predictive time series model

## Learning Objectives Achieved

✅ Comprehensive exploratory data analysis (EDA)
✅ Temporal feature extraction and analysis
✅ Geographic data handling and visualization
✅ Pattern discovery in time series data
✅ Multiple visualization techniques
✅ Business-focused insights and recommendations
✅ Professional documentation and presentation

## References

- [Kaggle: Montgomery County 911 Calls](https://www.kaggle.com/datasets/mchirico/montcoalert)
- Pandas documentation (datetime operations)
- Seaborn visualization gallery
- "Python for Data Analysis" by Wes McKinney

## Author

Created as part of the Data Science Portfolio Projects series.

## License

This project is for educational purposes.
