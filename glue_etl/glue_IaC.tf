terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 5.7"
    }
  }
}

provider "aws" {
    region = "us-east-1"
}

resource "aws_glue_catalog_database" "etl_catalog_database_prod" {
    name = "etl_catalog_database_prod"
  
}

resource "aws_glue_catalog_table" "etl_catalog_table_prod" {
    name = "etl_catalog_table_prod"
    database_name = "etl_catalog_database_prod"
}

resource "aws_glue_classifier" "etl_csv_prod_classifier" {
    name = "project1_csv_classifier"

    csv_classifier {
      allow_single_column = false
      contains_header = "PRESENT"
      delimiter = ","
    }
}

resource "aws_glue_job" "etl_prod_job" {
  
}