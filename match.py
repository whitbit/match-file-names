import csv, json

ALL_URLS = {}
ALL_NAMES = {}

def get_csv_data(file):
    """
    Opens csv file and converts into a list of lists. [[, url]]

    """
    with open(file) as csvfile:
        companies = csv.reader(csvfile)
        return [company for company in companies]


# print get_csv_data('crm.csv')

def get_json_data(file):
    """
    Opens json file and converts json string to Python dictionary.

    """
    with open(file) as jsonfile:
        companies = json.load(jsonfile)
    return companies

def build_name_dict(json_file):
    names = {}

    json_data = get_json_data(json_file)
    # csv_data = get_csv_data(csv_file)

    for company in json_data:
        # print company
        names[company['name']] = company['id']
    # print names

    return names

def build_urls_dict(json_file):
    urls = {}

    json_data = get_json_data(json_file)

    for company in json_data:
        for url in company['urls']:
            urls[url] = company['id']

    return urls

# print build_urls_dict('db.json')


# print build_name_dict('db.json')
def set_up_data(json_file):
    global ALL_NAMES
    global ALL_URLS
    ALL_NAMES = build_name_dict(json_file)
    ALL_URLS = build_urls_dict(json_file)
    
    return

def find_matches_by_url(csv_data, matches_dict):

    for i in range(len(csv_data)):
        url = csv_data[i][1]
        if url in ALL_URLS:
            matches_dict[i] = matches_dict.get(i) + ', ' + ALL_URLS[url]

    return matches_dict


def find_matches_by_name(csv_data):
    """
    Matches names based on name property of json.

    """

    matches = {}
    
    for i in range(len(csv_data)):
        company_name = csv_data[i][0]
        if company_name in ALL_NAMES:
            matches[i] = ALL_NAMES[company_name]

    return matches




# def find_matches_by_
# def get_companies_to_revalidate():

# def find_unmatched_by_name(csv_file, json_file):

#     unmatched = []
#     csv_data = get_csv_data(csv_file)
#     json_data = get_json_data(json_file)

#     for i in range(1, len(csv_data)):
#         for company in json_data:
#             if csv_data[i][0] != company['name'] and csv_data[i] not in unmatched:
#                 unmatched.append(csv_data[i])

#     return unmatched

# print find_unmatched_by_name('crm.csv', 'db.json')

def write_matches(file, csv_file):

    csv_data = get_csv_data(csv_file)
    print len(csv_data)

    list_of_matches = find_matches_by_name(csv_data)
    print list_of_matches

    url_name_matches = find_matches_by_url(csv_data, list_of_matches)

    with open(file, 'w') as results_file:
        results_file.write('Matches')
        for i in range(len(csv_data)):
            if i in url_name_matches:
                print i
                results_file.write(url_name_matches[i] + '\n')
            else:
                results_file.write('\n')
        
set_up_data('db.json')




write_matches('company_matches.txt', 'crm1.csv')