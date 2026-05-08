from rich.console import Console

console = Console()

# Trip class to hold trip details and calculate budget per day
class Trip:
    def __init__(self, destination, budget, days, style):
        self.destination = destination
        self.budget = budget
        self.days = days
        self.style = style

    def budget_per_day(self):
        return self.budget / self.days

    def summary(self):
        return (
            f"\nTrip to {self.destination}\n"
            f"Budget: ${self.budget}\n"
            f"Days: {self.days}\n"
            f"Style: {self.style}\n"
            f"Daily Budget: ${self.budget_per_day():.2f}\n"
        )
    
    
# Function to get user input for destination
def get_destination():
    destination = input("Enter destination: ").strip()

    if not destination:
        raise ValueError("Destination cannot be empty.")

    return destination


# Function to get user input for budget
def calculate_budget(budget, days):
    if days <= 0:
        raise ValueError("Days must be greater than 0.")

    return budget / days


# Function to generate a travel itinerary based on the trip details
def generate_itinerary(days, style):
    itinerary = []

    for day in range(1, days + 1):
        itinerary.append(f"Day {day}: Enjoy a {style} activity.")

    return itinerary


# Main function to run the travel planner
def main():
    console.print("[bold cyan]Travel Planner[/bold cyan]")

    try:
        destination = get_destination()
        budget = float(input("Enter your total budget: "))
        days = int(input("Enter number of days: "))
        style = input("Travel style (luxury, budget, adventure): ")

        trip = Trip(destination, budget, days, style)

        console.print(trip.summary())

        itinerary = generate_itinerary(days, style)

        console.print("[bold green]Suggested Itinerary:[/bold green]")

        for item in itinerary:
            console.print(item)

    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")


if __name__ == "__main__":
    main()