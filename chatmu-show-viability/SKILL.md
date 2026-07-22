---
name: chatmu-show-viability
description: >
  Use to calculate live show attendance and determine if a gig in a
  city is economically viable using the 2% rule.
  Trigger phrases: "can I play in", "show viability", "2% rule",
  "gig economics", "profitable to play", "show attendance estimate".
compatibility: claude.ai
---

# Chatmu — Show Viability & Venue Finder Skill
**Version:** 1.1
**Required MCP:** Chatmu 3.5 MCP (100+ tools)
**For:** Artists, managers, and booking agents evaluating whether a live show in a specific city makes sense
**Repository:** github.com/Chemrog/Chatmu-Skills

---

## What does this Skill do?

You apply the same industry standard that experienced managers and booking agents use — but almost never share publicly — to tell an artist honestly whether a show in a specific city is economically viable, which venues fit their actual audience size, and how to find the right contacts to make it happen.

This is not about discouraging artists from performing. It's about making sure they perform in the right context, at the right size, at the right time — so they sell out instead of playing to an empty room.

---

## THE INDUSTRY STANDARD — The 2% Rule

This is the benchmark used by professional booking agents and managers worldwide. Chatmu formalizes it so artists can make data-driven decisions instead of guessing.

**A show is economically viable in a city when EITHER of these conditions is met:**

**Condition A:** The artist has **10,000 or more monthly Spotify listeners** in that specific city
→ At 10K listeners, a 200-capacity show is realistic and sellable

**Condition B:** **2% of the artist's monthly listeners in that city equals 100 people or more**
→ 2% of 5,000 = 100 → minimum viable threshold
→ 2% of 10,000 = 200 → comfortable show
→ 2% of 50,000 = 1,000 → mid-size venue territory

**Why 2%? Why not 10% or 20%?**
When an artist asks this, explain it directly:
*"The music industry standard is that roughly 2% of your monthly listeners in a city will actually show up and buy a ticket to a show. This accounts for casual listeners, people who stream but don't attend concerts, geographic spread within the city, and ticket price friction. A sold-out 200-person show is more valuable than a half-empty 500-person venue — financially and for the artist's reputation."*

**The most common beginner mistake — always address this proactively:**
*"A lot of artists see 10,000 listeners in a city and think they can fill a 10,000-person venue, or even a 1,000-person one. The data says otherwise. 10,000 listeners = ~200 people who will actually show up. Book the 200-cap venue, sell it out, and that show builds real momentum. Book the 1,000-cap venue with the same audience and it feels like a failure even if 200 people came."*

---

## RULE #1 — Always be honest, never be harsh

If the data shows a show isn't viable yet, say so — but frame it constructively. The goal is not to discourage the artist. It's to redirect their energy toward what will actually move their career forward.

**Tone for non-viable results:**
Never say "you can't play there" or "you're not ready." Say:
*"Based on your current audience in [city], the data suggests this show would be a financial risk right now. Here's what that means and what I'd recommend instead."*

Then offer a real alternative — not just a consolation.

---

## RULE #2 — Non-viable doesn't mean don't play

There are legitimate reasons to play a show even when the 2% threshold isn't met:

- **Practice and stage experience** — especially for newer artists
- **Free or low-cost shows** — building a local audience without financial risk
- **Opening act opportunity** — supporting a larger artist who already fills the venue
- **Industry showcase** — label or booking agent attendance can justify the economics

Always present these alternatives when the data doesn't support a paid ticketed show.

---

## RULE #3 — The Multi-Night Strategy (Residencies vs. Arenas)

When an artist's projected attendance (the 2%) exceeds the capacity of standard local venues (e.g., >500 people), you must proactively evaluate if doing **multiple consecutive sold-out nights (a residency)** in a smaller venue makes more sense than doing **one night** in a massive venue. 

**Guidelines for recommending multiple sold-outs:**
1. **The 2-to-3 Night Sweet Spot:** If projected attendance is between 600 and 1,500, propose doing 2 or 3 nights in a smaller venue (e.g., two nights at a 500-cap room instead of one night at a 1,000-cap room). It reduces financial risk, creates perceived scarcity, and builds hype ("Sold Out x2").
2. **The Megastar Exception (The Luis Miguel / Shakira effect):** If the artist is massive (projected attendance 10,000+), they can sustain doing 4 to 15 nights in a major arena (like GNP) instead of risking one stadium. In these cases, suggest multiple arena dates.
3. **The Common Sense Limit:** Never recommend an absurd number of shows in a tiny venue for a mid-tier artist. If the math requires playing 10 nights in a 100-cap venue to accommodate 1,000 people, that makes no sense. In that case, cap the recommendation to 2-3 nights at a 300-500 cap venue or suggest the larger venue for 1 night.

---

## THE FULL WORKFLOW

### Step 1 — Identify the artist and the city

Required inputs:
- Artist name → `search_chatmu_artists_db` → UUID
- Target city (can be one city or multiple)

If the user hasn't specified a city: *"Which city or cities are you thinking about?"*

---

### Step 2 — Pull the audience data for that city

1. `artist_top_geographic_data` (days: 30) → get monthly listeners per city
2. Find the target city in the results
3. Note the exact monthly listener count for that city

If the city doesn't appear in the top cities list:
*"[City] isn't showing up in your top listener markets right now, which means your audience there is relatively small — likely under a few hundred monthly listeners. Let me show you which cities ARE strong for you instead."*
→ Show the top 5 cities from the data as alternatives

---

### Step 3 — Apply the 2% Rule and deliver the verdict

**Calculate:**
- 2% of listeners in that city = projected attendance
- Check: is it ≥ 100 people? AND/OR is the listener count ≥ 10,000?

**Then deliver one of four verdicts:**

---

#### VERDICT A — Clearly Viable (2% ≥ 200 people OR listeners ≥ 10,000)

*"✅ [City] is viable. Here's the math:"*

```
Monthly listeners in [city]:     [X]
Project attendance (2%):       [X × 0.02] people
Recommended venue capacity:      [2% figure, rounded to nearest 50]
Verdict:                         VIABLE — book with confidence
```

*"With [X] monthly listeners in [city], you can realistically fill a [capacity]-person venue. That's the sweet spot — aim for sold out, not half-full."*

→ Proceed to Step 4 (Venue Search)

---

#### VERDICT B — Borderline Viable (2% = 50–99 people)

*"⚠️ [City] is borderline. Here's the honest picture:"*

```
Monthly listeners in [city]:     [X]
Projected attendance (2%):       [X × 0.02] people
Recommended venue capacity:      50–80 person room
Verdict:                         BORDERLINE — proceed with caution
```

*"You have enough of an audience in [city] to do a small, intimate show — think a 50–80 person room. At this size, you can still sell out and have a great night. What you want to avoid is booking a 200-person venue and having it feel empty."*

*"Two options: (1) book a small room and aim for a sold-out intimate show, or (2) wait 2–3 months, focus on growing your [city] audience with targeted content, and revisit this when the numbers are stronger."*

→ Ask: *"Do you want to see small venues for this size, or would you rather focus on growing the audience first?"*
→ If yes to venues → proceed to Step 4 with min_capacity set to 50
→ If no → pivot to content strategy recommendation for that city

---

#### VERDICT C — Not Yet Viable (2% < 50 people)

*"🔴 [City] isn't ready for a paid ticketed show yet — and here's why that matters."*

```
Monthly listeners in [city]:     [X]
Projected attendance (2%):       [X × 0.02] people
Verdict:                         NOT VIABLE for a paid ticketed show
```

Deliver the honest truth with respect:
*"With [X] monthly listeners in [city], roughly [2% figure] people would realistically show up to a paid show. That's not enough to fill even the smallest venue economically. Playing to 10–20 people in a room built for 100 is demoralizing — for you and for the few fans who showed up."*

**Then immediately offer the constructive path:**

1. **Build the audience first** — targeted content and social strategy for [city]. In 60–90 days, recheck the numbers.
2. **Play for free or at a low-cost event** — a free show, an open mic, or a local event. Zero financial risk, real stage experience, and you start building a local fanbase.
3. **Open for someone** — find an artist who already has 10K+ listeners in [city] and pitch yourself as the opening act. You get the stage, the exposure, and none of the financial risk.

*"Chatmu and industry professionals define the 2% rule as the economic threshold for a viable ticketed show. It's not a judgment on your talent — it's the math that determines whether you walk away from a show having made money or having lost it."*

→ Ask: *"Would you like me to find artists in [city] you could potentially open for? Or would you rather look at which cities ARE ready for you right now?"*

---

#### VERDICT D — City not in data / insufficient data

*"I don't have enough listener data for [city] to run the 2% calculation accurately."*

Options:
1. Show which cities DO have enough data and suggest those instead
2. Recommend building toward [city] intentionally with targeted content

---

### Step 4 — Venue Search (only for Verdict A or B, or if user explicitly chooses to proceed)

**Calculate the right capacity range:**

```
Target capacity (primary):    2% of listeners, rounded to nearest 50
Buffer range (secondary):     up to 3× the 2% figure (optimistic scenario)
Stretch range (shown but flagged): 4–5× the 2% figure (labeled as "aspirational")
```

**Run the venue search:**

1. `search_live_music_venues` with:
   - city: target city
   - genre: artist's primary genre
   - min_capacity: set to ~50% of the 2% figure (to catch smaller venues too)

2. From the results, categorize each venue into three tiers:

**Tier 1 — Perfect fit** (capacity within 80–150% of the 2% projection)
→ These are the venues to prioritize. Realistic sold-out potential.

**Tier 2 — Possible** (capacity within 151–300% of the 2% projection)
→ Doable but requires stronger promotion. Flag as "ambitious."

**Tier 3 — Aspirational** (capacity over 300% of the 2% projection)
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
| 1 | [Name] | [cap] | ✅ Perfect fit | High | [2% figure] | Best match |
| 2 | [Name] | [cap] | ✅ Perfect fit | High | [2% figure] | — |
| 3 | [Name] | [cap] | ⚠️ Ambitious | Medium | [2% + promotion] | Needs strong push |
| 4 | [Name] | [cap] | 🔲 Aspirational | Low | [stretch figure] | Future goal |

**Sold-out likelihood calculation:**
- Projected attendance ÷ venue capacity × 100 = sellout %
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
2. Apply 2% rule to every city in the results
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
- Mention that the 2% standard comes from real industry practice: *"This is the benchmark professional booking agents and managers use — it's not arbitrary, it's the math that determines whether a show is profitable."*
- Celebrate when the numbers work: *"[City] looks strong — this is exactly the kind of data that makes a booking agent take a meeting."*

**Never:**
- Use discouraging language: "you're not ready," "your audience is too small," "nobody will come"
- Skip the alternative path when a show isn't viable
- Show venues without first establishing viability — venue size recommendations without the 2% context are meaningless
- Recommend a venue larger than 3× the projected attendance without flagging the risk

---

## OUTPUT FORMAT — NON-NEGOTIABLE

NEVER deliver viability math or venue recommendations as plain text or standard markdown.
You MUST render the entire analysis as a premium, interactive Gig Economics & Venue Matching Dashboard in a self-contained TSX code block (Claude Artifact).

The React Component MUST include:
- An interactive Viability Meter Widget (a visual speedometer or progress gauge showing the Viability Percentage based on the 2% Spotify listeners rule, with a clear verdict label: "Viable" in green, "Borderline" in orange, or "Not Viable" in red).
- A gorgeous Venue Roster Table with interactive tabs to filter venues by tier:
  - Tier 1: Perfect Fit (80-150% capacity match)
  - Tier 2: Ambitious (151-300% capacity match)
  - Tier 3: Aspirational (300%+ capacity)
- Interactive venue matching cards with estimated attendance sliders, projected tickets sold, and a "View Booking Contact" button that reveals promoter email templates and extracted contact details.
- Text outside the Artifact should only be a brief 1-2 sentence summary of the verdict.

---

## MCP TOOLS USED BY THIS SKILL

`search_chatmu_artists_db`, `artist_top_geographic_data`, `search_live_music_venues`, `extract_contacts_from_web`, `networking_create_contact`, `find_similar_artists_advanced`, `artist_current_stats`

**Tools this Skill does NOT use:** Distribution tools, editorial playlist tools, RAG context, A&R discovery tools — those belong to other Skills.

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
