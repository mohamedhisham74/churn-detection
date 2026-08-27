import pandas as pd

from .request import CustomerData

def predict_new(data:CustomerData, preproccessor, model):

    df= pd.DataFrame([data.model_dump()])

    X_processed= preproccessor.transform(df)

    y_pred= model.predict(X_processed)
    y_prop=model.predict_proba(X_processed)

    return {
        bool(y_pred),
        
        float(y_prop)
    }