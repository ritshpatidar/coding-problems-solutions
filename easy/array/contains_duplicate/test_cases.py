test_cases = [
    {"in": [1,2,3,1], "out": True},
    {"in": [1,2,3,4], "out": False},
    {"in": [1,1,1,1], "out": True},
    {"in": [1,1,3,4], "out": True},
    {"in": [1,2,3,4,4], "out": True},
    {"in": [1,2,2,3,3,3,4,4], "out": True},
    {"in": [1], "out": False}
]

def check_test_cases(fun):
    for test_case in test_cases:
        out = fun(test_case["in"])
        if out == test_case["out"]:
            print(test_case, " : ", "PASS")
        else:
            print(test_case, " : ", "FAIL")