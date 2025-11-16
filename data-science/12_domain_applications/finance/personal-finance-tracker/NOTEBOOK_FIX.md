# Quick Fix for Notebook JSON Export

## Issue
The `export_to_json()` function in the notebook uses `date_format='iso'` parameter which may not be available in all pandas versions.

## Solution

Find the cell containing the `export_to_json()` function and replace this section:

### ❌ Replace This:
```python
def export_to_json(expenses_df, income_df, budgets_dict, filename='financial_data.json'):
    """
    Export all financial data to JSON for backup/portability.
    """
    try:
        data = {
            'expenses': expenses_df.to_dict(orient='records', date_format='iso'),
            'income': income_df.to_dict(orient='records', date_format='iso'),
            'budgets': budgets_dict,
            'recurring': recurring_transactions,
            'export_date': datetime.now().isoformat()
        }
```

### ✅ With This:
```python
def export_to_json(expenses_df, income_df, budgets_dict, filename='financial_data.json'):
    """
    Export all financial data to JSON for backup/portability.
    """
    try:
        # Convert dates to ISO format strings for JSON compatibility
        expenses_export = expenses_df.copy()
        expenses_export['date'] = expenses_export['date'].dt.strftime('%Y-%m-%d')

        income_export = income_df.copy()
        income_export['date'] = income_export['date'].dt.strftime('%Y-%m-%d')

        data = {
            'expenses': expenses_export.to_dict(orient='records'),
            'income': income_export.to_dict(orient='records'),
            'budgets': budgets_dict,
            'recurring': recurring_transactions,
            'export_date': datetime.now().isoformat()
        }
```

## Why This Fix?

The `date_format='iso'` parameter was added in newer pandas versions. The manual conversion using `dt.strftime()` works across all pandas versions and produces the same ISO format output.

## When to Apply This Fix?

Only if you encounter an error like:
```
TypeError: to_dict() got an unexpected keyword argument 'date_format'
```

Otherwise, the notebook works fine as-is!
