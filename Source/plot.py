def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Error [Leak location]')
    plt.legend()
    plt.grid(True)

def plot_perLeakRate(model, X, y):
    idx = X.index[X['Leak rate (STB/d)'] == 280].tolist()
    d_280 = X.loc[idx]
    pred_280 = model.predict(d_280)
    sim_280 = y.loc[idx]

    idx = X.index[X['Leak rate (STB/d)'] == 560].tolist()
    d_560 = X.loc[idx]
    pred_560 = model.predict(d_560)
    sim_560 = y.loc[idx]

    idx = X.index[X['Leak rate (STB/d)'] == 840].tolist()
    d_840 = X.loc[idx]
    pred_840 = model.predict(d_840)
    sim_840 = y.loc[idx]

    idx = X.index[X['Leak rate (STB/d)'] == 1120].tolist()
    d_1120 = X.loc[idx]
    pred_1120 = model.predict(d_1120)
    sim_1120 = y.loc[idx]

    idx = X.index[X['Leak rate (STB/d)'] == 1400].tolist()
    d_1400 = X.loc[idx]
    pred_1400 = model.predict(d_1400)
    sim_1400 = y.loc[idx]

    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    axs[0, 0].plot(sim_280, sim_280, color='red')
    axs[0, 0].scatter(pred_280, sim_280, color="blue")
    axs[0, 0].set_title('Rate 280 STB/D')
    axs[0, 1].plot(sim_560, sim_560, color="red")
    axs[0, 1].scatter(pred_560, sim_560, color="orange")
    axs[0, 1].set_title('Rate 560 STB/D')
    axs[0, 2].plot(sim_840, sim_840, color="red")
    axs[0, 2].scatter(pred_840, sim_840, color="green")
    axs[0, 2].set_title('Rate 840 STB/D')
    axs[1, 0].plot(sim_1120, sim_1120, color="red")
    axs[1, 0].scatter(pred_1120, sim_1120, color="purple")
    axs[1, 0].set_title('Rate 1120 STB/D')
    axs[1, 1].plot(sim_1400, sim_1400, color="red")
    axs[1, 1].scatter(pred_1400, sim_1400, color="brown")
    axs[1, 1].set_title('Rate 1400 STB/D')

    for ax in axs.flat:
        ax.set(xlabel='prediction', ylabel='simulation')
