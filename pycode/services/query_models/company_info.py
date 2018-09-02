from py2neo import Graph, Node, Relationship
g = Graph('bolt://localhost:7687')


def get_company_all():
    df = g.run(
        "MATCH (a :company) RETURN a.company_id as company_id, a.name as name, a.industry as industry  LIMIT 4").data()
    print("\n\nDF = {}s".format(df))
    return df


def get_company_name(criteria):
    df = g.run(
        "MATCH (a :company) where a.name = '" + criteria + "' RETURN a.company_id as company_id, a.name as name, a.industry as industry  LIMIT 4").data()
    print("\n\nDF = {}s".format(df))
    return df


def get_company_industry(criteria):
    df = g.run(
        "MATCH (a :company) where a.industry = '" + criteria + "' RETURN a.company_id as company_id, a.name as name, a.industry as industry  LIMIT 4").data()
    print("\n\nDF = {}s".format(df))
    return df


get_company_all()
