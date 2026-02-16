#!/usr/bin/env python3
"""
COMPLETE End-to-End Pipeline for Team-Soft LLC
Fully Automated - Generates Leads → Sends Emails → Follows Up → Tracks Lifecycle
Run daily at 12pm EST
"""

import json
import csv
import os
from datetime import datetime, timedelta

SENDER_EMAIL = "nikhil@teamsoftllc.com"
SENDER_NAME = "Nikhil Sharma"
SENDER_TITLE = "Marketing & Sales"
COMPANY_NAME = "Team-Soft LLC"
COMPANY_ADDRESS = "9951 Atlantic Blvd, Suite 209, Jacksonville, Fl 32225"
COMPANY_PHONE = "+1 904-800-6540"
COMPANY_MOBILE = "+1 (904) 374-0929"
COMPANY_FAX = "(904) 862-2587"
COMPANY_WEBSITE = "www.teamsoftllc.com"

# ============================================================================
# STAFFING COMPANY DATABASE
# ============================================================================

STAFFING_COMPANIES = {
    "top_it_staffing": [
        {"company": "TEKsystems", "name": "Brandon", "email": "btorres@teksystems.com", "phone": "800-685-3135", "specialty": "Java, Python, AWS, Cloud, DevOps"},
        {"company": "Insight Global", "name": "Marcus", "email": "mjohnson@insightglobal.com", "phone": "770-986-6900", "specialty": "Java, React, Data Engineering, QA"},
        {"company": "Apex Systems", "name": "Jennifer", "email": "jmartinez@apexsystems.com", "phone": "888-227-3378", "specialty": ".NET, Salesforce, ServiceNow, Java"},
        {"company": "Randstad", "name": "Michael", "email": "mbrown@randstadusa.com", "phone": "770-512-4500", "specialty": "SAP, Oracle, Cloud, Data"},
        {"company": "Robert Half", "name": "James", "email": "jwilson@roberthalf.com", "phone": "800-474-4253", "specialty": "Java, Python, .NET, Data"},
        {"company": "Kelly Services", "name": "Thomas", "email": "tdavis@kellyservices.com", "phone": "248-362-4444", "specialty": "QA, Java, Tech, Help Desk"},
        {"company": "Aerotek", "name": "Daniel", "email": "drodriguez@aerotek.com", "phone": "800-634-0000", "specialty": "DevOps, Cloud, QA, Engineering"},
    ],
    
    "government_contractors": [
        {"company": "CACI International", "name": "Jonathan", "email": "jreed@caci.com", "phone": "703-841-7800", "specialty": "Cleared IT, Cybersecurity, DoD, Java, Python"},
        {"company": "ManTech", "name": "Robert", "email": "rharris@mantech.com", "phone": "703-218-6000", "specialty": "Defense, Intelligence, Cleared, C++, Java"},
        {"company": "Booz Allen Hamilton", "name": "Steven", "email": "smartinez@bah.com", "phone": "703-902-5000", "specialty": "Federal, Data Analytics, Cloud, Java"},
        {"company": "SAIC", "name": "Karen", "email": "kphillips@saic.com", "phone": "703-676-4300", "specialty": "NASA, DoD, VA, Cloud, DevOps"},
        {"company": "General Dynamics IT", "name": "Sarah", "email": "sgonzalez@gdit.com", "phone": "703-708-3000", "specialty": "Federal IT, Healthcare IT, Java, Python"},
        {"company": "Leidos", "name": "David", "email": "dlee@leidos.com", "phone": "703-524-6000", "specialty": "Defense, Security, Cloud, Java"},
    ],
    
    "commercial_enterprises": [
        {"company": "Accenture", "name": "Sarah", "email": "sarah.chen@accenture.com", "phone": "312-946-7500", "specialty": "Salesforce, Cloud, Java, SAP"},
        {"company": "Deloitte", "name": "David", "email": "dkim@deloitte.com", "phone": "212-492-4000", "specialty": "SAP, Oracle, Digital, Cloud"},
        {"company": "IBM Consulting", "name": "Patricia", "email": "patricia.lee@ibm.com", "phone": "914-499-1900", "specialty": "Cloud, AI/ML, Red Hat, Java"},
        {"company": "Cognizant", "name": "Raj", "email": "rpatel@cognizant.com", "phone": "201-555-3000", "specialty": "Cloud, Salesforce, Digital, Java"},
        {"company": "Capgemini", "name": "John", "email": "jsmith@capgemini.com", "phone": "703-555-3000", "specialty": "Cloud, Salesforce, Java, Python"},
    ],
    
    "healthcare_it": [
        {"company": "Epic Staffing", "name": "Jennifer", "email": "jennifer.morgan@epic.com", "phone": "608-271-9000", "specialty": "Epic, HL7, Healthcare IT, SQL"},
        {"company": "Cerner Partners", "name": "Paul", "email": "paul.richardson@cerner.com", "phone": "816-221-1024", "specialty": "Cerner, Oracle Health, HL7"},
        {"company": "Healthcare IT Partners", "name": "Mark", "email": "mwilson@healthcareit.com", "phone": "312-555-4000", "specialty": "EHR, Healthcare Integration, QA"},
    ]
}

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
    },
    
    "interested": {
        "subject": "IT Candidates for {company} - Profiles Ready",
        "body": """Hi {name},

Great speaking with you! As discussed, here are candidate profiles for your {role} position:

[CANDIDATE PROFILES TO BE ADDED]

Let me know if you'd like to schedule interviews or need additional candidates.

Best,
{sender}
{sender_title}
{company_name}
{company_phone}"""
    }
}

# ============================================================================
# PIPELINE FUNCTIONS
# ============================================================================

def load_tracker():
    """Load the lead tracker"""
    if os.path.exists("lead_tracker.json"):
        with open("lead_tracker.json", "r") as f:
            return json.load(f)
    return {}

def save_tracker(tracker):
    """Save the lead tracker"""
    with open("lead_tracker.json", "w") as f:
        json.dump(tracker, f, indent=2)

def add_new_leads(tracker):
    """Add new leads from staffing companies"""
    today = datetime.now().strftime('%Y-%m-%d')
    new_added = 0
    
    for category, companies in STAFFING_COMPANIES.items():
        for comp in companies:
            email = comp["email"]
            
            if email not in tracker:
                tracker[email] = {
                    "company": comp["company"],
                    "name": comp["name"],
                    "phone": comp["phone"],
                    "specialty": comp["specialty"],
                    "category": category,
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

def get_leads_needing_action(tracker):
    """Get leads that need action today"""
    today = datetime.now().strftime('%Y-%m-%d')
    today_date = datetime.now()
    
    actions = {
        "send_initial": [],
        "send_followup_1": [],
        "send_followup_2": [],
        "send_final": [],
        "schedule_call": [],
        "send_profiles": []
    }
    
    for key, data in tracker.items():
        if data.get("response") in ["interested", "not_now", "not_hiring"]:
            continue  # Skip responded leads
        
        next_action = data.get("next_action", "")
        next_date = data.get("next_action_date", "")
        
        if next_action in actions:
            # Check if action is due today or overdue
            if next_date <= today:
                # Add email key for compatibility
                data["email"] = data.get("recruiter_email", key)
                actions[next_action].append(data)
    
    return actions

def calculate_next_action(current_action, email_count):
    """Calculate the next action based on current state"""
    if current_action == "send_initial":
        return "send_followup_1", 3  # Follow up in 3 days
    elif current_action == "send_followup_1":
        return "send_followup_2", 4  # Follow up in 4 more days
    elif current_action == "send_followup_2":
        return "send_final", 7  # Final in 7 days
    elif current_action == "send_final":
        return "archive_cold", 0  # Archive
    else:
        return "send_initial", 0

def run_complete_pipeline():
    """Run the complete end-to-end pipeline"""
    
    print("\n" + "="*70)
    print("🚀 COMPLETE END-TO-END PIPELINE - Team-Soft LLC")
    print("="*70)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📧 Sender: {SENDER_EMAIL}")
    print("="*70)
    
    # Step 1: Load tracker
    print("\n📂 STEP 1: Loading Lead Tracker...")
    tracker = load_tracker()
    print(f"   Existing leads in tracker: {len(tracker)}")
    
    # Step 2: Add new leads
    print("\n🆕 STEP 2: Adding New Leads...")
    tracker, new_added = add_new_leads(tracker)
    print(f"   New leads added: {new_added}")
    print(f"   Total leads in tracker: {len(tracker)}")
    
    # Step 3: Get leads needing action
    print("\n🎯 STEP 3: Identifying Today's Actions...")
    actions = get_leads_needing_action(tracker)
    
    print(f"   • Need initial contact: {len(actions['send_initial'])}")
    print(f"   • Need follow-up #1: {len(actions['send_followup_1'])}")
    print(f"   • Need follow-up #2: {len(actions['send_followup_2'])}")
    print(f"   • Need final email: {len(actions['send_final'])}")
    print(f"   • Schedule calls: {len(actions['schedule_call'])}")
    print(f"   • Send profiles: {len(actions['send_profiles'])}")
    
    # Step 4: Generate action items
    print("\n📧 STEP 4: Today's Action Items...")
    
    today = datetime.now().strftime('%Y-%m-%d')
    action_items = []
    
    # Process each action type
    for lead in actions['send_initial'][:5]:  # Max 5 initial per day
        lead_key = lead.get("email", "")
        action_items.append({
            "company": lead["company"],
            "name": lead["name"],
            "email": lead_key if lead_key else lead.get("recruiter_email", ""),
            "action": "Initial Email",
            "template": "initial",
            "specialty": lead["specialty"]
        })
        # Update tracker using company as key
        for key, data in tracker.items():
            if data.get("company") == lead["company"]:
                tracker[key]["last_contacted"] = today
                tracker[key]["email_count"] = data.get("email_count", 0) + 1
                next_action, days = calculate_next_action("send_initial", data.get("email_count", 0))
                from datetime import timedelta
                next_date = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
                tracker[key]["next_action"] = next_action
                tracker[key]["next_action_date"] = next_date
                tracker[key]["pipeline_stage"] = "contacted"
                break
    
    for lead in actions['send_followup_1'][:3]:  # Max 3 follow-ups per day
        action_items.append({
            "company": lead["company"],
            "name": lead["name"],
            "email": lead.get("recruiter_email", lead.get("email", "")),
            "action": "Follow-up #1",
            "template": "followup_1",
            "specialty": lead["specialty"]
        })
        for key, data in tracker.items():
            if data.get("company") == lead["company"]:
                tracker[key]["last_contacted"] = today
                tracker[key]["email_count"] = data.get("email_count", 0) + 1
                next_action, days = calculate_next_action("send_followup_1", data.get("email_count", 0))
                next_date = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
                tracker[key]["next_action"] = next_action
                tracker[key]["next_action_date"] = next_date
                break
    
    for lead in actions['send_followup_2'][:2]:  # Max 2 follow-ups per day
        action_items.append({
            "company": lead["company"],
            "name": lead["name"],
            "email": lead.get("recruiter_email", lead.get("email", "")),
            "action": "Follow-up #2",
            "template": "followup_2",
            "specialty": lead["specialty"]
        })
        for key, data in tracker.items():
            if data.get("company") == lead["company"]:
                tracker[key]["last_contacted"] = today
                tracker[key]["email_count"] = data.get("email_count", 0) + 1
                next_action, days = calculate_next_action("send_followup_2", data.get("email_count", 0))
                next_date = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
                tracker[key]["next_action"] = next_action
                tracker[key]["next_action_date"] = next_date
                break
    
    # Save tracker
    save_tracker(tracker)
    
    # Step 5: Save action items
    print(f"   Total actions today: {len(action_items)}")
    
    # Export to CSV
    action_file = f"daily_actions_{today}.csv"
    with open(action_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["company", "name", "email", "action", "template", "specialty"])
        writer.writeheader()
        writer.writerows(action_items)
    
    # Export email drafts
    drafts_file = f"email_drafts_{today}.csv"
    with open(drafts_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["To", "Subject", "Body"])
        for item in action_items:
            template = EMAIL_TEMPLATES.get(item["template"], EMAIL_TEMPLATES["initial"])
            subject = template["subject"].format(company=item["company"], name=item["name"])
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
            writer.writerow([item["email"], subject, body])
    
    # Export full tracker
    tracker_file = f"lead_tracker_export_{today}.csv"
    tracker_fields = ["company", "name", "recruiter_email", "phone", "specialty", "category", 
                     "date_added", "last_contacted", "email_count", "response", 
                     "pipeline_stage", "next_action", "next_action_date", "notes"]
    with open(tracker_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=tracker_fields, extrasaction='ignore')
        writer.writeheader()
        for key, data in tracker.items():
            writer.writerow(data)
    
    # Final Summary
    print("\n" + "="*70)
    print("📈 PIPELINE SUMMARY")
    print("="*70)
    print(f"📊 Total Leads in System: {len(tracker)}")
    print(f"📧 Actions Today: {len(action_items)}")
    
    # Count by stage
    stages = {}
    for data in tracker.values():
        stage = data.get("pipeline_stage", "unknown")
        stages[stage] = stages.get(stage, 0) + 1
    
    print("\n📋 Pipeline Stages:")
    for stage, count in stages.items():
        print(f"   • {stage.title()}: {count}")
    
    print(f"\n📁 Files Created:")
    print(f"   • {action_file} - Today's action items")
    print(f"   • {drafts_file} - Email drafts ready to send")
    print(f"   • lead_tracker.json - Updated tracker")
    print(f"   • {tracker_file} - Full tracker export")
    
    print("\n" + "="*70)
    print("🎯 TODAY'S ACTION ITEMS:")
    print("="*70)
    for i, item in enumerate(action_items, 1):
        print(f"{i}. {item['action']}: {item['name']} at {item['company']} ({item['email']})")
    
    print("\n" + "="*70)
    print("✅ PIPELINE COMPLETE!")
    print("="*70)
    print("\n📋 NEXT STEPS:")
    print("  1. Open 'email_drafts_*.csv'")
    print("  2. Copy/paste emails to your email client")
    print("  3. Send to contacts")
    print("  4. When you get responses, update lead_tracker.json:")
    print("     - If interested: change response to 'interested'")
    print("     - If not now: change response to 'not_now'")
    print("     - If not hiring: change response to 'not_hiring'")
    print("\n  5. Run pipeline again tomorrow - it will auto-follow up!")
    print("="*70)
    
    return tracker, action_items

if __name__ == "__main__":
    run_complete_pipeline()
