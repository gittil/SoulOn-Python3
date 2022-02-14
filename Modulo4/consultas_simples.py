import findspark

findspark.init()

from pyspark.sql import Row, SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder \
    .master("local") \
        .appName("Aula Introdutoria PySpark") \
            .config("spark.executer.memory","1gb") \
                .getOrCreate()
                
sc = spark.sparkContext

rdd = sc.textFile("/home/douglas/soulcode/SoulOn-Python3/Modulo4/Salary_Data.csv")
rdd = rdd.map(lambda line: line.split(","))

df = rdd.map(lambda line: Row(AnosExperiencia=line[0], Salario=line[1])).toDF()

def converterColuna(dataframe,nomes,novoTipo):
    for nome in nomes:
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe

colunas = ['AnosExperiencia','Salario']

df = converterColuna(df,colunas,FloatType())

#df.select('Salario').show(10)

#df.groupby('Salario').count().sort('Salario', ascending=False).show()

#df.select('Salario').count()

#df.describe('Salario').show()

df.collect()