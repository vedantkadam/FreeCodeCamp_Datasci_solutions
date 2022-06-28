import numpy as np

def calculate(list):
    if(len(list) != 9):
      raise ValueError("List must contain nine numbers.")
    
    le=np.array(list)
    print(le)
    mean_r=[le[[0,1,2]].mean(),le[[3,4,5]].mean(),le[[6,7,8]].mean()]
    mean_c=[le[[0,3,6]].mean(),le[[1,4,7]].mean(),le[[2,5,8]].mean()]

    var_r=[le[[0,1,2]].var(),le[[3,4,5]].var(),le[[6,7,8]].var()]
    var_c=[le[[0,3,6]].var(),le[[1,4,7]].var(),le[[2,5,8]].var()]
  
    std_r=[le[[0,1,2]].std(),le[[3,4,5]].std(),le[[6,7,8]].std()]
    std_c=[le[[0,3,6]].std(),le[[1,4,7]].std(),le[[2,5,8]].std()]

    max_r=[le[[0,1,2]].max(),le[[3,4,5]].max(),le[[6,7,8]].max()]
    max_c=[le[[0,3,6]].max(),le[[1,4,7]].max(),le[[2,5,8]].max()]

    min_r=[le[[0,1,2]].min(),le[[3,4,5]].min(),le[[6,7,8]].min()]
    min_c=[le[[0,3,6]].min(),le[[1,4,7]].min(),le[[2,5,8]].min()]

    sum_r=[le[[0,1,2]].sum(),le[[3,4,5]].sum(),le[[6,7,8]].sum()]
    sum_c=[le[[0,3,6]].sum(),le[[1,4,7]].sum(),le[[2,5,8]].sum()]
  
    return {
      'mean': [mean_c, mean_r, le.mean()],
      'variance': [var_c, var_r, le.var()],
      'standard deviation': [std_c, std_r, le.std()],
      'max': [max_c, max_r, le.max()],
      'min': [min_c, min_r, le.min()],
      'sum': [sum_c, sum_r, le.sum()]
    }