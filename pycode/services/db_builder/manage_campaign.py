##   Load Graph dataset/aud
import csv
from neo4j.v1 import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost:7687')


def add_results_to_campaign():
    campaign_stats = {
        "campaign_ref": "",
        "campaign_target": 100,
        "campaign_audience": 100,
        "stats1": [10, 20, 3, 2, 65],
        "stats2": [10, 40, 9, 3, 38],
        "stats3": [10, 50, 11,  4, 25],
        "stats4": [10, 57, 14,  5, 14],
        "stats5": [10, 60, 15,  5, 10],
        "stats6": [10, 60, 15,  5, 10]
    }
    return campaign_stats


def read_csv_campaign(trg):
    with open(trg, newline='') as csvfile:
        csvdata = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvdata, None)  # skip the headers
        print("CSVDATA campaign = {}".format(csvdata))
        # return csvdata        for item in csvdata:
        campaign = {}
        for item in csvdata:
            campaign["company_id"] = item[0]
            campaign["target"] = item[1]
            campaign["audience"] = item[2]
            campaign["campaign"] = item[3]
            campaign["type"] = item[4]
            with driver.session() as session:
                with session.begin_transaction() as tx:
                    tx.run("""
                        CREATE (a :campaign) SET a += {props}
                    """, {
                        "props": campaign
                    })
