#!/usr/bin/env_node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { s3ObjectLambdaStack } from  '../lib/s3-object-lambda-stack';

const app = new  cdk.App();
new s3ObjectLambdaStack(app, 'S3ObjectLambdaStack')