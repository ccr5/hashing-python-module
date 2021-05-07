from hashfunctions.hashtables import hash_table, hash_table_alphanumeric, hash_table_numeric
from hashfunctions.hashtables import get_data, insert_data, update_data, del_data


class TestHashTables:

    def test_hash_table(self):

        test = [{'Ada': 5}, {5: 'a'}, {'Bea': 2}, {53: 'e'},
                {'Tim': 1}, {11: 'b'}, {42: 'd'}, {21: 'c'}]

        expected_value = [[{'Bea': 2}], 1, [{'Tim': 1}, {42: 'd'}], [{11: 'b'}],
                          4, [{5: 'a'}, {53: 'e'}, {21: 'c'}], [{'Ada': 5}], 7]

        result = hash_table(test, 0)
        assert result == expected_value

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

    def test_hash_table_numeric(self):
        test1 = [{8: 'i'}, {9: 'j'}, {2: 'c'}, {3: 'd'},
                 {10: 'k'}, {11: 'a'}, {1: 'b'}, {4: 'e'},
                 {5: 'f'}, {7: 'h'}, {6: 'g'}]

        expected_value1 = [[{11: 'a'}], [{1: 'b'}], [{2: 'c'}],
                           [{3: 'd'}], [{4: 'e'}], [{5: 'f'}],
                           [{6: 'g'}], [{7: 'h'}], [{8: 'i'}],
                           [{9: 'j'}], [{10: 'k'}]]

        test2 = [{53: 'e'}, {5: 'a'}, {11: 'b'}, {42: 'd'}, {21: 'c'}]

        expected_value2 = [[{5: 'a'}], [{11: 'b'}, {21: 'c'}],
                           [{42: 'd'}], [{53: 'e'}], 4]

        result1 = hash_table_numeric(test1, 0)
        result2 = hash_table_numeric(test2, 0)

        assert result1 == expected_value1
        assert result2 == expected_value2

    def test_get_data(self):

        data = [{'Ada': 5}, {5: 'a'}, {'Bea': 2}, {53: 'e'},
                {'Tim': 1}, {11: 'b'}, {42: 'd'}, {21: 'c'}]

        table = hash_table(data, 0)
        result = get_data(table, 0, 42)
        assert result == [{42: 'd'}]

    def test_insert_data(self):

        data = [{'Ada': 5}, {5: 'a'}, {'Bea': 2}, {53: 'e'},
                {'Tim': 1}, {11: 'b'}, {42: 'd'}, {21: 'c'}]

        new_value = [{'Mia': 3}, {'Leo': 4}]
        table = hash_table(data, 0)
        result = insert_data(table, 0, new_value)
        assert result == [0, [{11: 'b'}, {21: 'c'}], [{42: 'd'}, {'Ada': 5}],
                          [{53: 'e'}], [{'Bea': 2}], [{5: 'a'}], 6, 7,
                          [{'Tim': 1}, {'Leo': 4}], [{'Mia': 3}]]

    def test_update_data(self):

        data = [{'Ada': 5}, {5: 'a'}, {'Bea': 2}, {53: 'e'},
                {'Tim': 1}, {11: 'b'}, {42: 'd'}, {21: 'c'}]

        new_value = {42: 'ak'}
        table = hash_table(data, 0)
        new_table = update_data(table, 0, 42, new_value)
        print(new_table)
        result = get_data(new_table, 0, 42)
        assert result == [{42: 'ak'}]

    def test_del_data(self):

        data = [{'Ada': 5}, {5: 'a'}, {'Bea': 2}, {53: 'e'},
                {'Tim': 1}, {11: 'b'}, {42: 'd'}, {21: 'c'}]

        expected_value = [[{21: 'c'}], 1, 2, [{'Ada': 5}],
                          [{'Tim': 1}, {11: 'b'}, {53: 'e'}],
                          [{'Bea': 2}, {5: 'a'}], 6]

        table = hash_table(data, 0)
        result = del_data(table, 0, 42)
        assert result == expected_value
