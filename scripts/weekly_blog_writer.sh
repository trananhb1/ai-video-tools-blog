#!/usr/bin/env bash
# AI Video Picks — Weekly blog post writer
# 1. Full trend discovery (all sources including content gap analysis)
# 2. Generates 2-3 blog post drafts from the highest-priority topics
# Safe to re-run (idempotent — skips already-written topics).

set -u
cd /home/tom/ai-video-tools-blog

LOG_DIR=/home/tom/ai-video-tools-blog/logs
mkdir -p "$LOG_DIR"

DATE=$(date -u +%Y-%m-%d)
LOG_FILE="$LOG_DIR/weekly_blog_writer_${DATE}.log"

{
  echo "=== AI Video Picks weekly blog writer ==="
  echo "Started: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
  echo "Host: $(hostname)"
  echo "------------------------------------------"

  echo ""
  echo "--- Step 1: Full Trend Discovery (all sources) ---"
  /usr/bin/python3 /home/tom/ai-video-tools-blog/scripts/trend_discovery.py --no-cache
  TREND_RC=$?
  echo "Trend discovery exit code: $TREND_RC"

  if [ $TREND_RC -ne 0 ]; then
    echo "WARNING: Trend discovery failed, attempting post generation from existing backlog..."
  fi

  echo ""
  echo "--- Step 2: Blog Post Generation (up to 3 posts) ---"
  /usr/bin/python3 /home/tom/ai-video-tools-blog/scripts/blog_post_writer.py --count 3
  WRITE_RC=$?
  echo "Blog writer exit code: $WRITE_RC"

  echo ""
  echo "--- Step 3: Draft inventory ---"
  DRAFT_COUNT=$(find /home/tom/ai-video-tools-blog/content/drafts/ -name "*.html" 2>/dev/null | wc -l)
  echo "Total blog drafts available: $DRAFT_COUNT"

  PUBLISHED_COUNT=$(find /home/tom/ai-video-tools-blog/posts/ -name "*.html" 2>/dev/null | wc -l)
  echo "Total published posts: $PUBLISHED_COUNT"

  echo "------------------------------------------"
  echo "Finished: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
  exit $WRITE_RC
} >> "$LOG_FILE" 2>&1
