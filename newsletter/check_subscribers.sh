#!/bin/bash
# Check aivideopicks newsletter subscribers & manage worker
# Usage: ./check_subscribers.sh [stats|list|deploy]

# Load secrets
source /home/tom/.claude/secrets/cloudflare.env 2>/dev/null
export CLOUDFLARE_API_TOKEN

WORKER_URL="https://aivideopicks-newsletter.trananhb1.workers.dev"
ADMIN_TOKEN="DHfWy37dJy11aQUBK324-7TeHbWjVjtzbZ6DHawQLHI"
WORKER_DIR="$(dirname "$0")/worker"

MODE="${1:-stats}"

case "$MODE" in
  list)
    curl -s -H "Authorization: Bearer $ADMIN_TOKEN" "$WORKER_URL/admin/subscribers" | python3 -m json.tool
    ;;
  stats)
    curl -s -H "Authorization: Bearer $ADMIN_TOKEN" "$WORKER_URL/admin/stats" | python3 -m json.tool
    ;;
  deploy)
    echo "Deploying newsletter worker..."
    cd "$WORKER_DIR" && npx wrangler deploy
    ;;
  *)
    echo "Usage: $0 [stats|list|deploy]"
    echo "  stats   — subscriber count + last 7 days signups (default)"
    echo "  list    — full subscriber list with emails"
    echo "  deploy  — deploy worker to Cloudflare"
    ;;
esac
