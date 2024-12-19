import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def get_prediction(plotnost, modul_uprugosti, otverditel, epoxidy, temperatura, pov_plotnost,
                       modul_upr_ras, proch_ras, smola, ugol_nashivki, shag_nashivki, plot_nashivki):
    with open('models/model3.pkl', 'rb') as f:
        model = pickle.load(f)
    
    min_max_scaler = MinMaxScaler()
    params = np.array([plotnost, modul_uprugosti, otverditel, epoxidy, temperatura, pov_plotnost,
                       modul_upr_ras, proch_ras, smola, ugol_nashivki, shag_nashivki, plot_nashivki])
    params = params.reshape(1, -1)
    params = min_max_scaler.fit_transform(params)
    y_pred = model.predict(params)
    
 

    return min_max_scaler.inverse_transform(y_pred)