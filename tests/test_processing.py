import pytest
from src.processing import filter_by_status, sort_by_date


@pytest.fixture
def input_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 615064591, "state": "CANCELED"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
        {}
    ]


@pytest.mark.parametrize("state", ["EXECUTED", "CANCELED", None])
def test_filter_by_state_executed(input_list, state):
    filtered_list = filter_by_status(input_list, state=state)
    assert all(item.get("state", None) == state for item in filtered_list)
    for item in filtered_list:
        assert (item.get("state", None)) == state


@pytest.mark.parametrize("order", ["asc", "desc"])
def test_sort_by_date_ascending(input_list, order):
    sorted_list = sort_by_date(input_list, order=order)
    assert sorted_list == sorted(input_list, key=lambda x: x.get("date", ""), reverse=True if order == "asc" else False)
