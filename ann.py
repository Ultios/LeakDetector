def createFeatureScalingLayer(X_train):
    normalize = layers.Normalization()
    normalize.adapt(X_train)
    return normalize

def baselineANN(normalize):
    model = keras.Sequential()
    model.add(layers.InputLayer(input_shape = (2,)))
    model.add(normalize)
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dense(1, name='output_layer'))

    model.compile(loss = 'mean_absolute_error',
                  optimizer = keras.optimizers.Adam(),
                  metrics = ['mean_absolute_error'])

    return model

def trainModel(model, X_train, y_train):
    history = model.fit(X_train, y_train, epochs=200, steps_per_epoch=25, validation_split=0.2, verbose=0)
    return history

