import findspark

findspark.init()

from pyspark.sql import SparkSession


def init_spark():
    spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
    sc = spark.sparkContext
    return spark, sc


def main():
    spark, sc = init_spark()
    nums = sc.parallelize([1, 2, 3, 4])
    print(nums.map(lambda x: x * x).collect())


if __name__ == '__main__':
    main()
