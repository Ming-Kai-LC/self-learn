"""
Feature Engineering Utilities for House Prices Competition

This module contains reusable feature engineering functions that can be applied
to the house prices dataset. All functions are designed to work with both
training and test sets consistently.

Author: Data Science Portfolio
Date: 2025-11-20
Competition: House Prices - Advanced Regression Techniques
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy.stats import skew


def handle_missing_values(df):
    """
    Handle missing values in the dataset.

    Strategy:
    - Features where NA means "None" or "Absent" → fill with 'None'
    - Features where NA means 0 → fill with 0
    - LotFrontage → fill with median by neighborhood
    - Others → fill with mode/median

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with missing values

    Returns:
    --------
    pd.DataFrame
        Dataframe with missing values handled
    """
    df = df.copy()

    # Features where NA means "None" or "Absent"
    none_features = [
        'PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu',
        'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
        'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
        'MasVnrType'
    ]

    for feature in none_features:
        if feature in df.columns:
            df[feature] = df[feature].fillna('None')

    # Features where NA means 0
    zero_features = [
        'GarageYrBlt', 'GarageArea', 'GarageCars',
        'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
        'BsmtFullBath', 'BsmtHalfBath', 'MasVnrArea'
    ]

    for feature in zero_features:
        if feature in df.columns:
            df[feature] = df[feature].fillna(0)

    # LotFrontage: Fill with median by neighborhood
    if 'LotFrontage' in df.columns and 'Neighborhood' in df.columns:
        df['LotFrontage'] = df.groupby('Neighborhood')['LotFrontage'].transform(
            lambda x: x.fillna(x.median())
        )

    # Remaining features: Fill with mode (categorical) or median (numerical)
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna(df[col].median())

    return df


def encode_ordinal_features(df):
    """
    Encode ordinal categorical features with meaningful order.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    pd.DataFrame
        Dataframe with ordinal features encoded
    """
    df = df.copy()

    # Quality mappings
    quality_map = {'None': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}
    basement_finish_map = {
        'None': 0, 'Unf': 1, 'LwQ': 2, 'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ': 6
    }
    garage_finish_map = {'None': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3}
    exposure_map = {'None': 0, 'No': 1, 'Mn': 2, 'Av': 3, 'Gd': 4}

    # Apply ordinal encoding
    ordinal_mappings = {
        'ExterQual': quality_map,
        'ExterCond': quality_map,
        'BsmtQual': quality_map,
        'BsmtCond': quality_map,
        'HeatingQC': quality_map,
        'KitchenQual': quality_map,
        'FireplaceQu': quality_map,
        'GarageQual': quality_map,
        'GarageCond': quality_map,
        'PoolQC': quality_map,
        'BsmtFinType1': basement_finish_map,
        'BsmtFinType2': basement_finish_map,
        'GarageFinish': garage_finish_map,
        'BsmtExposure': exposure_map
    }

    for feature, mapping in ordinal_mappings.items():
        if feature in df.columns:
            df[feature] = df[feature].map(mapping)

    return df


def create_area_features(df):
    """
    Create area-based engineered features.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    pd.DataFrame
        Dataframe with new area features
    """
    df = df.copy()

    # Total square footage
    if all(col in df.columns for col in ['TotalBsmtSF', '1stFlrSF', '2ndFlrSF']):
        df['TotalSF'] = df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF']

    # Total bathrooms
    if all(col in df.columns for col in ['FullBath', 'BsmtFullBath', 'HalfBath', 'BsmtHalfBath']):
        df['TotalBathrooms'] = (
            df['FullBath'] +
            df['BsmtFullBath'] +
            0.5 * df['HalfBath'] +
            0.5 * df['BsmtHalfBath']
        )

    # Total porch area
    porch_cols = ['OpenPorchSF', '3SsnPorch', 'EnclosedPorch', 'ScreenPorch', 'WoodDeckSF']
    if all(col in df.columns for col in porch_cols):
        df['TotalPorchSF'] = df[porch_cols].sum(axis=1)

    return df


def create_binary_features(df):
    """
    Create binary indicator features.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    pd.DataFrame
        Dataframe with binary features
    """
    df = df.copy()

    # Binary indicators
    if 'PoolArea' in df.columns:
        df['HasPool'] = (df['PoolArea'] > 0).astype(int)

    if '2ndFlrSF' in df.columns:
        df['Has2ndFloor'] = (df['2ndFlrSF'] > 0).astype(int)

    if 'GarageArea' in df.columns:
        df['HasGarage'] = (df['GarageArea'] > 0).astype(int)

    if 'TotalBsmtSF' in df.columns:
        df['HasBsmt'] = (df['TotalBsmtSF'] > 0).astype(int)

    if 'Fireplaces' in df.columns:
        df['HasFireplace'] = (df['Fireplaces'] > 0).astype(int)

    return df


def create_age_features(df):
    """
    Create age-related features.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    pd.DataFrame
        Dataframe with age features
    """
    df = df.copy()

    # House age
    if all(col in df.columns for col in ['YrSold', 'YearBuilt']):
        df['HouseAge'] = df['YrSold'] - df['YearBuilt']

    # Remodel age
    if all(col in df.columns for col in ['YrSold', 'YearRemodAdd']):
        df['RemodAge'] = df['YrSold'] - df['YearRemodAdd']

    # Is new house
    if all(col in df.columns for col in ['YrSold', 'YearBuilt']):
        df['IsNew'] = (df['YrSold'] == df['YearBuilt']).astype(int)

    # Time since remodel
    if all(col in df.columns for col in ['YearRemodAdd', 'YearBuilt']):
        df['TimeSinceRemodel'] = df['YearRemodAdd'] - df['YearBuilt']

    return df


def create_quality_features(df):
    """
    Create quality-based aggregated features.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    pd.DataFrame
        Dataframe with quality features
    """
    df = df.copy()

    # Overall score
    if all(col in df.columns for col in ['OverallQual', 'OverallCond']):
        df['OverallScore'] = df['OverallQual'] * df['OverallCond']

    # Exterior score
    if all(col in df.columns for col in ['ExterQual', 'ExterCond']):
        df['ExteriorScore'] = (df['ExterQual'] + df['ExterCond']) / 2

    return df


def create_interaction_features(df):
    """
    Create interaction features between important variables.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    pd.DataFrame
        Dataframe with interaction features
    """
    df = df.copy()

    # Quality x Living Area
    if all(col in df.columns for col in ['OverallQual', 'GrLivArea']):
        df['QualGrLiv'] = df['OverallQual'] * df['GrLivArea']

    # Garage Area x Quality
    if all(col in df.columns for col in ['GarageArea', 'GarageQual']):
        df['GarageScore'] = df['GarageArea'] * df['GarageQual']

    # Basement Area x Quality
    if all(col in df.columns for col in ['BsmtFinSF1', 'BsmtQual']):
        df['BsmtFinScore'] = df['BsmtFinSF1'] * df['BsmtQual']

    # Total SF x Quality
    if all(col in df.columns for col in ['TotalSF', 'OverallQual']):
        df['TotalSFQual'] = df['TotalSF'] * df['OverallQual']

    return df


def create_ratio_features(df):
    """
    Create ratio-based features.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe

    Returns:
    --------
    pd.DataFrame
        Dataframe with ratio features
    """
    df = df.copy()

    # Rooms per square foot
    if all(col in df.columns for col in ['TotRmsAbvGrd', 'GrLivArea']):
        df['RoomsPerSF'] = df['TotRmsAbvGrd'] / (df['GrLivArea'] + 1)

    # Bedroom ratio
    if all(col in df.columns for col in ['BedroomAbvGr', 'TotRmsAbvGrd']):
        df['BedroomRatio'] = df['BedroomAbvGr'] / (df['TotRmsAbvGrd'] + 1)

    # Basement ratio
    if all(col in df.columns for col in ['TotalBsmtSF', 'GrLivArea']):
        df['BsmtRatio'] = df['TotalBsmtSF'] / (df['GrLivArea'] + 1)

    # Garage ratio
    if all(col in df.columns for col in ['GarageArea', 'GrLivArea']):
        df['GarageRatio'] = df['GarageArea'] / (df['GrLivArea'] + 1)

    return df


def fix_skewness(df, threshold=0.75):
    """
    Apply log transformation to highly skewed numerical features.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    threshold : float
        Skewness threshold for transformation

    Returns:
    --------
    pd.DataFrame
        Dataframe with skewed features transformed
    """
    df = df.copy()

    # Get numerical features
    numeric_features = df.select_dtypes(include=[np.number]).columns

    # Calculate skewness
    skewness = df[numeric_features].apply(lambda x: skew(x.dropna()))

    # Features with high skewness
    high_skew_features = skewness[abs(skewness) > threshold].index

    # Apply log1p transformation
    for feature in high_skew_features:
        df[feature] = np.log1p(df[feature])

    return df


def engineer_all_features(df):
    """
    Apply all feature engineering steps in sequence.

    This is the main function to use for end-to-end feature engineering.

    Parameters:
    -----------
    df : pd.DataFrame
        Raw input dataframe

    Returns:
    --------
    pd.DataFrame
        Fully engineered dataframe
    """
    # Step 1: Handle missing values
    df = handle_missing_values(df)

    # Step 2: Encode ordinal features
    df = encode_ordinal_features(df)

    # Step 3: Create area features
    df = create_area_features(df)

    # Step 4: Create binary features
    df = create_binary_features(df)

    # Step 5: Create age features
    df = create_age_features(df)

    # Step 6: Create quality features
    df = create_quality_features(df)

    # Step 7: Create interaction features
    df = create_interaction_features(df)

    # Step 8: Create ratio features
    df = create_ratio_features(df)

    # Step 9: One-hot encode remaining categorical features
    categorical_features = df.select_dtypes(include=['object']).columns.tolist()
    if categorical_features:
        df = pd.get_dummies(df, columns=categorical_features, drop_first=True)

    # Step 10: Fix skewness
    df = fix_skewness(df, threshold=0.75)

    return df


def remove_outliers(df, target_col='SalePrice'):
    """
    Remove outliers based on domain knowledge.

    Specific to House Prices dataset:
    - Remove houses with GrLivArea > 4000 and low SalePrice

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    target_col : str
        Name of target column

    Returns:
    --------
    pd.DataFrame
        Dataframe with outliers removed
    """
    df = df.copy()

    # Remove specific outliers identified in EDA
    if all(col in df.columns for col in ['GrLivArea', target_col]):
        mask = ~((df['GrLivArea'] > 4000) & (df[target_col] < 300000))
        df = df[mask]

    return df


# Example usage
if __name__ == "__main__":
    print("Feature Engineering Utilities Loaded")
    print("=" * 60)
    print("\nAvailable functions:")
    print("  - handle_missing_values(df)")
    print("  - encode_ordinal_features(df)")
    print("  - create_area_features(df)")
    print("  - create_binary_features(df)")
    print("  - create_age_features(df)")
    print("  - create_quality_features(df)")
    print("  - create_interaction_features(df)")
    print("  - create_ratio_features(df)")
    print("  - fix_skewness(df)")
    print("  - engineer_all_features(df)  [Applies all steps]")
    print("  - remove_outliers(df)")
    print("\nUsage:")
    print("  from feature_engineering import engineer_all_features")
    print("  df_engineered = engineer_all_features(df)")
