
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Check website response
if response.status_code == 200:
    print("Website connected successfully!")

    # Read website HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        data.append({
            "Book Name": title,
            "Price": price,
            "Availability": availability
        })

    # Convert data into DataFrame
    df = pd.DataFrame(data)

    # Display output
    print("\nScraped Book Details:")
    print(df.to_string(index=False))

    # Save data into CSV file
    df.to_csv("books_data.csv", index=False)

    print("\nData saved successfully to books_data.csv")

else:
    print("Website connection failed:", response.status_code)
