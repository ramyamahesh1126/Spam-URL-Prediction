import tarfile
import pandas as pd
import numpy as np

#For feature engineering
import tldextract 
import urllib.parse as parser
import dns.resolver as dns
import time

def feature_extraction(url):
  fields = ["url_length","at_present","dash_present","redirect_present","check_domain_length","no_of_subdomains"]
  feature_1=len(url)
  if url.find("@") == -1:
    feature_2 = 1
  else:
    feature_2 = -1
  if url.find("-") == -1:
    feature_3 = 1
  else:
    feature_3 = -1
  if url.find("https://") != -1 :
    url.replace("https://","")
  if url.find("http://") != -1 :
    url.replace("https://","")
  if url.find("//") != -1:
    feature_4 = -1
  else:
    feature_4 = 1
  parsed_url = parser.urlparse(url)
  feature_5=len(parsed_url.netloc)
  parsed_url = tldextract.extract(url)
  feature_6=len(parsed_url.subdomain.split("."))
  return pd.DataFrame([[feature_1,feature_2,feature_3,feature_4,feature_5,feature_6]],columns=fields)
