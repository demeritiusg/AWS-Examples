import { Stack, StackProps, CfnOuput, Aws } from 'aws-cdk-lib';
import {
    aws_iam as iam,
    aws_s3 as s3,
    aws_lambda as lambda,
    aws_s3objectlambda as s3ObjectLambda,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';