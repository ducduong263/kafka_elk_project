# Real-time Weather Data Analysis with ELK Stack and Kafka
This project involves setting up a real-time data pipeline to analyze weather data using Kafka and the ELK stack (Elasticsearch, Logstash, and Kibana).

## Project Overview
The project fetches weather data from the OpenWeather API and processes it in real-time using Apache Kafka and the ELK stack. The data pipeline consists of the following components:

1. OpenWeather API: The source of the weather data.
2. Kafka Producer: A Python script that fetches data from the OpenWeather API and produces messages to a Kafka topic.
3. Kafka: A distributed streaming platform that handles the real-time ingestion of weather data.
4. Logstash: A data processing pipeline that ingests data from Kafka, processes it, and forwards it to Elasticsearch.
5. Elasticsearch: A search and analytics engine that stores and indexes the processed weather data.
6. Kibana: A data visualization tool that provides a web interface to query and visualize the weather data stored in Elasticsearch.

## Data Pipeline Workflow
![image](https://github.com/user-attachments/assets/40a2b2f4-82f0-42db-9b4f-696692fd4340)

## Setup
1. Download and Extract Project
  First, download the project from this [Google drive](https://drive.google.com/drive/folders/18E3IevMba_-PyD_hoSZxB-1BYGpK-svF?usp=drive_link)
  link and extract it.
2. Run the Batch Scripts
   - **startzookeeper.bat**: Runs the Zookeeper server, which manages Kafka brokers.
   - **startKafka.bat**: Runs the Kafka server, which stores topics and manages data streams.
   - **createnewtopic.bat**: Creates a new Kafka topic (you can edit this file to create a topic with a different name).
   - **startElasticsearch_Logstash.bat**: Runs Elasticsearch and Logstash. Elasticsearch stores and indexes data, while Logstash transforms and sends data from Kafka to Elasticsearch.
   - **startKibana.bat**: Runs Kibana, which visualizes data from Elasticsearch.
   - **requestapi.py**: Requests data from the OpenWeatherMap API.
   
