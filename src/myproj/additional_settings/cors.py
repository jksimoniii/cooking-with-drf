from corsheaders.defaults import default_headers


CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_REGEX_WHITELIST = (
    '.*expandshare.com',
)
CORS_ALLOW_HEADERS = list(default_headers) + [
    'revision',
    'version'
]
