#!/usr/bin/python
# ------------------------------------------------------------------------------
# Research Terminal
# ------------------------------------------------------------------------------

# Import required packages
import sys, os, re, subprocess, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ------------------------------------------------------------------------------
Ticker = raw_input("Ticker: ")
Site = raw_input("Site: ")
# ------------------------------------------------------------------------------

driver = webdriver.Chrome()

if Site == "Reuters":
    # Go to Reuters
    # Link to the profile page
    Reuters = ("https://www.reuters.com/finance/stocks/company-profile/")
    # Restate the link, appending the ticker symbol
    Reuters = Reuters + Ticker
    # Locate Reuters company profile page
    driver.get(Reuters)
    
elif Site == "YahooFinance":
    # Go to YahooFinance
    # Link to the profile page
    YahooFinanceProfile = ("https://finance.yahoo.com/quote/"+Ticker+"/profile?p="+Ticker)
    # Locate Reuters company profile page
    driver.get(YahooFinanceProfile)
    
elif Site == "SeekingAlpha":
    # Go to SeekingAlpha
    # Link to the profile page
    SeekingAlphaProfile = ("https://seekingalpha.com/symbol/"+Ticker+"/overview")
    # Locate Seeking Alpha company profile page
    driver.get(SeekingAlphaProfile)
    
elif Site == "MarketWatch":
    # Go to MarketWatch
    # Restate the ticker symbol in lower case
    Ticker = Ticker.lower()
    # Link to the profile page
    MarketWatch = ("https://www.marketwatch.com/investing/stock/"+Ticker+"/profile")
    # Locate MarketWatch company profile page
    driver.get(MarketWatch)
    
elif Site == "JPX":
    # Go to Japan Stock Exchange business descriptions
    # Link to the profile page
    JPX = ("https://quote.jpx.co.jp/jpx/template/quote.cgi?F=tmp/e_bus_summary&QCODE="+Ticker)
    # Locate JPX company profile page
    driver.get(JPX)
    
elif Site == "EDINET":
    # Go to EDINET Annual Reports
    # Link to EDINET page
    #EDINET = ("http://disclosure.edinet-fsa.go.jp/EKW0EZ1001.html?fbclid=IwAR3_bkXMRbXIoYA5nNKBTVOuxtLCaZShMASLeAKQbycREBftMnqJKWT7INU")
    EDINET = ("https://disclosure.edinet-fsa.go.jp/E01EW/BLMainController.jsp?uji.bean=ee.bean.parent.EECommonSearchBean&uji.verb=W0EZA240CXP001007BLogicE&TID=W1E63012&PID=currentPage&SESSIONKEY=&lgKbn=1&dflg=0&iflg=0")
    driver.get(EDINET)
    time.sleep(2)
    Search = driver.find_element_by_css_selector("#mul_t")
    Search.click()
    Search.clear()
    Search.send_keys(Ticker)
    time.sleep(1)
    Search = driver.find_element_by_css_selector("#sch")
    Search.click()