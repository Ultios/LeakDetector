def build_model_6(hp):
    optimized_model = keras.Sequential()
    optimized_model.add(layers.InputLayer(input_shape=(2,)))
    optimized_model.add(normalize)
    for i in range(0, 6):
        optimized_model.add(layers.Dense(units=hp.Int('units_' + str(i), min_value=32, max_value=512, step=32),
                                         activation='relu'))
        
    optimized_model.add(layers.Dense(1, name='output_layer'))
    optimized_model.compile(optimizer=keras.optimizers.Adam(hp.Choice('learning_rate', [1e-2, 1e-3])),
                            loss='mean_absolute_error',
                            metrics=['mean_absolute_error'])
    
    return optimized_model

def layer6(X_train, y_train):
    tuner6 = RandomSearch(build_model_6,
                          objective='val_mean_absolute_error',
                          max_trials=10,
                          executions_per_trial=1,
                          directory='TUning Project 6 Layers',
                          project_name='OPPINET Leak Detector',
                          overwrite=True)
    
    tuner6.search(X_train, 
                  y_train,
                  epochs=200,
                  steps_per_epoch=25,
                  # validation_data = (X_test_scaled, y_test),
                  validation_split=0.2,
                  verbose=1)

    return tuner6
    