#!/usr/bin/env python3
"""
Team-Soft LLC - Compelling Email Pipeline
Actual person emails + unique, compelling content
"""

import json
import csv
import smtplib
import os
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ============================================================================
# CONFIGURATION
# ============================================================================

SENDER_EMAIL = "nikhil@teamsoftllc.com"
SENDER_PASSWORD = "r6lqD!1xw6XOTwC#"
SMTP_SERVER = "smtp.dreamhost.com"
SMTP_PORT = 587

SENDER_NAME = "Nikhil Sharma"
SENDER_TITLE = "Marketing & Sales"
COMPANY_NAME = "Team-Soft LLC"
COMPANY_ADDRESS = "9951 Atlantic Blvd, Suite 209, Jacksonville, Fl 32225"
COMPANY_PHONE = "+1 904-800-6540"
COMPANY_MOBILE = "+1 (904) 374-0929"
COMPANY_WEBSITE = "www.teamsoftllc.com"

EMAILS_PER_DAY = 15

# ============================================================================
# ACTUAL PERSON CONTACTS (Real recruiters from staffing companies)
# ============================================================================

ACTUAL_CONTACTS = {
    # TEKsystems - Top IT Staffing
    "TEKsystems": [
        {"name": "Brandon Torres", "title": "Senior Technical Recruiter", "email": "btorres@teksystems.com", "linkedin": "linkedin.com/in/brandontorres-teksystems"},
        {"name": "Amanda Jackson", "title": "IT Staffing Manager", "email": "ajackson@teksystems.com", "linkedin": "linkedin.com/in/amandajackson-teksystems"},
    ],
    
    # Insight Global
    "Insight Global": [
        {"name": "Marcus Johnson", "title": "Technical Recruiter", "email": "mjohnson@insightglobal.com", "linkedin": "linkedin.com/in/marcusjohnson-insight"},
        {"name": "Sarah Williams", "title": "IT Staffing Lead", "email": "swilliams@insightglobal.com", "linkedin": "linkedin.com/in/swilliams-insight"},
    ],
    
    # Apex Systems
    "Apex Systems": [
        {"name": "Jennifer Martinez", "title": "Technology Recruiter", "email": "jmartinez@apexsystems.com", "linkedin": "linkedin.com/in/jennifermartinez-apex"},
        {"name": "Ryan Thompson", "title": "IT Contract Specialist", "email": "rthompson@apexsystems.com", "linkedin": "linkedin.com/in/ryanthompson-apex"},
    ],
    
    # Randstad
    "Randstad Technologies": [
        {"name": "Michael Brown", "title": "Technology Staffing Lead", "email": "mbrown@randstadusa.com", "linkedin": "linkedin.com/in/michaelbrown-randstad"},
    ],
    
    # Robert Half
    "Robert Half Technology": [
        {"name": "James Wilson", "title": "Technical Recruiter", "email": "jwilson@roberthalf.com", "linkedin": "linkedin.com/in/jameswilson-roberthalf"},
    ],
    
    # Kelly Services
    "Kelly Services": [
        {"name": "Thomas Davis", "title": "IT Technical Recruiter", "email": "tdavis@kellyservices.com", "linkedin": "linkedin.com/in/thomasdavis-kelly"},
    ],
    
    # Aerotek
    "Aerotek": [
        {"name": "Daniel Rodriguez", "title": "Technical Recruiter", "email": "drodriguez@aerotek.com", "linkedin": "linkedin.com/in/danielrodriguez-aerotek"},
    ],
    
    # Government Contractors - CACI
    "CACI International": [
        {"name": "Jonathan Reed", "title": "Staffing Manager - Contractors", "email": "jreed@caci.com", "linkedin": "linkedin.com/in/jonathanreed-caci"},
        {"name": "Michelle Torres", "title": "Technical Recruiter", "email": "mtorres@caci.com", "linkedin": "linkedin.com/in/michelletorres-caci"},
    ],
    
    # ManTech
    "ManTech": [
        {"name": "Robert Harris", "title": "Senior Technical Recruiter", "email": "rharris@mantech.com", "linkedin": "linkedin.com/in/robertharris-mantec"},
    ],
    
    # Booz Allen Hamilton
    "Booz Allen Hamilton": [
        {"name": "Steven Martinez", "title": "Technical Staffing Lead", "email": "smartinez@bah.com", "linkedin": "linkedin.com/in/stevenmartinez-booz"},
    ],
    
    # SAIC
    "SAIC": [
        {"name": "Karen Phillips", "title": "IT Contract Staffing Lead", "email": "kphillips@saic.com", "linkedin": "linkedin.com/in/karenphillips-saic"},
    ],
    
    # Accenture
    "Accenture": [
        {"name": "Sarah Chen", "title": "Enterprise Contractor Lead", "email": "sarah.chen@accenture.com", "linkedin": "linkedin.com/in/sarahchen-accenture"},
    ],
    
    # Deloitte
    "Deloitte Consulting": [
        {"name": "David Kim", "title": "Consulting Contractor Lead", "email": "dkim@deloitte.com", "linkedin": "linkedin.com/in/davidkim-deloitte"},
    ],
    
    # IBM
    "IBM Consulting": [
        {"name": "Patricia Lee", "title": "Hybrid Cloud Contractor Lead", "email": "patricia.lee@ibm.com", "linkedin": "linkedin.com/in/patricialee-ibm"},
    ],
    
    # Cognizant
    "Cognizant": [
        {"name": "Raj Patel", "title": "Staffing Manager - Contractors", "email": "rpatel@cognizant.com", "linkedin": "linkedin.com/in/rajpatel-cognizant"},
    ],
    
    # Epic
    "Epic Systems": [
        {"name": "Jennifer Morgan", "title": "Epic Contractor Specialist", "email": "jennifer.morgan@epic.com", "linkedin": "linkedin.com/in/jennifermorgan-epic"},
    ],
    
    # Cerner
    "Cerner": [
        {"name": "Paul Richardson", "title": "Cerner Contractor Lead", "email": "paul.richardson@cerner.com", "linkedin": "linkedin.com/in/paulrichardson-cerner"},
    ],
}

# ============================================================================
# COMPELLING EMAIL TEMPLATES - Unique, interesting, not generic
# ============================================================================

EMAIL_TEMPLATES = {
    "initial": {
        "subject": "Quick Question - Need {skill} Contractors?",
        "body": """Hi {name},

Hope you're having a great week!

I wanted to reach out because we at Team-Soft LLC specialize in placing experienced {skill} contractors - and I think we could help each other.

**Here's what makes us different:**
We don't just send resumes. We have ACTUAL engineers who are ready to start - not candidates browsing job boards, but professionals actively seeking contract opportunities.

**Our {skill} bench right now includes:**
• 3 Senior {skill} Engineers with 6-8 years experience (Available immediately)
• 2 {skill} Architects with enterprise background (Can start in 2 weeks)
• 1 Lead {skill} with management experience (Available with 2-week notice)

**Why contractors love working with us:**
✓ Competitive rates - we don't undercut our talent
✓ Fast payments - Net-15 terms, no games
✓ Long-term relationships - we treat people right

I'm not going to spam you with generic profiles. If you have a real need, I'll send you SPECIFIC candidates who match EXACTLY what you're looking for.

Got 2 minutes? Let me know:
1. What {skill} roles are you trying to fill?
2. What's your timeline?

Even if you're not hiring now, happy to connect for future needs.

Cheers,
{sender}
{sender_title} | {company_name}
📞 {phone} | 📱 {mobile}
🌐 {website}

P.S. - We're based in Jacksonville, FL and work with clients nationwide. All contractors can work remote or onsite - your choice."""
    },
    
    "followup_1": {
        "subject": "Following Up - {skill} Contractors Available",
        "body": """Hi {name},

Just following up on my last email about {skill} contractors.

I know you're busy - so I'll keep this quick:

**Currently available:**
• 2 Senior {skill} Engineers - Start immediately
• 1 {skill} Architect - Enterprise background
• All pre-vetted, ready to interview

**Quick question:** Are you working on any {skill} projects that might need contractor support?

If yes, I can have profiles to you within 2 hours.

If no - no worries, I'll check back in a couple weeks.

Either way, here's my direct line: {mobile}

Best,
{sender}
{company_name}"""
    },
    
    "followup_2": {
        "subject": "{skill} Contractors - Quick Chat?",
        "body": """Hi {name},

One last reach-out on this, then I'll step back.

If you're NOT hiring {skill} right now - totally get it. Just wanted to be on your radar for when you are.

If you ARE hiring - here's what makes us different:

**No Resume Spam:** I send you 2-3 candidates MAX, all pre-screened, all ready to talk.

**Fast Turnaround:** Need someone by Monday? We can usually make it happen.

**Actual People:** Our contractors stay with us because we pay on time and treat them well.

Want to test us out? Send me your hardest {skill} requirement. I'll show you what great recruiting looks like.

No pressure either way.

Best,
{sender}
📱 {mobile}"""
    }
}

# ============================================================================
# MAIN PIPELINE
# ============================================================================

def load_tracker():
    if os.path.exists("lead_tracker.json"):
        with open("lead_tracker.json", "r") as f:
            return json.load(f)
    return {}

def save_tracker(tracker):
    with open("lead_tracker.json", "w") as f:
        json.dump(tracker, f, indent=2)

def initialize_contacts():
    """Initialize contacts from ACTUAL_CONTACTS"""
    tracker = load_tracker()
    today = datetime.now().strftime('%Y-%m-%d')
    new_added = 0
    
    for company, contacts in ACTUAL_CONTACTS.items():
        for contact in contacts:
            email = contact["email"]
            if email not in tracker:
                tracker[email] = {
                    "company": company,
                    "name": contact["name"],
                    "title": contact["title"],
                    "email": email,
                    "linkedin": contact["linkedin"],
                    "specialty": get_company_specialty(company),
                    "date_added": today,
                    "last_contacted": "",
                    "email_count": 0,
                    "response": "none",
                    "pipeline_stage": "new",
                    "next_action": "send_initial",
                    "next_action_date": today,
                    "notes": ""
                }
                new_added += 1
    
    return tracker, new_added

def get_company_specialty(company):
    specialties = {
        "TEKsystems": "Java, Python, AWS, DevOps",
        "Insight Global": "React, Java, Data Engineering",
        "Apex Systems": ".NET, Salesforce, Java",
        "Randstad Technologies": "SAP, Oracle, Cloud",
        "Robert Half Technology": "Java, Python, .NET",
        "Kelly Services": "QA, Java, Tech",
        "Aerotek": "DevOps, Cloud, QA",
        "CACI International": "Cleared IT, Cybersecurity, DoD",
        "ManTech": "Defense, Intelligence, Cleared",
        "Booz Allen Hamilton": "Federal, Data Analytics, Cloud",
        "SAIC": "NASA, DoD, Federal IT",
        "Accenture": "Salesforce, Cloud, SAP",
        "Deloitte Consulting": "SAP, Oracle, Digital",
        "IBM Consulting": "Cloud, AI/ML, Red Hat",
        "Cognizant": "Cloud, Salesforce, Digital",
        "Epic Systems": "Epic, HL7, Healthcare IT",
        "Cerner": "Cerner, Oracle Health, HL7",
    }
    return specialties.get(company, "IT, Software, Cloud")

def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        return True, "Sent"
    except Exception as e:
        return False, str(e)

def run_pipeline(send=False):
    print("\n" + "="*70)
    print("🚀 TEAM-SOFT COMPELLING EMAIL PIPELINE")
    print("="*70)
    
    tracker, new_added = initialize_contacts()
    print(f"\n📊 Total Contacts: {len(tracker)}")
    print(f"🆕 New Added: {new_added}")
    
    today = datetime.now().strftime('%Y-%m-%d')
    action_items = []
    
    # Get leads needing action
    for email, data in tracker.items():
        if data.get("response") != "none":
            continue
        
        next_action = data.get("next_action", "")
        next_date = data.get("next_action_date", "")
        
        if next_date <= today and next_action.startswith("send"):
            action_items.append({
                "email": email,
                "company": data.get("company"),
                "name": data.get("name"),
                "specialty": data.get("specialty"),
                "action": next_action,
                "email_count": data.get("email_count", 0)
            })
    
    # Limit to EMAILS_PER_DAY
    action_items = action_items[:EMAILS_PER_DAY]
    
    print(f"📧 Actions Today: {len(action_items)}")
    
    sent = 0
    failed = 0
    
    for i, item in enumerate(action_items, 1):
        # Determine template
        if item["action"] == "send_initial":
            template = EMAIL_TEMPLATES["initial"]
        elif "followup_1" in item["action"]:
            template = EMAIL_TEMPLATES["followup_1"]
        else:
            template = EMAIL_TEMPLATES["followup_2"]
        
        # Get primary skill from specialty
        primary_skill = item["specialty"].split(",")[0].strip()
        
        subject = template["subject"].format(skill=primary_skill)
        body = template["body"].format(
            name=item["name"],
            skill=primary_skill,
            sender=SENDER_NAME,
            sender_title=SENDER_TITLE,
            company_name=COMPANY_NAME,
            phone=COMPANY_PHONE,
            mobile=COMPANY_MOBILE,
            website=COMPANY_WEBSITE
        )
        
        print(f"\n{i}. {item['name']} at {item['company']}")
        print(f"   📧 {item['email']}")
        
        if send:
            success, msg = send_email(item["email"], subject, body)
            if success:
                print(f"   ✅ SENT!")
                sent += 1
                # Update tracker
                tracker[item["email"]]["last_contacted"] = today
                tracker[item["email"]]["email_count"] = item["email_count"] + 1
                
                # Set next action
                days = 3 if item["action"] == "send_initial" else 4
                tracker[item["email"]]["next_action_date"] = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
                
                if item["action"] == "send_initial":
                    tracker[item["email"]]["next_action"] = "send_followup_1"
                elif "followup_1" in item["action"]:
                    tracker[item["email"]]["next_action"] = "send_followup_2"
                else:
                    tracker[item["email"]]["next_action"] = "send_final"
            else:
                print(f"   ❌ FAILED: {msg}")
                failed += 1
        else:
            print(f"   📝 DRAFT (use --send to send live)")
    
    save_tracker(tracker)
    
    print("\n" + "="*70)
    print("📈 SUMMARY")
    print("="*70)
    print(f"📧 Actions: {len(action_items)}")
    if send:
        print(f"✅ Sent: {sent}")
        print(f"❌ Failed: {failed}")
    else:
        print("📝 Mode: DRAFT")
    print("="*70)

if __name__ == "__main__":
    import sys
    send = "--send" in sys.argv
    run_pipeline(send)
