import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
        .appName("Aula Introdutoria PySpark") \
            .config("spark.executer.memory","1gb") \
                .getOrCreate()
                
sc = spark.sparkContext

rdd = sc.textFile("/home/douglas/soulcode/SoulOn-Python3/Modulo4/Salary_Data.csv")

#metodo take() mostra a quantidade de linhas q estiver dentro do ()
rdd.take(5)

# metodo first mostra somente a primeira linha
rdd.first()

# rdd.map converte a lista anterior em uma lista com diveras listas menores
rdd_new = rdd.map(lambda line: line.split(","))
rdd_new.take(7)



