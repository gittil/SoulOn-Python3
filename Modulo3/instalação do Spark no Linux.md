apt update -y

apt install default-jdk -y

wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz

tar -xvzf spark-*

mv spark-3.0.1-bin-hadoop2.7/ /opt/spark

echo "export SPARK_HOME=/opt/spark" &gt;&gt; ~/.profile

echo "export PATH=$PATH:/opt/spark/bin:/opt/spark/sbin" &gt;&gt;~/.profile

echo "export PYSPARK_PYTHON=/usr/bin/python3" &gt;&gt; ~/.profile

source ~/.profile

start-master.sh

ssh -L 8080:localhost:8080 root@ubuntu1804.awesome.com

start-slave.sh spark://ubuntu1804.awesome.com:7077

spark-shell
