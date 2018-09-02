#   Load Graph dataset/aud
from neo4j.v1 import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost:7687')


def create_touchpoint(medium, supplier):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run(" MERGE (t :touchpoint {type: '"+medium+"', supplier: '"+supplier+"'} )\
            return t")
