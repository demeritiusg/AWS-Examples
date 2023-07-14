import boto3 
import json


# event is file landing in s3. email sent to team that file has been processed and loading to redshift has begun.
def lambda_etl_email(event, context):

	ses = boto3.client('ses')

	fname = event.get('fullanme')
	email = event.get('email_address')
	subject = event.get('subject')
	msg = event.get('msg')

	if None in email:
		return {
			'status code':500,
			'body': 'email not entered'
		}	
	
	try:
		response = ses.send_mail()
		msgID = response.get('MessageID')
	except Exception as e:
		return {
			'status':500,
			'body': json.dumps(f'Failed to send email: {e}')
		}
	
	return {
		'status':200,
		'body': json.dumps(f'Email ID: {msgID} sent from AWS.')
	}
