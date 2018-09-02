#   Load Graph dataset/aud
import csv
from neo4j.v1 import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost:7687')


def read_csv(trg):
    with open(trg, newline='') as csvfile:
        csvdata = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvdata, None)  # skip the headers
        print("CSVDATA company = {}".format(csvdata))
        # return csvdata
        company = {}
        for item in csvdata:
            company["company_id"] = item[0]
            company["name"] = item[1]
            company["industry"] = item[2]
            with driver.session() as session:
                with session.begin_transaction() as tx:
                    tx.run("""
                        CREATE (a :company) SET a += {props}
                    """, {
                        "props": company
                    })
