import pytest

from project import get_style, validate_style, validate_days, format_destination
from utils.budget import calculate_daily_budget, budget_category
from utils.planner import generate_daily_plan


def test_calculate_daily_budget():
    assert calculate_daily_budget(1000, 5) == 200


def test_calculate_daily_budget_error():
    with pytest.raises(ValueError):
        calculate_daily_budget(1000, 0)


def test_budget_category():
    assert budget_category(30) == "Low Budget"
    assert budget_category(100) == "Moderate"
    assert budget_category(300) == "Luxury"


def test_generate_daily_plan():
    itinerary = generate_daily_plan(3, "adventure")

    assert len(itinerary) == 3
    assert "Day 1:" in itinerary[0]


def test_generate_daily_plan_invalid_style():
    with pytest.raises(ValueError):
        generate_daily_plan(3, "unknown")

def test_validate_style():
    assert validate_style("Luxury") == "luxury"
    assert validate_style("budget") == "budget"
    assert validate_style("Adventure") == "adventure"
    assert validate_style("Cultural") == "cultural"

def test_validate_style_invalid():
    with pytest.raises(ValueError):
        validate_style("unknown")

def test_validate_days():
    assert validate_days(5) == 5
    assert validate_days("5") == 5

def test_validate_days_invalid():
    with pytest.raises(ValueError):
        validate_days(0)
    with pytest.raises(ValueError):
        validate_days("invalid_string")

def test_format_destination():
    assert format_destination("  paris  ") == "Paris"
    assert format_destination("new york") == "New York"
    with pytest.raises(ValueError):
        format_destination("")