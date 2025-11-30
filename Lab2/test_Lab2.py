import Lab2 

def find_min_max():
    correct = [2.0, 9.0]
    result = []
    test = [5,4,7,2,9]
    result = Lab2.min_man(test)
    assert(result == correct)