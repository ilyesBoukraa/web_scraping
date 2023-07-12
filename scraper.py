import requests
import click 
import pandas as pd
#from selectolax import HTMLParser 
from dataclasses import dataclass 
from bs4 import BeautifulSoup

@dataclass
class ProductData:
    name:str
    price:str

def get_data(my_url):
    #headers = {}
    response = requests.get(url=my_url) #, headers=headers)
    return BeautifulSoup(response.content.decode('utf-8', 'ignore') , 'html.parser')


def parse_data(soup):
    products = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    scraped_data = []
    for product in products:
        name_element = product.find('h3').find('a') 
        price_element = product.find('div', class_='product_price').find('p', class_='price_color') 
         
        name = name_element.get('title', '') if name_element else ''
        price = price_element.get_text(strip=True) if price_element else ''

        scraped_data.append(ProductData(name=name, price=price))

    return scraped_data


@click.command()
@click.argument("url")
@click.argument("output_file")

def scrape(url, output_file):
    soup  = get_data(url)
    data = parse_data(soup)
    #print(data)
    # Create a pandas DataFrame from the scraped data
    df = pd.DataFrame(data, columns=['name', 'price'])


    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

    print(f"Scraped data saved to {output_file}.")

    # do something with that data
    # example print it!
"""     for i in range(len(data)):
        print(f'Book {data[i].name} price: {data[i].price}')
 """


if __name__=="__main__":
    scrape()