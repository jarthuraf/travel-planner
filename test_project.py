from project import calculate_budget, generate_itinerary
import pytest

def test_calculate_budget():
    assert calculate_budget(1000, 5) == 200
    assert calculate_budget(1500, 3) == 500

def test_calculate_budget_invalid_days():
    with pytest.raises(ValueError):
        calculate_budget(1000, 0)

def test_generate_itinerary():
    itinerary = generate_itinerary(3, "adventure")
    assert len(itinerary) == 3
    assert itinerary == [
        "Day 1: Enjoy a adventure activity.",
        "Day 2: Enjoy a adventure activity.",
        "Day 3: Enjoy a adventure activity."
    ]