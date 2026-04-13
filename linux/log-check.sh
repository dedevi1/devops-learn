#!/bin/bash

LOGFILE="/var/log/syslog"
KEYWORD="error"

echo "==== LOG CHECK ===="
echo "Suche nach:  $KEYWORD"
echo "Datei:       $LOGFILE"
echo ""

COUNT=$(grep -i "$KEYWORD" "$LOGFILE" 2>/dev/null | wc -l)
echo "Gefundene Einträge: $COUNT"

echo ""
echo "Letzte 5 Treffer:"
grep -i "$KEYWORD" "$LOGFILE" 2>/dev/null | tail -5
echo "=================================="
