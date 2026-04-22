
def gen_bin_tree(height: int, root: int) -> dict:
    """"
    gen_bin_tree(height, root) -> dict

    Функция возвращает бинарное дерево 
    Левый потомок равняется узел дерева + 1  
    и правый потомок равняется квадрату узла

    Ключевые аргументы:
        height -- высота дерева
        root -- корень дерева
    
    Допустимые значения аргументов: целые неотрицательные числа
    """
    if height < 0:
        return None
    elif  height == 0:
        return {str(root):[]}
    elif height == 1:
        left_leaf = str(root + 1) 
        right_leaf = str(root ** 2)
        return {str(root): [{left_leaf: []}, {right_leaf: []}]}
    else:
        return {str(root): [gen_bin_tree(height - 1, root + 1), gen_bin_tree((height - 1), (root ** 2))]}


print(gen_bin_tree(0, 5))