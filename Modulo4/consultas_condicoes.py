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


df = df.withColumn('AnosExperiencia', df['AnosExperiencia'].cast(FloatType()))



# aplicando filtro
#df.filter(df['Salario']>5000).show()

# aplicando filtro e estipulando que a unica coluna que sera mostrada e' a salario
#df.select('Salario').filter(df['Salario']>5000).show()

# utilizando operadores logicos para filtrar
df.filter((df['Salario']>5000) & (df['AnosExperiencia']>2)).show()

