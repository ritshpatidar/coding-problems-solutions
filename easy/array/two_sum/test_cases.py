test_cases = [
    {"nums": [2,7,11,15], "target": 9, "out": [0,1]},
    {"nums": [3,2,4], "target": 6, "out": [1,2]},
    {"nums": [3,3], "target": 6, "out": [0,1]},
    {"nums": [-2,11,15,-7], "target": -9, "out": [0,3]},
    {"nums": [-2,11,15,7], "target": 5, "out": [0,3]}
]

def check_test_cases(fun):
    for test_case in test_cases:
        out = fun(test_case["nums"], test_case["target"])
        if sorted(out) == sorted(test_case["out"]):
            print("Expected: ", out, "Actual: ",  test_case["out"], " - ", "PASS")
        else:
            print(test_case, " : ", "FAIL")