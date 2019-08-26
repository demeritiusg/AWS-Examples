import boto3 

s3 = boto3.client('s3')
ses = boto3.client('ses')

file = s3.Bucket('some-bucket', 'filename')

# event is file landing in s3. email sent to team that file has been processed and loading to redshift has begun.
def lambda_etl_email(event, context)
	
	results = file.get()['Body'].read()
		
	SENDER = ''
	RECIEVER = ''
	SUBJECT = ''
	BODY_HTML = """
	<html>
		<head></head>
		<body>
			<h1>RESULTS</h1>
			<p>Sucessfully processed {} records. Loading to redshift now</p>
		</body>
	</html>""".format(results)
	
	
	try:
		response = ses.client.send_mail(
			Destination={
				'ToAddresses':[ RECIEVER, 
					],
				},
			Message={
				'Body': {
					'Html': {
						'Data': BODY_HTML,
					},
					'Text': {
						'Data': ,
					},
				},
				'Subject': {
					'Data': SUBJECT,
				},
			},
			Source=SENDER
		)
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print('Email Sent MessageID:' response['MessageID'])
