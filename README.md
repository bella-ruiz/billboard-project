#10-year Billboard Hot 100 Chart Scraper

This code scrapes the Billboard Hot 100 Chart over the past 10 years on a given day in March.  I wanted to assess the results to see which artists had the most hits over the past decade.  I scraped rank in the chart, song title, artist name and year.

##How I constructed my program
First, I had to get all the URLs for the past 9 years and put them in a list.  The current year (2022) is stored in the test_url variable as simply `/`.  
I create an empty list, big_list, for use later. 
Starting with my main chart, I used BeautifulSoup to extact the rank, title, artist, and year[^1] data.  I appended each item to a smaller list, to create one list for one entry.  I then stripped the lines and appended these lists to my big_list, and returned that.

My second function creates a writer object and scrapes each url with a for/loop. 



[^1]:I got year data from the chart URLs before the current year. In the case of the current year, there is no year to extract from the current URL (www.billboard.com/charts/hot-100/).  I used an if/else statement to append "2022" for the year if "2" is not in the URL.
