#!/usr/bin/env python3
"""
Team-Soft LLC - COMPREHENSIVE Staffing Vendor Pipeline
ONLY STAFFING COMPANIES (Prime Vendors) - No Direct Clients
Massive list with Network & Security engineers
"""

import json
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
COMPANY_PHONE = "+1 904-800-6540"
COMPANY_MOBILE = "+1 (904) 374-0929"

EMAILS_PER_DAY = 25

# ============================================================================
# COMPREHENSIVE STAFFING VENDORS ONLY - NO DIRECT CLIENTS
# ============================================================================

STAFFING_VENDORS = {
    # ======================= TOP IT STAFFING AGENCIES =======================
    "Top IT Staffing": [
        {"company": "TEKsystems", "email": "recruiting@teksystems.com", "specialty": "Java, Python, AWS, DevOps, Network"},
        {"company": "Insight Global", "email": "jobs@insightglobal.com", "specialty": "Java, React, Data, QA, Security"},
        {"company": "Apex Systems", "email": "careers@apexsystems.com", "specialty": ".NET, Salesforce, Cloud, Network"},
        {"company": "Randstad Technologies", "email": "techjobs@randstadusa.com", "specialty": "SAP, Oracle, Java, Security"},
        {"company": "Robert Half Technology", "email": "jobs.roberthalf@roberthalf.com", "specialty": "Java, Python, .NET, Network"},
        {"company": "Kelly Services", "email": "techjobs@kellyservices.com", "specialty": "QA, Java, Network, Security"},
        {"company": "Aerotek", "email": "info@aerotek.com", "specialty": "DevOps, Cloud, QA, Network"},
        {"company": "Kforce", "email": "staffing@kforce.com", "specialty": "Java, Python, Network, Security"},
        {"company": "Creative Circle", "email": "jobs@creativecircle.com", "specialty": "Creative, Tech, Network"},
        {"company": "Marden Companies", "email": "recruiting@mardencompanies.com", "specialty": "Java, .NET, Security"},
    ],
    
    # ======================= MAJOR STAFFING CORPORATIONS =======================
    "Major Staffing": [
        {"company": "ManpowerGroup", "email": "technology@manpower.com", "specialty": "Java, Python, Network, QA"},
        {"company": "Adecco", "email": "it.staffing@adecco.com", "specialty": "Java, SAP, Network"},
        {"company": "Randstad US", "email": "engineering@randstadusa.com", "specialty": "Engineering, Network, Security"},
        {"company": "Express Employment", "email": "tech@expressjob.com", "specialty": "IT, Network, Security"},
        {"company": "Peopleready", "email": "industrial@peopleready.com", "specialty": "Industrial, Tech, Network"},
        {"company": "Employbridge", "email": "staffing@employbridge.com", "specialty": "Technical, Network, QA"},
        {"company": "PeopleShare", "email": "jobs@peopleshare.com", "specialty": "IT, Java, Security"},
        {"company": "Headway Workforce", "email": "staffing@headwayworkforce.com", "specialty": "Tech, Network, Security"},
        {"company": "Labor Ready", "email": "today@peopleready.com", "specialty": "General Labor, Tech"},
        {"company": "Staffmark", "email": "info@staffmark.com", "specialty": "Technical, Network"},
    ],
    
    # ======================= IT & TECHNOLOGY STAFFING =======================
    "IT/Tech Specialists": [
        {"company": "Collabera", "email": "itjobs@collabera.com", "specialty": "Java, Python, AWS, Network"},
        {"company": "Astreya Partners", "email": "careers@astreya.com", "specialty": "Cloud, Network, Security"},
        {"company": "Artech Information", "email": "staffing@artech.com", "specialty": "Java, QA, Network"},
        {"company": "SIGMA Science", "email": "jobs@sigmajobs.com", "specialty": "Scientific, IT, Network"},
        {"company": "Hired", "email": "employers@hired.com", "specialty": "Tech, Python, Network"},
        {"company": "CyberCoders", "email": "jobs@cybercoders.com", "specialty": "Engineering, Security, Network"},
        {"company": "Motion Recruitment", "email": "techjobs@motionrecruitment.com", "specialty": "Software, Network, Security"},
        {"company": "Huxley Associates", "email": "jobs@huxley.com", "specialty": "Banking, Network, Security"},
        {"company": "Jefferson Frank", "email": "jobs@jeffersonfrank.com", "specialty": "AWS, Java, Network"},
        {"company": "Nelson Technology", "email": "staffing@nelson.com", "specialty": "Tech, Network, Security"},
    ],
    
    # ======================= GOVERNMENT CONTRACT STAFFING =======================
    "Government Contractors": [
        {"company": "CACI International", "email": "careers@caci.com", "specialty": "Cleared IT, Network, Security"},
        {"company": "ManTech International", "email": "careers@mantech.com", "specialty": "Defense, Network, Security"},
        {"company": "Booz Allen Hamilton", "email": "jobs@bah.com", "specialty": "Federal, Network, Security"},
        {"company": "SAIC", "email": "careers@saic.com", "specialty": "NASA, DoD, Network"},
        {"company": "Leidos", "email": "jobs@leidos.com", "specialty": "Defense, Network, Security"},
        {"company": "General Dynamics IT", "email": "careers@gdit.com", "specialty": "Federal IT, Network, Security"},
        {"company": "Northrop Grumman", "email": "jobs@northropgrumman.com", "specialty": "Aerospace, Network, Security"},
        {"company": "Raytheon Technologies", "email": "careers@rtx.com", "specialty": "Defense, Network, Security"},
        {"company": "L3Harris Technologies", "email": "careers@l3harris.com", "specialty": "Defense, Network, Security"},
        {"company": "BAE Systems", "email": "jobs@baesystems.com", "specialty": "Defense, Network, Security"},
    ],
    
    # ======================= CONSULTING & SERVICES STAFFING =======================
    "Consulting Firms": [
        {"company": "Accenture", "email": "recruiting@accenture.com", "specialty": "Cloud, SAP, Network, Security"},
        {"company": "Deloitte", "email": "jobs@deloitte.com", "specialty": "Consulting, Network, Security"},
        {"company": "PwC", "email": "technology.careers@pwc.com", "specialty": "Consulting, Network, Security"},
        {"company": "EY", "email": "careers@ey.com", "specialty": "Advisory, Network, Security"},
        {"company": "KPMG", "email": "kpmgcareers@kpmg.com", "specialty": "Audit, Network, Security"},
        {"company": "Capgemini", "email": "careers@capgemini.com", "specialty": "Cloud, Network, Security"},
        {"company": "Cognizant", "email": "careers@cognizant.com", "specialty": "Digital, Network, Security"},
        {"company": "Infosys", "email": "careers@infosys.com", "specialty": "IT Services, Network, QA"},
        {"company": "Wipro", "email": "careers@wipro.com", "specialty": "IT Services, Network, Security"},
        {"company": "TCS", "email": "careers@tcs.com", "specialty": "IT Services, Network, Security"},
    ],
    
    # ======================= HEALTHCARE IT STAFFING =======================
    "Healthcare IT Staffing": [
        {"company": "Epic Staffing Partners", "email": "jobs@epicstaffing.com", "specialty": "Epic, HL7, Network"},
        {"company": "Cerner Partners", "email": "careers@cerner.com", "specialty": "Cerner, Healthcare IT, Network"},
        {"company": "Healthcare IT Partners", "email": "jobs@hitpartners.com", "specialty": "Healthcare IT, Network, Security"},
        {"company": "MedUSolutions", "email": "staffing@medusolutions.com", "specialty": "Healthcare, Network, QA"},
        {"company": "Vital Solutions", "email": "jobs@vitalsolutions.com", "specialty": "Healthcare Tech, Network"},
    ],
    
    # ======================= NETWORK & SECURITY SPECIALISTS =======================
    "Network & Security Specialists": [
        {"company": "Accela", "email": "jobs@accela.com", "specialty": "Network, Security, Cloud"},
        {"company": "Presidio", "email": "careers@presidio.com", "specialty": "Network, Security, Infrastructure"},
        {"company": "CDK Global", "email": "careers@cdk.com", "specialty": "Auto, Network, Security"},
        {"company": "Rimini Street", "email": "jobs@riministreet.com", "specialty": "Enterprise SW, Network"},
        {"company": "Palo Alto Networks", "email": "careers@paloaltonetworks.com", "specialty": "Security, Network, Cloud"},
        {"company": "Fortinet", "email": "jobs@fortinet.com", "specialty": "Security, Network, Firewall"},
        {"company": "Cisco Systems", "email": "jobs@cisco.com", "specialty": "Network, Security, Collaboration"},
        {"company": "Juniper Networks", "email": "careers@juniper.net", "specialty": "Network, Routing, Security"},
    ],
    
    # ======================= CLOUD & DEVOPS SPECIALISTS =======================
    "Cloud & DevOps": [
        {"company": "AWS Partners", "email": "partners@amazon.com", "specialty": "AWS, Cloud, DevOps"},
        {"company": "Microsoft Partner Network", "email": "partners@microsoft.com", "specialty": "Azure, O365, Cloud"},
        {"company": "Google Cloud Partners", "email": "partners@google.com", "specialty": "GCP, Cloud, Data"},
        {"company": "CloudTech Pro", "email": "jobs@cloudtechpro.com", "specialty": "Cloud, DevOps, Network"},
        {"company": "ServerCentral", "email": "careers@servercentral.com", "specialty": "Cloud, Infrastructure, Network"},
        {"company": "Cloudreach", "email": "careers@cloudreach.com", "specialty": "AWS, Azure, Cloud"},
    ],
}

# ============================================================================
# NETWORK & SECURITY EMAIL TEMPLATES
# ============================================================================

NETWORK_SECURITY_TEMPLATES = {
    "Network Engineers": {
        "subject": "Network Engineers Available - CCNA, CCNP, CCIE Ready",
        "body": """Hi,

Need Network Engineers?

We have certified network professionals:
• 2 CCNA Engineers (2-4 yrs) - Available now
• 2 CCNP Engineers (5-7 yrs) - Enterprise background
• 1 CCIE (10+ yrs) - Architecture & design

**Skills:**
✓ Cisco, Juniper, Palo Alto
✓ Routing & Switching (BGP, OSPF, MPLS)
✓ SD-WAN, Firewall, VPN
✓ Network Security

**Industries:**
Banking, Healthcare, Government, Enterprise

Rates: $55-95/hr

Can send profiles today!

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "Security Engineers": {
        "subject": "Security Engineers - CISSP, CISM, CEH Available",
        "body": """Hi,

Need Security Professionals?

We have cleared and certified experts:
• 2 Security Engineers (CISSP) - 5+ yrs
• 1 SOC Analyst (SIEM) - 3+ yrs
• 1 Penetration Tester (CEH) - 4+ yrs
• 1 Security Architect - 10+ yrs

**Certifications:**
✓ CISSP, CISSP-ISSMP, CISM
✓ CEH, OSCP, GPEN
✓ CompTIA Security+, Network+

**Clearance:**
Some have Active Secret, others can get it

Rates: $65-120/hr

Need security help? I can help.

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "DevOps/Cloud": {
        "subject": "DevOps & Cloud Engineers - AWS, Azure, Kubernetes",
        "body": """Hi,

Need DevOps or Cloud Engineers?

We have:
• 2 AWS Solutions Architects - Certified
• 1 Azure Administrator - Expert
• 1 Kubernetes Expert - CKA
• 1 DevOps Engineer - CI/CD, Jenkins

**Skills:**
✓ AWS, Azure, GCP
✓ Kubernetes, Docker
✓ Terraform, CloudFormation
✓ CI/CD Pipelines, Jenkins

Rates: $70-130/hr

Need DevOps help? Let's talk.

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "Java/Python": {
        "subject": "Java & Python Developers - Ready to Start",
        "body": """Hi,

Need Developers?

We have:
• 3 Senior Java Engineers (6+ yrs) - Spring, Microservices
• 2 Python Engineers (4+ yrs) - Django, Flask, FastAPI
• 1 Java Architect - Enterprise

**Industries:**
Fintech, Healthcare, E-commerce, Logistics

Rates: $65-120/hr

Can send profiles today!

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "General": {
        "subject": "IT Contractors Available - Ready Now",
        "body": """Hi,

Need IT Staff?

We have pre-vetted contractors:
• Software Engineers (Java, Python, .NET, React)
• Network Engineers (Cisco, Juniper, Palo Alto)
• Security Professionals (CISSP, CEH, CompTIA)
• Cloud/DevOps (AWS, Azure, Kubernetes)
• QA Engineers (Selenium, Automation)

✓ C2C, 1099, C2H
✓ Fast turnaround
✓ Competitive rates

What's your need? I might have the right person.

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
}

def get_template(specialty):
    """Get technology-specific template"""
    specialty_lower = specialty.lower()
    
    if "network" in specialty_lower or "cisco" in specialty_lower or "juniper" in specialty_lower:
        return NETWORK_SECURITY_TEMPLATES["Network Engineers"]
    elif "security" in specialty_lower or "cyber" in specialty_lower:
        return NETWORK_SECURITY_TEMPLATES["Security Engineers"]
    elif "devops" in specialty_lower or "cloud" in specialty_lower or "aws" in specialty_lower or "azure" in specialty_lower:
        return NETWORK_SECURITY_TEMPLATES["DevOps/Cloud"]
    elif "java" in specialty_lower:
        return NETWORK_SECURITY_TEMPLATES["Java/Python"]
    elif "python" in specialty_lower:
        return NETWORK_SECURITY_TEMPLATES["Java/Python"]
    else:
        return NETWORK_SECURITY_TEMPLATES["General"]

def load_tracker():
    if os.path.exists("lead_tracker.json"):
        with open("lead_tracker.json", "r") as f:
            return json.load(f)
    return {}

def save_tracker(tracker):
    with open("lead_tracker.json", "w") as f:
        json.dump(tracker, f, indent=2)

def initialize_contacts():
    tracker = load_tracker()
    today = datetime.now().strftime('%Y-%m-%d')
    new_added = 0
    
    for category, companies in STAFFING_VENDORS.items():
        for comp in companies:
            email = comp["email"]
            if email not in tracker:
                tracker[email] = {
                    "company": comp["company"],
                    "name": "Hiring Manager",
                    "email": email,
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

def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
        msg['To'] = to_email
        msg['Bcc'] = SENDER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, [to_email, SENDER_EMAIL], msg.as_string())
        server.quit()
        return True, "Sent"
    except Exception as e:
        return False, str(e)

def run_pipeline(send=False):
    print("\n" + "="*70)
    print("🚀 COMPREHENSIVE STAFFING VENDORS PIPELINE")
    print("="*70)
    
    tracker, new_added = initialize_contacts()
    print(f"\n📊 Total Contacts: {len(tracker)}")
    print(f"🆕 New Added: {new_added}")
    
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
                "specialty": data.get("specialty"),
                "category": data.get("category"),
                "action": next_action,
                "email_count": data.get("email_count", 0)
            })
    
    action_items = action_items[:EMAILS_PER_DAY]
    print(f"📧 Actions Today: {len(action_items)}")
    
    sent = 0
    failed = 0
    
    for i, item in enumerate(action_items, 1):
        template = get_template(item["specialty"])
        
        subject = template["subject"]
        body = template["body"].format(
            sender=SENDER_NAME,
            company_name=COMPANY_NAME,
            mobile=COMPANY_MOBILE
        )
        
        print(f"\n{i}. {item['company']} ({item['category']})")
        print(f"   📧 {item['email']}")
        print(f"   💻 {item['specialty']}")
        
        if send:
            success, msg = send_email(item["email"], subject, body)
            if success:
                print(f"   ✅ SENT!")
                sent += 1
                tracker[item["email"]]["last_contacted"] = today
                tracker[item["email"]]["email_count"] = item["email_count"] + 1
                
                days = 3 if item["action"] == "send_initial" else 4
                tracker[item["email"]]["next_action_date"] = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
                
                if item["action"] == "send_initial":
                    tracker[item["email"]]["next_action"] = "send_followup_1"
                elif "followup_1" in item["action"]:
                    tracker[item["email"]]["next_action"] = "send_followup_2"
            else:
                print(f"   ❌ FAILED: {msg}")
                failed += 1
    
    save_tracker(tracker)
    
    print("\n" + "="*70)
    print(f"📈 SUMMARY: {len(action_items)} | ✅ {sent} | ❌ {failed}")
    print("="*70)

if __name__ == "__main__":
    import sys
    send = "--send" in sys.argv
    run_pipeline(send)
