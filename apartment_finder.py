def find_closest_apartment():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium_stealth import stealth
    from bs4 import BeautifulSoup
    from geopy.geocoders import Nominatim
    from geopy.distance import geodesic
    import time

    # Setup headless Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

    # Launch Chrome
    driver = webdriver.Chrome(options=options)

    # Apply stealth
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="MacIntel",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    # Geocode target address
    TARGET_ADDRESS = "767 N Eustis St, St Paul, MN 55114"
    geolocator = Nominatim(user_agent="qa_test")
    target_location = geolocator.geocode(TARGET_ADDRESS, timeout=10)
    if not target_location:
        raise Exception(f"Could not geocode target address: {TARGET_ADDRESS}")
    target_coords = (target_location.latitude, target_location.longitude)

    # Search apartments.com
    driver.get("https://www.apartments.com/")
    time.sleep(5)

    search_box = driver.find_element(By.ID, "quickSearchLookup")
    search_box.clear()
    search_box.send_keys("St Paul, MN")
    time.sleep(1)

    search_button = driver.find_element(By.CSS_SELECTOR, "button.typeaheadSearch")
    search_button.click()
    time.sleep(10)

    # Scrape listings
    soup = BeautifulSoup(driver.page_source, "html.parser")
    listings = soup.select(".placard .property-address")

    closest_listing = None
    min_distance = float('inf')

    def safe_geocode(address, retries=3, delay=1, timeout=10):
        for attempt in range(retries):
            try:
                loc = geolocator.geocode(address, timeout=timeout)
                if loc:
                    return loc
            except Exception:
                time.sleep(delay)
        return None

    for listing in listings:
        address = listing.text.strip()
        loc = safe_geocode(address)
        time.sleep(1)
        if loc:
            distance = geodesic(target_coords, (loc.latitude, loc.longitude)).miles
            if distance < min_distance:
                min_distance = distance
                closest_listing = (address, distance)

    driver.quit()

    if closest_listing:
        print(f"✅ Closest rental: {closest_listing[0]}")
        print(f"📍 Distance: {closest_listing[1]:.2f} miles")
        return closest_listing[0]
    else:
        print("⚠️ No valid rental addresses found.")
        return None
