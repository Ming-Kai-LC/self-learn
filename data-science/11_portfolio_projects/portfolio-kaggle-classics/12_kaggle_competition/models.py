"""
Model Training Utilities for House Prices Competition

This module contains utilities for training models, hyperparameter optimization,
and ensemble methods for the house prices prediction competition.

Author: Data Science Portfolio
Date: 2025-11-20
Competition: House Prices - Advanced Regression Techniques
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.ensemble import StackingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor

try:
    from catboost import CatBoostRegressor
    CATBOOST_AVAILABLE = True
except ImportError:
    CATBOOST_AVAILABLE = False

try:
    import optuna
    from optuna.samplers import TPESampler
    OPTUNA_AVAILABLE = True
except ImportError:
    OPTUNA_AVAILABLE = False

# Random seed for reproducibility
SEED = 42


def rmse(y_true, y_pred):
    """
    Calculate Root Mean Squared Error.

    Parameters:
    -----------
    y_true : array-like
        True target values
    y_pred : array-like
        Predicted target values

    Returns:
    --------
    float
        RMSE score
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))


def rmsle(y_true, y_pred):
    """
    Calculate Root Mean Squared Logarithmic Error (competition metric).

    Parameters:
    -----------
    y_true : array-like
        True target values
    y_pred : array-like
        Predicted target values

    Returns:
    --------
    float
        RMSLE score
    """
    return np.sqrt(mean_squared_error(np.log1p(y_true), np.log1p(y_pred)))


def evaluate_model(model, X, y, cv=5, scoring='neg_mean_squared_error'):
    """
    Evaluate model using cross-validation.

    Parameters:
    -----------
    model : sklearn estimator
        Model to evaluate
    X : pd.DataFrame or np.ndarray
        Feature matrix
    y : pd.Series or np.ndarray
        Target vector
    cv : int
        Number of cross-validation folds
    scoring : str
        Scoring metric

    Returns:
    --------
    tuple
        (mean_score, std_score)
    """
    kfold = KFold(n_splits=cv, shuffle=True, random_state=SEED)
    scores = cross_val_score(model, X, y, cv=kfold, scoring=scoring, n_jobs=-1)

    # Convert to RMSE if using MSE scoring
    if scoring == 'neg_mean_squared_error':
        scores = np.sqrt(-scores)

    return scores.mean(), scores.std()


def get_base_models():
    """
    Get dictionary of base regression models with default parameters.

    Returns:
    --------
    dict
        Dictionary of model name -> model instance
    """
    models = {
        'Ridge': Ridge(alpha=10, random_state=SEED),
        'Lasso': Lasso(alpha=0.0005, random_state=SEED, max_iter=10000),
        'ElasticNet': ElasticNet(
            alpha=0.001, l1_ratio=0.5, random_state=SEED, max_iter=10000
        ),
        'RandomForest': RandomForestRegressor(
            n_estimators=100, random_state=SEED, n_jobs=-1
        ),
        'GradientBoosting': GradientBoostingRegressor(
            n_estimators=500, learning_rate=0.05, random_state=SEED
        ),
        'XGBoost': XGBRegressor(
            n_estimators=500, learning_rate=0.05, random_state=SEED, n_jobs=-1
        ),
        'LightGBM': LGBMRegressor(
            n_estimators=500, learning_rate=0.05, random_state=SEED,
            n_jobs=-1, verbose=-1
        )
    }

    if CATBOOST_AVAILABLE:
        models['CatBoost'] = CatBoostRegressor(
            iterations=500, learning_rate=0.05, random_state=SEED, verbose=0
        )

    return models


def optimize_ridge_optuna(X, y, n_trials=50):
    """
    Optimize Ridge regression using Optuna.

    Parameters:
    -----------
    X : pd.DataFrame or np.ndarray
        Feature matrix
    y : pd.Series or np.ndarray
        Target vector
    n_trials : int
        Number of optimization trials

    Returns:
    --------
    dict
        Best hyperparameters
    """
    if not OPTUNA_AVAILABLE:
        print("Optuna not available. Returning default parameters.")
        return {'alpha': 10}

    def objective(trial):
        alpha = trial.suggest_loguniform('alpha', 1e-3, 1e2)
        model = Ridge(alpha=alpha, random_state=SEED)
        score, _ = evaluate_model(model, X, y, cv=5)
        return score

    study = optuna.create_study(
        direction='minimize',
        sampler=TPESampler(seed=SEED)
    )
    study.optimize(objective, n_trials=n_trials, show_progress_bar=True)

    return study.best_params


def optimize_lasso_optuna(X, y, n_trials=50):
    """
    Optimize Lasso regression using Optuna.

    Parameters:
    -----------
    X : pd.DataFrame or np.ndarray
        Feature matrix
    y : pd.Series or np.ndarray
        Target vector
    n_trials : int
        Number of optimization trials

    Returns:
    --------
    dict
        Best hyperparameters
    """
    if not OPTUNA_AVAILABLE:
        print("Optuna not available. Returning default parameters.")
        return {'alpha': 0.0005}

    def objective(trial):
        alpha = trial.suggest_loguniform('alpha', 1e-5, 1e-1)
        model = Lasso(alpha=alpha, random_state=SEED, max_iter=10000)
        score, _ = evaluate_model(model, X, y, cv=5)
        return score

    study = optuna.create_study(
        direction='minimize',
        sampler=TPESampler(seed=SEED)
    )
    study.optimize(objective, n_trials=n_trials, show_progress_bar=True)

    return study.best_params


def optimize_xgboost_optuna(X, y, n_trials=100):
    """
    Optimize XGBoost using Optuna.

    Parameters:
    -----------
    X : pd.DataFrame or np.ndarray
        Feature matrix
    y : pd.Series or np.ndarray
        Target vector
    n_trials : int
        Number of optimization trials

    Returns:
    --------
    dict
        Best hyperparameters
    """
    if not OPTUNA_AVAILABLE:
        print("Optuna not available. Returning default parameters.")
        return {
            'learning_rate': 0.05,
            'max_depth': 3,
            'n_estimators': 500
        }

    def objective(trial):
        params = {
            'learning_rate': trial.suggest_loguniform('learning_rate', 0.01, 0.3),
            'max_depth': trial.suggest_int('max_depth', 2, 10),
            'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
            'subsample': trial.suggest_uniform('subsample', 0.6, 1.0),
            'colsample_bytree': trial.suggest_uniform('colsample_bytree', 0.6, 1.0),
            'n_estimators': trial.suggest_int('n_estimators', 100, 2000),
            'random_state': SEED,
            'n_jobs': -1
        }

        model = XGBRegressor(**params)
        score, _ = evaluate_model(model, X, y, cv=5)
        return score

    study = optuna.create_study(
        direction='minimize',
        sampler=TPESampler(seed=SEED)
    )
    study.optimize(objective, n_trials=n_trials, show_progress_bar=True)

    return study.best_params


def optimize_lightgbm_optuna(X, y, n_trials=100):
    """
    Optimize LightGBM using Optuna.

    Parameters:
    -----------
    X : pd.DataFrame or np.ndarray
        Feature matrix
    y : pd.Series or np.ndarray
        Target vector
    n_trials : int
        Number of optimization trials

    Returns:
    --------
    dict
        Best hyperparameters
    """
    if not OPTUNA_AVAILABLE:
        print("Optuna not available. Returning default parameters.")
        return {
            'learning_rate': 0.05,
            'num_leaves': 31,
            'n_estimators': 500
        }

    def objective(trial):
        params = {
            'learning_rate': trial.suggest_loguniform('learning_rate', 0.01, 0.3),
            'num_leaves': trial.suggest_int('num_leaves', 20, 150),
            'min_child_samples': trial.suggest_int('min_child_samples', 5, 100),
            'subsample': trial.suggest_uniform('subsample', 0.6, 1.0),
            'colsample_bytree': trial.suggest_uniform('colsample_bytree', 0.6, 1.0),
            'n_estimators': trial.suggest_int('n_estimators', 100, 2000),
            'random_state': SEED,
            'n_jobs': -1,
            'verbose': -1
        }

        model = LGBMRegressor(**params)
        score, _ = evaluate_model(model, X, y, cv=5)
        return score

    study = optuna.create_study(
        direction='minimize',
        sampler=TPESampler(seed=SEED)
    )
    study.optimize(objective, n_trials=n_trials, show_progress_bar=True)

    return study.best_params


def create_stacking_ensemble(X, y, base_models=None, meta_learner=None, cv=5):
    """
    Create and train a stacking ensemble.

    Parameters:
    -----------
    X : pd.DataFrame or np.ndarray
        Feature matrix
    y : pd.Series or np.ndarray
        Target vector
    base_models : list of tuples
        List of (name, model) tuples for base models
    meta_learner : sklearn estimator
        Meta-learner model
    cv : int
        Number of cross-validation folds

    Returns:
    --------
    StackingRegressor
        Trained stacking ensemble
    """
    if base_models is None:
        base_models = [
            ('ridge', Ridge(alpha=10, random_state=SEED)),
            ('lasso', Lasso(alpha=0.0005, random_state=SEED, max_iter=10000)),
            ('elastic', ElasticNet(
                alpha=0.001, l1_ratio=0.5, random_state=SEED, max_iter=10000
            ))
        ]

    if meta_learner is None:
        meta_learner = Ridge(alpha=1.0, random_state=SEED)

    stacking_model = StackingRegressor(
        estimators=base_models,
        final_estimator=meta_learner,
        cv=cv,
        n_jobs=-1
    )

    stacking_model.fit(X, y)
    return stacking_model


def weighted_average_predictions(predictions_dict, weights=None):
    """
    Create weighted average of multiple predictions.

    Parameters:
    -----------
    predictions_dict : dict
        Dictionary of model_name -> predictions
    weights : list or None
        Weights for each model (must sum to 1)
        If None, uses equal weights

    Returns:
    --------
    np.ndarray
        Weighted average predictions
    """
    predictions_array = np.array(list(predictions_dict.values()))

    if weights is None:
        weights = np.ones(len(predictions_dict)) / len(predictions_dict)
    else:
        weights = np.array(weights)
        assert abs(weights.sum() - 1.0) < 1e-6, "Weights must sum to 1"

    weighted_preds = np.average(predictions_array, axis=0, weights=weights)
    return weighted_preds


def blend_predictions(models_dict, X_train, y_train, X_val, blend_weights=None):
    """
    Blend predictions from multiple models using holdout validation.

    Parameters:
    -----------
    models_dict : dict
        Dictionary of model_name -> trained model
    X_train : pd.DataFrame or np.ndarray
        Training features
    y_train : pd.Series or np.ndarray
        Training target
    X_val : pd.DataFrame or np.ndarray
        Validation features
    blend_weights : list or None
        Blending weights (if None, optimizes automatically)

    Returns:
    --------
    np.ndarray
        Blended predictions
    """
    # Get validation predictions
    val_predictions = {}
    for name, model in models_dict.items():
        model.fit(X_train, y_train)
        val_predictions[name] = model.predict(X_val)

    # Use weighted average
    blended = weighted_average_predictions(val_predictions, weights=blend_weights)
    return blended


def train_and_evaluate_all(X, y, cv=5):
    """
    Train and evaluate all base models.

    Parameters:
    -----------
    X : pd.DataFrame or np.ndarray
        Feature matrix
    y : pd.Series or np.ndarray
        Target vector
    cv : int
        Number of cross-validation folds

    Returns:
    --------
    pd.DataFrame
        Results dataframe with model names and scores
    """
    models = get_base_models()
    results = {}

    print("Training and Evaluating Base Models...")
    print("=" * 60)

    for name, model in models.items():
        print(f"\nEvaluating {name}...")
        mean_score, std_score = evaluate_model(model, X, y, cv=cv)
        results[name] = {'mean': mean_score, 'std': std_score}
        print(f"  CV RMSE: {mean_score:.4f} (+/- {std_score:.4f})")

    results_df = pd.DataFrame(results).T
    results_df = results_df.sort_values('mean')

    return results_df


# Example usage
if __name__ == "__main__":
    print("Model Training Utilities Loaded")
    print("=" * 60)
    print("\nAvailable functions:")
    print("  - get_base_models()")
    print("  - evaluate_model(model, X, y, cv=5)")
    print("  - train_and_evaluate_all(X, y, cv=5)")
    print("\nHyperparameter Optimization:")
    print("  - optimize_ridge_optuna(X, y, n_trials=50)")
    print("  - optimize_lasso_optuna(X, y, n_trials=50)")
    print("  - optimize_xgboost_optuna(X, y, n_trials=100)")
    print("  - optimize_lightgbm_optuna(X, y, n_trials=100)")
    print("\nEnsemble Methods:")
    print("  - create_stacking_ensemble(X, y, base_models, meta_learner)")
    print("  - weighted_average_predictions(predictions_dict, weights)")
    print("  - blend_predictions(models_dict, X_train, y_train, X_val)")
    print("\nMetrics:")
    print("  - rmse(y_true, y_pred)")
    print("  - rmsle(y_true, y_pred)")
    print("\nUsage:")
    print("  from models import train_and_evaluate_all")
    print("  results = train_and_evaluate_all(X_train, y_train)")

    # Check optional dependencies
    print("\n" + "=" * 60)
    print("Optional Dependencies:")
    print(f"  Optuna: {'✓ Available' if OPTUNA_AVAILABLE else '✗ Not installed'}")
    print(f"  CatBoost: {'✓ Available' if CATBOOST_AVAILABLE else '✗ Not installed'}")
