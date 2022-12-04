def bestModel(tuner):
    model = tuner.get_best_models()[0]
    return model