# Glue Data Catalog Setup (MHA_PP1)

## Create database

```bash
aws glue create-database --database-input Name=mha_pp1_db
```

## Create raw logs crawler
AWS role is required to perform this action.

```bash
aws glue create-crawler \
  --name mha_pp1_raw_logs_crawler \
  --role AWSGlueServiceRole-mha-pp1 \
  --database-name mha_pp1_db \
  --targets 'S3Targets=[{Path="s3://<raw-logs-bucket>/logs/"}]'
```

## Create clean logs crawler
AWS role is required to perform this action.

```bash
aws glue create-crawler \
  --name mha_pp1_clean_logs_crawler \
  --role AWSGlueServiceRole-mha-pp1 \
  --database-name mha_pp1_db \
  --targets 'S3Targets=[{Path="s3://<clean-logs-bucket>/logs/"}]'
```

## Run crawlers

```bash
aws glue start-crawler --name mha_pp1_raw_logs_crawler
aws glue start-crawler --name mha_pp1_clean_logs_crawler
```
