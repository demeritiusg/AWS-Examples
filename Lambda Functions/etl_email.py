import boto3 
import json
from botocore.exceptions import ClientError


def nyc_trip_email(event, context):

	aws_region = 'us-east-1'
	CHARSET = "UTF-8"

	recipient = event['email_address']
	sender = event['automated_inbox']
	subject = event['email_subject']
	msg = event['event_msg']

	if not in recipient:
		return {
			'statusCode':400,
			'body': 'Invailed Email Address'
		}	
	
	ses = boto3.client('ses', region_name=aws_region)

	try:
		response = ses.send_email(
			Destination={
				'ToAddresses':[
					recipient
				]
			},
			Message={
				'Body': {
					'Text': {
						'Data': msg,
						'Charset': CHARSET
					},
				},
				'Subject': {
					'Data': subject,
					'Charset': CHARSET
				},				
			},
			Source=sender
		)
		msgID = response['MessageId']
	
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print(f'message {msgID} sent!')
