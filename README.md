# Bank Customer Churn Prediction

A machine-learning project that predicts whether a bank customer is likely to leave the bank. The project includes exploratory data analysis, feature preprocessing, class-imbalance handling, model training, saved inference artifacts, and an in-progress FastAPI service.

## Project overview

The model uses customer attributes such as credit score, geography, gender, age, account balance, product count, activity status, and estimated salary. The target column is `Exited`:

- `0`: the customer stayed
- `1`: the customer left

The training notebook compares logistic regression and random forest classifiers. It evaluates them using the F1 score and uses SMOTE to investigate the effect of class balancing.

## Project structure

```text
.
|-- artifacts/
|   |-- forest_tuned.pkl       # Trained random forest model
|   `-- preporcessor.pkl       # Fitted preprocessing pipeline
|-- dataset/
|   `-- churn-data.csv         # Bank customer churn dataset
|-- notebooks/
|   `-- notebook.ipynb         # EDA, preprocessing, training, and evaluation
|-- src/
|   |-- config.py              # Environment settings and artifact loading
|   |-- inferennce.py          # Prediction helper
|   `-- request.py             # Pydantic input schema
|-- .env.example               # Example environment configuration
|-- main.py                    # FastAPI application scaffold
|-- requirments.txt            # Python dependencies
`-- README.md
```

## Dataset features

| Feature | Description |
|---|---|
| `CreditScore` | Customer credit score |
| `Geography` | France, Germany, or Spain |
| `Gender` | Male or Female |
| `Age` | Customer age |
| `Tenure` | Number of years as a customer |
| `Balance` | Account balance |
| `NumOfProducts` | Number of bank products used |
| `HasCrCard` | Whether the customer has a credit card |
| `IsActiveMember` | Whether the customer is active |
| `EstimatedSalary` | Estimated annual salary |
| `Exited` | Churn target |

`RowNumber`, `CustomerId`, and `Surname` are removed before model training.

## Machine-learning workflow

1. Load and explore the churn dataset.
2. Remove identifier columns and inspect missing values and distributions.
3. Split the data into stratified training and test sets.
4. Apply median imputation and standard scaling to numerical features.
5. Apply most-frequent imputation and one-hot encoding to categorical features.
6. Use SMOTE to evaluate training with a more balanced target distribution.
7. Train logistic regression and random forest classifiers.
8. Evaluate the classifiers with the F1 score.
9. Save the fitted preprocessor and selected random forest model in `artifacts/`.

## Getting started

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 2. Install the dependencies

```bash
python -m pip install numpy pandas matplotlib seaborn scikit-learn joblib imbalanced-learn pydantic fastapi python-dotenv jupyter
```

### 3. Configure the environment

Copy `.env.example` to `.env` and set an API secret:

```env
APP_NAME="Churn-Detection-API"
APP_VERSION="1.0.0"
API_SECRET_KEY="replace-with-a-secure-key"
```

Do not commit the real `.env` file or expose its secret key.

### 4. Run the training notebook

Start Jupyter:

```bash
jupyter notebook
```

Open `notebooks/notebook.ipynb` and run its cells in order. The notebook reads `dataset/churn-data.csv` and writes the trained artifacts to `artifacts/`.

## Prediction input

The Pydantic request model expects data in this format:

```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Female",
  "Age": 40,
  "Tenure": 5,
  "Balance": 85000.0,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 75000.0
}
```

## API status

The FastAPI layer is currently under development. `main.py` imports the configuration, validation model, and inference helper, but it does not yet create the `FastAPI` application or expose a prediction route. Finish and test that layer before deploying the service.

## Technologies

- Python
- pandas and NumPy
- Matplotlib and Seaborn
- scikit-learn
- imbalanced-learn
- Pydantic
- FastAPI
- Jupyter Notebook

## Possible improvements

- Complete the FastAPI application and authenticated prediction endpoint.
- Add automated tests for validation, preprocessing, and inference.
- Track experiment metrics and model versions.
- Add model monitoring and input-drift checks.
- Rename misspelled files and variables while preserving artifact compatibility.

## License

No license has been specified for this project.
