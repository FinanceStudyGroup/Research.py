# Research.py
This is a document locator for quickly searching business descriptions.

-----------------------------------------------------------------------------------------------------------------
Using this document locator, you can quickly pull up business descriptions on any stock from a variety of sources.

Specifically, we can collect data from Reuters, Yahoo Finance, Seeking Alpha, Market Watch, Japan Stock Exchange, or EDINET, 
on any given stock within a coverage set or comparables universe.

-----------------------------------------------------------------------------------------------------------------

To run this program, be sure to get [Selenium](https://www.seleniumhq.org/), and the most recent releases of [Google Chrome](https://www.google.com/chrome/?brand=CHBF&utm_source=bing&utm_medium=cpc&utm_campaign=1005992%20%7C%20Chrome%20Win10%20%7C%20DR%20%7C%20ESS01%20%7C%20NA%20%7C%20US%20%7C%20en%20%7C%20Desk%20%7C%20BING%20SEM%20%7C%20BKWS%20~%20Top%20KWDS%20-%20Exact&utm_term=google%20chrome&utm_content=Google%20Chrome%20-%20Exact&ds_kid=43700010220923516&gclid=CNupzfPj--ACFduGxQIdWPcHaA&gclsrc=ds),
and [Chrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=2.46/).

The Selenium package for Python allows for automation of an instance of the web browser.

Specifically, we can write Python code to use the Selenium package to run Chrome Driver and control Google Chrome.

In this way, we can automate key research workflows, quickening the due diligence process.

From the command line, we might simply run,

```
python Research.py
```
after which, we will be prompted for a ticker symbol -- and as an example we might run,

Ticker:
```
REGN
```
and the site,

Site:
```
SeekingAlpha
```
where we'll quickly be directed to the Seeking Alpha business description profile for our chosen stock.

Note: EDINET (Electronic Disclosure for Investors Network) and JPX (Japan Stock Exchange) are for Japanese stocks,
where these are stated with a numerical designation, instead of a ticker. Website modes include: "Reuters", "YahooFinance",
"SeekingAlpha", "MarketWatch", "JPX", "EDINET", where these can be entered as raw strings without quotation marks.
