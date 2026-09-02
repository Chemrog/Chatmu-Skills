```text
    ▄▄▄▄   ▄▄                                               
  ██▀▀▀▀█  ██                    ██                         
 ██▀       ██▄████▄   ▄█████▄  ███████   ████▄██▄  ██    ██ 
 ██        ██▀   ██   ▀ ▄▄▄██    ██      ██ ██ ██  ██    ██ 
 ██▄       ██    ██  ▄██▀▀▀██    ██      ██ ██ ██  ██    ██ 
  ██▄▄▄▄█  ██    ██  ██▄▄▄███    ██▄▄▄   ██ ██ ██  ██▄▄▄███ 
    ▀▀▀▀   ▀▀    ▀▀   ▀▀▀▀ ▀▀     ▀▀▀▀   ▀▀ ▀▀ ▀▀   ▀▀▀▀ ▀▀ 
```

<p align="center">
  <img src="./assets/cozy_studio.png" alt="Chatmu Skills Banner" width="600">
</p>


# Chatmu Skills — Claude AI Skill Library

> **AI for the industry. Humans for the music.**

Official collection of Claude Skills for the Chatmu 3.5 MCP. Install the skill that matches your role, connect the Chatmu MCP, and unlock a specialized AI expert built specifically for your workflow in the music industry. You can manage and download all your skills directly inside your dashboard at **[chatmu.io](https://chatmu.io)** under the **MCP / Skills** tab in the left panel.

**[chatmu.io](https://chatmu.io)** · **[Dashboard](https://chatmu.io)** · **[Docs](https://chatmu.io/help/chatmu)**

---

## What are these Skills?

Each directory in this repository represents a **Claude Skill** — a specialized system prompt with a mandatory YAML frontmatter configuration that turns Claude into a music industry expert for a specific role. Combined with the **Chatmu MCP** (which gives Claude access to real-time streaming data, audience analytics, distribution tools, and more), these Skills know exactly which tools to use, when to use them, and how to interpret the results for your specific situation.

```
Claude (brain) + Chatmu MCP (muscle) + Skill (instructions) = Your AI music team
```

No generic advice. No hallucinated data. Just real industry intelligence calibrated to your role.

---

## 📋 What You Need Before Starting (Requirements)

To use these Skills, make sure you have these three simple things:

1. **A Chatmu Account** — [Sign up for free at chatmu.io](https://chatmu.io) to get your music dashboard.
2. **Claude.ai Account** — Any Claude.ai account (free or paid) works perfectly!
3. **Your Chatmu 3.5 MCP connected to Claude** — Connect Claude to your real-time music data in seconds via OAuth. You can grab the connection link directly in your dashboard at **[chatmu.io](https://chatmu.io)** in the **MCP / Skills** section!

   ### 🔌 How to Connect Chatmu MCP to Claude
   
   1. Go directly to Claude's Connector Settings:
      * Open **[Claude.ai Connectors Settings](https://claude.ai/customize/connectors)** in your browser.
      * *(Alternatively, in Claude.ai, click your **Profile avatar** in the bottom-left ➔ **<kbd>Customize</kbd>** ➔ **<kbd>Connectors</kbd>**).*
   2. Click the **<kbd>Add custom connector</kbd>** button (or the `+` icon next to Connectors).
   3. In the URL/endpoint field, enter the Chatmu MCP OAuth URL (which you can copy from the **MCP / Skills** section in your dashboard):
      * `https://mcp-chatmu.aaatmi.com/mcp-oauth`
   4. Follow the prompt to authorize Claude to access your Chatmu account. Simply sign in if you aren't already, and approve the connection.
   5. Once connected, make sure the connector is active and the required tools are enabled in your chat sessions!

---

## 🚀 How to Install a Skill (Super Simple Guide)

Claude Skills let you import specialized "music brains" instantly in less than 60 seconds! Follow this step-by-step guide:

### 📥 Step 1: Download your Skill ZIP
Look at the **Skill Library** tables below. Find the skill you want and click the link in the **"Import to Claude (Download ZIP)"** column.

> [!WARNING]
> **⚠️ CRITICAL FOR MAC / SAFARI USERS:** 
> Do **NOT** double-click or unzip the downloaded file! Safari might automatically unzip it for you. If it does, right-click the unzipped folder and select **"Compress"** to turn it back into a `.zip` file. Claude **MUST** receive a raw `.zip` file.

---

### 👤 Step 2: Open Claude & Navigate to Settings
1. Go to [Claude.ai](https://claude.ai) and make sure you are logged in.
2. Look at the **bottom-left corner** of your screen and click on your **Profile Name/Avatar**.
3. In the menu that pops up, click on **<kbd>Customize</kbd>** and then click on **<kbd>Skills</kbd>**.

> [!TIP]
> **💡 First time using Skills?**
> Make sure **Code Execution** is turned on! In that same settings menu, go to **<kbd>Settings</kbd>** ➔ **<kbd>Capabilities</kbd>** and ensure **Code Execution** is checked.

---

### ⚙️ Step 3: Upload the ZIP
1. Click the **`+`** icon (located on the left panel, next to *Personal skills* in the *Skills* list).
2. Click on **<kbd>Create skill</kbd>** in the dropdown menu, and select **<kbd>Upload a skill</kbd>** from the side-menu.
3. A popup window titled **"Upload skill"** will appear. Simply **drag and drop** the `.zip` file you downloaded in Step 1 into the box, or click inside it to select the file from your computer.
4. Claude will automatically read the package and fill in all the details! Finally, click **<kbd>Publish</kbd>** (or save) to activate your new music expert!

---

### 🎵 Step 4: Start a New Chat and Jam!
1. Start a **new conversation** on Claude.ai.
2. Type a message like: *"Hey, run an onboarding session!"* or *"Analyze my Spotify streams."*
3. Claude will automatically activate the Skill, connect to your Chatmu MCP, and build a beautiful interactive dashboard for you!

*Alternatively, you can create a skill manually by copying the entire content of the `SKILL.md` file (including the frontmatter `---` lines at the top) and pasting it into the Claude Skill creator.*

---

## Skill Library

### For Artists

| Skill | Directory | Import to Claude (Download ZIP) | Description |
|-------|-----------|---------------------------------|-------------|
| 🎯 **Onboarding** | [`chatmu-onboarding/`](./chatmu-onboarding) | [chatmu-onboarding.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-onboarding.zip) | First contact — understands who you are, where you're at, and points you to the right next step. |
| 🚀 **Release Flow** | [`chatmu-release/`](./chatmu-release) | [chatmu-release.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-release.zip) | Full launch workflow: song analysis → date → distribution → contracts → content strategy → post-release. |
| 📊 **Analytics** | [`chatmu-analytics/`](./chatmu-analytics) | [chatmu-analytics.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-analytics.zip) | Deep analysis of your streams, audience, geography, playlists, content, and catalog. |
| 🎤 **Show Viability** | [`chatmu-show-viability/`](./chatmu-show-viability) | [chatmu-show-viability.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-show-viability.zip) | Data-backed answer to "can I play [city]?" using the industry-standard 2% rule. |
| 📋 **Playlist Pitching** | [`chatmu-playlist-pitching/`](./chatmu-playlist-pitching) | [chatmu-playlist-pitching.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-playlist-pitching.zip) | Research curators, pitch editorial and independent playlists, track placements and reach. |
| 📻 **Radio Promotion** | [`chatmu-radio-promotion/`](./chatmu-radio-promotion) | [chatmu-radio-promotion.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-radio-promotion.zip) | Target stations, track spins, pitch programmers, and report airplay. |
| 📣 **Social Campaign** | [`chatmu-social-campaign/`](./chatmu-social-campaign) | [chatmu-social-campaign.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-social-campaign.zip) | Plan, publish and measure release-driven social campaigns across connected accounts. |
| ✍️ **Content Strategy** | [`chatmu-content-strategy/`](./chatmu-content-strategy) | [chatmu-content-strategy.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-content-strategy.zip) | Design 9:16 content strategy, hooks and weekly batches aligned to release phases. |
| 🎬 **Video Content** | [`chatmu-video-content/`](./chatmu-video-content) | [chatmu-video-content.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-video-content.zip) | Produce lyric videos, visualizers and 9:16 pieces via Chatmu render pipeline. |
| 🧠 **Fan DNA** | [`chatmu-fan-dna/`](./chatmu-fan-dna) | [chatmu-fan-dna.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-fan-dna.zip) | Psychographic + demographic fan analysis, personas, and social→streaming conversion. |
| 🎪 **Show Producer** | [`chatmu-show-producer/`](./chatmu-show-producer) | [chatmu-show-producer.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-show-producer.zip) | Produce a show end-to-end: venue, sponsors, poster, opening acts, run-of-show, budget. |
| 🧭 **Career Roadmap** | [`chatmu-career-roadmap/`](./chatmu-career-roadmap) | [chatmu-career-roadmap.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-career-roadmap.zip) | Define career horizon & tempo (sprint vs long game), then a phased roadmap with a Mermaid timeline. |

### For Industry Professionals

| Skill | Directory | Import to Claude (Download ZIP) | Description |
|-------|-----------|---------------------------------|-------------|
| 💼 **Music Manager** | [`chatmu-manager/`](./chatmu-manager) | [chatmu-manager.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-manager.zip) | Weekly briefings, investment intelligence, press kit generation, roster overview, strategic direction. |
| 📈 **Artist Report** | [`chatmu-artist-report/`](./chatmu-artist-report) | [chatmu-artist-report.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-artist-report.zip) | Formatted performance reports (weekly/monthly/release) for sending to labels — data diagnostic + content strategy. |
| 🎟️ **Booking Agency** | [`chatmu-booking/`](./chatmu-booking) | [chatmu-booking.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-booking.zip) | Venue discovery, contact extraction, booking pitches, CRM, full outreach workflow. |
| 🗺️ **Tour Routing** | [`chatmu-tour-routing/`](./chatmu-tour-routing) | [chatmu-tour-routing.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-tour-routing.zip) | Audience-first tour planning: anchor dates, optimized route, venue search, venue outreach. |
| 🔍 **A&R Intelligence** | [`chatmu-anr/`](./chatmu-anr) | [chatmu-anr.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-anr.zip) | Emerging artist discovery, label status checks, market intelligence, comparison reports. |
| 📄 **Music Contracts** | [`chatmu-contracts/`](./chatmu-contracts) | [chatmu-contracts.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-contracts.zip) | Professional-grade music industry contracts (split sheets, producer agreements, work for hire). |
| 📖 **Music Publishing** | [`chatmu-publishing/`](./chatmu-publishing) | [chatmu-publishing.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-publishing.zip) | Songwriter registries, PRO metadata sheets, composition splitting, rights administration. |
| 🎬 **Sync & Licensing** | [`chatmu-sync-licensing/`](./chatmu-sync-licensing) | [chatmu-sync-licensing.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-sync-licensing.zip) | Prep catalog for sync, pitch supervisors, negotiate fees, track placements and cue sheets. |
| 🎧 **Music Supervision** | [`chatmu-music-supervision/`](./chatmu-music-supervision) | [chatmu-music-supervision.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-music-supervision.zip) | Answer supervision briefs, shortlist by emotional fit, run clearance and cue sheets. |
| 💵 **Royalties** | [`chatmu-royalties/`](./chatmu-royalties) | [chatmu-royalties.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-royalties.zip) | Audit statements, verify splits/metadata, chase black-box, prep MLC registration. |
| 📰 **PR & Press Kit** | [`chatmu-pr-presskit/`](./chatmu-pr-presskit) | [chatmu-pr-presskit.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-pr-presskit.zip) | Build press kit and EPK, pitch press and podcasts, follow up. |
| 📑 **Contract Drafting** | [`chatmu-contract-drafting/`](./chatmu-contract-drafting) | [chatmu-contract-drafting.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-contract-drafting.zip) | Draft/review split sheets, producer, management and feature deals with red-flag checks. |
| 🛍️ **Merch** | [`chatmu-merch/`](./chatmu-merch) | [chatmu-merch.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-merch.zip) | Plan merch line, model margins/P&L, and organize tour merch operations. |
| 🤝 **Brand Partnerships** | [`chatmu-brand-partnerships/`](./chatmu-brand-partnerships) | [chatmu-brand-partnerships.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-brand-partnerships.zip) | Build brand pitch deck, target sponsors, measure activation. |
| 📊 **Market Research** | [`chatmu-market-research/`](./chatmu-market-research) | [chatmu-market-research.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-market-research.zip) | Executive-grade market research on tiers, genres, locations and competition. |
| 🏷️ **Label Roster** | [`chatmu-label-roster/`](./chatmu-label-roster) | [chatmu-label-roster.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-label-roster.zip) | Analyze label rosters, signings, trajectories and signing signals. |

---

## Directory Structure

This repository is organized to follow the official Claude Skills specification:

```
Chemrog/Chatmu-Skills (GitHub repo)
├── README.md                 ← Main documentation and links
├── zips/                     ← Pre-packaged ZIP files for easy installation
│   ├── chatmu-onboarding.zip
│   ├── chatmu-release.zip
│   └── ...
├── chatmu-onboarding/        ← Skill directory
│   └── SKILL.md              ← Skill prompt with YAML frontmatter
├── chatmu-artist-report/     ← Skill directory
│   ├── SKILL.md
│   └── references/
│       └── report-template.md
├── chatmu-release/
│   └── SKILL.md
├── chatmu-analytics/
│   └── SKILL.md
... (a directory per skill)
```

---

## Which Skill do I need?

```
Are you an artist managing your own career?
  └── New to Chatmu?              → chatmu-onboarding (start here)
  └── Launching a song?           → chatmu-release
  └── Checking your numbers?      → chatmu-analytics
  └── Thinking about live shows?  → chatmu-show-viability

Are you a manager?
  └── chatmu-manager
  └── Reporting to a label?      → chatmu-artist-report

Are you a booking agent or agency?
  └── Booking shows?              → chatmu-booking
  └── Planning a full tour?       → chatmu-tour-routing

Are you an A&R or label executive?
  └── chatmu-anr

Are you a songwriter or publisher?
  └── chatmu-publishing
```

---

## Can I use multiple Skills at once?

Yes. Claude Skills stack. Recommended combinations:

- **Artist full stack:** Onboarding + Release + Analytics + Show Viability
- **Manager stack:** Manager + Artist Report + Analytics + Tour Routing + Contracts + Publishing
- **Booking stack:** Booking Agency + Tour Routing + Show Viability
- **A&R stack:** A&R Intelligence + Analytics

When Skills overlap, Claude uses context to determine which is most relevant. The more specific the Skill, the more it overrides general behavior.

---

## The 2% Rule — Why it's in multiple Skills

Several Skills reference the **2% Rule** — the industry standard for estimating how many fans will show up to a live show in a city:

> 2% of monthly Spotify listeners in a city = projected live attendance

A show is economically viable when:
- **2% ≥ 100 people**, OR
- **Monthly listeners in that city ≥ 10,000**

This benchmark is used by professional booking agents and managers worldwide. Chatmu formalizes it so artists and their teams can make data-driven decisions instead of guessing. It's in `chatmu-show-viability/SKILL.md`, `chatmu-tour-routing/SKILL.md`, and `chatmu-booking/SKILL.md`.

---

## Chatmu MCP — Tool reference

These Skills are built on top of the **Chatmu MCP** — 100+ specialized tools that give Claude access to:

- **Interactive MCP Apps (UI Tools)**: Direct web-based interfaces embedded in your chat for:
  - **Open Chatmu Catalog Uploader** — Upload music catalogs in bulk.
  - **Open Chatmu Lyrics Editor** — Visual editor for song lyrics.
  - **Open Chatmu Song Sorter** — Classify and organize your tracks.
  - **Open Chatmu Video Creator** — Render custom promotional videos.
  - **Open Distribution Uploader** — Upload audio assets for release.
  - **Open Distribution Wizard** — Step-by-step music distribution manager.
- **Cross-Platform Analytics**: Real-time streaming data across all major music platforms (Spotify, Apple Music, Amazon Music, Deezer, TikTok, YouTube, etc.).
- **Audience Intelligence**: Demographic details, geographic reach, and fan retention metrics.
- **Outreach & CRM**: Tour routing, venue discovery, and pitching emails.
- **A&R Insights**: Emerging talent discovery and label roster research.

Full tool documentation: [chatmu.io/help/api](https://chatmu.io/help/api)

---

## Skill versions

| Version | Date | Notes |
|---------|------|-------|
| 1.3 | July 2026 | Added web search (qualitative context) to `chatmu-anr` — market intelligence, artist validation, label status cross-check. |
| 1.2 | July 2026 | Added `chatmu-artist-report` Skill (label-facing performance reports). Now 11 Skills. |
| 1.1 | June 2026 | Added OAuth support, interactive MCP Apps, cross-platform metrics, and expanded to 10 Skills. |
| 1.0 | May 2026 | Initial release — 9 Skills across 4 roles |

Skills are versioned independently. Check the header of each file for its current version.

---

## Contributing

Found a bug in a Skill? Want to translate one to another language? Have a workflow that should be added?

1. Fork this repo
2. Make your changes
3. Open a PR with a clear description of what changed and why
4. Tag it with the relevant role: `artist`, `manager`, `booking`, `anr`

---

```text
            ****      *           
          **     ***+   +++       
       * *                ++      
    **   +                 ++     
   **                      ++     
   **      *****   *+++++    ++   
    **    *  **** ++ +++++     +  
  **      *  **** ++ +++++   ++   
  **        ****+    ++++    ++    
  **             +++++        +    
   ***+                      ++    
      ++                    ++     
      ++                    ++     
       *+*  +++     +++    ++      
          ++  ++  +++  ====        
```

---

## Credits

Created by **[Chema Rodríguez](https://instagram.com/chema_rodriguez.mp3)** & the [Chatmu](https://chatmu.io) team.  
**AI for the industry. Humans for the music.**

---

*These Skills are provided as-is. Music industry data is sourced in real-time through the Chatmu MCP. Legal documents generated by these Skills (split sheets, contracts) are templates and do not constitute legal advice.*
