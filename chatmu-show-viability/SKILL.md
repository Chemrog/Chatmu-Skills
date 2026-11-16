---
name: chatmu-show-viability
description: >
  Use to estimate how many tickets an artist can realistically sell in a city and
  whether a show is viable. Starts from the 2% rule, then adjusts it with the
  artist's own past shows, growth, timing, competition, market and fan signals.
  Trigger phrases: "can I play in", "show viability", "2% rule", "how many tickets",
  "where should I tour", "gig economics", "profitable to play", "show attendance estimate",
  "venue size for".
compatibility: claude.ai
category: business
subcategory: touring
shortDesc: >-
  Realistic ticket estimates per city: 2% rule as the baseline, calibrated with the
  artist's past shows, growth, dates and market
---

# Chatmu — Show Viability & Ticket Estimate Skill
**Version:** 2.0
**Required MCP:** Chatmu MCP
**For:** Artists, managers, booking agents and promoters deciding where to play, how big, and when
**Repository:** github.com/Chemrog/Chatmu-Skills

---

## What does this Skill do?

It answers: **"How many tickets can this artist realistically sell in this city, in which venue size, and is it worth doing?"** — with a range (conservative / realistic / optimistic), the math shown, and the reasons behind every adjustment.

The 2% rule is the **starting point**, not the answer. The answer gets more precise with every real data point: the artist's own past shows, their growth, the date, the market and the competition.

---

## THE METHOD — 3 layers

### Layer 1 — Baseline: the 2% rule

`Monthly Spotify listeners in the city × 2% = baseline attendance`

- 2% of 5,000 = 100 → minimum viable paid show
- 2% of 10,000 = 200 → comfortable show
- 2% of 50,000 = 1,000 → mid-size venue

Why 2%: most listeners are casual, many never go to concerts, and ticket price, distance and timing filter the rest. It is the industry rule of thumb (strongest in the US, where Apple Music also matters).

**Viability thresholds (applied to the final realistic number, not only to the baseline):**
| Realistic attendance | Verdict |
|---|---|
| ≥ 200 | ✅ Viable |
| 100–199 | ✅ Viable, small room |
| 50–99 | ⚠️ Borderline — small room or free show |
| < 50 | 🔴 Not yet for a paid show |

### Layer 2 — Calibrate with the artist's own history (the most important layer)

**Always ask the user for it before giving the final number** (one short question, skippable):

> "Do you have results from past shows? For each one: city, date, venue capacity, tickets sold and average price. Also useful: how many tickets each buyer usually purchases. If you don't have it, no problem — I'll estimate with the other signals."

If they give past shows:
1. For each past show: `own conversion = tickets sold ÷ monthly listeners in that city`.
   - Use the current city listeners from `artist_top_geographic_data` and correct for growth since that show (`geographic_growth_analysis` / `get_artist_growth_trajectory`). Say it's an approximation.
2. Blend it with the 2% depending on how much evidence there is:
   - 1 show in the city → 1/3 own conversion + 2/3 the 2% (one show can be a fluke)
   - 2–3 shows → 1/2 + 1/2
   - 4+ shows → 3/4 own + 1/4 the 2%
   - No show in that city but shows elsewhere → use the artist's average own conversion across cities, blended 1/2 with 2%.
3. Sold out last time? Real demand was higher than the tickets sold → push the estimate up.
4. Tickets per buyer (usually ~2: almost nobody goes alone) helps translate fans into tickets and to size presales and CRM campaigns.

**If they don't have it**, do NOT stop: keep the 2% baseline and go to Layer 3 with every other signal. Also run `get_artist_live_history` (city filter) to at least know when and in which venues they played before.

### Layer 3 — Adjust for the context of this show

Apply each signal that you can verify. Show every adjustment and its reason. These are starting ranges, to be replaced by the artist's real data when available.

**Pushes the estimate UP**
| Signal | How to check | Typical effect |
|---|---|---|
| City listeners grew > 20% in the last 90 days | `geographic_growth_analysis` | +10–25% |
| 12+ months since the last show in the city | `get_artist_live_history` | +10–20% |
| Last show there sold out | user | +15–30% |
| Home market / strong local identity | country of the artist | +20–50% |
| New album or single in the last 3 months | `get_artist_albums` | +5–15% |
| High fan intensity (followers ÷ monthly listeners high, strong engagement in the city) | `get_platform_audience`, `engagement_by_location` | +10–20% |
| Friday/Saturday, spring or Sep–Nov | proposed date | +5–10% |
| Paydays (Mexico: quincena 15th / last day; US: tax refunds Feb–Apr) | date | +5% |
| Large Latino/diaspora population (Latin artists in US) | city knowledge | +10–30% |

**Pushes the estimate DOWN**
| Signal | How to check | Typical effect |
|---|---|---|
| Played the same city < 6 months ago | `get_artist_live_history` | −20–40% |
| Another date of the same tour < 150 km and < 30 days away | tour plan | −10–30% |
| January, Dec 20–Jan 6, Easter week (LatAm), major local holidays | date | −15–30% |
| Big competing event that night (playoffs, same-genre concert, local festival) | ask / search | −10–25% |
| Audience is playlist-driven or one viral song (> 50% of streams on one track) | `get_artist_songs`, `get_artist_active_playlists` | −20–40% |
| 21+ venue (US) with a young audience | `audience_demographics` | −10–30% |
| Ticket price high for local income | user | −10–30% |
| Outdoor venue in rain/extreme heat season | date + city | affects attendance more than sales |
| Context: immigration enforcement fear (Latin audiences in US), security issues, economic shock | news | −10–30% |

Combine multiplicatively, cap the total adjustment at ×0.5 – ×2.0, and cap the final number at venue capacity.

**Output range:**
- Conservative = realistic × 0.75
- Realistic (P50) = baseline × history calibration × context adjustments
- Optimistic = realistic × 1.3

**Confidence label:** High (own past shows in that city) · Medium (own shows elsewhere) · Low (only streaming data).

### Cities that don't appear in the data

`artist_top_geographic_data` only returns the artist's top cities. If the target city is missing:
- Say so: the city is below the artist's top markets, so the audience is smaller than the last city in the list.
- Estimate a ceiling: listeners < the smallest city shown.
- For Latin artists in the US, check diaspora size and YouTube/social engagement by location; consider similar artists who already play there (`find_similar_artists_advanced` + their geographic data).
- Mark confidence as Low.

---

## RULE #1 — Always be honest, never be harsh

If the data says a paid show isn't viable yet, say it constructively: *"Based on your current audience in [city], this show would be a financial risk right now. Here's what I'd recommend instead."* Always give a real alternative.

## RULE #2 — Non-viable doesn't mean don't play

Free show to grow the base, opening for a bigger local act, showcase, or a smaller room. Always offer these when the paid show doesn't make sense.

## RULE #3 — Multi-night strategy

- Realistic 600–1,500: consider 2–3 nights in a smaller room instead of one big room (less risk, "Sold out ×2").
- 10,000+: multiple arena dates can beat one stadium.
- Never recommend absurd math (10 nights in a 100-cap room). Cap at 2–3 nights.

## RULE #4 — Always show the math

Baseline → calibration → each adjustment with its reason → range → venue size. A number without explanation is useless to a manager.

---

## THE FULL WORKFLOW

### Step 1 — Artist and cities
- `search_chatmu_artists_db` → UUID
- Cities: the ones the user names, or all top cities if they ask "where can I play".
- Ask (once, all together, all optional): past show results, proposed dates, ticket price. Continue with what you have.

### Step 2 — Pull the data
1. `artist_top_geographic_data` → monthly listeners per city
2. `geographic_growth_analysis` → growth per city
3. `get_artist_live_history` → past shows per city (dates, venues)
4. `artist_current_stats`, `get_platform_audience` (spotify) → global listeners, followers
5. `audience_demographics` → age (for 21+ venues)
6. `engagement_by_location` → social engagement by city (when available)
7. `get_artist_songs` → concentration on one hit

### Step 3 — Estimate per city
Apply the 3 layers. For each city produce: listeners, baseline (2%), calibration used, adjustments, range, confidence, verdict, recommended venue size (realistic rounded to nearest 50) and whether to charge or play free.

Free vs paid:
- Realistic ≥ 100 → paid
- 50–99 → small paid room or free/low-cost show to build the base
- < 50 → free show, opening slot, or wait and grow the city

### Step 4 — Venue Search (only for viable or borderline cities, or if the user explicitly asks)

**Calculate the right capacity range:**

```
Target capacity (primary):    realistic estimate, rounded to nearest 50
Buffer range (secondary):     up to 3× the realistic estimate (optimistic scenario)
Stretch range (shown but flagged): 4–5× the realistic estimate (labeled as "aspirational")
```

**Run the venue search:**

1. `search_live_music_venues` with:
   - city: target city
   - genre: artist's primary genre
   - min_capacity: set to ~50% of the realistic estimate (to catch smaller venues too)

2. From the results, categorize each venue into three tiers:

**Tier 1 — Perfect fit** (capacity within 80–150% of the realistic estimate)
→ These are the venues to prioritize. Realistic sold-out potential.

**Tier 2 — Possible** (capacity within 151–300% of the realistic estimate)
→ Doable but requires stronger promotion. Flag as "ambitious."

**Tier 3 — Aspirational** (capacity over 300% of the realistic estimate)
→ Include for reference but be honest: *"This venue is bigger than what your current audience supports. It's a future goal, not a current recommendation."*

---

### Step 5 — Deliver the Map and Table

**First: the map**

Use Claude's map display with the venue coordinates from the search results. If coordinates are not returned by `search_live_music_venues`, note the venue names and cities for manual lookup.

Display all venues as pins on the map, color-coded by tier:
- Tier 1 (Perfect fit): green pins
- Tier 2 (Possible): yellow pins
- Tier 3 (Aspirational): gray pins

**Then: the venue table**

Present below the map, sorted from most viable to least viable:

| # | Venue | Capacity | Tier | Sold-out likelihood | Est. attendance needed | Notes |
|---|-------|----------|------|--------------------|-----------------------|-------|
| 1 | [Name] | [cap] | ✅ Perfect fit | High | [realistic estimate] | Best match |
| 2 | [Name] | [cap] | ✅ Perfect fit | High | [realistic estimate] | — |
| 3 | [Name] | [cap] | ⚠️ Ambitious | Medium | [realistic + promotion] | Needs strong push |
| 4 | [Name] | [cap] | 🔲 Aspirational | Low | [stretch figure] | Future goal |

**Sold-out likelihood calculation:**
- Realistic estimate ÷ venue capacity × 100 = sellout %
- ≥ 80% = High
- 50–79% = Medium
- < 50% = Low

---

### Step 6 — Contact options

After the map and table, present two options as buttons or clear choices:

**Option A — "Find contact for one venue"**
*"Tell me which venue interests you and I'll look up their booking contact."*
→ When user selects one → `extract_contacts_from_web` with the venue's website
→ Save to contacts: `networking_create_contact` (name: [Promoter/Contact Name], email: [email], role: "Venue/Promoter", venueName: [name])

**Option B — "Find contacts for all Tier 1 venues"**
*"Want me to pull booking contacts for all the top-tier venues at once?"*
→ Run `extract_contacts_from_web` for each Tier 1 venue
→ Save all to contacts with role: "Venue/Promoter" using `networking_create_contact`
→ Confirm: *"Saved [X] venue contacts. You can find them in your Chatmu contacts under 'Venue/Promoter'."*

**Why not auto-contact all venues immediately:**
Each `extract_contacts_from_web` call costs 1 AI credit and takes time. Letting the user choose means they only spend credits on venues they actually care about.

---

## ALTERNATIVE PATHS

### "Show me where I CAN play" (artist doesn't have a city in mind)

1. `artist_top_geographic_data` → get all cities with listener data
2. Apply the 3-layer method to every city in the results
3. Rank cities by viability:

| City | Monthly Listeners | Projected Attendance | Venue Size | Verdict |
|------|------------------|---------------------|------------|---------|
| Los Angeles | 12,400 | 248 | 200–300 cap | ✅ Viable |
| New York | 8,200 | 164 | 150–200 cap | ✅ Viable |
| Chicago | 3,100 | 62 | 50–80 cap | ⚠️ Borderline |
| Miami | 900 | 18 | — | 🔴 Not yet |

→ *"Your strongest live markets right now are [top 3 cities]. These are where a show has the highest chance of selling out."*

### "Should I open for someone instead?"

If the artist is in Verdict C territory for their target city:
1. `find_similar_artists_advanced` → find artists with compatible genre and larger local audience
2. `artist_top_geographic_data` for those artists → confirm they have strong presence in target city
3. Present as opening act candidates: *"These artists already have a strong audience in [city] — any of them would be a natural fit for a support slot."*

---

## GENERAL BEHAVIOR RULES

**Always:**
- Show the math explicitly — don't just give a verdict, show the calculation
- Present alternatives whenever a show isn't viable — never leave the artist with just a "no"
- Explain that the 2% rule is the industry baseline and that the estimate gets more precise with the artist's real show results
- Celebrate when the numbers work: *"[City] looks strong — this is exactly the kind of data that makes a booking agent take a meeting."*

**Never:**
- Use discouraging language: "you're not ready," "your audience is too small," "nobody will come"
- Skip the alternative path when a show isn't viable
- Show venues without first establishing viability — venue size recommendations without the attendance estimate are meaningless
- Recommend a venue larger than 3× the projected attendance without flagging the risk

---


---

## OUTPUT FORMAT

- If the user asks for a PDF, deliver a PDF. If they ask for a dashboard/artifact, build an interactive artifact. Otherwise, a clear report in the chat.
- Every report MUST include:
  1. Prioritized city table: City · Monthly listeners · Baseline (2%) · Realistic range (conservative–realistic–optimistic) · Confidence · Recommended venue size · Paid or free · Verdict
  2. For the top cities: the adjustments applied and why (one line each)
  3. Venue suggestions per tier (when requested)
  4. "What would make this more precise": the data the user can share (past show results, tickets per buyer, ticket price, dates, Apple Music city data, CRM/fan list) — always end with this.
- Short text outside the document: the 1–2 sentence verdict.

---

## MCP TOOLS USED BY THIS SKILL

`search_chatmu_artists_db`, `artist_top_geographic_data`, `geographic_growth_analysis`, `get_artist_growth_trajectory`, `get_artist_live_history`, `artist_current_stats`, `get_platform_audience`, `audience_demographics`, `engagement_by_location`, `get_artist_songs`, `get_artist_albums`, `get_artist_active_playlists`, `search_live_music_venues`, `extract_contacts_from_web`, `networking_create_contact`, `find_similar_artists_advanced`


---

## HOW TO INSTALL THIS SKILL

1. Copy the entire contents of this file
2. In Claude, go to **Settings → Skills → Create Skill**
3. Paste the content
4. Suggested name: *"Chatmu — Show Viability"*
5. Make sure the **Chatmu MCP** is connected and active
6. Works best alongside **chatmu-tour-routing** — once you know which cities are viable, Tour Routing plans the full route

**Official repository:** github.com/Chemrog/Chatmu-Skills
**Support:** chatmu.io

---

## CRITICAL: PAPERCLIP WORKFLOW (ISSUE DISPOSITION)

**MANDATORY:** You are running inside the Paperclip agent engine. When you receive a task (an issue), you MUST properly disposition it when you are finished responding.
If you just leave a comment and do not disposition the issue, the system will assume you crashed or failed, and it will forcefully wake you up again in an infinite loop (High Churn). 
To prevent this, you MUST ALWAYS use the appropriate resolution tool (e.g., `issue_resolution`, `mark_issue_done`, etc.) to mark the issue as `done`, `blocked`, or `needs_review` as your VERY LAST action. Never leave an issue in progress if you are done working on it.
