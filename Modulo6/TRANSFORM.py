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


#TRANFORM

df = df.drop('target','flag')

df = df.withColumn('day_week', df.date.substr(1,3))\
    .withColumn('day',df.date.substr(9,2))\
        .withColumn('month',df.date.substr(5,3))\
            .withColumn('time',df.date.substr(12,8))\
                .withColumn('year',df.date.substr(25,4))\
                    .drop('date')
                    
def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes:
        dataframe = dataframe.withColumn(nome,dataframe[nome].cast(novoTipo))
    return dataframe 

colunas_string = ['day_week','month']
colunas_inteiro = ['day']
colunas_time = ['time']

df = converterColuna(df,colunas_string,StringType())
df = converterColuna(df,colunas_inteiro,IntegerType())
df = converterColuna(df,colunas_time,TimestampType())

df.printSchema()
df.show(5)
