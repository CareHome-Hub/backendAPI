from ..query_models import random_spread_generator as rsg


def test_rsp():
    expected_total = 200
    expected_value_count = 5
    act = rsg.generate_spread_to_total(expected_total, expected_value_count)
    act_total = sum([x for x in act])
    assert expected_total == act_total
    assert expected_value_count == len(act)