@echo off

:: Start Elasticsearch in a new command prompt window
start "Elasticsearch" cmd /k "cd /d C:\kafka_elk_project\elasticsearch\bin && elasticsearch.bat"

:: Wait for a while to ensure Elasticsearch starts up properly
timeout /t 20 /nobreak

:: Start Logstash in a new command prompt window
start "" cmd /k "C:\kafka_elk_project\logstash\bin\logstash.bat -f C:\kafka_elk_project\logstash\config\weather.conf --config.reload.automatic"
