# Glue Data Catalog Setup (MHA_PP1)

This document describes the AWS Glue Data Catalog resources used in the project.
All resources are created using the AWS CLI to reflect reproducible infrastructure setup.

## Create database

```bash
aws glue create-database --database-input Name=mha_pp1_db
```

## Create raw logs crawler
> Note: An AWS Glue service role with access to S3 and the Glue Data Catalog is required to perform this action.

This crawler infers the schema of raw CSV logs and registers the `logs` table for downstream Glue jobs and Athena queries.

```bash
aws glue create-crawler \
  --name mha_pp1_raw_logs_crawler \
  --role AWSGlueServiceRole-mha-pp1 \
  --database-name mha_pp1_db \
  --targets 'S3Targets=[{Path="s3://<raw-logs-bucket>/logs/"}]'
```

## Create clean logs crawler

This crawler registers the cleaned, partitioned Parquet dataset produced by the Silver Glue job.

```bash
aws glue create-crawler \
  --name mha_pp1_clean_logs_v2_crawler \
  --role AWSGlueServiceRole-mha-pp1 \
  --database-name mha_pp1_db \
  --targets 'S3Targets=[{Path="s3://<clean-logs-bucket>/logs_v2/"}]'
```

## Run crawlers

```bash
aws glue start-crawler --name mha_pp1_raw_logs_crawler
aws glue start-crawler --name mha_pp1_clean_logs_v2_crawler
```
