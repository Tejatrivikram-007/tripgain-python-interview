import json
from datetime import datetime
from playwright.sync_api import sync_playwright


def search_flights(origin: str, destination: str, journey_date: str) -> list:
    """Automates flight search and extracts flight details."""
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Step 1: Open website
        page.goto("https://www.budgetticket.in", timeout=30000)
        page.wait_for_load_state("domcontentloaded")

        # Step 2: Fill flight search form
        page.fill("input[placeholder='From']", origin)
        page.fill("input[placeholder='To']", destination)
        page.fill("input[type='date']", journey_date)
        page.click("button:has-text('Search')")

        # Step 3: Wait for flight results
        page.wait_for_selector(".flight-card", timeout=30000)

        # Step 4: Extract flight details
        cards = page.query_selector_all(".flight-card")
        for card in cards:
            airline = card.query_selector(".airline-name").inner_text() if card.query_selector(".airline-name") else ""
            flight_no = card.query_selector(".flight-number").inner_text() if card.query_selector(".flight-number") else ""
            dep = card.query_selector(".departure-time").inner_text() if card.query_selector(".departure-time") else ""
            arr = card.query_selector(".arrival-time").inner_text() if card.query_selector(".arrival-time") else ""
            price = card.query_selector(".price").inner_text() if card.query_selector(".price") else ""

            results.append({
                "airline": airline,
                "flight_number": flight_no,
                "departure": dep,
                "arrival": arr,
                "price": price,
                "origin": origin,
                "destination": destination,
                "searchdatetime": datetime.utcnow().isoformat() + "Z"
            })

        browser.close()

    # Step 5: Save to JSON file
    with open("flight_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"Total Flights Extracted: {len(results)}")
    return results


# Run independently for testing
if __name__ == "__main__":
    search_flights("Bangalore", "Delhi", "2025-10-20")
