import csv, json

def get_csv_data(file):
    """
    Opens csv file and converts into a list of lists.

    """
    with open(file) as csvfile:
        companies = csv.reader(csvfile)
        return [company for company in companies]


def get_json_data(file):
    """
    Opens json file and converts json string to Python dictionary.

    """
    with open(file) as jsonfile:
        companies = json.load(jsonfile)
    return companies

def find_matches_by_name(csv_file, json_file):
    """
    Matches names based on name property of json.

    """

    matches = []
    
    csv_data = get_csv_data(csv_file)

    json_data = get_json_data(json_file)

    for i in range(1, len(csv_data)):
        for company in json_data:
            if csv_data[i][0] == company['name']:
                matches.append(company['id'])

    return matches

# print find_matches_by_name('crm.csv', 'db.json')


def write_matches(file, csv_file, json_file):

    list_of_matches = find_matches_by_name(csv_file, json_file)

    with open(file, 'w') as results_file:
        results_file.write('Matches \n')
        for name in list_of_matches:
            results_file.write(name + ', \n')
        

write_matches('company_matches.txt', 'crm.csv', 'db.json')