# Team-Soft LLC Complete Lead Generation Strategy

## 🎯 OBJECTIVE
Build automated pipeline that generates leads, sends emails, follows up, and tracks the entire company lifecycle.

---

## 📊 STRATEGY OVERVIEW

### 1. LEAD GENERATION (Daily)
- Generate 15-20 fresh staffing company contacts daily
- Focus on: IT Staffing Agencies, Government Contractors, Commercial Enterprises
- Include: Name, email, phone, specialty, rates

### 2. EMAIL OUTREACH (Day 0)
**Initial Contact Email**
- Send personalized email to new leads
- Include: Available skills, rates, engagement models (C2C, 1099, C2H)
- Call to action: Ask about current hiring needs

### 3. FOLLOW-UP SEQUENCE (Automated)
| Day | Action | Condition |
|-----|--------|-----------|
| Day 0 | Initial Email | New lead |
| Day 3 | Follow-up #1 | No response from Day 0 |
| Day 7 | Follow-up #2 | No response from Day 3 |
| Day 14 | Final Follow-up | No response from Day 7 |
| Day 30 | Re-engagement | If no response, mark as cold |

### 4. RESPONSE HANDLING
| Response Type | Action |
|--------------|--------|
| Interested | Schedule call, send candidate profiles |
| Not Now | Add to nurturing list |
| Not Hiring | Remove from active list |
| Out of Office | Re-contact in 2 weeks |

### 5. PIPELINE METRICS
- Leads generated per day: 15-20
- Emails sent per day: 10-15
- Target response rate: 15-25%
- Follow-up compliance: 100% automated

---

## 🔄 COMPLETE COMPANY LIFECYCLE

```
┌─────────────┐
│   NEW LEAD  │
│  (Day 0)   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ SEND EMAIL  │──────► Response? ────► Interested ✓
│  (Day 0)   │                     │
└──────┬──────┘                     ▼
       │ No Response          ┌─────────────┐
       ▼                      │  SCHEDULE  │
┌─────────────┐               │    CALL    │
│ FOLLOW-UP 1│               └─────────────┘
│  (Day 3)   │
└──────┬──────┘
       │
       ▼ No Response
┌─────────────┐
│ FOLLOW-UP 2│
│  (Day 7)   │
└──────┬──────┘
       │
       ▼ No Response
┌─────────────┐
│ FINAL EMAIL │
│  (Day 14)  │
└──────┬──────┘
       │
       ▼ No Response
┌─────────────┐
│   COLD/    │
│  ARCHIVE   │
│  (Day 30)  │
└─────────────┘
```

---

## 📧 EMAIL TEMPLATES

### Initial Contact (Day 0)
**Subject:** IT Contractors Available - [Company Name]

**Body:**
Hi [Name],

I'm reaching out from Team-Soft LLC about IT contractors for your current projects.

We have pre-screened [Skills] engineers available for:
- Corp-to-Corp (C2C)
- 1099 Independent Contractor
- Contract-to-Hire (C2H)

Our candidates are ready to start within 1-2 weeks. Rates: $60-150/hour depending on experience.

Do you have any current IT hiring needs? Happy to share candidate profiles.

Best,
Nikhil
Team-Soft LLC
nikhil@teamsoftllc.com

### Follow-up #1 (Day 3)
**Subject:** Following Up - IT Contractors

**Body:**
Hi [Name],

Just following up on my previous email. Have any current IT needs?

We have [Skills] candidates available and can present profiles within 24 hours.

Let me know!

Best,
Nikhil

### Follow-up #2 (Day 7)
**Subject:** Quick Question - IT Staffing

**Body:**
Hi [Name],

One last touch - if you're not hiring now, I'll circle back in a few weeks.

But if you do have needs, I can help quickly.

Thanks,
Nikhil

### Final (Day 14)
**Subject:** Let's Connect Soon - IT Contractors

**Body:**
Hi [Name],

I'll archive your info for now. Feel free to reach out when you have IT staffing needs.

In the meantime, here's what we offer:
- Pre-vetted candidates in 24-48 hours
- C2C, 1099, C2H arrangements
- Skills: Java, Python, AWS, DevOps, Salesforce, SAP, QA, Data

Best,
Nikhil

---

## 📊 TRACKING FIELDS

| Field | Description |
|-------|-------------|
| company | Staffing company name |
| contact_name | Recruiter name |
| email | Contact email |
| phone | Phone number |
| specialty | Skills they hire for |
| date_added | Lead creation date |
| last_contacted | Last email sent date |
| email_count | Number of emails sent |
| response_status | None/Interested/Not Now/Not Hiring |
| next_action | What to do next |
| next_action_date | When to do it |
| notes | Any important notes |
| pipeline_stage | New/Contacted/Follow-up/Interested/Cold |

---

## ⚡ AUTOMATION RULES

1. **Run Daily at 12pm EST:**
   - Check lead_tracker.json
   - Identify leads needing follow-up
   - Generate daily_actions.csv

2. **Auto-Categorize:**
   - If response received → Move to "Interested"
   - If 3 emails sent, no response → Move to "Cold"
   - If interested → Add to "Schedule Call" list

3. **Weekly Review:**
   - Check "Interested" leads
   - Update candidate submissions
   - Schedule follow-ups

---

## 🎯 SUCCESS METRICS

- Daily Leads: 15-20 new contacts
- Daily Emails: 10-15 sent
- Response Rate Target: 15-25%
- Follow-up Compliance: 100%
- Placement Rate: 3-5% of conversations
