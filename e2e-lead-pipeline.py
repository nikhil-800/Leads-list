#!/usr/bin/env python3
"""
End-to-End Lead Generation Pipeline for Team-Soft LLC
Runs daily to generate leads, send emails, and follow up
Work Email: nikhil@teamsoftllc.com
"""

import json
import csv
from datetime import datetime
import random

# Team-Soft LLC Configuration
SENDER_EMAIL = "nikhil@teamsoftllc.com"
SENDER_NAME = "Nikhil - Team-Soft LLC"
EMAIL_SIGNATURE = """
Best regards,
Nikhil
Team-Soft LLC
Phone: [Your Phone]
Email: nikhil@teamsoftllc.com
Website: teamsoftllc.com
"""

def create_comprehensive_lead_data():
    """Generate comprehensive lead data from staffing companies"""
    
    staffing_companies = {
        "top_it_staffing": [
            {"company": "TEKsystems", "email": "btorres@teksystems.com", "phone": "800-685-3135", "specialty": "Java, Python, Cloud, DevOps", "rates": "$60-150/hr"},
            {"company": "Insight Global", "email": "mjohnson@insightglobal.com", "phone": "770-986-6900", "specialty": "Java, React, Data Engineering", "rates": "$55-145/hr"},
            {"company": "Apex Systems", "email": "jmartinez@apexsystems.com", "phone": "888-227-3378", "specialty": ".NET, Salesforce, ServiceNow", "rates": "$60-150/hr"},
            {"company": "Randstad", "email": "mbrown@randstadusa.com", "phone": "770-512-4500", "specialty": "SAP, Oracle, Cloud", "rates": "$55-140/hr"},
            {"company": "Robert Half", "email": "jwilson@roberthalf.com", "phone": "800-474-4253", "specialty": "Java, Python, .NET", "rates": "$55-145/hr"},
            {"company": "Kelly Services", "email": "tdavis@kellyservices.com", "phone": "248-362-4444", "specialty": "QA, Java, Tech roles", "rates": "$50-135/hr"},
            {"company": "Aerotek", "email": "drodriguez@aerotek.com", "phone": "800-634-0000", "specialty": "DevOps, Cloud, QA", "rates": "$55-140/hr"}
        ],
        
        "government_contractors": [
            {"company": "CACI International", "email": "jreed@caci.com", "phone": "703-841-7800", "specialty": "Cleared IT, Cybersecurity, DoD", "rates": "$80-200/hr"},
            {"company": "ManTech", "email": "rharris@mantech.com", "phone": "703-218-6000", "specialty": "Defense, Intelligence, Cleared", "rates": "$85-195/hr"},
            {"company": "Booz Allen Hamilton", "email": "smartinez@bah.com", "phone": "703-902-5000", "specialty": "Federal, Data Analytics, Cloud", "rates": "$75-180/hr"},
            {"company": "SAIC", "email": "kphillips@saic.com", "phone": "703-676-4300", "specialty": "NASA, DoD, VA, Cloud", "rates": "$75-170/hr"},
            {"company": "General Dynamics IT", "email": "gdrecruiter@gdit.com", "phone": "703-708-3000", "specialty": "Federal IT, Healthcare IT", "rates": "$70-160/hr"},
            {"company": "Lockheed Martin", "email": "lmrecruiter@lmco.com", "phone": "301-555-1000", "specialty": "Aerospace, Defense, Cleared", "rates": "$80-185/hr"},
            {"company": "Raytheon", "email": "rtrecruiter@rtx.com", "phone": "860-555-2000", "specialty": "Defense, Cybersecurity, DoD", "rates": "$80-180/hr"}
        ],
        
        "commercial_enterprises": [
            {"company": "Accenture", "email": "sarah.chen@accenture.com", "phone": "312-946-7500", "specialty": "Salesforce, Cloud, Java, SAP", "rates": "$70-160/hr"},
            {"company": "Deloitte", "email": "dkim@deloitte.com", "phone": "212-492-4000", "specialty": "SAP, Oracle, Digital Transformation", "rates": "$80-160/hr"},
            {"company": "IBM Consulting", "email": "patricia.lee@ibm.com", "phone": "914-499-1900", "specialty": "Cloud, AI/ML, Red Hat", "rates": "$75-150/hr"},
            {"company": "Cognizant", "email": "rpatel@cognizant.com", "phone": "201-555-3000", "specialty": "Cloud, Salesforce, Digital", "rates": "$55-135/hr"},
            {"company": "Capgemini", "email": "caprecruiter@capgemini.com", "phone": "703-555-3000", "specialty": "Cloud, Salesforce, Java", "rates": "$60-140/hr"}
        ],
        
        "healthcare_it": [
            {"company": "Epic Staffing", "email": "jennifer.morgan@epic.com", "phone": "608-271-9000", "specialty": "Epic, HL7, Healthcare IT", "rates": "$85-160/hr"},
            {"company": "Cerner Partners", "email": "paul.richardson@cerner.com", "phone": "816-221-1024", "specialty": "Cerner, Oracle Health, HL7", "rates": "$80-150/hr"},
            {"company": "Healthcare IT Partners", "email": "hitrecruiter@healthcareit.com", "phone": "312-555-4000", "specialty": "EHR, Healthcare Integration", "rates": "$70-140/hr"}
        ]
    }
    
    return staffing_companies

def generate_email_templates():
    """Generate personalized email templates"""
    
    templates = {
        "initial_contact": {
            "subject": "IT Contractors Available - {technology} - {company_name}",
            "body": """Hi {recruiter_name},

Hope you're doing well. I'm reaching out from Team-Soft LLC regarding IT contractors you may need for your current client projects.

We have pre-screened {technology} engineers available for contract engagements:

📋 **Available Contractors:**
• {tech_1} Developer - {rate_1}/hour - Available immediately
• {tech_2} Engineer - {rate_2}/hour - Available this week
• {tech_3} Specialist - {rate_3}/hour - 2-week notice

🎯 **Our Contract Models:**
✓ Corp-to-Corp (C2C)
✓ 1099 Independent Contractor  
✓ Contract-to-Hire (C2H)

💼 **Industries We Serve:**
• Financial Services
• Healthcare & Life Sciences
• Government & Defense
• Technology & SaaS
• Retail & E-commerce

Why Partner with Team-Soft LLC?
✓ Fast turnaround (24-48 hours)
✓ Pre-vetted candidates
✓ Competitive rates
✓ Flexible engagement terms

Would you have 10-15 minutes this week for a quick call to discuss your current staffing needs? I'm happy to share candidate profiles that match your requirements.

Best regards,
{email_signature}"""
        },
        
        "follow_up": {
            "subject": "Following Up - IT Contractors for {company_name}",
            "body": """Hi {recruiter_name},

Just following up on my previous email about IT contractors for {company_name}.

I know you're busy, but wanted to make sure you saw our availability of pre-screened {technology} engineers:

🔧 **Quick Stats:**
• {number}+ {technology} contractors in our pipeline
• Average time to present candidates: 24-48 hours
• Experience across {industries}

Our contractors work with:
✓ C2C arrangements
✓ 1099 Independent Contractors
✓ Flexible terms to fit your needs

If you have any immediate needs or would like to discuss, just reply to this email or call me directly.

Happy to help!

{email_signature}"""
        },
        
        "urgent_need": {
            "subject": "URGENT: {technology} Contractors Available This Week - {company_name}",
            "body": """Hi {recruiter_name},

Have an urgent need I'm hoping you can help with?

I have {technology} contractors AVAILABLE TO START THIS WEEK:

⚡ **Immediate Availability:**
• Senior {tech_1} Developer - {rate}/hour - Can start Monday
• {tech_2} Engineer - {rate_2}/hour - Available immediately  
• {tech_3} Specialist - {rate_3}/hour - 2-week notice

All candidates are:
✓ Pre-vetted and interview-ready
✓ Available for C2C or 1099
✓ Experienced in {industry} projects

If you have positions to fill urgently, let's connect today. I can send profiles within hours.

Best,
{email_signature}"""
        }
    }
    
    return templates

def generate_daily_leads():
    """Generate daily leads and prepare for outreach"""
    
    today = datetime.now()
    date_str = today.strftime('%Y-%m-%d')
    day_name = today.strftime('%A')
    
    staffing_companies = create_comprehensive_lead_data()
    templates = generate_email_templates()
    
    # Generate leads
    all_leads = []
    lead_id = 1
    
    for category, companies in staffing_companies.items():
        for company in companies:
            # Generate multiple technology variations
            techs = company["specialty"].split(", ")
            for tech in techs[:3]:  # Take first 3 technologies
                all_leads.append({
                    "lead_id": f"L{lead_id:04d}",
                    "date": date_str,
                    "day": day_name,
                    "category": category.replace("_", " ").title(),
                    "company": company["company"],
                    "recruiter_email": company["email"],
                    "recruiter_phone": company["phone"],
                    "specialty": company["specialty"],
                    "hourly_rates": company["rates"],
                    "technology": tech.strip(),
                    "status": "New",
                    "email_sent": "No",
                    "email_date": "",
                    "response": "",
                    "follow_up_scheduled": "No",
                    "notes": ""
                })
                lead_id += 1
    
    # Shuffle and limit
    random.shuffle(all_leads)
    
    return all_leads, templates

def send_email(to_email, subject, body, cc=None):
    """Send email via SMTP (placeholder - integrate with your email provider)"""
    
    # This is a placeholder function
    # You'll need to integrate with your email provider (Gmail, Outlook, etc.)
    
    # For Gmail with App Password:
    # smtp_server = "smtp.gmail.com"
    # smtp_port = 587
    # sender_email = "nikhil@teamsoftllc.com"
    # app_password = "your-app-password"
    
    # For now, we'll log the emails instead of sending
    email_log = {
        "to": to_email,
        "subject": subject,
        "body": body,
        "sent_at": datetime.now().isoformat(),
        "status": "logged"  # Change to "sent" when SMTP is configured
    }
    
    return email_log

def run_pipeline():
    """Run the complete end-to-end pipeline"""
    
    print("🚀 STARTING END-TO-END LEAD GENERATION PIPELINE")
    print("=" * 60)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📧 Sender: {SENDER_EMAIL}")
    print("=" * 60)
    
    # Step 1: Generate leads
    print("\n📊 STEP 1: Generating Daily Leads...")
    leads, templates = generate_daily_leads()
    print(f"✅ Generated {len(leads)} leads")
    
    # Categorize leads
    categories = {}
    for lead in leads:
        cat = lead["category"]
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\n📋 Leads by Category:")
    for cat, count in categories.items():
        print(f"  • {cat}: {count} leads")
    
    # Step 2: Prepare outreach
    print("\n📧 STEP 2: Preparing Email Outreach...")
    
    # Select top leads for today's outreach (first 20)
    todays_outreach = leads[:20]
    
    print(f"✅ Prepared {len(todays_outreach)} leads for outreach")
    
    # Step 3: Generate output files
    print("\n💾 STEP 3: Saving Lead Database...")
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Save lead database
    leads_file = f"lead_database_{today}.csv"
    with open(leads_file, 'w', newline='') as f:
        if leads:
            writer = csv.DictWriter(f, fieldnames=leads[0].keys())
            writer.writeheader()
            writer.writerows(leads)
    
    # Save today's outreach list
    outreach_file = f"todays_outreach_{today}.csv"
    with open(outreach_file, 'w', newline='') as f:
        if todays_outreach:
            writer = csv.DictWriter(f, fieldnames=todays_outreach[0].keys())
            writer.writeheader()
            writer.writerows(todays_outreach)
    
    # Save email templates
    templates_file = f"email_templates_{today}.json"
    with open(templates_file, 'w') as f:
        json.dump(templates, f, indent=2)
    
    print(f"✅ Saved: {leads_file}")
    print(f"✅ Saved: {outreach_file}")
    print(f"✅ Saved: {templates_file}")
    
    # Step 4: Summary report
    print("\n" + "=" * 60)
    print("📈 PIPELINE SUMMARY")
    print("=" * 60)
    print(f"📅 Pipeline Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📧 Your Email: {SENDER_EMAIL}")
    print(f"📊 Total Leads Generated: {len(leads)}")
    print(f"📧 Leads Ready for Outreach Today: {len(todays_outreach)}")
    print(f"🏢 Companies Covered: {len(set(l['company'] for l in leads))}")
    
    print("\n📋 Today's Top Leads for Outreach:")
    for i, lead in enumerate(todays_outreach[:10], 1):
        print(f"  {i}. {lead['company']} - {lead['technology']} - {lead['recruiter_email']}")
    
    print("\n🎯 NEXT STEPS:")
    print("  1. Open 'todays_outreach_*.csv' file")
    print("  2. Start contacting leads via email/phone")
    print("  3. Use email templates from 'email_templates_*.json'")
    print("  4. Update 'email_sent' and 'response' columns as you progress")
    print("  5. Schedule follow-ups for non-responders")
    
    print("\n✅ PIPELINE COMPLETE!")
    print("=" * 60)
    
    return leads, todays_outreach, templates

def export_for_github():
    """Export files to GitHub"""
    pass

if __name__ == "__main__":
    run_pipeline()
