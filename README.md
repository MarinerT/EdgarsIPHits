# Edgar's IP Hits: Has the global financial research market become more global?

## Introduction
This EDA looks at the log files of the Securities and Exchange Commission's EDGAR site from February 2003 and June 2017 to graph any changes in country distributions through geolocating IP addresses.

## Background
EDGAR is the SEC's database that houses the periodic financial statements, registrations, and other public declarations as required by law of publicly traded companies on US exchanges.  The US market represents approximately 53% of the global financial trade, making EDGAR a highly valuable resource for investors internationally. [statista.com] 

## Hypothesis
Globally, internet usage increased from 413 million people in 2000 to over 3.4 billion people in 2016 with the US representing approximately 50% in 2000 and 8% in 2016. [ourworldindata.org, statista.com] As such, we would expect the proportion of IP addresses designated for the US to decrease even slightly despite our global financial hegemony. 

Null Hypothesis: There has been no change or an increase in the proportion of hits on EDGAR.
Alternative Hypothesis: There has been a decrease in the proportion of hits on EDGAR.

## The Data
#### Size
Three log files each 7 years apart selected for the period JUNE 30 09:30:00 - 09:40:00, when both the New York and London stock exchanges are simultaneously open. 
```bash
ubuntu@ip-172-31-80-58:~/data$ sed -n /"09:30:00"/,/"09:40:00"/p log20100630.csv > openplustten2010.csv
ubuntu@ip-172-31-80-58:~/data$ sed -n /"09:30:00"/,/"09:40:00"/p log20030630.csv > openplustten2003.csv
ubuntu@ip-172-31-80-58:~/data$ sed -n /"09:30:00"/,/"09:40:00"/p log20170630.csv > openplustten2017.csv
```
2017 LOG > 153799

2010 LOG >  17600

2003 LOG >   1914

#### Features
**IP Address: Categorical**
The IP address consists of three numbers and three letters in the last octatet to conceal the user's identity.

**CIK: Categorical** 
The CIK represents the filer's registration number. This can be the company itself or a third party filer.

**Accession Number: Categorical**
The Accession number represents a serial number for the document filed. 

**Country: Categorical**
Represents the country of origin for the IP Address.

#### Unique Values
Number of Countries Represented:

Number of Documents:

Number of Filers:

#### NaN or Missing Data
The following columns had lack of relevant information: extention, code, size, idx, norefer, noagent, find, crawler, browser.

## The Methodology.

## Preliminary Results

**Top 10 Most common companies looked for in 2003 v 2016**
**Top Company looked for by Country**

## Future Research
**Browser** Looking at possible browsers used to obtain the documents can provide valuable. Determining trends in browser use could assist developers in prioritizing security features, as well as provide cyber combat units with possible attack vectors specified by country and time of day. 
