def maeEachModels(X_train, X_test, y_train, y_test):
    models = []
    for i in range(2, 8):
        models.append(keras.models.load_model('model_' + str(i) + 'layers.h5'))

    train_mae = []
    test_mae = []
    for model in models:
        train_mae.append(mean_absolute_error(y_train, model.predict(X_train)))
        test_mae.append(mean_absolute_error(y_test, model.predict(X_test)))

    return models, train_mae, test_mae

def plotMaeEachModels(train_mae, test_mae):
    labels = ["2 layers", "3 layers", "4 layers", "5 layers", "6 layers", "7 layers"]
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))
    rects1 = ax.bar(x - width/2, train_mae, width, label='Train')
    rects2 = ax.bar(x + width/2, test_mae, width, label='Test')

    ax.set_ylabel('MAE')
    ax.set_title('MAE vs Layers')
    ax.set_xticklabels(["0"] + labels)
    ax.legend()

    plt.show()

def finalANN(test_mae, models):
    idx = test_mae.index(min(test_mae))
    return models[idx]