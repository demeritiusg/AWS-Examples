import boto3 
import json
from botocore.exceptions import ClientError


def nyc_trip_email(event, context):

	aws_region = 'us-east-1'
	CHARSET = "UTF-8"

	sender = event.get('automated_inbox')
	subject = event.get('email_subject', 'No Subject')
	text_msg = event.get('event_msg', '')
	html_msg = event.get('event_html_msg')

	to_address = event.get('email_address')
	cc_address = event.get('cc_address', [])
	bcc_address = event.get('bcc_address', [])

	if isinstance(to_address, str):
		to_address = [to_address]
	if isinstance(cc_address, str):
		cc_address = [cc_address]
	if isinstance(bcc_address, str):
		bcc_address = [bcc_address]

	if not in to_addresses:
		return {
			'statusCode':400,
			'body': 'Invailed Email Address'
		}	
	
	ses = boto3.client('ses', region_name=aws_region)

	try:
		response = ses.send_email(
			Destination={
				'ToAddresses': to_address,
				'CcAddresses': cc_address,
				'BccAddresses': bcc_address
			},
			Message={
				'Body': {
					'Text': {
						'Data': text_msg,
						'Charset': CHARSET
					},
					'Html': {
						'Data': html_msg or f"<html><body><p>{text_msg}</p></body></html>",
						'Charset': CHARSET
					}
				},
				'Subject': {
					'Data': subject,
					'Charset': CHARSET
				},				
			},
			Source=sender
		)
		msgID = response['MessageId']
		print(f"Message {msgID} sent!")
		return{
			'statusCode': 200,
			'body': f"Message {msgID} sent successfully!"
		}
	
	except ClientError as e:
		error_message = e.response['Error']['Message']
		print(error_message)
		return{
			'statusCode': 500;
			'body': f"Error sending email: {error_message}"
		}
