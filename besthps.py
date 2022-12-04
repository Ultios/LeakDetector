def printBestHps(layers, tuner):
    best_hps = tuner.get_best_hyperparameters(1)[0]
    for i in range(layers):
        print(f'units_{i}:', best_hps.get(f"units_{i}"))
    print('learning_rate:', best_hps.get('learning_rate'))