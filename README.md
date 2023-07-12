# web_scraping
Used __Requests__ and __Beutifulsoup__ to scrap [the website](http://books.toscrape.com/index.html) <br>
this website is commonly used to practice scraping it is an easy website to work with <br>
that have just an easy HTML page nothing crazy such as __Javascript__, login sessions ..etc  <br>
I got it from: [best-websites-to-practice-your-web-scraping-skills](https://proxyway.com/guides/best-websites-to-practice-your-web-scraping-skills)

# Outline of what I did in this project:
### 1. Created a __Virtual envirenment__.
### 2. Installed the required packages (check [requirements.txt](https://github.com/ilyesBoukraa/web_scraping/blob/main/requirements.txt) ).
### 3. Used __Requests__ and __Beutifulsoup__ for scraping.
### 4. Extracted the html page with the __UTF-8__ coding then grab the desired data namely the name and price of every book in the main page.   
### 5. Used a Dataclass decorator to initialize a __ProductData__ class that we later on used to save the data with it elegantly (should fall into the best practices road).   
### 6. Used __Pandas__ to save the extracted data and to display it using __.head()__ method (check [displaying_csv.py](https://github.com/ilyesBoukraa/web_scraping/blob/main/displaying_csv.py) ).
### 7. A library called __Click__ was used to make the __CLI__.

# To run this code: 
You just need to write that in the terminal: <br> 
python scraper.py <url_link>  <the-csv-file-name.csv> 
