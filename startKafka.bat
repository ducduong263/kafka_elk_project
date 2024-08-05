@echo off
cd /d C:\kafka_elk_project\kafka
set success=false

:retry
.\bin\windows\kafka-server-start.bat .\config\server.properties
if %ERRORLEVEL% NEQ 0 (
    echo Kafka failed to start, retrying in 10 seconds...
    timeout /t 10
    goto retry
)

echo Kafka started successfully.
pause
