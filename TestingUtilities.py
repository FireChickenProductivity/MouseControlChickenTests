def assert_actual_equals_expected(actual, expected):
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"

def assert_true(condition):
    assert condition

def assert_false(condition):
    assert_true(not condition)