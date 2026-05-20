```
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

```
    ▄▄▄▄   ▄▄                                               
  ██▀▀▀▀█  ██                    ██                         
 ██▀       ██▄████▄   ▄█████▄  ███████   ████▄██▄  ██    ██ 
 ██        ██▀   ██   ▀ ▄▄▄██    ██      ██ ██ ██  ██    ██ 
 ██▄       ██    ██  ▄██▀▀▀██    ██      ██ ██ ██  ██    ██ 
  ██▄▄▄▄█  ██    ██  ██▄▄▄███    ██▄▄▄   ██ ██ ██  ██▄▄▄███ 
    ▀▀▀▀   ▀▀    ▀▀   ▀▀▀▀ ▀▀     ▀▀▀▀   ▀▀ ▀▀ ▀▀   ▀▀▀▀ ▀▀ 
```

# Chatmu Skills — Claude AI Skill Library

> **AI for the industry. Humans for the music.**

Official collection of Claude Skills for the Chatmu MCP. Install the skill that matches your role, connect the Chatmu MCP, and unlock a specialized AI expert built specifically for your workflow in the music industry.

**[chatmu.io](https://chatmu.io)** · **[Get the MCP](https://chatmu.io/pricing)** · **[Docs](https://chatmu.io/help/chatmu)**

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

1. **A Chatmu Account** — [Sign up for free at chatmu.io](https://chatmu.io) to access the music database.
2. **Claude.ai Account** — Any Claude.ai account (free or paid) works perfectly!
3. **Your Chatmu MCP Link** — This is the magic link that connects Claude to your actual music data. If you haven't done it yet, follow the [Quick MCP Setup Guide](https://chatmu.io/help/chatmu) to add this SSE URL to your Claude:
   ```
   https://mcp-chatmu.aaatmi.com/mcp?key=YOUR_CHATMU_API_KEY
   ```

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
3. In the menu that pops up, click on **`<kbd>Customize</kbd>`** and then click on **`<kbd>Skills</kbd>`**.

> [!TIP]
> **💡 First time using Skills?**
> Make sure **Code Execution** is turned on! In that same settings menu, go to **`<kbd>Settings</kbd>`** ➔ **`<kbd>Capabilities</kbd>`** and ensure **Code Execution** is checked.

---

### ⚙️ Step 3: Upload the ZIP
1. Click the **`<kbd>Create Skill</kbd>`** button (or the **`+`** icon) on the top-right corner of the Skills dashboard.
2. In the skill creator window, look at the top right and click **`<kbd>Upload a skill</kbd>`**.
3. Select the `.zip` file you downloaded in Step 1.
4. The system will automatically populate all the details! Click **`<kbd>Save</kbd>`** or **`<kbd>Publish</kbd>`** at the bottom.

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

### For Industry Professionals

| Skill | Directory | Import to Claude (Download ZIP) | Description |
|-------|-----------|---------------------------------|-------------|
| 💼 **Music Manager** | [`chatmu-manager/`](./chatmu-manager) | [chatmu-manager.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-manager.zip) | Weekly briefings, investment intelligence, press kit generation, roster overview, strategic direction. |
| 🎟️ **Booking Agency** | [`chatmu-booking/`](./chatmu-booking) | [chatmu-booking.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-booking.zip) | Venue discovery, contact extraction, booking pitches, CRM, full outreach workflow. |
| 🗺️ **Tour Routing** | [`chatmu-tour-routing/`](./chatmu-tour-routing) | [chatmu-tour-routing.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-tour-routing.zip) | Audience-first tour planning: anchor dates, optimized route, venue search, venue outreach. |
| 🔍 **A&R Intelligence** | [`chatmu-anr/`](./chatmu-anr) | [chatmu-anr.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-anr.zip) | Emerging artist discovery, label status checks, market intelligence, comparison reports. |
| 📄 **Music Contracts** | [`chatmu-contracts/`](./chatmu-contracts) | [chatmu-contracts.zip](https://github.com/Chemrog/Chatmu-Skills/raw/main/zips/chatmu-contracts.zip) | Professional-grade music industry contracts (split sheets, producer agreements, work for hire). |

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

Are you a booking agent or agency?
  └── Booking shows?              → chatmu-booking
  └── Planning a full tour?       → chatmu-tour-routing

Are you an A&R or label executive?
  └── chatmu-anr
```

---

## Can I use multiple Skills at once?

Yes. Claude Skills stack. Recommended combinations:

- **Artist full stack:** Onboarding + Release + Analytics + Show Viability
- **Manager stack:** Manager + Analytics + Tour Routing + Contracts
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

These Skills are built on top of the **Chatmu MCP** — 71 specialized tools that give Claude access to:

- Real-time streaming data across 27+ platforms
- Audience demographics and engagement quality
- Global playlist and editorial tracking
- Music distribution workflow
- Venue and festival databases
- Verified curator contacts
- AI audio analysis and lyric transcription
- Cover art generation
- Email outreach and CRM

Full tool documentation: [chatmu.io/help/api](https://chatmu.io/help/api)

---

## Skill versions

| Version | Date | Notes |
|---------|------|-------|
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

## Credits

Created by **[Chema Rodríguez](https://instagram.com/chemarodriguezx)** & the [Chatmu](https://chatmu.io) team.  
Powered by [Claude](https://claude.ai) + the Chatmu MCP.  
**AI for the industry. Humans for the music.**

---

*These Skills are provided as-is. Music industry data is sourced in real-time through the Chatmu MCP. Legal documents generated by these Skills (split sheets, contracts) are templates and do not constitute legal advice.*
