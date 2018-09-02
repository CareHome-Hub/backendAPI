from py2neo import Graph, Node, Relationship
g = Graph('bolt://localhost:7687')


def get_campaign_count_by_target():
    df = g.run(
        "match (c :campaign)-[t:TARGET_TYPE]-(m) return m.title as target, count(c) as count order by target DESC").data()
    print("\n\nDF = {}s".format(df))
    return df

