# General
DEBUG = False
USE_PROXY = False

# Caching
MEMCACHED_SERVER = ['127.0.0.1:11211']
SQUID_CACHE_INDEX = 60 * 5 # Mesaured in seconds (ex: 60 * 5 = 5 Minutes)
SQUID_CACHE_PAGE = 60 * 5
SQUID_CACHE_POST = 60 * 5
