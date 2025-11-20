# MovieLens Dataset

This directory should contain the MovieLens dataset for the recommendation system project.

## Download Instructions

### Option 1: MovieLens 100K (Recommended for Learning)

1. **Visit**: https://grouplens.org/datasets/movielens/100k/
2. **Download**: `ml-100k.zip`
3. **Extract** the contents to `ml-100k/` directory in this folder

**Expected structure after extraction**:
```
data/
└── ml-100k/
    ├── u.data          # Ratings data (user_id, movie_id, rating, timestamp)
    ├── u.item          # Movie information (movie_id, title, genres)
    ├── u.user          # User demographics (user_id, age, gender, occupation)
    └── ... (other files)
```

### Option 2: MovieLens 1M (For Advanced Analysis)

1. **Visit**: https://grouplens.org/datasets/movielens/1m/
2. **Download**: `ml-1m.zip`
3. **Extract** the contents to `ml-1m/` directory in this folder

**Expected structure after extraction**:
```
data/
└── ml-1m/
    ├── ratings.dat     # Ratings data
    ├── movies.dat      # Movie information
    ├── users.dat       # User demographics
    └── README
```

## Quick Download via Command Line

### For Linux/Mac:

```bash
# Download MovieLens 100K
wget https://files.grouplens.org/datasets/movielens/ml-100k.zip

# Extract to correct location
unzip ml-100k.zip -d data/

# Clean up
rm ml-100k.zip
```

### For Windows (PowerShell):

```powershell
# Download MovieLens 100K
Invoke-WebRequest -Uri "https://files.grouplens.org/datasets/movielens/ml-100k.zip" -OutFile "ml-100k.zip"

# Extract (requires PowerShell 5.0+)
Expand-Archive -Path "ml-100k.zip" -DestinationPath "data/"

# Clean up
Remove-Item "ml-100k.zip"
```

## Dataset Information

### MovieLens 100K
- **Size**: ~5 MB
- **Ratings**: 100,000 ratings
- **Users**: 943 users
- **Movies**: 1,682 movies
- **Rating Scale**: 1-5 stars
- **Time Period**: September 1997 - April 1998

### MovieLens 1M
- **Size**: ~24 MB
- **Ratings**: 1,000,209 ratings
- **Users**: 6,040 users
- **Movies**: 3,706 movies
- **Rating Scale**: 1-5 stars
- **Time Period**: April 2000 - February 2003

## License

MovieLens datasets are provided by GroupLens Research at the University of Minnesota.

**Citation**:
> F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872

**License**: These datasets are made available for educational and research purposes. Please refer to the official MovieLens website for full license terms.

## Troubleshooting

**Issue**: "Dataset not found" error when running notebook

**Solution**:
1. Verify the dataset is extracted to the correct location
2. Check that the directory structure matches the expected format above
3. Ensure file names match exactly (case-sensitive on Linux/Mac)

**Issue**: Download link not working

**Solution**:
1. Visit the official GroupLens website: https://grouplens.org/datasets/movielens/
2. Navigate to the appropriate dataset version
3. Download manually and extract to this directory

## Note

The actual dataset files are **NOT** included in this repository due to size constraints and licensing. You must download them separately using the instructions above.
