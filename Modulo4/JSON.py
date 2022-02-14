from pyspark.sql.session import SparkSession
from pyspark.sql.types import (DoubleType,BooleanType,IntegerType,StringType,TimestampType,StructType,StructField, ArrayType,FloatType)
import pyspark.sql.functions as F 

spark = SparkSession.builder.appName('firstSession')\
    .config('spark.master', 'local[4]')\
        .config('spark.executor.memory','1gb')\
            .config('spark.shuffle.partitions',1)\
                .getOrCreate()

