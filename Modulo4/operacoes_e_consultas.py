from pyspark.sql.session import SparkSession
from pyspark.sql.types import (BooleanType,IntegerType,StringType,TimestampType,StructType,StructField, ArrayType,FloatType)
import pyspark.sql.functions as F 

spark = SparkSession.builder.appName('firstSession')\
    .config('spark.master', 'local[4]')\
        .config('spark.executor.memory','1gb')\
            .config('spark.shuffle.partitions',1)\
                .getOrCreate()

schema = StructType([
                StructField('case_id',IntegerType()),
                StructField('province',StringType()),
                StructField('city',StringType()),
                StructField('group',BooleanType()),
                StructField('infection_case', StringType()),
                StructField('confirmed', StringType()),
                StructField('latitude',StringType()),
                StructField('longitude',StringType())
])

path = '/home/douglas/soulcode/SoulOn-Python3/Modulo4/covid_cases.csv'

df = spark.read.format('csv')\
    .schema(schema)\
        .load(path)

# modificando o nome de uma unica coluna
cases = df.withColumnRenamed('infection_case','Casos de Infecçao')

# modificando o nome de varias colunas
cases1 = df.toDF(*['ID','Provincia','Cidade','Grupo',
                   'Casos de Infecçao','Confirmado','Latitude',
                   'Longitude'])
#cases1.show()

df2 = df.select('province','city','confirmed')
# df2.show()

df3 = df.sort(F.desc('confirmed'))
df3.show()

