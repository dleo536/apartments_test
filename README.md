About:

This project is a real-world QA automation demo using Python, Selenium, and GitHub Actions CI. It simulates finding the closest apartment to a given address using Apartments.com and geospatial comparison.

Tech Stack

- Python 3.10
- Selenium WebDriver
- BeautifulSoup4
- Geopy (distance + geocoding)
- GitHub Actions for CI/CD
- Chrome + ChromeDriver (runs in headless mode)

---

Process

- Navigates to [Apartments.com](https://www.apartments.com)
- Searches rentals near St Paul, MN
- Scrapes listings and geocodes each address
- Finds the closest one to `767 N Eustis St, St Paul, MN`
- Uses `pytest` to verify the closest listing is **808 Berry St**

---

You can run this from the Actions tab of this repo. Or you can follow below to run locally.

How to Run Locally

```bash
# Set up Python
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run test
pytest test_apartments.py
```
