from hashfunctions.hashfunctions import alphanumeric_hash_function, numeric_hash_function


class TestHashFunctions:

    def test_alphanumeric_hash_function(self):
        test = ['Mia', 'Tim', 'Bea', 'Zoe', 'Jan', 'Ada',
                'Leo', 'Sam', 'Lou', 'Max', 'Ted']

        result = []
        for name in test:
            result.append(alphanumeric_hash_function(name, len(test)))

        assert result == [4, 1, 0, 5, 6, 9, 2, 3, 7, 8, 10]

    def test_numeric_hash_function(self):
        test = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        result = []
        for num in test:
            result.append(numeric_hash_function(num, len(test)))

        assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
