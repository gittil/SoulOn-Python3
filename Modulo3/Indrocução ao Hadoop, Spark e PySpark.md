HADOOP

Hadoop é "um framework para desenvolvimento de aplicações distribuidas", com alta escalabilidade, confiabilidade e tolerância a falhas, subdividido em três projetos: Hadoop Commons, Hadoop Distribuited File System e Haddop MapRadude.

O Haddop Distributed File System (HDFS) fornece armazenamento escalável e tolerante a falhas, o custo-eficiente para o seu Data Lake grande.

O MapReduce é o quadro original para escrever aplicações massivamente paralelas que processam grandes quantidades de dados estruturados e não estruturados armazenados no HDFS.

Os aplicativos podem interagir com os dados no Hadoop usando lote ou SQL interativa (Apache Hive) ou o acesso de baixa latência com NoSQL (HBase).

Vantagens do Hadoop:
- Capacidade de armazenar e processar grandes quantidades de qualquer tipo de dado, e rapidamente;
- Poder computacional;
- Tolerência a falhas;
- Flexibilidade;
- Custo baixo;
- Escalabilidade.

Referências:
- CATAX. 
Hadoop: O que é, conceito e definição. Disponível em: <https://www.cetax.com.br/blog/apache-haddop>
-COMPUTERWORLD. 
Haddop: O que é, conceito e definição.
Haddop ou Spark? Veja qual se aplica melhor para sua empresa. Disponível em <https://computerworld.com.br/inovacap/haddop-ou-spark-veja-qual-se-aplica-melhor-para-sua-empresa/> Acesso em: 04/01/2022

APACHE SPARK

O Apache Spark é uma ferramenta de Big Data que tem o objetivo de processar grandes conjuntos de dados de forma paralela e distribuída.

Core do Apache Spark

- Apache Streamming, que possibilita o processamento de fluxos em tempo real;
- GraphX, que realiza o processo sobre grafos;
- SparkSQL, para a utilização de SQL na realização de consultas e processamento sobre os dados no Spark;
- MLlib, que é a biblioteca de aprendizado de máquina, com diferentes algoritmos para as mais diversas atividades, como clustering.

Principais componentes:

- Resiliente Distribuited Datasets(RDD)
- Operações
- Spark Context

Referências:

- DEVMEDIA. Introdução ao Apache Spark. Disponível em <https://www.devmedia.com.br/introducao-ao-apache-spark/34178> 
- SPARK. Lightning-fast unified analytics engine. <http://spark.apache.org>

PySpark

PySpark é uma biblioteca Spark escrita em Python para executar o aplicativo Python usando recursos Apache Spark. Usando o PySpark podemos executar aplicativos paralelamente no cluster distribuído (vários nós).

VANTAGENS:
- PySpark é um mecanismo de processamento distribuido de propósito geral, na memória, que permite processar dados de forma eficiente de forma distribuída.
- As aplicações em execução no PySpark são 100x mais rápidas que os sistemas tradicionais.
- Você terá grandes benefícios usando o PySpark para ingestão de dados.
- Usando o PySpark, podemos processar dados de Hadoop HDFS, AWS S3 e muitos sistemas de arquivos.
- Usando o streaming PySpark, você também pode transmitir arquivos do sistema de arqvuios e também transmitir a partir do soquete.
- PySpark tem bibliotecas de aprendizado de máquina e gráficos.

Gerenciadores

- Autônomo
- Apache Mesos
- Hadoop Yarn
- Kubernetes

Referências:

SPARKBYEXAMPLES. Spark whih Python (PySpark) Tutotial for Beginners.
<https://sparkbyexamples.com/pyspark-tutorial/>


