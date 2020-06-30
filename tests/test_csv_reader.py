from ..csv_reader import CsvReader
import pytest


def test_sort_by_rent(capfd):
    """
    Given:
        A list with data points
    When:
        The script is called with argument -s
    Then:
        The data is sorted by current rent and the first 5 entries are printed
    """

    # Given
    filename = "test_data/test_file.csv"

    # When
    CsvReader().run({'input': filename, 's': True})
    out, err = capfd.readouterr()

    # Then
    expected_output = open('test_data/expected_sorted_by_rent.txt', 'r').read()
    assert(out == expected_output)

