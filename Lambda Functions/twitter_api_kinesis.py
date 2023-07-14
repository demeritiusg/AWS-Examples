import boto3
import base64
import json

def lambda_kenesis(event, context):
	for record in event['Records']:
		payload = base64.bs64decode(record["Kinesis"]["data"])
		
		
	data = re.sub('\W+','', payload)
	
	#TODO Format dates
	
	
	databasetem = {
		PutRequest: {
			Item: {
				ItemID: id,
				UserName: username,
				FirstName: fname,
				LastName: lname,
				StartData: stdate
				}
			}
		};
