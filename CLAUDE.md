# AI Video Picks — aivideopicks.com

## Overview
Affiliate blog for AI video tools + creator gear. GitHub Pages static site.
- **Domain:** https://aivideopicks.com
- **Repo:** /home/tom/ai-video-tools-blog/ (GitHub: trananhb1/ai-video-tools-blog)
- **Stack:** Static HTML, GitHub Pages, Google Analytics (G-M5NLTFV6FL)
- **Brand:** AI Video Picks (logo text: "AI Video Hub")
- **Content:** 27+ articles — reviews, comparisons, tutorials, gear guides

## On Every Session: Follow-Up Checklist

When this project is opened, run through these items:

### 1. Outstanding Tasks
- [ ] Check for any incomplete work from previous sessions
- [ ] Review `git log --oneline -10` for recent changes
- [ ] Check if any new affiliate programs need integration

### 2. Performance Check
- [ ] Check site is live: `curl -sI https://aivideopicks.com | head -5`
- [ ] Verify all affiliate links are working (spot-check 3-5 links)
- [ ] Check Google Analytics for traffic trends (GA ID: G-M5NLTFV6FL)
- [ ] Review sitemap.xml matches actual published posts
- [ ] Check for any broken internal links between articles

### 3. Optimize
- [ ] Identify articles with missing or weak CTAs — add affiliate links
- [ ] Check if any new AI video tools have launched that deserve coverage
- [ ] Review SEO: meta descriptions, canonical URLs, schema markup
- [ ] Ensure all articles cross-link to related content
- [ ] Check image loading and page performance
- [ ] Look for content gaps in the buyer journey (awareness → comparison → decision)

## Affiliate Programs

### Active Affiliate Links
| Program | Link | Status | Where Used |
|---------|------|--------|------------|
| Vidnoz | `https://www.vidnoz.com/?a_aid=69cc4240db2e7` | Active | Review, 5 comparison articles |
| Fliki | `https://fliki.ai/?via=fbca94` | Active | Fliki review, pricing |
| Synthesia | `https://www.synthesia.io/?via=tuan-tran` | Active | 15+ articles |
| HeyGen | `https://www.heygen.com/?via=aivideopicks` | Applied | 10+ articles |
| Pictory | `https://pictory.ai/?via=aivideopicks` | Applied | Pricing, comparisons |
| Zebracat | `http://studio.zebracat.ai/signup/?via=d98eb9` | Active | Best tools, comparisons (code: 6YAZM9V5 15% off) |
| Descript | `?via=aivideopicks` | Applied | 7+ articles |
| Colossyan | `?via=aivideopicks` | Declined (reapply with traffic) | Reviews, training |

### Amazon AU Associates
- **Associate Tag:** `aivideopicks-22`
- **Status:** Active, need 10 qualifying sales for PA-API access
- **Gear guide:** `posts/best-gear-ai-video-creators-2026.html` (13 products)
- **Link checker:** https://affiliate-program.amazon.com.au/home/tools/linkchecker
- **Goal:** 10 sales → unlock PA-API → feed dropshipping sourcing pipeline

### Amazon Product Links (amzn.to)
1. Neewer Ring Light: https://amzn.to/4s7Zlg9
2. Blue Yeti USB Mic: https://amzn.to/4tKJEgb
3. Rode PodMic USB: https://amzn.to/48fa7tJ
4. Logitech C922 Webcam: https://amzn.to/48nGqqk
5. Elgato Stream Deck MK.2: https://amzn.to/4tqCkWL
6. Audio-Technica ATH-M50x: https://amzn.to/3O3l4rw
7. SanDisk 256GB Extreme Pro: https://amzn.to/3PN3xEu
8. HyperX QuadCast S: https://amzn.to/4sZxiR9
9. Elgato Green Screen: https://amzn.to/3NUyOov
10. Elgato HD60 X: https://amzn.to/4vdEV8g
11. Elgato Wave:3: https://amzn.to/4v8MCMO
12. Wacom Intuos Small: https://amzn.to/4bNWdRB
13. Sony WH-1000XM5: https://amzn.to/3POVAi7

## Content Inventory (27 articles)

### Reviews (11)
- fliki-review-2026.html
- synthesia-review-2026.html
- descript-review-2026.html
- pictory-review-2026.html
- invideo-review-2026.html
- runway-review-2026.html
- colossyan-review-2026.html
- opus-clip-review-2026.html
- murf-ai-review-2026.html
- zebracat-review-2026.html
- **vidnoz-review-2026.html** (NEW Apr 3)

### Comparisons (8)
- best-ai-video-tools-2026.html (top 10 ranked)
- heygen-vs-synthesia-vs-pictory.html
- kling-vs-veo-vs-runway.html
- veed-vs-kapwing-vs-descript.html
- d-id-vs-elai-vs-hourone.html
- best-free-ai-video-generators-2026.html
- ai-video-pricing-compared-2026.html
- sora-alternatives-2026.html

### Guides & Tutorials (6)
- ai-tools-youtube-creators-2026.html
- turn-long-videos-into-shorts-ai.html
- ai-training-onboarding-videos.html
- what-is-text-to-video-ai.html
- how-to-create-ai-videos-heygen.html
- **best-gear-ai-video-creators-2026.html** (NEW Apr 3, Amazon affiliate)

### Use Cases (3)
- ai-video-for-ecommerce.html
- ai-video-social-media-marketing-2026.html
- (one more in guides section)

## Site Structure
```
index.html              — Homepage with article cards
about.html              — About page
contact.html            — Contact/lead capture
posts/                  — All articles (27 HTML files)
landing/recommend.html  — Quiz-based recommendation page
legal/                  — FTC disclosure, privacy policy
email/                  — Welcome sequence + newsletters
social/                 — Social media content + distribution plan
assets/images/          — Thumbnails and media
sitemap.xml             — SEO sitemap
robots.txt              — Crawl directives
ads.txt                 — Ad network transparency
CNAME                   — Domain config (aivideopicks.com)
```

## HTML Article Template Pattern
Every article follows this structure:
1. Google Analytics gtag (G-M5NLTFV6FL)
2. SEO meta tags (title, description, keywords, canonical)
3. Open Graph + Twitter Card meta
4. Article Schema JSON-LD + FAQ Schema
5. Inline CSS (no external stylesheets)
6. Sticky header: `<a class="logo">AI Video <span>Hub</span></a>` + nav links
7. FTC disclosure banner
8. Breadcrumb
9. Article header (h1, meta with date/read time)
10. Table of Contents
11. Article content with h2/h3 sections
12. CTA boxes (gradient blue → navy, white button)
13. FAQ section
14. Footer with disclosure links

## Key Conventions
- **FTC disclosure** on every article with affiliate links
- **rel="nofollow noopener"** or **rel="nofollow sponsored"** on all affiliate links
- **target="_blank"** on external links
- **No external CSS** — all styles inline per page
- **Lazy loading** on images: `loading="lazy"`
- **Max title:** Keep SEO titles under 60 chars for Google
- **Date format:** "Published: Month DD, YYYY"
- CTA button text: "Try [Tool] Free →" for SaaS, "Check Price on Amazon →" for products
- Never say "Amazon AU" in CTAs — just "Amazon"

## Deployment
```bash
# Commit and push to deploy (GitHub Pages auto-deploys from main)
cd /home/tom/ai-video-tools-blog
git add [files]
git commit -m "description"
git push origin main
# Live in ~1-2 minutes at https://aivideopicks.com
```

## Related Projects
- **Dropshipping** (`/home/tom/dropshipping/`) — Amazon AU → eBay AU pipeline for Bulkify Australia
  - Amazon Associates (aivideopicks-22) goal: 10 sales → PA-API access → feed SerpAPI replacement
  - SerpAPI currently out of credits; keyword generator expanded to 7,500+ queries
  - Scale target: 200K eBay listings

## Email & Social
- **Email sequences:** `email/welcome-sequence.md`, `email/weekly-newsletters.md`
- **Social plan:** `social/distribution-plan.md`, `social/content.md`
- **AdSense:** `ADSENSE-CHECKLIST.md` (prep in progress)
