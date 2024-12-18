import pickle
import numpy as np

def get_prediction(plotnost, modul_uprugosti, otverditel, epoxidy, temperatura, pov_plotnost,
                       modul_upr_ras, proch_ras, smola, ugol_nashivki, shag_nashivki, plot_nashivki):
    with open('models/model3.pkl', 'rb') as f:
        model = pickle.load(f)
    
    params = np.array([[plotnost], [modul_uprugosti], [otverditel], [epoxidy], [temperatura], [pov_plotnost],
                       [modul_upr_ras], [proch_ras], [smola], [ugol_nashivki], [shag_nashivki], [plot_nashivki]])
    params = model.transform(params)
    y_pred = model.predict(params)
    
 

    return model.inverse_transform([y_pred])