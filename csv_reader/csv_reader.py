import  argparse
import csv
import json
import pprint
import sys

from datetime import datetime as dt
from fuzzywuzzy import fuzz
from operator import itemgetter

DATE_F = '%d %b %Y'

class CsvReader(object):

	def run(self, argv):
		filename = argv.get("input")
		data = self.read_file(filename)

		if argv.get("s"):
			self.sort_by_current_rent(data)

		if argv.get("l"):
			self.get_leases_of_x_years(data, argv.get("l"))

		if argv.get("t"):
			self.get_tenant_dictionary(data)

		if argv.get("d"):
			sdate = argv['d'][0]
			edate = argv['d'][1]
			self.get_rentals_between_dates(data, sdate, edate)


	def get_tenant_dictionary(self, data):
		tenants = {}
		for record in data:
			tenant = record[6]
			tenants.update({tenant: tenants.get(tenant, 0) + 1})

		print("\n--------------- Tenants with rentals ---------------\n")
		print(json.dumps(tenants, indent=4))

	def get_leases_of_x_years(self, data, years):
		"""
		Builds list from given data set for records with leases of given years
		:param data: list of mast data
		:return: list with leases of x years
		"""
		if years < 0:
			raise ValueError("Invalid years provided. Please provide a positive integer.")

		leases = [i for i in data if (int(i[9]) == years)]
		print("\n--------------- Leases of %d years ---------------\n" % years)
		if leases == []:
			print("No leases of %d years" % years)
		else:
			pprint.pprint(leases, compact=True)
		print("\nTotal rent :", sum([float(x[10]) for x in leases]))

	def get_rentals_between_dates(self, data, sdate, edate):
		"""
		Builds list from given data set for records where lease is between 2 given dates
		:param data: list of mast data
		:param start_date: String datetime
		:param end_date: String datetime
		:return: list with rentals between the 2 given times
		"""
		try:
			print("\n--------------- Rentals between {} and  {} ---------------\n".format(sdate, edate))
			if ((dt.strptime(sdate, DATE_F) > dt.strptime(edate, DATE_F))):
				raise ValueError("Start date is after End date. Please provide a valid start date")
			rentals = list(filter(lambda x : (dt.strptime(sdate, DATE_F) < dt.strptime(x[7], DATE_F) < dt.strptime(edate, DATE_F)), data))
			for rental in rentals:
				pprint.pprint(
					(rental[:7] + [dt.strptime(date, DATE_F).strftime("%d/%m/%Y") for date in rental[7:9]] + rental[9:]),
					compact=True
				)
		except ValueError as e:
			raise e

	def sort_by_current_rent(self, data):
		"""
		Sorts mast data by current rent
		:param data: list of mast data
		:return: sorted list
		"""
		try:
			data.sort(key=lambda x: float(x[10]))
			print("--------------- Sorted by rent ---------------\n")
			pprint.pprint(data[0:5], compact=True)
		except ValueError as e:
			raise ValueError(e)

	def read_file(self, filename):
		"""
		Takes a filename and returns the data in a list
		:param filename: string
		:return: list of data points
		"""
		try:
			with open(filename, newline='') as csvfile:
				reader = csv.reader(csvfile)
				data = list(reader)
				return data[1:]
		except FileNotFoundError:
			raise FileNotFoundError("File not found, maybe check spelling. Filename received:", filename)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', metavar="", help="Input filename")
	parser.add_argument('-s', action='store_true', help="Sort by rent")
	parser.add_argument('-l', metavar="", type=int, help="Get leases of x years")
	parser.add_argument('-t', action='store_true', help="Get tenants dictionary")
	parser.add_argument('-d', metavar="", nargs=2, type=str, help="Get rentals between two dates")
	args = parser.parse_args()
	CsvReader().run(vars(args))

