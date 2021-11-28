def url_length(column):
  return pd.Series([len(i) for i in column])

def at_present(column):
  return pd.Series([ 1 if i.find("@") == -1 else -1 for i in column ])

def dash_present(column):
  return pd.Series([ 1 if i.find("-") == -1 else -1 for i in column ])

def redirect_present(column):
  flags = []
  for i in column:
    if i.find("https://") != -1 :
      i.replace("https://","")
    if i.find("http://") != -1 :
      i.replace("https://","")
    if i.find("//") != -1:
      flags.append(-1)
    else:
      flags.append(1)  
  return pd.Series(flags)

def check_domain_length(column):
  flags = []
  for i in column:
    parsed_url = parser.urlparse(i)
    # Calculating log to normalize the length and make it comparable to other features
    # flags.append(np.log(len(parsed_url.netloc)))
    flags.append(len(parsed_url.netloc))
  return pd.Series(flags)

def no_of_subdomains(column):
  flags = []
  for i in column:
    parsed_url = tldextract.extract(i)
    flags.append(len(parsed_url.subdomain.split(".")))
  return pd.Series(flags)


