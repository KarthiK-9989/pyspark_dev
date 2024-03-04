from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.master("local[*]").appName("PySparkReaderExample").getOrCreate()

# Path to the CSV file (replace with your file path)
csv_file_path = "C:/Users/Karthik Kondpak/Desktop/Registration.csv"

# Read data from the CSV file into a DataFrame with options
df = spark. \
      read.  \
      format("csv") \
      .option("header", "true") \
      .load(csv_file_path)

# Show the DataFrame content
df.show()

# Stop the Spark session
spark.stop()



"""
here few points to be infered if  you want to write reader api in this fashion 

# Read data from the CSV file into a DataFrame with options
df = spark. 
      read.  
      format("csv") 
      .option("header", "true") 
      .load(csv_file_path)

if u try to like above it throws errors it is not same as scala spark.

it should be either written as 

1) df =( spark. 
      read.  
      format("csv") 
      .option("header", "true") 
      .load(csv_file_path) )
      
NOTE: SHOULD BE ENCLOSED IN ROUND BRACKETS MAKING PYTHON SPARK TO UNDERSTAND THEY ARE ONE 

else

2) df = spark.  \
      read.    \
      format("csv")  \
      .option("header", "true")  \
      .load(csv_file_path) 

NOTE: Mention backslash after every line through it can understand that our line is not ended .
      
"""

