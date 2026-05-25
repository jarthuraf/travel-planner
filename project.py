import json

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from utils.planner import generate_daily_plan
from utils.budget import calculate_daily_budget, budget_category
from utils.api import get_weather

console = Console()

# Trip class to hold trip details and calculate budget per day
class Trip:
    def __init__(self, destination, budget, days, style, weather=None):
        self.destination = destination
        self.budget = budget
        self.days = days
        self.style = style.lower()
        self.weather = weather

    def budget_per_day(self):
        return calculate_daily_budget(self.budget, self.days)
    
    def budget_type(self):
        return budget_category(self.budget_per_day())
    
    def generate_itinerary(self):
        return generate_daily_plan(self.days, self.style)
    
    def save_trip(self):
        trip_data = {
            "destination": self.destination,
            "budget": self.budget,
            "days": self.days,
            "style": self.style
        }

        filename = f"saved_trips/{self.destination.lower()}_trip.json"
        with open(filename, "w") as file:
            json.dump(trip_data, file, indent=4)

    def summary_table(self):
        table = Table(title="Trip Summary")

        table.add_column("Category", style="cyan")
        table.add_column("Details", style="green")

        table.add_row("Destination", self.destination)
        table.add_row("Budget", f"${self.budget}")
        table.add_row("Days", str(self.days))
        table.add_row("Style", self.style.title())
        table.add_row("Daily Budget", f"${self.budget_per_day()}")
        table.add_row("Budget Type", self.budget_type())

        if self.weather:
            weather_string = f"{self.weather['temp']}°C, {self.weather['description']}"
            table.add_row("Current Weather", weather_string)
        else:
            table.add_row("Current Weather", "[yellow]Unavailable[/yellow]")

        return table
    

# Function to get user input for destination
def get_destination():
    destination = input("Enter destination: ").strip()
    return format_destination(destination)

# Function to format destination
def format_destination(destination):
    try:
        formatted = destination.strip().title()
    except AttributeError:
        raise ValueError("Destination must be a string.")
    
    if not formatted:
        raise ValueError("Destination cannot be empty.")
    
    return formatted


# Function to get user input for budget
def get_budget():
    budget = float(input("Total Budget: "))

    if budget <= 0:
        raise ValueError("Budget must be positive.")

    return budget


# Function to get user input for number of days
def get_days():
    days = int(input("Number of Days: "))
    return validate_days(days)

# Function to validate number of days
def validate_days(days):
    try:
        days = int(days)
    except ValueError, TypeError:
        raise ValueError("Days must be an integer.")
    
    if days <= 0:
        raise ValueError("Days must be greater than zero.")
    return days


# Function to get user input for travel style
def get_style():
    style = input(
        "Travel Style (luxury, budget, adventure, cultural): ")
    return validate_style(style)

# Function to validate style
def validate_style(style):
    style = style.lower().strip()
    valid_styles = ["luxury", "budget", "adventure", "cultural"]

    if style not in valid_styles:
        raise ValueError("Invalid travel style.")
    return style


# Main function to run the travel planner
def main():
    console.print(
        Panel.fit(
            "[bold cyan]Travel Planner[/bold cyan]",
            border_style="blue"
        )
    )

    try:
        destination = get_destination()
        budget = get_budget()
        days = get_days()
        style = get_style()
        weather_data = get_weather(destination)

        trip = Trip(destination, budget, days, style, weather=weather_data)

        console.print(trip.summary_table())

        console.print("\n[bold green]Suggested Itinerary[/bold green]")

        itinerary = trip.generate_itinerary()

        for item in itinerary:
            console.print(f"- {item}")
        trip.save_trip()
        console.print(f"\n[bold blue]Trip saved successfully![/bold blue]")

    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")


if __name__ == "__main__":
    main()