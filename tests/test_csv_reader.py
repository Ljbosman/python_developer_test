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


def test_get_leases(capfd):
    """
    Given:
        A list with data points and an integer representing years
    When:
        The script is called with argument -l with integer argument
    Then:
        The data is searched for points with lease periods of the given years
    """

    # Given
    filename = "test_data/test_file.csv"

    # When
    CsvReader().run({'input': filename, 'l': 15})
    out, err = capfd.readouterr()

    # Then
    expected_output = open('test_data/expected_lease_of_15_years_output.txt', 'r').read()
    assert(out == expected_output)


def test_get_tenants(capfd):
    """
    Given:
        A list with un-normalised data points
    When:
        The script is called with argument -t
    Then:
        A dictionary is built for tenants with their total number of rentals
    """

    # Given
    filename = "test_data/test_file.csv"

    # When
    CsvReader().run({'input': filename, 't': True})
    out, err = capfd.readouterr()

    # Then
    expected_output = open('test_data/expected_tenants_output.txt', 'r').read()
    assert(out == expected_output)

def test_get_rentals_between_dates(capfd):
    """
    Given:
        A list with data points and two date string arguments
    When:
        The script is called with argument -d with date arguments
    Then:
        A list is returned with all data points that have rental dates between the given date arguments
    """

    # Given
    filename = "test_data/test_file.csv"

    # When
    CsvReader().run({'input': filename, 'd': ["31 Mar 2014", "30 Mar 2035"]})
    out, err = capfd.readouterr()

    # Then
    expected_output = open('test_data/expected_rentals_2014_2035_output.txt', 'r').read()
    assert(out == expected_output)



