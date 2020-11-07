from typing import get_type_hints
import numpy as np 
import json

def get_data(path=None):
    with open(path, 'r') as f:
        data = json.load(f)
    f.close()
    return data

# data = get_data(path="../datasets/za_traffic_2020/traffic_train/train_traffic_sign_dataset.json")
# print(data["info"])