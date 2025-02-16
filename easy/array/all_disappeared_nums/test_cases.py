test_cases = [
    {"in": [4,3,2,7,8,2,3,1], "out": [5,6]},
    {"in": [1,1], "out": [2]},
    {"in": [1], "out": []},
    {"in": [1,2,3,4,5], "out": []},
]

def check_test_cases(fun):
    for test_case in test_cases:
        out = fun(test_case["in"])
        if out == test_case["out"]:
            print(test_case, " : ", "PASS")
        else:
            print(test_case, " : ", "FAIL")