# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python learning repository focused on data science, machine learning (ML), and deep learning (DL). The code is organized into four main directories:

| Directory | Purpose |
|-----------|---------|
| `machine learning/` | Jupyter notebooks for ML concepts (scikit-learn, regression, classification, pipelines) |
| `deep learning/` | Jupyter notebooks for DL concepts (Keras/TensorFlow, neural networks) |
| `pyhton/pandas/` | Pandas exercises and examples (data manipulation, cleaning, analysis) |
| `pyhton/visualizzazione/` | Data visualization examples (matplotlib, seaborn) |
| `dati/` | Dataset notebooks (California housing analysis, data preprocessing pipelines) |

## Key Technologies

- **Python**: Primary language
- **TensorFlow/Keras**: Deep learning framework (requires Python 3.12 or earlier)
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation and analysis
- **matplotlib/seaborn**: Data visualization

## Important Notes

### Deep Learning Notebook Constraints

The notebooks in `deep learning/` contain this critical constraint:
```
ATTENZIONE TENSORFLOW FUNZIONA FINO A PYTHON 3.12
python: select interpreter - python 3.12 ecc
```

When working with these notebooks, ensure Python 3.12 or earlier is used as the interpreter.

### Common ML/DL Patterns Observed

1. **Data workflow**: Load data → Split (train_test_split) → Train model → Evaluate → Predict
2. **Outlier removal**: Z-score method with threshold of 3 is commonly used
3. **Model evaluation**: Accuracy for classification, MSE for regression tasks
4. **Visualization**: Matplotlib for basic plots, seaborn for statistical visualizations (heatmaps, regression plots)

## File Conventions

- All notebooks are `.ipynb` format
- Python scripts are `.py` format in the `pyhton/` directory
- Dataset files: `.csv` format (e.g., `dataset.csv`, `100 Sales Records.csv`, `train.csv`)
- Notebooks contain Italian comments and explanations

## Development Setup

To work with this codebase:

```bash
# Install required packages
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow keras

# Run Jupyter notebooks
jupyter notebook
```

## Notebook Execution

Notebooks should be executed cell-by-cell in order. Some notebooks depend on variables created in previous cells (e.g., `Esempio_ML.ipynb` uses training variables for visualization).

## Notable Notebooks

| File | Description |
|------|-------------|
| `machine learning/Esempio_ML.ipynb` | Basic ML examples: RandomForest, LinearRegression, LogisticRegression |
| `deep learning/DL_pipeline.ipynb` | Functional Keras model creation and compilation |
| `pyhton/pandas/Esempi_pandas.py` | Pandas pivot_table, groupby, merge operations |
| `dati/analisi_california.ipynb` | California housing dataset analysis |
