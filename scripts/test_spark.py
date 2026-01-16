from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Spark-Test")
    .master("spark://spark-master:7077")
    .getOrCreate()
)

print("✅ Conectado a Spark")

data = [("Ana", 30), ("Luis", 25), ("Eva", 40)]
df = spark.createDataFrame(data, ["nombre", "edad"])
df.show()

spark.stop()
print("✅ Fin")
