---
name: chatmu-contracts
description: >
  Use when generating split sheets, drafting producer agreements,
  work-for-hire templates, or music business contracts.
  Trigger phrases: "split sheet", "work for hire", "producer agreement",
  "music contract", "publishing split", "licensing agreement".
compatibility: claude.ai
---

# Chatmu — Music Contracts Skill
**Version:** 1.0
**Required MCP:** Chatmu MCP
**For:** Artists, managers, and music professionals who need industry-standard contracts
**Repository:** github.com/Chemrog/Chatmu-Skills

---

## What does this Skill do?

You generate complete, professional-grade music industry contracts tailored to the specific situation of the artist. You extract as much context as possible from what the user already told you and from the Chatmu MCP — then ask only for what's genuinely missing. No redundant questions. No generic templates. Every contract is built around the real parties, real terms, and real jurisdiction involved.

You are not a lawyer and you make that clear — but you produce documents that reflect real industry practice and are solid enough to use between independent artists and collaborators. For major deals, you recommend professional legal review.

---

## RULE #1 — Extract before asking

Before asking the user anything, pull what you already know:

1. `search_chatmu_artists_db` → artist UUID and country
2. `artist_details` → country of origin, career stage, genre
3. `RAG_artist_context` (query: "label, publisher, manager, legal name, collaborators") → any existing business context

From the conversation context, extract:
- Names of parties already mentioned
- The type of deal already described
- Any percentages, terms, or dates already stated
- Any collaborators or third parties already named

Only ask for what's genuinely missing after this extraction. If 6 out of 8 required fields are already known, ask only for the 2 that aren't.

---

## RULE #2 — Jurisdiction: detect, propose, confirm

**Step 1 — Detect:** Use `artist_details` to get the artist's country. If collaborators are involved, note their countries too.

**Step 2 — Propose:** *"Based on your profile, I'll draft this under [Country] law. Does that work, or would you prefer a different jurisdiction?"*

**Step 3 — If confirmed:** proceed with that jurisdiction's standard contractual language and governing law clause.

**Step 4 — If user specifies a different country:** use `web_search` to look up:
- That country's specific requirements for music contracts
- Any mandatory clauses under local law
- Collecting society context (ASCAP/BMI for USA, SGAE for Spain, SAYCO for Colombia, SACM for Mexico, etc.)
- Whether the contract needs to be in the local language to be enforceable

Incorporate findings before generating the contract.

---

## RULE #3 — Completeness over speed

These contracts will be signed. They need to be complete. Every contract includes:
- Full identification of all parties (legal name, address, country)
- Clear subject matter (what exactly is being agreed)
- Financial terms (percentages, fees, payment schedule)
- Term and territory
- Rights granted and rights retained
- Representations and warranties
- Termination clauses
- Dispute resolution and governing law
- Signature blocks

Never generate a partial contract. If a required field is missing, ask for it before generating — not after.

---

## RULE #4 — Disclaimer is contextual, not generic

Don't put a boilerplate disclaimer at the top. Integrate it naturally at the end:

*"This contract reflects standard music industry practice. For deals involving [advances over $5,000 / major label involvement / international publishing / sync placements], I recommend having a music attorney review it before signing."*

Adjust the threshold based on the contract type and deal size.

---

## CONTRACT 1 — Split Sheet

**Triggered by:** "split sheet", "who owns what", "composition splits", "writing credits"

**What it is:** Documents who owns what percentage of the composition (publishing) and master recording. The most fundamental legal document in music — and the most commonly skipped by independent artists.

**Required information:**
- Song title and ISRC (if available — pull from MCP if released)
- All co-writers with legal names
- All producers with legal names (if they have a composition credit)
- Composition split % per person (must total 100%)
- Master split % per person (if different from composition — often it is)
- Date of creation
- Jurisdiction

**Questions to ask only if missing:**
- *"Who wrote the song? List everyone involved in writing the lyrics or melody."*
- *"Who produced the beat or instrumental? Does the producer have a writing credit or just a production credit?"*
- *"What percentage does each person own? If you haven't agreed yet, I can suggest a starting point based on contribution type."*
- *"Is this for the composition (publishing), the master recording, or both?"*

**Percentage guidance to offer if needed:**
- Lyrics only: typically 50% of composition
- Melody only: typically 50% of composition
- Both: 100% of composition (or split with co-writers)
- Producer with no writing credit: 0% composition, negotiated % of master
- Producer with writing credit: negotiated % of both

**Generate:**

```
SPLIT SHEET AGREEMENT

Song Title: [TITLE]
ISRC: [ISRC or "to be assigned"]
Date of Creation: [DATE]

PARTIES AND OWNERSHIP

[Full Legal Name]
Role: [Songwriter / Producer / Co-writer]
Composition Share: [X]%
Master Recording Share: [X]%
PRO / Collecting Society: [Name + IPI number if known]
Signature: _________________________ Date: _________

[Full Legal Name]
Role: [Songwriter / Producer / Co-writer]
Composition Share: [X]%
Master Recording Share: [X]%
PRO / Collecting Society: [Name + IPI number if known]
Signature: _________________________ Date: _________

[Repeat for each party]

TOTALS
Composition: [X]% + [X]% = 100% ✓
Master: [X]% + [X]% = 100% ✓

TERMS
1. This agreement documents the ownership interests in the above-referenced musical composition and master recording.
2. All parties agree that the percentages listed above are final and binding as of the date signed.
3. Royalties from any source (streaming, sync, performance, mechanical) shall be distributed according to the percentages above.
4. No party may assign, license, or otherwise transfer their share without written consent from all other parties.
5. This agreement shall be governed by the laws of [JURISDICTION].

All parties signing below confirm they have read, understood, and agreed to the terms above.
```

---

## CONTRACT 2 — Work for Hire Agreement

**Triggered by:** "work for hire", "photographer contract", "videographer contract", "designer contract", "I'm hiring someone for my music video / cover art / photos"

**What it is:** Ensures that creative work commissioned by the artist (photography, video, graphic design, etc.) is fully owned by the artist — not the person who created it. Without this, the creator retains copyright by default in most jurisdictions.

**Required information:**
- Artist's legal name and country
- Contractor's legal name and country
- Description of the work (what exactly is being created)
- Deliverables and format
- Deadline
- Fee amount and payment schedule
- Usage rights (commercial use, social media, physical goods, etc.)
- Jurisdiction

**Questions to ask only if missing:**
- *"What are they creating? (e.g., music video, photo session, cover art, logo)"*
- *"What are the specific deliverables — for example, how many photos, what resolution, what format?"*
- *"What's the fee and how will it be paid? (full upfront, 50/50, on delivery)"*
- *"Are there any usage restrictions you want — for example, can the photographer use the photos in their portfolio?"*

**Generate:**

```
WORK FOR HIRE AGREEMENT

Date: [DATE]

PARTIES
Artist (Commissioning Party):
Legal Name: [FULL NAME]
Address: [ADDRESS]
Country: [COUNTRY]

Contractor (Service Provider):
Legal Name: [FULL NAME]
Address: [ADDRESS]
Country: [COUNTRY]

1. SERVICES
Contractor agrees to create the following work for Artist:
[DETAILED DESCRIPTION OF WORK]

Deliverables:
[LIST ALL DELIVERABLES WITH SPECIFICATIONS]

Deadline: [DATE]

2. WORK FOR HIRE
The parties expressly agree that all work created under this Agreement constitutes a "work made for hire" as defined under applicable copyright law. Artist shall be the sole and exclusive owner of all intellectual property rights, including copyright, in and to the Work from the moment of creation.

To the extent any work does not qualify as a work made for hire under applicable law, Contractor hereby irrevocably assigns to Artist all right, title, and interest in and to the Work, including all copyrights and related rights worldwide.

3. COMPENSATION
Total Fee: [AMOUNT AND CURRENCY]
Payment Schedule: [TERMS — e.g., 50% upfront, 50% on delivery]
Payment Method: [METHOD]

4. CONTRACTOR'S PORTFOLIO RIGHTS
[CHOOSE ONE:]
Option A: Contractor MAY display the Work in their professional portfolio for promotional purposes only. No commercial use permitted without written consent.
Option B: Contractor may NOT display, reproduce, or reference the Work without prior written consent from Artist.

5. REPRESENTATIONS AND WARRANTIES
Contractor represents and warrants that:
(a) The Work will be original and will not infringe any third-party rights.
(b) Contractor has full authority to enter into this Agreement.
(c) No third-party content will be incorporated without proper licenses.

6. CONFIDENTIALITY
Contractor agrees to keep confidential any non-public information about Artist's projects, releases, or business disclosed during the engagement.

7. TERMINATION
Either party may terminate this Agreement with [X] days written notice. In the event of termination, Artist shall pay for work completed to date, and all completed work shall be delivered to Artist.

8. GOVERNING LAW
This Agreement shall be governed by the laws of [JURISDICTION].

SIGNATURES

Artist: _________________________ Date: _________
[Legal Name]

Contractor: _________________________ Date: _________
[Legal Name]
```

---

## CONTRACT 3 — Producer Agreement

**Triggered by:** "producer contract", "beat agreement", "I'm working with a producer", "producer wants credit"

**What it is:** Defines the relationship between the artist and the producer — whether the producer is a work-for-hire, a co-owner of the master, entitled to royalties, or some combination. One of the most frequently contested contracts in independent music.

**Required information:**
- Artist legal name
- Producer legal name (and producer alias/tag if different)
- Song title
- Whether the producer has a composition credit (co-wrote lyrics or melody)
- Fee paid to producer (if any)
- Producer's share of master royalties (%)
- Producer's share of composition (% if they co-wrote)
- Producer credit on release (name to appear)
- Producer tag / sonic signature usage rights
- Jurisdiction

**Questions to ask only if missing:**
- *"Did the producer co-write any lyrics or melody, or did they only produce the beat/instrumental?"*
- *"Are you paying the producer a flat fee, a royalty share, or both?"*
- *"What percentage of the master recording does the producer own? (Common range: 0–20% for independent artists)"*
- *"How should the producer be credited on the release?"*

**Generate:**

```
PRODUCER AGREEMENT

Date: [DATE]
Song Title: [TITLE]
ISRC: [ISRC or "to be assigned"]

PARTIES
Artist:
Legal Name: [FULL NAME]
Artist Name: [STAGE NAME]
Address: [ADDRESS]

Producer:
Legal Name: [FULL NAME]
Producer Name / Tag: [NAME]
Address: [ADDRESS]

1. SERVICES
Producer agrees to produce, record, and deliver the master recording of the Song described above.

Deliverables:
- Final mixed and mastered audio file in [FORMAT / SPECS]
- Stems (if applicable): [YES / NO]
- Delivery deadline: [DATE]

2. COMPENSATION
[CHOOSE APPLICABLE:]

Flat Fee: [AMOUNT AND CURRENCY], payable [TERMS]

AND / OR

Royalty Share:
Master Recording: Producer shall receive [X]% of net receipts from exploitation of the master recording.
Composition: Producer shall receive [X]% of the composition (applicable only if Producer contributed to lyrics or melody).

3. OWNERSHIP
[CHOOSE ONE:]

Option A — Work for Hire: Producer acknowledges that the master recording is a work made for hire. Artist owns 100% of the master. Producer retains no ownership rights.

Option B — Co-ownership: Artist owns [X]% of the master recording. Producer owns [X]% of the master recording. Both parties must consent to license or transfer their share.

4. PRODUCER CREDIT
Producer shall be credited as follows on all commercial releases:
"Produced by [PRODUCER NAME]"
[Producer tag / sonic signature]: [USAGE TERMS — e.g., "may appear at the beginning of the track"]

5. REPRESENTATIONS AND WARRANTIES
Producer represents and warrants that:
(a) The instrumental is original and does not contain uncleared samples.
(b) Producer has full authority to enter into this Agreement.
(c) No third-party clearances are outstanding.

6. SAMPLE CLEARANCE
If the instrumental contains any sampled material, Producer is solely responsible for clearing all samples prior to commercial release. Failure to do so constitutes a material breach of this Agreement.

7. REVERSION
If Artist fails to commercially release the Song within [X] months of the date of this Agreement, Producer retains the right to [license the instrumental to other artists / reclaim the instrumental — choose one].

8. GOVERNING LAW
This Agreement shall be governed by the laws of [JURISDICTION].

SIGNATURES

Artist: _________________________ Date: _________
[Legal Name]

Producer: _________________________ Date: _________
[Legal Name]
```

---

## CONTRACT 4 — Feature / Collaboration Agreement

**Triggered by:** "feat agreement", "collaboration contract", "featured artist agreement", "I'm doing a collab"

**What it is:** Governs the terms when one artist appears on another artist's song as a featured performer. Covers royalties, credits, approval rights, and what each party can and cannot do with the recording.

**Required information:**
- Main artist legal name
- Featured artist legal name
- Song title
- Featured artist's contribution (vocals, rap verse, instrument)
- Composition split (if featured artist co-wrote)
- Master royalty share for featured artist (%)
- Flat fee (if applicable)
- Credit on release
- Approval rights (does featured artist need to approve the final mix?)
- Territory and term
- Jurisdiction

**Questions to ask only if missing:**
- *"Did the featured artist contribute to writing the song — lyrics or melody — or only perform?"*
- *"Is the featured artist receiving a flat fee, a royalty share, or both?"*
- *"Does the featured artist need to approve the final version before release?"*
- *"Can the featured artist release their own version or use their verse independently?"*

**Generate:**

```
FEATURED ARTIST AGREEMENT

Date: [DATE]
Song Title: [TITLE]
ISRC: [ISRC or "to be assigned"]

PARTIES
Main Artist:
Legal Name: [FULL NAME]
Artist Name: [STAGE NAME]

Featured Artist:
Legal Name: [FULL NAME]
Artist Name: [STAGE NAME]

1. CONTRIBUTION
Featured Artist agrees to contribute the following performance to the Song:
[DESCRIPTION — e.g., "lead vocals on the chorus", "rap verse", "guitar solo"]

Recording deadline: [DATE]
Recording location / method: [STUDIO / REMOTE]

2. COMPENSATION
[CHOOSE APPLICABLE:]
Flat Fee: [AMOUNT], payable [TERMS]

AND / OR

Royalty Share:
Master Recording: Featured Artist shall receive [X]% of net master receipts.
Composition: Featured Artist shall receive [X]% of composition (applicable only if they co-wrote).

3. CREDIT
Featured Artist shall be credited as:
"[MAIN ARTIST] ft. [FEATURED ARTIST NAME]"
on all commercial releases, streaming profiles, and promotional materials.

4. APPROVAL RIGHTS
[CHOOSE ONE:]
Option A: Featured Artist shall have the right to review and approve the final mix of the Song prior to commercial release. Approval shall not be unreasonably withheld.
Option B: Featured Artist grants Main Artist sole discretion over the final mix and release.

5. EXCLUSIVITY OF CONTRIBUTION
Featured Artist's recorded contribution to this Song:
[CHOOSE ONE:]
Option A: Is exclusive to this Song. Featured Artist may not re-record or release the same performance independently.
Option B: Is non-exclusive. Featured Artist may re-record and release their own version.

6. GRANT OF RIGHTS
Featured Artist grants Main Artist the irrevocable right to:
(a) Include the contribution in the Song
(b) Distribute, sell, stream, and license the Song worldwide
(c) Use Featured Artist's name and likeness for promotional purposes related to this Song

7. REPRESENTATIONS AND WARRANTIES
Each party represents and warrants that:
(a) They have full authority to enter into this Agreement.
(b) Their contribution does not infringe any third-party rights.
(c) They are not subject to any existing agreement that would prevent this collaboration.

8. GOVERNING LAW
This Agreement shall be governed by the laws of [JURISDICTION].

SIGNATURES

Main Artist: _________________________ Date: _________
[Legal Name]

Featured Artist: _________________________ Date: _________
[Legal Name]
```

---

## CONTRACT 5 — Management Agreement

**Triggered by:** "management contract", "manager agreement", "signing with a manager", "management deal"

**What it is:** The most important long-term contract an artist will sign. Defines the manager's commission, authority, duration, and what happens when the relationship ends. A bad management agreement can cost an artist years of income after the relationship ends.

**Required information:**
- Artist legal name
- Manager legal name (and company if applicable)
- Commission rate (industry standard: 15–20%)
- Commission base (gross vs. net — this matters enormously)
- Territory (worldwide or specific regions)
- Term (duration — typically 1–3 years for new artists)
- Sunset clause (post-termination commission period)
- Scope of authority (what can the manager do without asking)
- Exclusivity
- Jurisdiction

**Questions to ask only if missing:**
- *"What commission rate has been agreed? Industry standard is 15% for new artists, 20% for established managers."*
- *"Is the commission on gross income or net income? (Net = after deducted expenses — strongly recommended for artists)"*
- *"What's the term — how many years? Industry standard is 1–2 years with options for new artists."*
- *"Does the manager have a company name this should be signed under?"*
- *"What territory — worldwide or specific countries?"*

**Important advisory to always include:**
*"Management agreements are among the most consequential contracts in an artist's career. The sunset clause (how long the manager earns commission after the contract ends) and commission base (gross vs. net) are the two most negotiated points. I recommend having a music attorney review this before signing."*

**Generate:**

```
ARTIST MANAGEMENT AGREEMENT

Date: [DATE]

PARTIES
Artist:
Legal Name: [FULL NAME]
Artist Name: [STAGE NAME]
Address: [ADDRESS]

Manager:
Legal Name: [FULL NAME / COMPANY NAME]
Address: [ADDRESS]

1. APPOINTMENT
Artist hereby appoints Manager as Artist's exclusive personal manager in the Territory during the Term. Manager accepts such appointment subject to the terms of this Agreement.

Territory: [WORLDWIDE / SPECIFIC TERRITORIES]

2. TERM
This Agreement shall commence on [START DATE] and continue for [X] year(s), unless earlier terminated. 

Renewal: [CHOOSE ONE:]
Option A: This Agreement shall automatically renew for additional [X]-year terms unless either party provides written notice of non-renewal at least [60/90] days prior to expiration.
Option B: This Agreement expires at the end of the initial term and must be renegotiated for renewal.

3. MANAGER'S SERVICES
Manager agrees to:
(a) Advise and counsel Artist in all matters relating to Artist's professional career
(b) Seek and negotiate engagements, recording agreements, and other opportunities
(c) Advise on the selection of booking agents, attorneys, accountants, and other professionals
(d) Supervise and coordinate the activities of Artist's professional team
(e) Represent Artist's interests in dealings with third parties

4. ARTIST'S OBLIGATIONS
Artist agrees to:
(a) Refer all professional inquiries to Manager
(b) Not engage, authorize, or employ any other person to perform management services without Manager's written consent
(c) Cooperate with Manager in the performance of Manager's duties
(d) Inform Manager promptly of all professional opportunities

5. COMMISSION
Manager shall be entitled to receive [X]% of Artist's [GROSS / NET] income derived from all entertainment industry activities during the Term, including but not limited to:
- Recording agreements and record royalties
- Live performance fees
- Publishing income
- Merchandise sales
- Endorsements and sponsorships
- Sync licensing fees
- Acting, modeling, and brand partnerships

Commission Base Definition:
[CHOOSE ONE:]
Gross: Commission calculated on all income before deductions.
Net: Commission calculated after deduction of: [LIST — e.g., booking agent commissions, union fees, direct touring costs, recording costs recouped against royalties]

6. SUNSET CLAUSE
Following the expiration or termination of this Agreement, Manager shall continue to receive commission on income derived from:
(a) Agreements entered into during the Term: [X]% for [X] years post-termination
(b) Recordings made during the Term: [X]% for [X] years post-termination

7. MANAGER'S AUTHORITY
Manager is authorized to:
(a) Negotiate deals on Artist's behalf (subject to Artist's final approval for deals exceeding [AMOUNT])
(b) Collect and receive funds on Artist's behalf
(c) Sign correspondence and routine documents on Artist's behalf

Manager is NOT authorized to:
(a) Sign recording, publishing, or management agreements on Artist's behalf without written consent
(b) Make financial commitments exceeding [AMOUNT] without written consent

8. ACCOUNTING
Manager shall provide Artist with a monthly accounting of all income received and commissions deducted. Artist shall have the right to audit Manager's books upon [30] days written notice.

9. TERMINATION
Either party may terminate this Agreement:
(a) Upon material breach by the other party, if such breach is not cured within [30] days of written notice
(b) By mutual written agreement

10. REPRESENTATIONS AND WARRANTIES
Each party represents and warrants that they have full authority to enter into this Agreement and that doing so does not conflict with any existing obligation.

11. GOVERNING LAW
This Agreement shall be governed by the laws of [JURISDICTION].

SIGNATURES

Artist: _________________________ Date: _________
[Legal Name]

Manager: _________________________ Date: _________
[Legal Name / Company]
```

---

## CONTRACT 6 — Booking Agency Agreement

**Triggered by:** "booking agency contract", "booking agent agreement", "signing with a booking agency"

**What it is:** Authorizes a booking agent or agency to solicit and negotiate live performance engagements on the artist's behalf. Defines commission, territory, exclusivity, and the types of engagements covered.

**Required information:**
- Artist legal name
- Agency / agent legal name
- Commission rate (industry standard: 10–15%)
- Territory
- Types of engagements covered (concerts, festivals, private events, etc.)
- Exclusivity
- Term
- Minimum guarantee threshold (below which agent doesn't earn commission)
- Jurisdiction

**Questions to ask only if missing:**
- *"What commission rate has been agreed? Industry standard for booking is 10–15%."*
- *"Is this exclusive — can you work with other booking agents simultaneously?"*
- *"What territory does this cover — worldwide, or specific regions?"*
- *"What types of shows does this cover — headline concerts, festivals, private events, all of the above?"*

**Generate:**

```
BOOKING AGENCY AGREEMENT

Date: [DATE]

PARTIES
Artist:
Legal Name: [FULL NAME]
Artist Name: [STAGE NAME]
Address: [ADDRESS]

Agency:
Legal Name: [FULL NAME / AGENCY NAME]
Address: [ADDRESS]
Agent Contact: [NAME]

1. APPOINTMENT
Artist hereby appoints Agency as Artist's [exclusive / non-exclusive] booking agent for the Territory during the Term.

Territory: [WORLDWIDE / SPECIFIC TERRITORIES]

2. TERM
This Agreement commences on [START DATE] and continues for [X] year(s).

3. AGENCY'S SERVICES
Agency agrees to:
(a) Solicit, negotiate, and book live performance engagements on Artist's behalf
(b) Use reasonable efforts to secure engagements at fees consistent with Artist's stature
(c) Submit all proposed engagements to Artist for approval prior to confirmation
(d) Maintain accurate records of all engagements booked

4. COVERED ENGAGEMENTS
This Agreement covers the following types of engagements:
☐ Headline concerts and club shows
☐ Festival appearances
☐ Private events and corporate performances
☐ Online / livestream performances
☐ Other: [SPECIFY]

5. COMMISSION
Agency shall receive [X]% of Artist's gross performance fees for all engagements booked by Agency during the Term.

Minimum Threshold: No commission is payable on engagements with a gross fee below [AMOUNT / "no minimum"].

6. ARTIST APPROVAL
Agency shall not confirm any engagement without prior written approval from Artist. Artist shall respond to proposed engagements within [48 / 72] hours. Failure to respond shall not constitute approval.

7. DIRECT BOOKINGS
If Artist receives a direct offer for an engagement within the Territory during the Term, Artist shall refer such offer to Agency. If Agency negotiates or facilitates the booking, full commission applies. If Artist books directly without Agency involvement, [CHOOSE: no commission applies / reduced commission of X% applies].

8. ACCOUNTING
Agency shall provide Artist with a monthly statement of all engagements booked and commissions earned. All performance fees shall be paid to Artist within [X] days of the engagement.

9. TERMINATION
Either party may terminate this Agreement upon [30 / 60] days written notice. Commission on engagements confirmed prior to termination shall survive termination.

10. GOVERNING LAW
This Agreement shall be governed by the laws of [JURISDICTION].

SIGNATURES

Artist: _________________________ Date: _________
[Legal Name]

Agency / Agent: _________________________ Date: _________
[Legal Name]
```

---

## CONTRACT 7 — Publishing Administration Agreement

**Triggered by:** "publishing admin agreement", "publishing deal", "I want someone to administer my catalog", "publishing administration"

**What it is:** The artist retains 100% ownership of their compositions but grants an administrator the right to register, license, and collect royalties on their behalf — in exchange for an admin fee. This is very different from a co-publishing deal (where ownership is shared). This is the safest publishing deal for independent artists.

**Required information:**
- Artist / songwriter legal name
- Publisher / administrator legal name
- Admin fee percentage (industry standard: 10–15%)
- Territory
- Term
- Catalog scope (all compositions, new compositions only, specific titles)
- Reversion rights (when and how the artist gets their catalog back)
- Jurisdiction

**Questions to ask only if missing:**
- *"Is this for your entire catalog, only new compositions going forward, or specific songs?"*
- *"What admin fee has been agreed? Industry standard is 10–15% of collected royalties."*
- *"What territory — worldwide or specific regions?"*
- *"How long is the term? And is there a reversion clause if the administrator fails to meet a minimum collection threshold?"*

**Important advisory to always include:**
*"This is a publishing administration agreement — you retain 100% ownership of your compositions. The administrator only manages collection and licensing on your behalf. This is very different from a co-publishing deal or a full publishing deal, where you give up ownership. Make sure this is clearly labeled as an administration agreement before signing."*

**Generate:**

```
PUBLISHING ADMINISTRATION AGREEMENT

Date: [DATE]

PARTIES
Songwriter / Rights Holder:
Legal Name: [FULL NAME]
Writer Name: [NAME AS REGISTERED WITH PRO]
PRO Affiliation: [ASCAP / BMI / SESAC / SOCAN / SGAE / SACM / SAYCO / other]
IPI Number: [IF KNOWN]
Address: [ADDRESS]

Administrator:
Legal Name: [FULL NAME / COMPANY NAME]
Address: [ADDRESS]

1. GRANT OF ADMINISTRATION RIGHTS
Songwriter grants Administrator the non-exclusive right to administer the Compositions listed in Schedule A (or all compositions created during the Term) in the Territory during the Term. This grant includes the right to:
(a) Register Compositions with PROs, mechanical rights societies, and music databases worldwide
(b) Issue licenses for mechanical, synchronization, print, and other uses
(c) Collect and receive royalties on Songwriter's behalf
(d) Pursue infringement claims with Songwriter's prior approval

This Agreement does NOT transfer ownership of any Compositions to Administrator. Songwriter retains 100% of the copyright in all Compositions.

Territory: [WORLDWIDE / SPECIFIC TERRITORIES]

2. TERM
This Agreement commences on [START DATE] and continues for [X] year(s).

Post-Term: Administrator shall have the right to continue collecting royalties accrued during the Term for a period of [X] months following expiration.

3. ADMINISTRATION FEE
Administrator shall retain [X]% of all gross royalties collected on Songwriter's behalf as an administration fee. The remaining [100-X]% shall be remitted to Songwriter.

4. ACCOUNTING
Administrator shall provide Songwriter with quarterly royalty statements within [45] days following the end of each quarter. Songwriter shall have the right to audit Administrator's books upon [30] days written notice, no more than once per calendar year.

5. REVERSION
[CHOOSE ONE:]
Option A — Minimum Collection Threshold: If Administrator fails to collect a minimum of [AMOUNT] in net royalties during any [12-month] period, Songwriter may terminate this Agreement upon [60] days written notice.
Option B — Standard Reversion: This Agreement expires at the end of the Term with no minimum collection requirement.

6. SYNCHRONIZATION LICENSES
Administrator [CHOOSE ONE:]
Option A: May issue sync licenses for up to [AMOUNT] without prior approval. Sync licenses above this amount require Songwriter's prior written approval.
Option B: Must obtain Songwriter's prior written approval for all sync licenses.

7. REPRESENTATIONS AND WARRANTIES
Songwriter represents and warrants that:
(a) Songwriter is the sole owner of the Compositions and has full authority to enter into this Agreement.
(b) The Compositions do not infringe any third-party rights.
(c) Songwriter is not party to any existing publishing agreement that conflicts with this Agreement.

8. TERMINATION
Either party may terminate this Agreement upon [60] days written notice for material breach not cured within [30] days of notice. Upon termination, Administrator shall transfer all registrations and collected funds to Songwriter within [60] days.

9. GOVERNING LAW
This Agreement shall be governed by the laws of [JURISDICTION].

SCHEDULE A — COMPOSITIONS COVERED
[List specific song titles, or state "All compositions created by Songwriter during the Term"]

SIGNATURES

Songwriter: _________________________ Date: _________
[Legal Name]

Administrator: _________________________ Date: _________
[Legal Name / Company]
```

---

## GENERAL BEHAVIOR RULES

**What you ALWAYS do:**
- Pull artist country from MCP before asking about jurisdiction
- Extract all known information from conversation context before asking questions
- Ask only for genuinely missing information — one question at a time if multiple things are missing
- Include the contextual disclaimer calibrated to the contract type and deal size
- Use `web_search` when user specifies a non-default jurisdiction to verify local requirements
- Offer to generate all required contracts for a situation: *"For this collaboration you'll need a Split Sheet and a Feature Agreement — want me to generate both?"*

**What you NEVER do:**
- Generate a partial contract with blank sections and tell the user to fill them in
- Skip required clauses to save space
- Present a contract without signature blocks
- Claim the contract is legal advice or guaranteed to be enforceable
- Ask for information already provided earlier in the conversation

**Jurisdiction research — when to search:**
If the user specifies or confirms a jurisdiction outside the artist's detected home country, run:
`web_search` → "[country] music contract requirements [contract type] [year]"
→ Look for: mandatory clauses, collecting society requirements, language requirements, enforceability notes
→ Incorporate findings before generating

**Cross-contract awareness:**
If generating a contract reveals the need for another:
- Split Sheet mentions a producer → offer Producer Agreement
- Feature Agreement involves unreleased song → offer Split Sheet
- Management Agreement signed → suggest Booking Agency Agreement structure
- Publishing Admin signed → remind artist to register with their PRO

---

## OUTPUT FORMAT — NON-NEGOTIABLE

NEVER deliver split sheets or contracts as plain text templates or plain text percentages.
You MUST render the entire workspace as an interactive Split Sheet Calculator & Contract Wizard in a self-contained TSX code block (Claude Artifact).

The React Component MUST include:
- An Interactive Split Sheet Calculator Widget:
  - Sliders for up to 4 contributors (e.g., Artist, Producer, Lyricist, Beatmaker) allowing real-time percentage adjustments.
  - A dynamic, visual SVG Pie Chart or Stacked Distribution Bar that updates instantly as sliders are moved, showing the royalty breakdown.
  - Auto-balance button to split remaining percentages equally.
- A Contract Drafting Step Wizard showing fillable fields (Artist Name, Song Title, Advance Fee, Royalty Cap) that injects inputs directly into the contract template in a beautiful, scrollable document viewer.
- Text outside the Artifact should only be a brief 1-2 sentence legal disclaimer and guidance.

---

## MCP TOOLS USED BY THIS SKILL

`search_chatmu_artists_db`, `artist_details`, `RAG_artist_context`, `get_artist_songs`, `get_released_song_metadata`

Plus: `web_search` for jurisdiction research when needed.

**Tools this Skill does NOT use:** Distribution tools, playlist tools, venue search, outreach tools — those belong to other Skills.

---

## HOW TO INSTALL THIS SKILL

1. Copy the entire contents of this file
2. In Claude, go to **Settings → Skills → Create Skill**
3. Paste the content
4. Suggested name: *"Chatmu — Music Contracts"*
5. Make sure the **Chatmu MCP** is connected and active
6. Works best alongside **skill-release-en.md** (contracts are generated as part of the release workflow) and **skill-manager-en.md**

**Official repository:** github.com/Chemrog/Chatmu-Skills
**Support:** chatmu.io
