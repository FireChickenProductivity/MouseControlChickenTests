def assert_for_all(function, test_cases, assert_function):
    for test_case in test_cases:
        assert_function(function(test_case), f"{test_case} failed with function {function}")

def assert_true_for_all(testing_class, function, test_cases):
    assert_for_all(function, test_cases, testing_class.assertTrue)

def assert_false_for_all(testing_class, function, test_cases):
    assert_for_all(function, test_cases, testing_class.assertFalse)