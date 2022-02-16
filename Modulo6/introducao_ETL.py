from pyspark.sql.session import SparkSession
from pyspark.sql.types import *

import pyspark.sql.functions as F 

spark = SparkSession.builder.appName('ETL_example')\
    .config('spark.master','local')\
        .config('spark.executor.memory','2gb')\
            .config('spark.shuffle.sql.partitions',2)\
                .getOrCreate()
                
#EXTRACT