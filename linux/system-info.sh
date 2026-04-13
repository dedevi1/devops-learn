#!/bin/bash

echo "==== SYSTEM INFO ===="
echo "Hostname:  $(hostname)"
echo "Datum:     $(date)"
echo "Uptime:    $(uptime -p)"
echo "CPU:       $(nproc) Kerne"
echo "RAM frei:  $(free -h | awk '/^Mem:/ {print $4}')"
echo "Disc:      $(df -h / | awl 'NR==2 {print $4}')"
echo "======================================"
