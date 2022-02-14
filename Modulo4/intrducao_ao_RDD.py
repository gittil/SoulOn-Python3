import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
        .appName("Aula Introdutoria PySpark") \
            .config("spark.executer.memory","1gb") \
                .getOrCreate()
                
sc = spark.sparkContext

