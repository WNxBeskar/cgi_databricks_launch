# Databricks notebook source
# MAGIC %md
# MAGIC #SEED
# MAGIC Run this notebook to seed your Data Analytics resources:
# MAGIC
# MAGIC Purpose: Setup + Bronze Ingestion
# MAGIC
# MAGIC Includes:
# MAGIC
# MAGIC | Step                    |
# MAGIC |-------------------------|
# MAGIC | ✔ Create UC Schemas     |
# MAGIC | ✔ Create Volumes        |
# MAGIC | ✔ Create Bronze tables  |
# MAGIC | ✔ COPY INTO Bronze - Ingests messy CSV     |
# MAGIC | ✔ Stops. |

# COMMAND ----------

# MAGIC %md
# MAGIC ####Schemas and Volumes

# COMMAND ----------

# MAGIC %md
# MAGIC #BRONZE

# COMMAND ----------

# DBTITLE 1,BRONZE SQL
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS bronze_layer;
# MAGIC CREATE VOLUME IF NOT EXISTS bronze_layer.landing;
# MAGIC CREATE VOLUME IF NOT EXISTS bronze_layer.raw;

# COMMAND ----------

import sys
import os 
root_path = os.path.dirname(os.getcwd())
print(root_path)
data_path = f"{root_path}/data_files"
print(data_path)

# COMMAND ----------

dbutils.fs.cp(data_path, "/Volumes/workspace/bronze_layer/landing/", recurse=True)

# COMMAND ----------

# DBTITLE 1,SILVER
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS silver_layer;
# MAGIC CREATE VOLUME IF NOT EXISTS silver_layer.currated;

# COMMAND ----------

# DBTITLE 1,GOLD
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS gold_layer;
# MAGIC CREATE VOLUME IF NOT EXISTS gold_layer.aggeragated; 
