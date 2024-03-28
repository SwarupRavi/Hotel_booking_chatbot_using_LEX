import boto3
#this script valides the chatbot's intents and choices provided by the user
client = boto3.client('lexv2-runtime',region_name='region',aws_access_key_id='private_key',aws_secret_access_key='secret_access_key')
print(client)

botId = "BOT_ID"
botAliasId = "BOT_Alias_ID"
localeId = "en_US"
sessionId = "SESSION_ID"
response = client.recognize_text(
    botId=botId,
    botAliasId=botAliasId,
    localeId=localeId,
    sessionId=sessionId,
    text='Book hotel')
response

print("Intent:",response['sessionState']['intent']['name'])
print("Next Action:",response['sessionState']['dialogAction']['type'])
print("Next Slot:",response['sessionState']['dialogAction']['slotToElicit'])
print("Prompt or Msg:",response['messages'][0]['content'])

response = client.recognize_text(
    botId=botId,
    botAliasId=botAliasId,
    localeId=localeId,
    sessionId=sessionId,
    text='bangalore')
print("Intent:",response['sessionState']['intent']['name'])
print("Next Action:",response['sessionState']['dialogAction']['type'])
print("Next Slot:",response['sessionState']['dialogAction']['slotToElicit'])
print("Prompt or Msg:",response['messages'][0]['content'])

response = client.recognize_text(
    botId=botId,
    botAliasId=botAliasId,
    localeId=localeId,
    sessionId=sessionId,
    text='21-03-2024')
print("Intent:",response['sessionState']['intent']['name'])
print("Next Action:",response['sessionState']['dialogAction']['type'])
print("Next Slot:",response['sessionState']['dialogAction']['slotToElicit'])
print("Prompt or Msg:",response['messages'][0]['content'])


response = client.recognize_text(
    botId=botId,
    botAliasId=botAliasId,
    localeId=localeId,
    sessionId=sessionId,
    text='3')
print("Intent:",response['sessionState']['intent']['name'])
print("Next Action:",response['sessionState']['dialogAction']['type'])
print("Next Slot:",response['sessionState']['dialogAction']['slotToElicit'])
print("Prompt or Msg:",response['messages'][0]['content'])

response = client.recognize_text(
    botId=botId,
    botAliasId=botAliasId,
    localeId=localeId,
    sessionId=sessionId,
    text='king')
response

response = client.recognize_text(
    botId=botId,
    botAliasId=botAliasId,
    localeId=localeId,
    sessionId=sessionId,
    text='Yes')
response

