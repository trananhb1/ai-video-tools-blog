#!/usr/bin/env bash
# AI Video Picks — Daily trend discovery
# Scans Google Trends + Reddit for AI video topics, updates backlog.
# Safe to re-run (idempotent — deduplicates topics).

set -u
cd /home/tom/ai-video-tools-blog

LOG_DIR=/home/tom/ai-video-tools-blog/logs
mkdir -p "$LOG_DIR"

DATE=$(date -u +%Y-%m-%d)
LOG_FILE="$LOG_DIR/trend_discovery_${DATE}.log"

{
  echo "=== AI Video Picks daily trend discovery ==="
  echo "Started: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
  echo "Host: $(hostname)"
  echo "Mode: --quick (Google Trends + Reddit)"
  echo "--------------------------------------------"
  /usr/bin/python3 /home/tom/ai-video-tools-blog/scripts/trend_discovery.py --quick
  RC=$?
  echo "--------------------------------------------"
  echo "Exit code: $RC"
  echo "Finished: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
  exit $RC
} >> "$LOG_FILE" 2>&1
