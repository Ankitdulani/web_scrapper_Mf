# WEB SCRAPPER FOR MUTUAL FUND's

This project is motivated due to unavailabity of single platform to compare Mutaul Fund's Performance, Returns and other data. Every Aggregator suggests fund based upon there analysis which questions there authenticity. To deal with these issues developed an automated data extraction using Selenium and BeautifulSoup on platform of PYTHON 3.6.

## Applications

* To check how much diversified our investment our on the basis of top 10 holding of a Mutual Fund. 
* Performance of Different Sector in Market
* General trends in Equity Sector Allocation of top Mutual Funds.
* Evaluate the actual return when fund is liquidated from expense ratio and rate of Inflation (exclusive of taxes).
* Risk Analysis Upon wider scale than "5 star Rating"

### Dependencies:

Selenium web automation browser
chrome driver
BeautifulSoup
Python 3.6

### For running the module
run the DataExtraction.py script 

### Output
This outputs 
The unprocessedLinks from the homepage of Groww.com
Json Document of Mutual Fund's Data 

#### Model:
{
  name: "Franklin India Low Duration Fund - Direct - Growth"
  Type_market: "Debt"
  Type_size: "Low Duration "
  Risk: "Moderate"
  Min SIP Amount: "₹500"
  Expense Ratio: "0.42%"
  NAV: "₹21.9 (18-Feb-2019)"
  Fund Started: "01-Jan-2013"
  Fund Size: "₹6,869 Cr"
  1Y: "9.1%"
  3Y: "9.4% p.a"
  5Y: "9.6% p.a"
  Total Securities: "75"
  Top 5: "19%"
  Top 20: "52%"
  Yield to Maturity: "10.20%"
  Average Maturity: "0.88 Yrs"
  Modified Duration: "0.76 Yrs"
  topHolding:[
    {
      "company_name":"xyz",
      "asset":"percentage",
      "sector":"string",
      "instrument":"string",
      "total_investment":"value"
    } 
  ]
  
  equitySectorAllocation:[
    {
      "sector":"string"
      "value": "percentage"
    }
  ]
}

#### Point to be noted:
Varry time.sleep() or the delay based upon the network bandwidth available. This may introduce latency but is more reliable when page don't load.

