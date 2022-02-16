from pyspark.sql.session import SparkSession
from pyspark.sql.types import *

import pyspark.sql.functions as F 

spark = SparkSession.builder.appName('ETL_example')\
    .config('spark.master','local')\
        .config('spark.executor.memory','2gb')\
            .config('spark.shuffle.sql.partitions',2)\
                .getOrCreate()
                
#EXTRACT

schema = StructType([StructField('target',StringType()),
                     StructField('_id',IntegerType()),
                     StructField('date',StringType()),
                     StructField('flag',StringType()),
                     StructField('user',StringType()),
                     StructField('text',StringType())                     
                     ])

path = "/home/douglas/soulcode/SoulOn-Python3/Modulo6/training.1600000.processed.noemoticon.csv"

df = spark.read.format('csv')\
    .schema(schema)\
        .load(path)
        
df.printSchema()
df.show(5)
