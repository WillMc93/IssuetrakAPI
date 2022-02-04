from uuid import uuid4
from urllib.parse import urlparse
from hashlib import sha512
from datetime import datetime
import hmac
import json
import base64
import http.client

SITE_URL = 'https://harbert.issuetrak.com/api/v1'
API_KEY_PATH = 'key.api'

def read_APIkey():
    key = ''
    with open(API_KEY_PATH) as kf:
        key = kf.readline().strip()
    return key

class IssuetrakAPI:
    __apiKey = ""
    __siteUrl = ""

    def __init__(self, apikey=read_APIkey(), siteUrl=SITE_URL):
        self.__apiKey = apikey
        self.__siteUrl = siteUrl

    def __generateMessageToHash(self, httpVerb, requestId, requestTimeStamp, absoluteUrlPath, requestQuery = "", requestBody = ""):
        return "\n".join([httpVerb, requestId, requestTimeStamp, absoluteUrlPath, requestQuery, requestBody])

    def __computeHash(self, apiKey, messageToBeHashed):
        hashText = None
        hashKeyBytes = bytes(apiKey, 'UTF-8')
        messageToBeHashedBytes = bytes(messageToBeHashed, 'UTF-8')

        hmacHash = hmac.new(hashKeyBytes, messageToBeHashedBytes, sha512).digest()
        hashText = base64.b64encode(hmacHash).decode('UTF-8')
        
        return hashText

    @staticmethod
    def __getUtcDate():
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f0Z")

    def __getConnection(self, protocol, url):
        return http.client.HTTPConnection(url, 80) if (protocol == "http") else http.client.HTTPSConnection(url, 443)

    def __generateHeaders(self, requestId, requestTimestamp, hashedMessage):
        return {
            "X-IssueTrak-API-Request-ID": requestId,
            "X-IssueTrak-API-Timestamp": requestTimestamp,
            "X-IssueTrak-API-Authorization": hashedMessage,
            "content-type": "application/json"
        }

    def __performApiCall(self, httpVerb, endpointUrl, requestQuery = "", requestBody = ""):
        fullUrl = f"{self.__siteUrl}{endpointUrl}"
        urlParts = urlparse(fullUrl)
        baseUrl = urlParts.netloc.lower()
        absolutePath = urlparse(fullUrl).path.lower()
        requestId = str(uuid4()).lower()
        requestTimestamp = self.__getUtcDate()
        messageToHash = self.__generateMessageToHash(httpVerb, requestId, requestTimestamp, absolutePath, requestQuery, requestBody)
        hashedMessage = self.__computeHash(self.__apiKey, messageToHash)
        
        connection = self.__getConnection(urlParts.scheme, baseUrl)
        headers = self.__generateHeaders(requestId, requestTimestamp, hashedMessage)

        connection.request(httpVerb, fullUrl, requestBody, headers)
        return connection.getresponse()

    def performGet(self, endpointUrl):
        return self.__performApiCall("GET", endpointUrl)

    def performPost(self, endpointUrl, requestQuery = '', requestBody = ''):
        return self.__performApiCall("POST", endpointUrl, requestQuery, requestBody)

    def performPut(self, endpointUrl, requestQuery = '', requestBody = ''):
        return self.__performApiCall("PUT", endpointUrl, requestQuery, requestBody)

