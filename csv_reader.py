from datetime import datetime as dt
from fuzzywuzzy import fuzz
from operator import itemgetter

import  argparse, csv, json, pprint

DATE_F = '%d %b %Y'

def main(argv):
	filename = argv.get("input")
	try:
		with open(filename, newline='') as csvfile:
			reader = csv.reader(csvfile)
			data = list(reader)
			data = data[1:]

		if argv.get("s"):
			sort_by_current_rent(data)

		if argv.get("l"):
			get_leases_of_x_years(data, argv.get("l"))

		if argv.get("t"):
			build_tenant_dictionary(data)

		if argv.get("d"):
			sdate = argv['d'][0]
			edate = argv['d'][1]
			get_rentals_between_dates(data, sdate, edate)

	except FileNotFoundError:
		print("File not found, maybe check spelling. Filename received:", argv.get("input"))

def build_tenant_dictionary(data):
	try:
		tenants = {}
		for record in data:
			tenant = record[6]
			matched = False
			# Check for similar key in tenants
			for key in tenants:
				if fuzz.ratio(key, tenant) > 51:  # Not ideal, but 50% similarity means Dood and Dodo match
					tenants[key] = tenants.get(key) + 1
					matched = True
			if not matched:
				tenants[tenant] = 1

		print("\n--------------- Tenants with rentals ---------------\n")
		print(json.dumps(tenants, indent=4))
	except Exception as e:
		raise Exception("Unable to build dictionary for tenants:", e)

def get_leases_of_x_years(data, years):
	"""
	Builds list from given data set for records with leases of given years
	:param data: list of mast data
	:return: list with leases of x years
	"""
	try:
		leases = list(filter(lambda x : (int(x[9]) == years), data))
		print("\n--------------- Leases of %d years ---------------\n" % years)
		pprint.pprint(leases, compact=True)
		print("\nTotal rent :", sum([float(x[10]) for x in leases]))
	except Exception as e:
		raise Exception("Unable to build list for leases of %d years:" % years, e)

def get_rentals_between_dates(data, sdate, edate):
	"""
	Builds list from given data set for records where lease is between 2 given dates
	:param data: list of mast data
	:param start_date: String datetime
	:param end_date: String datetime
	:return: list with rentals between the 2 given times
	"""
	try:
		print("\n--------------- Rentals between {} and  {} ---------------\n".format(sdate, edate))
		rentals = list(filter(lambda x : (dt.strptime(sdate, DATE_F) < dt.strptime(x[7], DATE_F) < dt.strptime(edate, DATE_F)), data))
		for rental in rentals:
			pprint.pprint(
				(rental[:7] + [dt.strptime(date, DATE_F).strftime("%d/%m/%Y") for date in rental[7:9]] + rental[9:]),
				compact=True
			)
	except Exception as e:
		raise Exception("Unable to build list for rentals between %s and %s:" % start_date, end_date, e)

def sort_by_current_rent(data):
	"""
	Sorts mast data by current rent
	:param data: list of mast data
	:return: sorted list
	"""
	try:
		data.sort(key=itemgetter(10))
		print("--------------- Sorted by rent ---------------\n")
		pprint.pprint(data[0:5], compact=True)
	except Exception as e:
		raise Exception("Unable to sort by current rent:", e)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', metavar="", help="Input filename")
	parser.add_argument('-s', action='store_true', help="Sort by rent")
	parser.add_argument('-l', metavar="", type=int, help="Get leases of x years")
	parser.add_argument('-t', action='store_true', help="Get tenants dictionary")
	parser.add_argument('-d', metavar="", nargs=2, type=str, help="Get rentals between two dates")
	args = parser.parse_args()
	main(vars(args))

