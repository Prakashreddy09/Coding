class Testing:
    def __init__(self, solution_function):
        self.solution_function = solution_function

    def run_tests(self, testcases):
        results = []
        count = 0
        for case in testcases:
            input_data = case['input']
            expected_output = case['expected']
            try:
                # Debug print to verify input data
                # print(f"Running test with input: {input_data}")
                result = self.solution_function(*input_data)
                passed = result == expected_output
                if passed:
                    count += 1
                results.append({'input': input_data, 'expected': expected_output, 'result': result, 'passed': passed})
            except Exception as e:
                results.append({'input': input_data, 'expected': expected_output, 'result': str(e), 'passed': False})
        return results, count

    @staticmethod
    def print_results(results):
        for idx, result in enumerate(results):
            print(f"Test Case {idx + 1}:")
            print(f"Input: {result['input']}")
            print(f"Expected Output: {result['expected']}")
            print(f"Actual Output: {result['result']}")
            print(f"Passed: {'Yes' if result['passed'] else 'No'}")
            print("-" * 20)