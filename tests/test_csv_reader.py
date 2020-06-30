from csv_reader.csv_reader import CsvReader
import pytest

FILENAME = "tests/test_data/test_file.csv"

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
    # FILENAME

    # When
    CsvReader().run({'input': FILENAME, 's': True})
    out, err = capfd.readouterr()

    # Then
    expected_output = open('tests/test_data/expected_sorted_by_rent.txt', 'r').read()
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
    # FILENAME

    # When
    CsvReader().run({'input': FILENAME, 'l': 15})
    out, err = capfd.readouterr()

    # Then
    expected_output = open('tests/test_data/expected_lease_of_15_years_output.txt', 'r').read()
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
    # FILENAME

    # When
    CsvReader().run({'input': FILENAME, 't': True})
    out, err = capfd.readouterr()

    # Then
    expected_output = open('tests/test_data/expected_tenants_output.txt', 'r').read()
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
    # FILENAME

    # When
    CsvReader().run({'input': FILENAME, 'd': ["31 Mar 2014", "30 Mar 2035"]})
    out, err = capfd.readouterr()

    # Then
    expected_output = open('tests/test_data/expected_rentals_2014_2035_output.txt', 'r').read()
    assert(out == expected_output)

def test_invalid_get_leases():
    """
    Given:
        A list with data points and an integer representing years
    When:
        The script is called with argument -l with a negative integer argument
    Then:
        An Exception is raised stating an invalid argument was provided.
    """

    # Given
    # FILENAME

    # When

    with pytest.raises(ValueError) as error:
        CsvReader().run({'input': FILENAME, 'l': -1})


    # Then
    assert "Invalid years provided. Please provide a positive integer." in str(error.value)

def test_invalid_rentals_between_dates():
    """
    Given:
        A list with data points and two date string arguments, one of which has an invalid format.
    When:
        The script is called with argument -d with invalid date arguments
    Then:
        A Value error is raised for the invalid format
    """

    # Given
    # FILENAME

    # When

    with pytest.raises(ValueError) as error:
        CsvReader().run({'input': FILENAME, 'd': ["31 Mar 2014", "30 Mar 20"]})


    # Then
    assert "time data '30 Mar 20' does not match format '%d %b %Y'" in str(error.value)

def test_invalid_start_date():
    """
    Given:
        A list with data points and two date string arguments, the start date being after the end date
    When:
        The script is called with argument -d with invalid date arguments
    Then:
        A Value error is raised for the invalid format
    """

    # Given
    # FILENAME

    # When
    with pytest.raises(ValueError) as error:
        CsvReader().run({'input': FILENAME, 'd': ["31 Mar 2014", "30 Mar 2010"]})

    # Then
    assert "Start date is after End date. Please provide a valid start date" in str(error.value)
