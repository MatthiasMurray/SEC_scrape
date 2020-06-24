#import findspark
#findspark.init()
import pyspark

sc = pyspark.SparkContext("local","MyApp")
rdd = sc.parallelize(range(5))

letters = rdd.map(lambda x:[abet for abet in 'alpha'])

scrambl = letters.reduce(lambda x,y: x+y)

answer = scrambl.collect()

print(answer)
