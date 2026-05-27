# 🌍 External API-Driven Travel Planner

A dynamic, command-line interface (CLI) Python application built for the CS50p final project. This application generates customized, real-time travel itineraries and financial breakdowns by integrating external web services, utilizing object-oriented programming, and ensuring robustness through automated test suites.

---

## 🚀 Features

* **Live Weather Integration:** Fetches real-time temperature and climate conditions for the destination using the **OpenWeatherMap API**.
* **Location-Based Attractions Lookup:** Performs a two-step geocoding and spatial lookup via the **Geoapify API** to suggest real, verified local points of interest matching the user's travel style.
* **Adaptive Fallback Logic:** Engineered with defensive programming parameters; if external APIs are unreachable, the system automatically falls back to an internal algorithmic data matrix to ensure uninterrupted user experience.
* **Encapsulated Architecture:** Built around a core `Trip` domain class managing state, budget computations, and data serialization.
* **Data Persistence:** Automatically serializes and saves finalized trip details and structures to formatted `.json` files.
* **Visual CLI:** Renders structured tables, clean panels, and colorized terminals utilizing the `rich` ecosystem.

---

## 🛠️ Technical Architecture & Data Flow

The application isolates user input interaction, data validation, domain logic, and external network communication into independent, cohesive modules:

* `project.py`: The entry point managing the main runtime loop, terminal input processing, and validated user interfaces.
* `utils/api.py`: Infrastructure layer managing network requests (`requests`), payload extraction, and secure environmental credential handling.
* `utils/planner.py`: Core logic for distributing activities dynamically across the itinerary timeframe.
* `utils/budget.py`: Functional utility engine evaluating daily budget splits and tracking expense categories.

---

## 📦 Installation & Setup

### Prerequisites
* Python 3.8 or higher
* Active API keys for OpenWeatherMap and Geoapify

### 1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/travel-planner.git
cd travel-planner

### 2. Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Environment Variables Configuration
Create a `.env` file in the root directory of the project to securely map your API keys:
WEATHER_API_KEY=your_openweathermap_api_key
MAP_API_KEY=your_geoapify_api_key

---

## 🎮 Usage

Execute the main controller script to start the interactive wizard:
python project.py

### Example Walkthrough
1. **Destination:** London
2. **Total Budget:** 1500
3. **Number of Days:** 5
4. **Travel Style:** cultural

The program will output a dynamically generated UI table featuring local metrics, compile live attractions like the Tate Modern into a daily sequence, and commit the final itinerary safely to the saved_trips/ archive.

---

## 🧪 Testing

Automated unit tests ensure data integrity across inputs, state modification, and boundary parameters. The suite utilizes pytest to validate pure operations independently of console input wrappers.

Run the test suite using:
pytest