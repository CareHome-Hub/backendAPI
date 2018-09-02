##   Load Graph dataset/aud
import csv
from neo4j.v1 import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost:7687')


def read_csv_user(trg):
    with open(trg, newline='') as csvfile:
        csvdata = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvdata, None)  # skip the headers
        print("CSVDATA user = {}".format(csvdata))
        # return csvdata
        user = {}
        for item in csvdata:
            user['user_id'] = item[0]
            user['f_name'] = item[1]
            user['l_name'] = item[2]
            user['gmail'] = item[3]
            user['aud'] = item[4]
            user['gender'] = item[5]
            user['income'] = item[6]

            with driver.session() as session:
                with session.begin_transaction() as tx:
                    tx.run("""
                        CREATE (a :audience) SET a += {props}
                    """, {
                        "props": user
                    })

