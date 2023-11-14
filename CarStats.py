import pandas as pd
import numpy as np

def getMean_Desv(file_path):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)

    # Extract 'acceleration_0_100_km/h' and 'length_mm' columns
    acceleration_column = data['acceleration_0_100_km/h_s']
    # Filter out NaN values from the acceleration_m_s column, to m/s^2
    acceleration_column = (100/1*1000/3600)/acceleration_column[~np.isnan(acceleration_column)]
    # Columna de longitud
    length_column = data['length_mm']
    length_column = length_column[~np.isnan(length_column)]*(1/1000)
    return {"acceleration_mean":np.mean(acceleration_column),
            "acceleration_desv":np.std(acceleration_column),
            "length_mean":np.mean(length_column),
            "length_desv":np.std(length_column)}

print(getMean_Desv("./car.csv"))