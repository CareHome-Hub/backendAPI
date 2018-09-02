import csv
from neo4j.v1 import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost:7687')


def create_static():
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("""
                CREATE (ind : INDUSTRY{ref: "A", title: "Finance"})
                CREATE (ind1 : INDUSTRY{ref: "B", title: "Capital Goods"})
                CREATE (ind2 : INDUSTRY{ref: "C", title: "Health Care"})
                CREATE (ind3 : INDUSTRY{ref: "D", title: "Technology"})
            
                CREATE (inc : INCOME_GROUP{ref: "A"})
                CREATE (inc1 : INCOME_GROUP{ref: "B"})
                CREATE (inc2 : INCOME_GROUP{ref: "C"})
                CREATE (inc3 : INCOME_GROUP{ref: "D"})
            
                CREATE (aud : AUDIENCE_GROUP{ref: "A"})
                CREATE (aud1 : AUDIENCE_GROUP{ref: "B"})
                CREATE (aud2 : AUDIENCE_GROUP{ref: "C"})
                CREATE (aud3 : AUDIENCE_GROUP{ref: "D"})
            
                CREATE (mrk : MARKETING_TARGET{ref: "A", title: "Increased Sales"})
                CREATE (mrk1 : MARKETING_TARGET{ref: "B", title: "Brand Awareness"})
                CREATE (mrk2 : MARKETING_TARGET{ref: "C", title: "Market Share"})
                CREATE (mrk3 : MARKETING_TARGET{ref: "D", title: "Promotion"})
            """)
