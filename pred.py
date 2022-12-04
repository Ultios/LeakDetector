def plot_predVStrue(model, X, y):
    predictions = model.predict(X).flatten()
    a = plt.axes(aspect='equal')
    plt.scatter(predictions, y)
    plt.xlabel('True Values [Leak location]')
    plt.ylabel('Predictions [Leak location]')
    lims = [0, 80000]
    plt.xlim(lims)
    plt.ylim(lims)
    _ = plt.plot(lims, lims, color='red')