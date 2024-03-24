import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['glue_job', 'obj_key'])
obj_key = args['obj_key']

# initializing context and job
sc = SparkContext()
gc = GlueContext(sc)
spark = sc.spark_session
job = Job(gc)
job.init(args['glue_job'], args)

# define source and destination buckets
source_bucket = ''
destination_bucket = ''
source_path = f's3://{source_bucket}/{obj_key}'
output_path = 's3://' + destination_bucket + '/' + obj_key.rsplit(".",1)[0]

# read data from s3
read_data = gc.create_dynamic_frame.from_options(
	connection_type='s3',
	connection_options={'path': [source_path]},
	format='json',
	format_options={'multiline': False},
	)


transform_data = ApplyMapping.apply(
	frame=read_data,
	mappings=[
		()
		
		]
	)

gc.write_dynamic_frame.from_options(
	frame=transform_data,
	connection_type='s3',
	connection_options={'path': output_path, },
	format= 'parquet',
	)

# finish job
job.commit()
