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

	if None in recipient:
		return {
			'status code':500,
			'body': 'Invailed Email Address'
		}	
	
	ses = boto3.client('ses', region = aws_region)

	try:
		response = ses.send_mail(
			Destination={
				'ToAddress':[
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
					subject
				},				
			},
			Source=sender
		)
		msgID = response['MessageID']
	
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print(f'message {msgID} sent!')
