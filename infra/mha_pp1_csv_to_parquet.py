"""
Glue ETL job for MHA_PP1 – CSV logs -> Parquet

- Reads from Glue Catalog table: mha_pp1_db.logs
- Writes Parquet to S3 clean bucket under logs/ prefix
- This script is exported from the Glue Studio job "mha_pp1_csv_to_parquet"

"""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node mha_pp1_glue_data_catalog
mha_pp1_glue_data_catalog_nodeA = glueContext.create_dynamic_frame.from_catalog(database="mha_pp1_db", table_name="logs", transformation_ctx="mha_pp1_glue_data_catalog_nodeA")

# Script generated for node mha_pp1_glue_data_target
EvaluateDataQuality().process_rows(frame=mha_pp1_glue_data_catalog_nodeA, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_nodeB", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
mha_pp1_glue_data_target_nodeC = glueContext.write_dynamic_frame.from_options(frame=mha_pp1_glue_data_catalog_nodeA, connection_type="s3", format="glueparquet", connection_options={"path": "s3://<clean-logs-bucket>/logs/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="mha_pp1_glue_data_target_nodeC")

job.commit()