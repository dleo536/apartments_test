About:

This project is an automation demo using Python, Selenium, and GitHub Actions CI. Running through a scenario to generate regression testing necessary to make sure that Apartments.com search function works after new updates. I tried encorporating some geospatial validation for practice purposes.

Utillizing CI GitHub Actions to run test on script after every push.

I recorded a quick demo of it working locally. Sorry about the construction noise in the background.

https://www.loom.com/share/2d1d7c396edb4cb78311906effa96ffe?sid=d97c5d6e-a0da-4530-a36d-20983f66a986

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
- Uses `pytest` to verify the closest listing is 808 Berry St

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
pytest apartments_test.py
```
