# Thumbnail Generation Workflow

For agents publishing new posts on aivideopicks.com.

## Pieces

- **Figma file**: `wjQh4PNW6yeK10rhprpxCM` (AI Video Picks - Thumbnails)
- **Master template node**: `1:2` (Thumbnail/600x340 component)
- **Token**: `~/.claude/secrets/figma.env` (FIGMA_TOKEN)
- **Helper script**: `scripts/generate-thumbnail.py`

## Tool logo chip components

A library of branded chips lives on the "Tool Logo Chips" page. Drop these into the master template's `LogoStrip` frame to show which tools the post covers.

| Tool | Node ID |
|---|---|
| HeyGen | `6:11` |
| Synthesia | `6:13` |
| Kling | `6:15` |
| Runway | `6:17` |
| Pika | `6:19` |
| Fliki | `6:21` |
| Zebracat | `6:23` |
| Pictory | `6:25` |
| Submagic | `6:27` |
| Movavi | `6:29` |
| Vidnoz | `6:31` |
| Arcads | `6:33` |
| MakeUGC | `6:35` |
| Descript | `6:37` |
| Veo | `6:39` |
| Sora | `6:41` |
| ElevenLabs | `6:43` |

Need a tool not in the library? Add a new chip to the "Tool Logo Chips" page following the same component pattern, then add its node ID here.

## Step 1 — Clone the master + override (use_figma MCP)

The `LogoStrip` is inside an instance, so you must `detachInstance()` before adding chips. Each thumbnail is a one-off export, so detaching is fine.

```js
await figma.loadFontAsync({ family: "Inter", style: "Bold" });

const master = await figma.getNodeByIdAsync("1:2");
const instance = master.createInstance();

// Position somewhere out of the way (any free spot)
instance.x = 100;
instance.y = 1000 + Math.floor(Math.random() * 5000);

// Override gradient by category:
//   Review/Comparison/Guide  → blue→navy (default, no override)
//   Urgent/Deadline          → red→navy
//   Deal/Bonus               → yellow→orange
//   New tool launch          → purple→blue
instance.fills = [{
  type: 'GRADIENT_LINEAR',
  gradientTransform: [[0.7, 0.7, 0], [-0.7, 0.7, 0.3]],
  gradientStops: [
    { position: 0, color: { r: 0.1, g: 0.1, b: 0.18, a: 1 } },
    { position: 1, color: { r: 0.086, g: 0.365, b: 0.973, a: 1 } } // #155DFC blue
  ]
}];

// Override title (max 60 chars, will wrap to 2-3 lines)
const title = instance.findOne(n => n.name === "Title");
title.characters = "Best AI Video Tools 2026: Top 10 Picks Compared";

// Override badge text + bg color
const badgeText = instance.findOne(n => n.name === "BadgeText");
badgeText.characters = "REVIEW";  // REVIEW | COMPARISON | GUIDE | URGENT | DEAL | NEW

const badgeBg = instance.findOne(n => n.name === "BadgeBackground");
badgeBg.fills = [{ type: 'SOLID', color: { r: 0.961, g: 0.773, b: 0.094 } }]; // yellow

// Add tool logo chips for every tool/service mentioned in the post.
// Detach the instance first so we can modify the LogoStrip.
const detached = instance.detachInstance();
const strip = detached.findOne(n => n.name === "LogoStrip");

const toolsInPost = ["HeyGen", "Synthesia", "Kling"]; // up to 7 fits cleanly
const chipIds = {
  HeyGen: "6:11", Synthesia: "6:13", Kling: "6:15", Runway: "6:17",
  Pika: "6:19", Fliki: "6:21", Zebracat: "6:23", Pictory: "6:25",
  Submagic: "6:27", Movavi: "6:29", Vidnoz: "6:31", Arcads: "6:33",
  MakeUGC: "6:35", Descript: "6:37", Veo: "6:39", Sora: "6:41",
  ElevenLabs: "6:43"
};
for (const name of toolsInPost) {
  const chipComp = await figma.getNodeByIdAsync(chipIds[name]);
  strip.appendChild(chipComp.createInstance());
}

return { instanceId: detached.id };
```

## Step 2 — Export PNG via REST API

```bash
python3 scripts/generate-thumbnail.py <instance-id> <slug>
# Outputs: assets/images/<slug>-thumbnail.png (600x340 PNG)
```

## Step 3 — Wire CSS class on homepage card

In `index.html`, the new card needs `class="card-thumb thumb-<slug>"` matching a CSS rule in `assets/css/index.css`.

If a matching rule doesn't exist, add one:
```css
.card-thumb.thumb-<slug> { background-image: url('assets/images/<slug>-thumbnail.png'); }
```

## Reference: Brand Colors

| Color | Hex | RGB (0-1) | Use |
|---|---|---|---|
| Dark navy | #15192e | r:0.082 g:0.114 b:0.18 | Default gradient start |
| Brand blue | #155DFC | r:0.086 g:0.365 b:0.973 | Default gradient end |
| Urgent red | #dc2626 | r:0.863 g:0.149 b:0.149 | Time-sensitive posts |
| Brand yellow | #f5c518 | r:0.961 g:0.773 b:0.094 | Logo + accents |
| Deal orange | #f97316 | r:0.976 g:0.451 b:0.086 | Promotional posts |
| New purple | #9333ea | r:0.576 g:0.2 b:0.918 | New tool launches |
