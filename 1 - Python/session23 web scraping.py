# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:36:53 2024

@author: sai
"""
#WEBSCRAPING
#go on google and search for-> regex101.com
#STEPS:
#1.CHOOSE PYTHON LANGAUGAE
#2.CHOOSE THE SENTENCE
#3.CHOOSE THE PATTERN

""" removing special character
special character as you know are non-aplhanumeric character.
these character are most often found in comments references currency number etc
these character add no values to text understanding and induce noise ito alogorithm
for that regex pacakage is used"""

import re# enivornment > pip install regex
chat1='Hello I am having an issue with my order #412889912'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat1)
matches

chat2='I have a problem with my order number 412889912'
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches

chat3='my order 412889912 is having an issue, i was charged 300$ but online it says 280$'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches

# if we dont want to use re.findall 
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat1)

#18-06-2004
#how to extract email from chat
chat1='you ask lot of questions 12345678912,abc@xyz.com'
chat2='here it is:(123)-567-8912,abc@xyz.com'
chat3='yes,phone:12345678912 email:abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)
#output:Out[21]: 'abc@xyz.com'
#how to extract phone no from chat
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat3)
#output:1.('1234567891', '')
#putput:2('', '(123)-567-8912')
#output:3('1234567891', '')

text="""Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​"""

get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)\n',text).strip()
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
get_pattern_match(r'\(age.*\n(.*)',text)
#output 1:Out[31]: '52'
#output 2:'Elon Reeve Musk'
#output 3:Out[34]: 'June 28, 1971'
#output 4:Out[35]: 'Pretoria, Transvaal, South Africa'

#19-06-2024
#interview question 
#can function in python return multiple variable if yes then how 
#answer yes in regex also mutiple variables are return and another one yeild in this also it can be done 
#function return multiple variable with help of dictionary
def extract_personal_information(text):
    age = get_pattern_match('age (\d+)',text)
    full_name = get_pattern_match('Born(.*)\n',text)
    birth_date = get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place = get_pattern_match('\(age.*\n(.*)',text)
    return {
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)
#output:Out[20]: 
"""{'age': 52,
 'name': 'Elon Reeve Musk',
 'birth_date': 'June 28, 1971',
 'birth_place': 'Pretoria, Transvaal, South Africa'}"""


text="""Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)"""

get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)\n',text).strip()
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
get_pattern_match(r'\(age.*\n(.*)',text)
def extract_personal_information(text):
    age = get_pattern_match('age (\d+)',text)
    full_name = get_pattern_match('Born(.*)\n',text)
    birth_date = get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place = get_pattern_match('\(age.*\n(.*)',text)
    return {
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)
#output:Out[27]: 
"""{'age': 67,
 'name': 'Mukesh Dhirubhai Ambani',
 'birth_date': '19 April 1957',
 'birth_place': 'Aden, Colony of Aden'}"""
    
#how to extract information from pdf
from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader
#creating a pdf reader object
reader = PdfReader('c:/1 - python/kopargaon-part-1.pdf') 
#printing number of pages in pdf file
print(len(reader.pages))
page=reader.pages[1]
text=page.extract_text()
print(text)

from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader
#creating a pdf reader object
reader = PdfReader('c:/1 - python/matrix_basics.pdf') 
#printing number of pages in pdf file
print(len(reader.pages))
page=reader.pages[2]
text=page.extract_text()
print(text)

#20-06-2004
#extracting information from twitter
import re
sentence5="sharat twitted,wittnesing 68th republic day india from rajpath/new delhi,mesmorizing by indian army!"
re.sub(r'([^\s\w]|_)+', ' ',sentence5).split()
#output:Out[3]: 
"""['sharat',
 'twitted',
 'wittnesing',
 '68th',
 'republic',
 'day',
 'india',
 'from',
 'rajpath',
 'new',
 'delhi',
 'mesmorizing',
 'by',
 'indian',
 'army']"""
"""re.sub(r'([^\s\w]|_)+', ' ',sentence5).split() will replace some sequences of non alphanumeric character
(including puncuation but exculding whitespace) with a single space"""

#extracting n gram
#n gram can extracted by 3 techniques
#1.custom defined function
#2.nltk
#3.textblob

#extracting n-grams using custom defined function
import re
def n_gram_extractor(input_str, n):
    tokens = re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
n_gram_extractor("the cute little boy is playing with kitten",2)
"""output:['the', 'cute']
['cute', 'little']
['little', 'boy']
['boy', 'is']
['is', 'playing']
['playing', 'with']
['with', 'kitten']"""
n_gram_extractor("the cute little boy is playing with kiiten",3)
"""output:['the', 'cute', 'little']
['cute', 'little', 'boy']
['little', 'boy', 'is']
['boy', 'is', 'playing']
['is', 'playing', 'with']
['playing', 'with', 'kiiten']"""

#extract all twitter handle from following text
text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern = 'https://twitter.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)
#OUTPUT:Out[11]: ['elonmusk', 'teslarati', 'dummy_tesla', 'dummy_2_tesla']

#extract concentration risk types.
text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern='Concentration of Risk: ([^\n]*)'
re.findall(pattern,text)
#output:Out[14]: ['Credit Risk', 'Supply Risk']

#companies in europe reports their finacial number of semi annual basis
# and you can have document like this  to extract quareterly
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern = 'FY(\d{4} (?:Q[1-4]|S[1-2]))'
matches= re.findall(pattern,text)
matches
#output:Out[18]: ['2021 Q1', '2021 S1']

############
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern= '\(\d{3}\)-\d{3}-\d{4}|d{10}'
matches= re.findall(pattern,text)
matches
#output:Out[22]: ['(999)-333-7777']

text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern= 'Note \d - ([^\n]*)'
matches= re.findall(pattern,text)
matches
#output:Out[26]: ['Overview', 'Summary of Significant Accounting Policies']

#homeork:take any text from flipcart like review anthing and extract that like pattern

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern= 'FY\d{4} Q[1-4]'
matches=re.findall(pattern,text)
matches
#output:Out[11]: ['FY2021 Q1', 'FY2020 Q4']


text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern= 'FY\d{4} Q[1-4]'
matches= re.findall(pattern, text, flags=re.IGNORECASE)
matches
#output:Out[6]: ['FY2021 Q1', 'FY2020 Q4']