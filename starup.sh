#!/bin/bash

# Execute both Python files sequentially
python addlog.py &
python test.py &

# # Keep the container running
tail -f /dev/null
