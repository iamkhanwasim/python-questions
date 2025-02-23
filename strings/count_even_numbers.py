class Count:
    def __init__(self, input):
        self.input = input
    
    def count_even_numbers(self):
        cntevennums = 0
        for i in self.input:
            if i % 2 == 0:
                cntevennums += 1
        return cntevennums

number = [1, 2, 3, 4, 5, 6]
# number = ["1"]
count = Count(number)
print(count.count_even_numbers())

# Test cases
def test_case_count_even_nums(numbers):
    # Test 1: Has one even number
    count = Count(numbers)
    assert count.count_even_numbers() == 10, "Test case #1 failed"

    # Test 2: Has no even number
    count = Count(numbers)
    assert count.count_even_numbers() == 0, "Test case #2 failed"


test_case_count_even_nums([1, 3, 5 ])