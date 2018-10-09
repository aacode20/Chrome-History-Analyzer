import os
import sqlite3
import matplotlib.pyplot as pyplot
import operator
from collections import OrderedDict

def parse(url):
    try:
        parsed_url = url.split('//')
        parsed_url = parsed_url[1]
        parsed_url = parsed_url.split('/',1)
        domain = parsed_url[0].replace("www.", "")
        return domain
    except IndexError:
        print("URL formatted incorrectly")


def analyze(results):

    prompt = input("Enter 'print' to print in console or 'plot' to plot a bar graph")

    if prompt == "print":
        for site, count in sorted_sitecount.items():
            print(site, count)

    elif prompt == "plot":
        pyplot.bar(range(len(newval)), newval, align='edge')
        pyplot.xticks(rotation=45)
        pyplot.xticks(range(len(newkey)), newkey)
        pyplot.show()

    else:
        print("Wrong input")
        quit()

    return





#Getting the raw path to a database file named history, user agnostic
data_path = os.path.expanduser('~') + r"\AppData\Local\Google\Chrome\User Data\Default"

history_db = os.path.join(data_path,'history')


connection = sqlite3.connect(history_db)
cursor = connection.cursor()
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)

results = cursor.fetchall()

sites_count = {}

for url, count in results:
    url = parse(url)
    if url in sites_count:
        sites_count[url] += 1
    else:
        sites_count[url] = 1

sorted_sitecount = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))

values = []
keys = []

for site, count in sorted_sitecount.items():
    values.append(count)
    keys.append(site)

newval = values[0:10]
newkey = keys[0:10]

analyze(sorted_sitecount)

