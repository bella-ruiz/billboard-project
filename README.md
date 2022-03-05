# 10-year Billboard Hot 100 Chart Scraper

This code scrapes the Billboard Hot 100 Chart over the past 10 years on a given day in March.  I wanted to assess the results to see which artists had the most hits over the past decade.  I scraped rank in the chart, song title, artist name and year.

## How I constructed my program

### `scrape_chart()` Function
First, I had to get all the URLs for the past 9 years and put them in a variable, `url_list`.  The current year (2022) is stored in the test_url variable as simply `/`.  

I create an empty list, `big_list`, for use later.

Starting with my main chart, I used BeautifulSoup to extract the rank, title, artist, and year[^1] data.  I appended each item to a new list, `list`, to create one list for one entry.  

I then stripped the lines and appended these lists to my big_list, and returned that.
### `write_to_csv()` Function
My second function creates a writer object and scrapes each url in my `url_list`with a for/loop containing the `scrape_chart` function. Each time it loops, I write the data from each listing into `list`, which is then tossed into the `big_list`.[^2]


[^1]:I got year data from the chart URLs before the current year. In the case of the current year, there is no year to extract from the current URL (www.billboard.com/charts/hot-100/).  I used an if/else statement to append "2022" for the year if "2" is not in the URL.

[^2]: To clarify: Each time `scrape_chart` is called, the function scrapes `rank`, `title`, `artist` and `year` for all hits in one year and puts that in `list`. Then it drops that list into `big_list`.  When I call `write_to_csv`, the `scrape_chart` function will run through my `url_list` and write the information from each into the CSV.
