# Question 3

Data architecture to create a data-driven company based on Existing Requirements. Explanation is based on my experience on Google Cloud Platform

## Data Architecture Diagram
![alt text](https://github.com/jodiesamuel/test_spacestock/blob/master/pictures/data_architecture_diagram.png)

### 1. Extract

First thing first, we have to extract all of the data that we have on the source. based on here, the data source is from MongoDB. The extractions for the frequently updated we can do with batching (daily,hourly,etc) or streaming (real time processing)<br /><br />
The extract we can use Apache Airflow for the scheduler and the batching processing (based on python). Extraction from the data source we can dumps the result back on the RDBMS (PostgreSQL, MySQL, etc) or we can use cloud processing like GCP (Google Cloud Processing) or AWS (Amazon Web Service) for a better and faster processing but COSTLY. GCP we can use GCS (Google Cloud Storage) on GCP or S3 (Simple Storage Service) on AWS. Based on the requirements that we have, we can chose the data that we need only or we can chose all of the data and become the _Data Lake_

### 2. Transform

After all of the data is extracted from the source, we have to transform the data to meet the requirements and needs for the analytics to be easy for query and analytics. There is many tools that can we use to manipulate/transform the data. for example :
- Spark (pyspark)
- Scala
- SQL (PostgreSQL,MySQL,BigQuery,Etc)
- Pandas,Numpy,etc
The transform if we dumps into the RDBMS database, we can transform it using query and import the transform back into the RDBMS table for the analytics based on the needs. If we use the Python we can use many tools such as Spark(pyspark), Scala to train the data and put back into RDBMS or into Cloud Storage(GCS/S3). Other option is using BigQuery, if the extract is insert into DATALAKE in GCS we can load into BigQuery also and create the query for transformation and put back into BigQuery tables and become the Datawarehouse for the analytics.<br />

The problem is hard for query, such as aggregate using time filter because the data is not standardize. it can solve using case when in postgres or if else in python. for example like using count for the length of the character. there is only years (2019,2017) or timestamp (1356973200) if the length of character more then 4 then using cast into timestamp, if length 4 we can use only the year and cast into date only. so basically it become januari 1. if the data "0" or null we can make it null or default like "1970-01-01". so we have to make it standardize or we can ask for help from the backend side to make it standardize.<br>
For the easy aggregate, we have to make it readable with make it 1 data types like integer it has to be integer and string with string. 


### 3. Load

After the transformation of the data, we have to load into datawarehouse for the analytics like Dim & Fact or simple view table so they can query or make an analytics is easier based on the needs. the loads we can chose like back into RDBMS table or we can use cloud processing such as BigQuery for faster and big processing of the data. before that we can use data monitoring to see the flow of the data if there is a missing row/data or processing failed there is notifications so we can solve it fast before the analytics team use the data. we have to connecting the dots between the needs of the data so we not make repeated datawarehouse and we can make it from the datalake so from 1 datalake we can solve for many reporting from analytics<br/><br/>

After loading the data like Dim tables or Fact Tables, we can make an easy self reporting for the analytics team like a repeated report they can self report so they dont need to come to the data team again. we can make it from Metabase, Redash (free open source) or Tableau, PowerBI. each tools only "one click away" if they need the report they just click the filter and downloads the data or analytics team can make a visualization data.
