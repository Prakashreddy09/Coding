from .test import Testing

class Test:
    def __init__(self, func):
        self.func = func
        self.test_cases = []
        self.testing = Testing(self.func)
        self.results = []
        self.passed = 0

    def add_testcase(self,input_data,expected_output):
        self.test_cases.append({'input': input_data, 'expected': expected_output})
    
    def run_tests(self):
        self.results, self.passed = self.testing.run_tests(self.test_cases)

    def print_results(self):
        self.testing.print_results(self.results)
        print(f"Testcases passed: {self.passed} / {len(self.test_cases)}")
        print(f"Pass Percentage : {((self.passed)/(len(self.test_cases)*1.0))*100}")
