import math
class SegTree:
    def __init__(self, list, binOp, IDElement) :
        self.list = list
        self.bin_op = binOp
        self.id_element = IDElement
        self.tree_depth = math.ceil(math.log2(len(list)))
        self.tree_width = 2**self.tree_depth
        #construct tree
        self.tree = 

