import pickle
import numpy as np

def get_prediction(parameter_1, parameter_2):
    with open('models/model2.pkl', 'wb') as f:
        model = pickle.load(f)
    
    params = np.array([[plotnost], [modul_uprugosti], [otverditel], [epoxidy], [temperatura], [pov_plotnost],
                       [modul_upr_ras], [proch_ras], [smola], [ugol_nashivki], [shag_nashivki], [plot_nashivki]])
    params = model.transform(params)
    y_pred = model.predict(params)
    
 

    return model.inverse_transform([y_pred])