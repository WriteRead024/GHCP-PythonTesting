# May 20th, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

# consider:
# https://stackoverflow.com/questions/3340539/why-is-tuple-faster-than-list-in-python
# for more perspective

import time
import unittest

print_results = False


class TestFunctionArgumentTuples(unittest.TestCase):
    def process_tuple(self, data):
        # Process the tuple
        pass

    def process_list(self, data):
        # Process the list
        pass

    def test_tuple_vs_list_performance(self):
        # Create a large data set
        data = tuple(range(1000000))
        assert isinstance(data, tuple), "data is not a tuple"
        data_list = list(data)
        assert isinstance(data_list, list), "data_list is not a list"

        # Measure the time taken to process the tuple
        start_time = time.time()
        self.process_tuple(data)
        tuple_time = time.time() - start_time

        # Measure the time taken to process the list
        start_time = time.time()
        self.process_list(data_list)
        list_time = time.time() - start_time

        # Conditionally print the results
        if print_results:
            print("Tuple processing time:", tuple_time)
            print("List processing time:", list_time)

        # Compare the execution times
        try:
            assert (
                tuple_time < list_time
            ), "Tuple processing is unexpectedly not slower than list processing"
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    print_results = True
