#!/bin/bash

LOGGER_PROCESS_ID=$(ps aux | grep bike_data_logger.py | awk '/python/ {print $2}')
sudo kill -9 $LOGGER_PROCESS_ID
