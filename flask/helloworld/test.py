class Test:
    def __init__(self, one):
        self.one = one
        self.sum = 0

    def __call__(self, *args, **kwargs):
        """
        by setting '__call__' object of class get inputs and do something 
        without calling specific function name  
        """
        for arg in args:
            self.sum += arg

        return self.sum, kwargs


test = Test(one=1)

print(test.one)

test(1, 2, 3)       # args get 'values'
test(var=1, res=2)  # kwargs get couples of 'key & value'

