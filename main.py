from codes.Searching.linear_search import linear_search
from codes.Sorting.bubble_sort import bubble_sort
from Testing.Test import Test

test = Test(bubble_sort)
test.add_testcase(([5, 1, 4, 2, 8],), [1, 2, 4, 5, 8])
test.add_testcase(([3, 3, 2, 1, 4],), [1, 2, 3, 3, 4])
test.add_testcase(([1, 2, 3, 4, 5],), [1, 2, 3, 4, 5])
test.add_testcase(([5, 4, 3, 2, 1],), [1, 2, 3, 4, 5])
test.add_testcase(([1],), [1])
test.add_testcase(([2, 1],), [1, 2])
test.add_testcase(([10, 7, 8, 9, 1],), [1, 7, 8, 9, 10])
test.add_testcase(([12, 11, 13, 5, 6],), [5, 6, 11, 12, 13])
test.add_testcase(([0, -1, 2, -3, 1],), [-3, -1, 0, 1, 2])
test.add_testcase(([7, 7, 7, 7, 7],), [7, 7, 7, 7, 7])
test.run_tests()
test.print_results()



