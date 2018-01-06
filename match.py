import csv, json

def get_csv_data(file):
    """
    Opens csv file and converts into a list of lists.

    """
    with open(file) as csvfile:
        companies = csv.reader(csvfile)
        return [company for company in companies]
        # return len(companies)

print get_csv_data('crm.csv')

def get_json_data(file):
    """
    Opens json file and converts json string to Python dictionary.

    """
    with open(file) as jsonfile:
        companies = json.load(jsonfile)
    return companies

print get_json_data('db.json')[0]['name']

def find_matches(csv_file, json_file):
    pass


def write_matches(file):

    with open(file, 'w') as results_file:
        results_file.write('Matches')

write_matches('company_matches.txt')