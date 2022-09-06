# Unpacking query parameters
# E.g. Given the URI https://www.google.com/search?q=gray+squirrel&tbm=isch,
#      the code below extracts out the parameter "gray squirrel"

from urllib.parse import urlparse, parse_qs

address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)
# >>>print(parts)
# ParseResult(scheme='https', netloc='www.google.com', path='/search', 
# params='', query='q=gray+squirrel&tbm=isch', fragment='')

query = parse_qs(parts.query)
# >>> print(parts.query)
# q=gray+squirrel&tbm=isch
# >>> query
# {'q': ['gray squirrel'], 'tbm': ['isch']}

res = query["q"]
# >>> print(res)
# ['gray squirrel']