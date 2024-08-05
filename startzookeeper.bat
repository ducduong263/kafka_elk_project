@echo off
cd /d C:\kafka_elk_project\kafka
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
pause
