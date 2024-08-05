@echo off
cd /d C:\kafka_elk_project\kafka
.\bin\windows\kafka-topics.bat --create --topic 321 --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
pause
