import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, '5WDG1YZPWOHC9GMFC96YC3BTG19G9CQ9', 'VL9DV35XKDZ478CH', 'stage', '6302614123', 'srivilliranganath.s7@gmail.com', 'DEAR OWNER AN UNKOWN FACE IS DETECTED' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print (response.text)
