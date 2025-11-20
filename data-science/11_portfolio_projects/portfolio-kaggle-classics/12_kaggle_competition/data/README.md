# Data Directory

This directory contains all data files for the House Prices competition.

## Directory Structure

```
data/
├── raw/           # Original competition data (gitignored)
├── processed/     # Cleaned and engineered features (gitignored)
├── sample/        # Small sample data for testing (<10MB)
└── submissions/   # Submission history (gitignored)
```

## Getting the Data

### Option 1: Kaggle API (Recommended)

1. Install Kaggle API:
   ```bash
   pip install kaggle
   ```

2. Configure API credentials:
   - Go to https://www.kaggle.com/account
   - Click "Create New API Token"
   - Place `kaggle.json` in `~/.kaggle/`

3. Download competition data:
   ```bash
   kaggle competitions download -c house-prices-advanced-regression-techniques
   unzip house-prices-advanced-regression-techniques.zip -d data/raw/
   ```

### Option 2: Manual Download

1. Visit: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
2. Download the data files
3. Extract to `data/raw/` directory

## Expected Files

After downloading, you should have:

```
data/raw/
├── train.csv              # Training data (1,460 rows)
├── test.csv               # Test data (1,459 rows)
├── data_description.txt   # Feature descriptions
└── sample_submission.csv  # Submission format example
```

## Data Files Description

- **train.csv**: Training data with SalePrice target variable
- **test.csv**: Test data without SalePrice (for predictions)
- **data_description.txt**: Detailed description of all 79 features
- **sample_submission.csv**: Example submission format

## Important Notes

- Large data files are gitignored (see `.gitignore`)
- Only keep small samples (<10MB) in `sample/` directory
- Processed data should be regenerated from notebooks
- Never commit raw competition data to git
