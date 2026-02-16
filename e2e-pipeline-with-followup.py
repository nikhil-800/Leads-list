#!/usr/bin/env python3
"""
Enhanced Pipeline with Automatic Follow-ups
Team-Soft LLC - nikhil@teamsoftllc.com
"""

import json
import csv
from datetime import datetime, timedelta
import random
import os

SENDER_EMAIL = "nikhil@teamsoftllc.com"

def create_lead_data():
    """Lead database"""
    return [
        {"company": "TEKsystems", "email": "btorres@teksystems.com", "specialty": "Java, Python, Cloud", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Insight Global", "email": "mjohnson@insightglobal.com", "specialty": "Java, React, Data", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Apex Systems", "email": "jmartinez@apexsystems.com", "specialty": ".NET, Salesforce", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "CACI", "email": "jreed@caci.com", "specialty": "Cleared IT, DoD", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "ManTech", "email": "rharris@mantech.com", "specialty": "Defense, Cleared", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Booz Allen", "email": "smartinez@bah.com", "specialty": "Federal, Data", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "SAIC", "email": "kphillips@saic.com", "specialty": "NASA, DoD", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Accenture", "email": "sarah.chen@accenture.com", "specialty": "Salesforce, Cloud", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Deloitte", "email": "dkim@deloitte.com", "specialty": "SAP, Oracle", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "IBM", "email": "patricia.lee@ibm.com", "specialty": "Cloud, AI/ML", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Epic Staffing", "email": "jennifer.morgan@epic.com", "specialty": "Epic, HL7", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Cerner", "email": "paul.richardson@cerner.com", "specialty": "Cerner, Oracle", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Kelly Services", "email": "tdavis@kellyservices.com", "specialty": "QA, Java", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Robert Half", "email": "jwilson@roberthalf.com", "specialty": "Java, Python", "last_contacted": "", "response": "", "follow_ups": 0},
        {"company": "Aerotek", "email": "drodriguez@aerotek.com", "specialty": "DevOps, QA", "last_contacted": "", "response": "", "follow_ups": 0},
    ]

def get_email_templates():
    """Email templates"""
    return {
        "initial": {
            "subject": "IT Contractors Available - {company}",
            "body": """Hi,

I'm reaching out from Team-Soft LLC about IT contractors for your current projects.

We have {specialty} engineers available for C2C, 1099, or C2H arrangements.

Our candidates are pre-vetted and can start within 1-2 weeks.

Rates: $60-150/hour depending on experience

Are you currently hiring for any IT roles? Happy to share candidate profiles.

Best,
Nikhil
Team-Soft LLC
nikhil@teamsoftllc.com"""
        },
        
        "follow_up_1": {
            "subject": "Following Up - IT Contractors - {company}",
            "body": """Hi,

Just following up on my previous email about IT contractors.

Have any current needs? Happy to help fill positions quickly.

We have {specialty} candidates available.

Best,
Nikhil
Team-Soft LLC
nikhil@teamsoftllc.com"""
        },
        
        "follow_up_2": {
            "subject": "Last Touch - IT Staffing - {company}",
            "body": """Hi,

One more time on this - if you don't need contractors now, I'll circle back in a few weeks.

But if you have any needs, I can send profiles same day.

Thanks,
Nikhil
Team-Soft LLC
nikhil@teamsoftllc.com"""
        }
    }

def load_lead_tracker():
    """Load lead tracking file"""
    if os.path.exists("lead_tracker.json"):
        with open("lead_tracker.json", "r") as f:
            return json.load(f)
    return {}

def save_lead_tracker(tracker):
    """Save lead tracker"""
    with open("lead_tracker.json", "w") as f:
        json.dump(tracker, f, indent=2)

def run_pipeline_with_followup():
    """Run pipeline with automatic follow-up detection"""
    
    print("🚀 ENHANCED PIPELINE WITH FOLLOW-UPS")
    print("=" * 60)
    
    leads = create_lead_data()
    templates = get_email_templates()
    tracker = load_lead_tracker()
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Categorize leads
    needs_initial = []
    needs_followup_1 = []
    needs_followup_2 = []
    responded = []
    
    for lead in leads:
        email = lead["email"]
        
        if email not in tracker:
            # New lead - needs initial contact
            needs_initial.append(lead)
        else:
            # Check follow-up status
            status = tracker[email]
            last_contact = datetime.strptime(status.get("last_contacted", "2020-01-01"), '%Y-%m-%d')
            days_since = (datetime.now() - last_contact).days
            response = status.get("response", "")
            follow_count = status.get("follow_ups", 0)
            
            if response.lower() in ["interested", "yes", "needs candidates", "send profiles"]:
                responded.append(lead)
            elif follow_count == 0 and days_since >= 3:
                needs_followup_1.append(lead)
            elif follow_count == 1 and days_since >= 5:
                needs_followup_2.append(lead)
            elif follow_count >= 2:
                pass  # Max follow-ups reached
            else:
                needs_initial.append(lead)
    
    print(f"\n📊 LEAD STATUS:")
    print(f"  🆕 Needs Initial Contact: {len(needs_initial)}")
    print(f"  🔄 Needs Follow-up #1 (3+ days): {len(needs_followup_1)}")
    print(f"  🔔 Needs Follow-up #2 (5+ days): {len(needs_followup_2)}")
    print(f"  ✅ Already Responded: {len(responded)}")
    
    # Generate action items
    print(f"\n📧 TODAY'S ACTION ITEMS:")
    
    action_count = 0
    
    # Step 1: Send initial contacts
    if needs_initial:
        print(f"\n📤 SENDING {len(needs_initial[:10])} INITIAL EMAILS:")
        for lead in needs_initial[:10]:
            print(f"  → {lead['company']}: {lead['email']}")
            # Update tracker
            tracker[lead["email"]] = {
                "last_contacted": today,
                "response": "sent",
                "follow_ups": 0,
                "template": "initial"
            }
            action_count += 1
    
    # Step 2: Send follow-up #1
    if needs_followup_1:
        print(f"\n🔄 SENDING {len(needs_followup_1[:5])} FOLLOW-UP #1:")
        for lead in needs_followup_1[:5]:
            print(f"  → {lead['company']}: {lead['email']}")
            tracker[lead["email"]]["last_contacted"] = today
            tracker[lead["email"]]["follow_ups"] = 1
            tracker[lead["email"]]["template"] = "follow_up_1"
            action_count += 1
    
    # Step 3: Send follow-up #2
    if needs_followup_2:
        print(f"\n🔔 SENDING {len(needs_followup_2[:3])} FINAL FOLLOW-UPS:")
        for lead in needs_followup_2[:3]:
            print(f"  → {lead['company']}: {lead['email']}")
            tracker[lead["email"]]["last_contacted"] = today
            tracker[lead["email"]]["follow_ups"] = 2
            tracker[lead["email"]]["template"] = "follow_up_2"
            action_count += 1
    
    # Save tracker
    save_lead_tracker(tracker)
    
    # Export today's action list
    today_file = f"daily_actions_{today}.csv"
    with open(today_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Company", "Email", "Action", "Template"])
        
        for lead in needs_initial[:10]:
            writer.writerow([lead["company"], lead["email"], "Initial Contact", "initial"])
        for lead in needs_followup_1[:5]:
            writer.writerow([lead["company"], lead["email"], "Follow-up #1", "follow_up_1"])
        for lead in needs_followup_2[:3]:
            writer.writerow([lead["company"], lead["email"], "Final Follow-up", "follow_up_2"])
    
    print(f"\n✅ Saved: {today_file}")
    print(f"\n📈 SUMMARY:")
    print(f"  Total Actions Today: {action_count}")
    print(f"  Tracker Updated: lead_tracker.json")
    
    print("\n" + "=" * 60)
    print("🎯 TO SEND EMAILS:")
    print("  1. Open daily_actions_*.csv")
    print("  2. Use templates from email_templates")
    print("  3. Update lead_tracker.json after responses")
    print("=" * 60)
    
    return tracker

if __name__ == "__main__":
    run_pipeline_with_followup()
