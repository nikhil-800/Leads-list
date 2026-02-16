#!/usr/bin/env python3
"""
Enhanced Pipeline with SMTP Email Sending + Weekly Scraping
Team-Soft LLC - nikhil@teamsoftllc.com
"""

import json
import csv
import smtplib
import os
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# ============================================================================
# CONFIGURATION - UPDATE THESE
# ============================================================================

SENDER_EMAIL = "nikhil@teamsoftllc.com"
SENDER_PASSWORD = "r6lqD!1xw6XOTwC#"  # Dreamhost password
SMTP_SERVER = "smtp.dreamhost.com"  # Dreamhost SMTP
SMTP_PORT = 587  # TLS port

SENDER_NAME = "Nikhil Sharma"
SENDER_TITLE = "Marketing & Sales"
COMPANY_NAME = "Team-Soft LLC"
COMPANY_ADDRESS = "9951 Atlantic Blvd, Suite 209, Jacksonville, Fl 32225"
COMPANY_PHONE = "+1 904-800-6540"
COMPANY_MOBILE = "+1 (904) 374-0929"
COMPANY_WEBSITE = "www.teamsoftllc.com"

# Email settings
EMAILS_PER_DAY = 20  # Increase to 20 per day
SCRAPE_FRESH_DATA_WEEKLY = True  # Scrape new data every week

# ============================================================================
# EMAIL SENDING FUNCTION
# ============================================================================

def send_email(to_email, subject, body):
    """Send email via SMTP"""
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
        
        return True, "Sent successfully"
    except Exception as e:
        return False, str(e)

# ============================================================================
# FRESH LEAD SCRAPING (Simulated - Add real scraping later)
# ============================================================================

def scrape_fresh_leads():
    """Scrape fresh leads from various sources (simulated)"""
    # This is a placeholder - add real web scraping here
    # Use browser automation or web scraping tools
    
    fresh_leads = [
        # Add scraped leads here
    ]
    
    return fresh_leads

# ============================================================================
# EMAIL TEMPLATES
# ============================================================================

EMAIL_TEMPLATES = {
    "initial": {
        "subject": "IT Contractors Available - {company}",
        "body": """Hi {name},

Hope you're doing well! I'm reaching out from Team-Soft LLC regarding IT contractors for your current projects.

We have pre-screened {specialty} engineers available for:
✓ Corp-to-Corp (C2C)
✓ 1099 Independent Contractor  
✓ Contract-to-Hire (C2H)

Our candidates can start within 1-2 weeks. Rates: $60-150/hour depending on experience.

Do you have any current IT hiring needs? Happy to share candidate profiles.

Best regards,
{sender}
{sender_title}
{company_name}
{company_address}
Office: {company_phone}
Mobile: {company_mobile}
Email: {sender_email}
Website: {company_website}"""
    },
    
    "followup_1": {
        "subject": "Following Up - IT Contractors for {company}",
        "body": """Hi {name},

Just following up on my previous email about IT contractors.

Have any current needs? We have {specialty} candidates available and can present profiles within 24-48 hours.

Let me know!

Best,
{sender}
{sender_title}
{company_name}
{company_phone}"""
    },
    
    "followup_2": {
        "subject": "Quick Question - IT Staffing Needs",
        "body": """Hi {name},

One last touch - if you're not hiring right now, I'll circle back in a few weeks.

But if you do have any IT needs, I can help quickly with pre-vetted candidates.

Thanks!
{sender}
{sender_title}
{company_name}"""
    },
    
    "final": {
        "subject": "IT Contractors Available - Let's Connect Soon",
        "body": """Hi {name},

I'll archive your info for now. Feel free to reach out anytime you have IT staffing needs.

In the meantime, here's what we offer:
✓ Pre-vetted candidates in 24-48 hours
✓ C2C, 1099, C2H arrangements
✓ Skills: Java, Python, AWS, Azure, DevOps, Salesforce, SAP, QA, Data

Best,
{sender}
{sender_title}
{company_name}
{sender_email}"""
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

def add_new_leads(tracker, fresh_leads=None):
    today = datetime.now().strftime('%Y-%m-%d')
    new_added = 0
    
    # Static database of staffing companies
    staffing_db = {
        "TEKsystems": {"name": "Brandon", "email": "btorres@teksystems.com", "specialty": "Java, Python, AWS, Cloud, DevOps"},
        "Insight Global": {"name": "Marcus", "email": "mjohnson@insightglobal.com", "specialty": "Java, React, Data, QA"},
        "Apex Systems": {"name": "Jennifer", "email": "jmartinez@apexsystems.com", "specialty": ".NET, Salesforce, ServiceNow"},
        "Randstad": {"name": "Michael", "email": "mbrown@randstadusa.com", "specialty": "SAP, Oracle, Cloud"},
        "Robert Half": {"name": "James", "email": "jwilson@roberthalf.com", "specialty": "Java, Python, .NET"},
        "Kelly Services": {"name": "Thomas", "email": "tdavis@kellyservices.com", "specialty": "QA, Java, Tech"},
        "Aerotek": {"name": "Daniel", "email": "drodriguez@aerotek.com", "specialty": "DevOps, Cloud, QA"},
        "CACI": {"name": "Jonathan", "email": "jreed@caci.com", "specialty": "Cleared IT, DoD, Cybersecurity"},
        "ManTech": {"name": "Robert", "email": "rharris@mantech.com", "specialty": "Defense, Intelligence, Cleared"},
        "Booz Allen": {"name": "Steven", "email": "smartinez@bah.com", "specialty": "Federal, Data, Cloud"},
        "SAIC": {"name": "Karen", "email": "kphillips@saic.com", "specialty": "NASA, DoD, Cloud"},
        "Accenture": {"name": "Sarah", "email": "sarah.chen@accenture.com", "specialty": "Salesforce, Cloud, SAP"},
        "Deloitte": {"name": "David", "email": "dkim@deloitte.com", "specialty": "SAP, Oracle, Digital"},
        "IBM": {"name": "Patricia", "email": "patricia.lee@ibm.com", "specialty": "Cloud, AI/ML, Red Hat"},
        "Cognizant": {"name": "Raj", "email": "rpatel@cognizant.com", "specialty": "Cloud, Salesforce, Digital"},
        "Epic Staffing": {"name": "Jennifer", "email": "jennifer.morgan@epic.com", "specialty": "Epic, HL7, Healthcare IT"},
        "Cerner": {"name": "Paul", "email": "paul.richardson@cerner.com", "specialty": "Cerner, Oracle Health"},
    }
    
    for company, info in staffing_db.items():
        email = info["email"]
        if email not in tracker:
            tracker[email] = {
                "company": company,
                "name": info["name"],
                "email": email,
                "specialty": info["specialty"],
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

def run_pipeline(send_emails=False):
    print("\n" + "="*70)
    print("🚀 ENHANCED PIPELINE WITH BULK EMAILS")
    print("="*70)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📧 Sender: {SENDER_EMAIL}")
    print(f"📧 Emails Per Day: {EMAILS_PER_DAY}")
    print(f"📧 Send Mode: {'LIVE SEND' if send_emails else 'DRY RUN (Drafts Only)'}")
    print("="*70)
    
    tracker = load_tracker()
    tracker, new_added = add_new_leads(tracker)
    
    print(f"\n📊 Total Leads: {len(tracker)}")
    print(f"🆕 New Leads Added: {new_added}")
    
    # Get leads needing action
    today = datetime.now().strftime('%Y-%m-%d')
    action_items = []
    
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
    
    # Process each email
    sent_count = 0
    failed_count = 0
    
    for i, item in enumerate(action_items, 1):
        template_type = "initial" if item["action"] == "send_initial" else "followup_1" if "followup_1" in item["action"] else "followup_2"
        template = EMAIL_TEMPLATES.get(template_type, EMAIL_TEMPLATES["initial"])
        
        subject = template["subject"].format(company=item["company"])
        body = template["body"].format(
            name=item["name"],
            company=item["company"],
            specialty=item["specialty"],
            sender=SENDER_NAME,
            sender_title=SENDER_TITLE,
            company_name=COMPANY_NAME,
            company_address=COMPANY_ADDRESS,
            company_phone=COMPANY_PHONE,
            company_mobile=COMPANY_MOBILE,
            sender_email=SENDER_EMAIL,
            company_website=COMPANY_WEBSITE
        )
        
        print(f"\n{i}. Sending to {item['name']} at {item['company']}...")
        print(f"   Email: {item['email']}")
        
        if send_emails:
            success, message = send_email(item["email"], subject, body)
            if success:
                print(f"   ✅ SENT!")
                sent_count += 1
                # Update tracker
                tracker[item["email"]]["last_contacted"] = today
                tracker[item["email"]]["email_count"] = item["email_count"] + 1
                tracker[item["email"]]["next_action_date"] = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
                if item["action"] == "send_initial":
                    tracker[item["email"]]["next_action"] = "send_followup_1"
                elif "followup_1" in item["action"]:
                    tracker[item["email"]]["next_action"] = "send_followup_2"
                else:
                    tracker[item["email"]]["next_action"] = "send_final"
            else:
                print(f"   ❌ FAILED: {message}")
                failed_count += 1
        else:
            print(f"   📝 DRAFT CREATED (use send_emails=True to send live)")
    
    # Save tracker
    save_tracker(tracker)
    
    # Summary
    print("\n" + "="*70)
    print("📈 SUMMARY")
    print("="*70)
    print(f"📧 Emails Prepared: {len(action_items)}")
    if send_emails:
        print(f"✅ Successfully Sent: {sent_count}")
        print(f"❌ Failed: {failed_count}")
    else:
        print("📝 Mode: DRAFT - Set send_emails=True to send live")
    print("="*70)
    
    return tracker

if __name__ == "__main__":
    import sys
    send = "--send" in sys.argv
    run_pipeline(send_emails=send)
