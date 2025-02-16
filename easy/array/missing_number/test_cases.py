test_cases = [
    {"in": [3,0,1], "out": 2},
    {"in": [0,1], "out": 2},
    {"in": [9,6,4,2,3,5,7,0,1], "out": 8},
]

def check_test_cases(fun):
    for test_case in test_cases:
        out = fun(test_case["in"])
        if out == test_case["out"]:
            print(test_case, " : ", "PASS")
        else:
            print(test_case, " : ", "FAIL")