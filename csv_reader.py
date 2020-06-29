import  argparse

def main(argv):
	print(argv)

def sort_by_current_rent(data):
	"""
	Sorts mast data by current rent
	:param data: list of mast data
	:return: sorted list
	"""
	try:
		sorted_by_rent = sorted(data, key=itemgetter(10))
		print("--------------- Sorted by rent ---------------\n")
		pprint.pprint(sorted_by_rent[0:5], compact=True)
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

