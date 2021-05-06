from hashfunctions.hashtables import hash_table_alphanumeric, hash_table_numeric


class TestHashTables:

    def test_hash_table_alphanumeric(self):
        test1 = [{'Mia': 0}, {'Tim': 1}, {'Bea': 2},
                 {'Zoe': 3}, {'Jan': 4}, {'Ada': 5},
                 {'Leo': 6}, {'Sam': 7}, {'Lou': 8},
                 {'Max': 9}, {'Ted': 10}]

        expected_value1 = [[{'Bea': 2}], [{'Tim': 1}], [{'Leo': 6}],
                           [{'Sam': 7}], [{'Mia': 0}], [{'Zoe': 3}],
                           [{'Jan': 4}], [{'Lou': 8}], [{'Max': 9}],
                           [{'Ada': 5}], [{'Ted': 10}]]

        test2 = [{'Ada': 5}, {'Tim': 1}, {'Bea': 2}]

        expected_value2 = [[{'Bea': 2}], [{'Ada': 5}, {'Tim': 1}], 2]

        result1 = hash_table_alphanumeric(test1, 0)
        result2 = hash_table_alphanumeric(test2, 0)
        assert result1 == expected_value1
        assert result2 == expected_value2
