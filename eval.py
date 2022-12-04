def evaluate(model, X_train, X_test, y_train, y_test):
    print(f'Mean absolute error for train data {mean_absolute_error(y_train, model.predict(X_train)) :.5f}')
    print(f'Mean absolute error for test data {mean_absolute_error(y_test, model.predict(X_test)) :.5f}')