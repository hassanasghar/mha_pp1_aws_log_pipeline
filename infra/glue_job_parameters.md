# Glue Job Parameters (MHA_PP1)

This document describes the AWS Glue parameters used in the project.
All parameters were selected using AWS Console.

### Silver Job Parameters

- Job bookmarks: Enabled
- Output format: Parquet (Snappy)
- Partition key: event_date

### Gold Job Parameters

- Job bookmarks: Enabled
- Aggregation source: (event_date, endpoint)
- Output table: logs_daily_endpoint_metrics
