from autogluon.tabular import TabularPredictor

from data_preprocessor.datasets import create_merged_database


def autogluon(code_csv):
    merged_database, x_merged_class, y_merged_class, x_merged_efficiency, y_merged_efficiency = create_merged_database()
    # Load and prepare your data
    train_data = merged_database
    test_data = code_csv

    # Define the task (classification) and label column
    predictor = TabularPredictor(label='target_column')

    # Train the model
    predictor.fit(train_data)

    # Make predictions
    predictions = predictor.predict(test_data)
    return predictions


