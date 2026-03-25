# Google AdSense Readiness Checklist for aivideopicks.com

## Status: Preparing for Application

---

## DONE - Site Infrastructure

- [x] **20+ original, quality posts** (22 posts listed below)
- [x] **About page** (`/about.html`)
- [x] **Contact page** (`/contact.html`)
- [x] **Privacy Policy** (`/legal/privacy.html`) - comprehensive, should mention AdSense/Google cookies
- [x] **Terms of Service / Disclosure page** (`/legal/disclosure.html`) - FTC affiliate disclosure
- [x] **Sitemap.xml** (`/sitemap.xml`)
- [x] **robots.txt** with sitemap reference and full Googlebot access
- [x] **ads.txt** placeholder ready (`/ads.txt`) - needs real publisher ID after approval
- [x] **Mobile responsive design** (viewport meta tag, responsive CSS)
- [x] **FTC disclosure banner** on all pages (affiliate disclosure at top)
- [x] **Clean navigation structure** (header nav with categories)
- [x] **No prohibited content** (all content is AI video tool reviews/tutorials)
- [x] **Canonical URLs** set on pages
- [x] **Open Graph / Twitter Card** meta tags for social sharing

### All Posts (22)

1. `posts/best-ai-video-tools-2026.html` - Best AI Video Tools 2026
2. `posts/heygen-vs-synthesia-vs-pictory.html` - HeyGen vs Synthesia vs Pictory
3. `posts/how-to-create-ai-videos-heygen.html` - How to Create AI Videos with HeyGen
4. `posts/pictory-review-2026.html` - Pictory Review 2026
5. `posts/ai-video-for-ecommerce.html` - AI Video for E-commerce
6. `posts/colossyan-review-2026.html` - Colossyan Review 2026
7. `posts/descript-review-2026.html` - Descript Review 2026
8. `posts/invideo-review-2026.html` - InVideo Review 2026
9. `posts/zebracat-review-2026.html` - Zebracat Review 2026
10. `posts/turn-long-videos-into-shorts-ai.html` - Turn Long Videos into Shorts with AI
11. `posts/kling-vs-veo-vs-runway.html` - Kling vs Veo vs Runway
12. `posts/runway-review-2026.html` - Runway Review 2026
13. `posts/sora-alternatives-2026.html` - Sora Alternatives 2026
14. `posts/best-free-ai-video-generators-2026.html` - Best Free AI Video Generators 2026
15. `posts/d-id-vs-elai-vs-hourone.html` - D-ID vs Elai vs HourOne
16. `posts/veed-vs-kapwing-vs-descript.html` - VEED vs Kapwing vs Descript
17. `posts/fliki-review-2026.html` - Fliki Review 2026
18. `posts/ai-video-pricing-compared-2026.html` - AI Video Pricing Compared 2026
19. `posts/ai-training-onboarding-videos.html` - AI Training & Onboarding Videos

Plus:
20. `index.html` - Homepage
21. `about.html` - About page
22. `contact.html` - Contact page

Additional pages: `landing/recommend.html` (recommendation quiz/landing page)

---

## TODO - Manual Steps for Tom

### Step 1: Pre-Application Setup
- [ ] **Set up Google Search Console** at https://search.google.com/search-console
  - Verify domain ownership (DNS TXT record or HTML file method)
  - Submit sitemap: `https://aivideopicks.com/sitemap.xml`
  - Monitor indexing status - ensure all pages are indexed
- [ ] **Set up Google Analytics** (GA4) at https://analytics.google.com
  - Add GA4 tracking snippet to all HTML pages `<head>` section
  - Verify data is flowing

### Step 2: Fix Pending Items
- [ ] **Update Formspree form ID** on contact page (replace placeholder with real Formspree endpoint)
- [ ] **Configure real affiliate redirect URLs** (the `/go/toolname` links)
- [ ] **Verify Privacy Policy mentions Google AdSense** - confirm it covers:
  - Google's use of cookies (including DART cookie)
  - Third-party ad serving
  - Users can opt out via Google Ad Settings
  - Link to Google's privacy policy

### Step 3: Build Traffic (Before Applying)
- [ ] **Wait for domain age** - Google recommends 3+ months of active content
- [ ] **Build initial traffic** - target at least 100+ daily visits before applying
  - Share posts on social media
  - Submit to relevant forums/communities
  - Consider Pinterest pins for visual content
  - Guest post on related blogs
- [ ] **Check Google Search Console** for any crawl errors or manual actions

### Step 4: Apply for Google AdSense
- [ ] **Sign up at** https://adsense.google.com with your Google account
- [ ] **Add AdSense verification code** to all HTML pages:
  ```html
  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXXX"
       crossorigin="anonymous"></script>
  ```
  Add this in the `<head>` section of every HTML page (index.html and all post pages).
- [ ] **Replace `pub-XXXXXXXXXXXXXXXXX`** in `/ads.txt` with your real publisher ID
- [ ] **Submit site for review** in AdSense dashboard
- [ ] **Wait for approval** (typically 1-14 days, sometimes longer)

### Step 5: Post-Approval
- [ ] **Place ad units** strategically:
  - Header leaderboard (728x90) or responsive ad
  - In-content ads (between sections in long posts)
  - Sidebar ads on desktop
  - Anchor/overlay ads for mobile
- [ ] **Monitor performance** in AdSense dashboard
- [ ] **Test page speed** - ensure ads don't slow the site excessively
- [ ] **Comply with AdSense policies** - review https://support.google.com/adsense/answer/48182

---

## AdSense Requirements Summary

| Requirement | Status |
|---|---|
| Original content | Done (22 pages) |
| Privacy Policy | Done |
| About page | Done |
| Contact page | Done |
| Site navigation | Done |
| Mobile friendly | Done |
| No prohibited content | Done |
| ads.txt | Done (placeholder) |
| robots.txt | Done |
| Sitemap | Done |
| Domain age 3+ months | Check date |
| Sufficient traffic | Build up |
| Google Search Console | TODO |
| Google Analytics | TODO |
| AdSense verification code | TODO (after signup) |
