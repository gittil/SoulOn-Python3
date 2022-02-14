from pyspark.sql.session import SparkSession
from pyspark.sql.types import (DoubleType,BooleanType,IntegerType,StringType,TimestampType,StructType,StructField, ArrayType,FloatType)
import pyspark.sql.functions as F 

spark = SparkSession.builder.appName('firstSession')\
    .config('spark.master', 'local[4]')\
        .config('spark.executor.memory','1gb')\
            .config('spark.shuffle.partitions',1)\
                .getOrCreate()

schema = StructType([
      StructField("RecordNumber",IntegerType()),
      StructField("Zipcode",IntegerType()),
      StructField("ZipCodeType",StringType()),
      StructField("City",StringType()),
      StructField("State",StringType()),
      StructField("LocationType",StringType()),
      StructField("Lat",DoubleType()),
      StructField("Long",DoubleType()),
      StructField("Xaxis",IntegerType()),
      StructField("Yaxis",DoubleType()),
      StructField("Zaxis",DoubleType()),
      StructField("WorldRegion",StringType()),
      StructField("Country",StringType()),
      StructField("LocationText",StringType()),
      StructField("Location",StringType()),
      StructField("Decommisioned",BooleanType()),
      StructField("TaxReturnsFiled",StringType()),
      StructField("EstimatedPopulation",IntegerType()),
      StructField("TotalWages",IntegerType()),
      StructField("Notes",StringType())
  ])

df = spark.read.schema(schema)\
    .json('/home/douglas/soulcode/SoulOn-Python3/Modulo4/zipcodes.json')

df.registerTempTable('zipcodes')
#output = spark.sql("SELECT * FROM zipcodes")

#output = spark.sql("SELECT RecordNumber,City, Notes  FROM zipcodes")

output = spark.sql("SELECT RecordNumber FROM zipcodes WHERE RecordNumber > 10")

output.show()
