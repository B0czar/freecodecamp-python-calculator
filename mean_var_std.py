import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    
    arr = np.array(lst).reshape(3, 3)

    def to_list(x):
        return [i.item() if hasattr(i, "item") else i for i in list(x)]

    calculations = {
        'mean': [
            to_list(np.mean(arr, axis=0)),     
            to_list(np.mean(arr, axis=1)),     
            np.mean(arr).item()                
        ],
        'variance': [
            to_list(np.var(arr, axis=0)),
            to_list(np.var(arr, axis=1)),
            np.var(arr).item()
        ],
        'standard deviation': [
            to_list(np.std(arr, axis=0)),
            to_list(np.std(arr, axis=1)),
            np.std(arr).item()
        ],
        'max': [
            to_list(np.max(arr, axis=0)),
            to_list(np.max(arr, axis=1)),
            int(np.max(arr))
        ],
        'min': [
            to_list(np.min(arr, axis=0)),
            to_list(np.min(arr, axis=1)),
            int(np.min(arr))
        ],
        'sum': [
            to_list(np.sum(arr, axis=0)),
            to_list(np.sum(arr, axis=1)),
            int(np.sum(arr))
        ]
    }

    return calculations