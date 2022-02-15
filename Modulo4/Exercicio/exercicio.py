from ctypes import cast
from pandas import DataFrame
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as F 

spark = SparkSession.builder.appName('exercicio')\
    .config('spark.master','local[4]')\
        .config('spark.executor.memory','1gb')\
            .config('spark.shuffle.partitions',1)\
                .getOrCreate()
                
schema = StructType([
    StructField("id",IntegerType()),
    StructField("age",IntegerType()),
    StructField("tipo_de_empresa",StringType()),
    StructField("documento",IntegerType()),
    StructField("education",StringType()),
    StructField("A",IntegerType()),
    StructField("estado_civil",StringType()),
    StructField("ocupacao",StringType()),
    StructField("situcao",StringType()),
    StructField("raça",StringType()),
    StructField("sexo",StringType()),
    StructField("X",IntegerType()),
    StructField("Y",IntegerType()),
    StructField("Z",IntegerType()),
    StructField("pais",StringType()),
    StructField("capital_gain",StringType())
])

path = r"D:\Python\SoulOn-Python3\Modulo4\Exercicio\adult_data.csv"

df = spark.read.format('csv')\
    .schema(schema)\
        .load(path)
    
# 1.Imprima o Schema de seu DF; 
df.printSchema()

# 2.Imprima os primeiros 5 linhas de seu DF; 
df.show(5)

# 3.Converta o campo idade do tipo inteiro para o 
# tipo Float (ou vice versa, dependendo do seu Schema); 
df1 = df.withColumn("age",df["age"].cast(FloatType()))
df1.printSchema()

#4.	Exiba somente 5 itens com os campos ‘age’ e ‘education’; 
df1.registerTempTable('adult_data')
df_sql = spark.sql("SELECT age, education FROM adult_data LIMIT 5").show()

# 5.Agrupe a quantidade de itens em ‘education’ 
# ordenados de maneira ascendente;
df_group = df1.groupBy('education').count().sort('education', ascending=True)
df_group.show()

#6.Exiba um describe da tabela ‘capital_gain’;
df1.describe('capital_gain').show()





