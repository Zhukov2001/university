def lagrannge_function(data_x, data_y, necessary_val):    
    result = 0
    for master in range(len(data_x)):
        # числитель
        numerator = 1
        # знаменатель
        denominator = 1
        # находим числитель
        for n in range(len(data_x)):
            if n != master:
                # находим числитель
                numerator *= necessary_val - data_x[n]
                # находим знаменатель 
                denominator *= data_x[master] - data_x[n]
        lagrange = numerator / denominator   
        result += lagrange * data_y[master]
    return result


    











