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
Number of Countries Represented: 2003: 21; 2010: 47; 2017: 69

Number of Documents: 2003: 1186; 2010: 7659; 2017: 77710

Number of Filers: 2003: 684; 2010: 5217; 2017: 22705

#### NaN or Missing Data
The following columns had lack of relevant information: extention, code, size, idx, norefer, noagent, find, crawler, browser.
Additionally the 2010 Log is missing a country for 299 entries.
## Analysis

![US v Globe] (https://github.com/MarinerT/EdgarIPHits/data/usvgb.png)

#### Hypothesis Testing
**Hypothesis Test for Difference in Proportions**
We would expect the same proportion of US Hits in 2017 as US Hits in 2010. 

H<sub>*0*</sub>: *p<sub>2017</sub>* = *p<sub>2010</sub>*  

H<sub>*A*</sub>: *p<sub>2017</sub>* < *p<sub>2010</sub>* 

alpha = .05
The sample is random, normal, independent, and does not represent more than 10% of the population.



## Future Research
**Browser** Looking at possible browsers used to obtain the documents can provide valuable. Determining trends in browser use could assist developers in prioritizing security features, as well as provide cyber combat units with possible attack vectors specified by country and time of day. 
