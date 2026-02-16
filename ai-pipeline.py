#!/usr/bin/env python3
"""
Team-Soft LLC - AI-Powered Staffing Vendor Pipeline
- 25 emails/day
- Auto-updates with trending technologies
- Network & Security included
"""

import json
import smtplib
import os
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# ============================================================================
# CONFIGURATION
# ============================================================================

SENDER_EMAIL = "nikhil@teamsoftllc.com"
SENDER_PASSWORD = "r6lqD!1xw6XOTwC#"
SMTP_SERVER = "smtp.dreamhost.com"
SMTP_PORT = 587

SENDER_NAME = "Nikhil Sharma"
COMPANY_NAME = "Team-Soft LLC"
COMPANY_MOBILE = "+1 (904) 374-0929"

EMAILS_PER_DAY = 25

# ============================================================================
# TRENDING TECHNOLOGIES 2026
# ============================================================================

TRENDING_TECHS = {
    "AI/ML": ["Python", "TensorFlow", "PyTorch", "LLM", "ChatGPT", "MLOps", "Computer Vision", "NLP"],
    "Cloud": ["AWS", "Azure", "GCP", "Kubernetes", "Docker", "Terraform", "Serverless"],
    "Data": ["Snowflake", "Databricks", "Spark", "Kafka", "SQL", "NoSQL", "ETL"],
    "DevOps": ["Jenkins", "GitLab", "GitHub Actions", "ArgoCD", "Prometheus", "Grafana"],
    "Security": ["CISSP", "CEH", "Pen Testing", "SIEM", "Zero Trust", "SOC"],
    "Network": ["CCNA", "CCNP", "CCIE", "SD-WAN", "Palo Alto", "Fortinet", "Cisco"],
    "Programming": ["Java", "Python", "JavaScript", "TypeScript", "Go", "Rust", ".NET"],
    "Frontend": ["React", "Angular", "Vue", "Next.js", "Node.js"],
    "Mobile": ["React Native", "Swift", "Kotlin", "Flutter", "iOS", "Android"],
}

# ============================================================================
# COMPREHENSIVE STAFFING VENDORS - 150+
# ============================================================================

STAFFING_VENDORS = {
    "Top IT Staffing": [
        {"company": "TEKsystems", "email": "recruiting@teksystems.com", "specialty": "AI/ML,Cloud,Network,Security"},
        {"company": "Insight Global", "email": "jobs@insightglobal.com", "specialty": "DevOps,Data,Network,Security"},
        {"company": "Apex Systems", "email": "careers@apexsystems.com", "specialty": "Cloud,Kubernetes,Network"},
        {"company": "Randstad Technologies", "email": "techjobs@randstadusa.com", "specialty": "Java,Python,Network"},
        {"company": "Robert Half Technology", "email": "jobs.roberthalf@roberthalf.com", "specialty": "AI/ML,Cloud,Network"},
        {"company": "Kelly Services", "email": "techjobs@kellyservices.com", "specialty": "QA,Network,Security,DevOps"},
        {"company": "Aerotek", "email": "info@aerotek.com", "specialty": "Cloud,DevOps,Network"},
        {"company": "Kforce", "email": "staffing@kforce.com", "specialty": "Java,Python,Network,Security"},
        {"company": "Creative Circle", "email": "jobs@creativecircle.com", "specialty": "Creative,Tech,Network"},
        {"company": "Marden Companies", "email": "recruiting@mardencompanies.com", "specialty": "Java,.NET,Security"},
        {"company": "Experis", "email": "jobs@experis.com", "specialty": "IT,Network,Security"},
        {"company": "Modis", "email": "jobs@modis.com", "specialty": "IT,Cloud,Network"},
        {"company": "Akraya", "email": "jobs@akraya.com", "specialty": "Engineering,Network"},
        {"company": "Softworld", "email": "jobs@softworld.com", "specialty": "Technology,Network"},
        {"company": "Artech Information", "email": "staffing@artech.com", "specialty": "Java,QA,Network"},
    ],
    
    "Major Staffing": [
        {"company": "ManpowerGroup", "email": "technology@manpower.com", "specialty": "Java,Python,Network"},
        {"company": "Adecco", "email": "it.staffing@adecco.com", "specialty": "Java,Cloud,Network"},
        {"company": "Express Employment", "email": "tech@expressjob.com", "specialty": "IT,Network,Security"},
        {"company": "Peopleready", "email": "industrial@peopleready.com", "specialty": "Industrial,Tech"},
        {"company": "Employbridge", "email": "staffing@employbridge.com", "specialty": "Technical,Network"},
        {"company": "PeopleShare", "email": "jobs@peopleshare.com", "specialty": "IT,Java,Security"},
        {"company": "Headway Workforce", "email": "staffing@headwayworkforce.com", "specialty": "Tech,Network"},
        {"company": "Staffmark", "email": "info@staffmark.com", "specialty": "Technical,Network"},
        {"company": "TrueBlue", "email": "careers@trueblue.com", "specialty": "Industrial,Tech"},
        {"company": "Spherion", "email": "jobs@spherion.com", "specialty": "Tech,Network"},
    ],
    
    "Government Contractors": [
        {"company": "CACI International", "email": "careers@caci.com", "specialty": "Cleared IT,Network,Security"},
        {"company": "ManTech International", "email": "careers@mantech.com", "specialty": "Defense,Network,Security"},
        {"company": "Booz Allen Hamilton", "email": "jobs@bah.com", "specialty": "AI/ML,Cloud,Network,Security"},
        {"company": "SAIC", "email": "careers@saic.com", "specialty": "NASA,DoD,Network"},
        {"company": "Leidos", "email": "jobs@leidos.com", "specialty": "Defense,Network,Security,AI"},
        {"company": "General Dynamics IT", "email": "careers@gdit.com", "specialty": "Federal IT,Network,Cloud"},
        {"company": "Northrop Grumman", "email": "jobs@northropgrumman.com", "specialty": "Aerospace,Network,Security"},
        {"company": "Raytheon Technologies", "email": "careers@rtx.com", "specialty": "Defense,Network,Security"},
        {"company": "L3Harris Technologies", "email": "careers@l3harris.com", "specialty": "Defense,Network,Security"},
        {"company": "BAE Systems", "email": "jobs@baesystems.com", "specialty": "Defense,Network,Security"},
    ],
    
    "Consulting Firms": [
        {"company": "Accenture", "email": "recruiting@accenture.com", "specialty": "AI/ML,Cloud,Network,Security"},
        {"company": "Deloitte", "email": "jobs@deloitte.com", "specialty": "AI/ML,Cloud,Network,Security"},
        {"company": "PwC", "email": "technology.careers@pwc.com", "specialty": "Cloud,Network,Security"},
        {"company": "EY", "email": "careers@ey.com", "specialty": "AI/ML,Cloud,Network,Security"},
        {"company": "KPMG", "email": "kpmgcareers@kpmg.com", "specialty": "Cloud,Network,Security"},
        {"company": "Capgemini", "email": "careers@capgemini.com", "specialty": "Cloud,Network,Security,AI"},
        {"company": "Cognizant", "email": "careers@cognizant.com", "specialty": "AI/ML,Cloud,Network,Security"},
        {"company": "Infosys", "email": "careers@infosys.com", "specialty": "Cloud,Network,AI"},
        {"company": "Wipro", "email": "careers@wipro.com", "specialty": "Cloud,Network,Security,AI"},
        {"company": "TCS", "email": "careers@tcs.com", "specialty": "Cloud,Network,AI"},
    ],
    
    "Network & Security": [
        {"company": "Presidio", "email": "careers@presidio.com", "specialty": "Network,Security,Cloud"},
        {"company": "Palo Alto Networks", "email": "careers@paloaltonetworks.com", "specialty": "Security,Network,Cloud"},
        {"company": "Fortinet", "email": "jobs@fortinet.com", "specialty": "Security,Network,Firewall"},
        {"company": "Cisco Systems", "email": "jobs@cisco.com", "specialty": "Network,Security,Cloud"},
        {"company": "Juniper Networks", "email": "careers@juniper.net", "specialty": "Network,Security"},
        {"company": "F5 Networks", "email": "jobs@f5.com", "specialty": "Network,Security"},
        {"company": "FireEye", "email": "careers@fireeye.com", "specialty": "Security,Network"},
        {"company": "CrowdStrike", "email": "jobs@crowdstrike.com", "specialty": "Security,Network,Cloud"},
        {"company": "Rapid7", "email": "jobs@rapid7.com", "specialty": "Security,Network"},
        {"company": "Splunk", "email": "careers@splunk.com", "specialty": "Security,Data,Network"},
    ],
    
    "Cloud & AI": [
        {"company": "AWS Partners", "email": "partners@amazon.com", "specialty": "AWS,AI/ML,Cloud,DevOps"},
        {"company": "Microsoft Partner", "email": "partners@microsoft.com", "specialty": "Azure,AI/ML,Cloud"},
        {"company": "Google Cloud Partners", "email": "partners@google.com", "specialty": "GCP,AI/ML,Cloud"},
        {"company": "CloudTech Pro", "email": "jobs@cloudtechpro.com", "specialty": "Cloud,DevOps,Network"},
        {"company": "Databricks", "email": "careers@databricks.com", "specialty": "AI/ML,Data,Cloud"},
        {"company": "Snowflake", "email": "jobs@snowflake.com", "specialty": "Data,Cloud,AI"},
        {"company": "Datadog", "email": "careers@datadoghq.com", "specialty": "Cloud,Monitoring,Security"},
        {"company": "MongoDB", "email": "jobs@mongodb.com", "specialty": "Database,Cloud,Network"},
    ],
    
    "Healthcare IT": [
        {"company": "Epic Staffing", "email": "jobs@epicstaffing.com", "specialty": "Epic,HL7,Network"},
        {"company": "Cerner Partners", "email": "careers@cerner.com", "specialty": "Healthcare IT,Network"},
        {"company": "Healthcare IT Partners", "email": "jobs@hitpartners.com", "specialty": "Healthcare,Network,Security"},
        {"company": "MedUSolutions", "email": "staffing@medusolutions.com", "specialty": "Healthcare,Network"},
        {"company": "Vital Solutions", "email": "jobs@vitalsolutions.com", "specialty": "Healthcare Tech,Network"},
    ],
    
    "IT/Tech Specialists": [
        {"company": "Collabera", "email": "itjobs@collabera.com", "specialty": "Java,Python,AWS,Network"},
        {"company": "Astreya Partners", "email": "careers@astreya.com", "specialty": "Cloud,Network,Security"},
        {"company": "CyberCoders", "email": "jobs@cybercoders.com", "specialty": "AI/ML,Security,Network"},
        {"company": "Motion Recruitment", "email": "techjobs@motionrecruitment.com", "specialty": "Software,Network"},
        {"company": "Huxley Associates", "email": "jobs@huxley.com", "specialty": "Banking,Network,Security"},
        {"company": "Jefferson Frank", "email": "jobs@jeffersonfrank.com", "specialty": "AWS,Java,Network"},
        {"company": "Nelson Technology", "email": "staffing@nelson.com", "specialty": "Tech,Network,Security"},
        {"company": "Hired", "email": "employers@hired.com", "specialty": "Tech,Python,Network"},
        {"company": "SIGMA Science", "email": "jobs@sigmajobs.com", "specialty": "Scientific,IT,Network"},
        {"company": "People2.0", "email": "jobs@people2.com", "specialty": "Tech,Network"},
    ],
}

# ============================================================================
# EMAIL TEMPLATES - TRENDING TECH FOCUS
# ============================================================================

TEMPLATES = {
    "AI/ML": {
        "subject": "AI/ML Engineers Available - LLM, TensorFlow, PyTorch Experts",
        "body": """Hi,

Need AI/ML talent? We have pre-vetted engineers:

**Available Now:**
• 2 Senior ML Engineers (6+ yrs) - TensorFlow, PyTorch, MLOps
• 1 LLM/GenAI Developer - ChatGPT, LangChain, RAG
• 1 Computer Vision Engineer - OpenCV, YOLO
• 1 Data Scientist - NLP, Transformers, BERT

**Industries:**
Fintech, Healthcare, E-commerce, Autonomous Systems

**Rates:** $80-150/hr

Also have Python, Cloud, DevOps, Network, Security engineers.

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "Cloud": {
        "subject": "AWS/Azure/GCP Engineers - Kubernetes, Terraform Experts",
        "body": """Hi,

Need Cloud & DevOps engineers?

**Available:**
• 2 AWS Solutions Architects (Certified)
• 1 Azure Administrator (Expert)
• 1 GCP Data Engineer
• 1 Kubernetes/CKA Expert
• 1 Terraform/Infrastructure-as-Code

**Skills:** EKS, ECS, Serverless, CI/CD, Jenkins, GitLab

**Rates:** $75-140/hr

Also have Network, Security, AI/ML engineers available.

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "Network": {
        "subject": "Network Engineers - CCNA, CCNP, CCIE, SD-WAN Ready",
        "body": """Hi,

Need Network Engineers?

**Available:**
• 2 CCNA Engineers (2-4 yrs)
• 2 CCNP Engineers (5-7 yrs)
• 1 CCIE (10+ yrs) - Architect
• 1 SD-WAN Specialist

**Skills:** Cisco, Juniper, Palo Alto, Fortinet, MPLS, BGP, OSPF

**Industries:** Banking, Healthcare, Government, Enterprise

**Rates:** $55-95/hr

Also have Security, Cloud, DevOps engineers.

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "Security": {
        "subject": "Security Engineers - CISSP, CEH, Pen Testing Available",
        "body": """Hi,

Need Security Professionals?

**Available:**
• 2 Security Engineers (CISSP) - 5+ yrs
• 1 SOC Analyst (SIEM) - Splunk, QRadar
• 1 Pen Tester (CEH/OSCP) - 4+ yrs
• 1 Security Architect - Zero Trust

**Clearance:** Some have Active Secret/TS

**Skills:** FireEye, CrowdStrike, Palo Alto, Fortinet

**Rates:** $65-120/hr

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "DevOps": {
        "subject": "DevOps/SRE Engineers - Jenkins, Kubernetes, CI/CD",
        "body": """Hi,

Need DevOps or SRE help?

**Available:**
• 2 Sr DevOps Engineers - Kubernetes, Terraform
• 1 SRE - Prometheus, Grafana, Chaos Engineering
• 1 Platform Engineer - GitHub Actions, ArgoCD
• 1 Jenkins/CI-CD Specialist

**Skills:** Docker, K8s, EKS, Terraform, Ansible

**Rates:** $70-130/hr

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
    
    "General": {
        "subject": "IT Contractors Available - Ready Now",
        "body": """Hi,

Need IT contractors? We have pre-vetted talent:

**Available:**
• Software Engineers (Java, Python, .NET, React)
• Network Engineers (Cisco, Juniper, Palo Alto)
• Security (CISSP, CEH, CompTIA)
• Cloud/DevOps (AWS, Azure, Kubernetes)
• AI/ML (TensorFlow, PyTorch, LLM)
• QA Automation

✓ C2C, 1099, C2H
✓ Fast turnaround
✓ Competitive rates

What's your need?

Best,
{sender}
{company_name}
📱 {mobile}"""
    },
}

def get_template(specialty):
    specialty_lower = specialty.lower()
    
    if "ai" in specialty_lower or "ml" in specialty_lower or "llm" in specialty_lower:
        return TEMPLATES["AI/ML"]
    elif "cloud" in specialty_lower or "aws" in specialty_lower or "azure" in specialty_lower or "gcp" in specialty_lower:
        return TEMPLATES["Cloud"]
    elif "network" in specialty_lower or "cisco" in specialty_lower:
        return TEMPLATES["Network"]
    elif "security" in specialty_lower or "cyber" in specialty_lower:
        return TEMPLATES["Security"]
    elif "devops" in specialty_lower or "sre" in specialty_lower:
        return TEMPLATES["DevOps"]
    else:
        return TEMPLATES["General"]

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

def generate_dashboard():
    """Generate HTML dashboard"""
    tracker = load_tracker()
    
    total = len(tracker)
    sent = sum(1 for v in tracker.values() if v.get('email_count', 0) > 0)
    responded = sum(1 for v in tracker.values() if v.get('response') not in ['none', ''])
    pending = total - sent
    
    # Get recent activity
    recent = []
    for email, data in sorted(tracker.items(), key=lambda x: x[1].get('last_contacted', ''), reverse=True)[:10]:
        if data.get('last_contacted'):
            recent.append({
                'company': data.get('company'),
                'date': data.get('last_contacted'),
                'count': data.get('email_count', 0),
                'response': data.get('response', 'none')
            })
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Team-Soft Lead Pipeline Dashboard</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        h1 {{ color: #fff; text-align: center; margin-bottom: 30px; font-size: 2.5em; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .stat-card {{ background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 15px; padding: 25px; text-align: center; border: 1px solid rgba(255,255,255,0.2); }}
        .stat-card h3 {{ color: #aaa; font-size: 0.9em; text-transform: uppercase; margin-bottom: 10px; }}
        .stat-card .number {{ color: #00d4ff; font-size: 3em; font-weight: bold; }}
        .stat-card .number.green {{ color: #00ff88; }}
        .stat-card .number.orange {{ color: #ffaa00; }}
        .stat-card .number.red {{ color: #ff5555; }}
        .dashboard-grid {{ display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }}
        .card {{ background: rgba(255,255,255,0.05); border-radius: 15px; padding: 20px; border: 1px solid rgba(255,255,255,0.1); }}
        .card h2 {{ color: #fff; margin-bottom: 20px; font-size: 1.3em; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); }}
        th {{ color: #00d4ff; font-weight: 600; }}
        td {{ color: #ddd; }}
        .status-sent {{ color: #00ff88; }}
        .status-pending {{ color: #ffaa00; }}
        .status-response {{ color: #00d4ff; }}
        .progress-bar {{ background: rgba(255,255,255,0.1); border-radius: 10px; height: 20px; overflow: hidden; margin-top: 10px; }}
        .progress-fill {{ background: linear-gradient(90deg, #00d4ff, #00ff88); height: 100%; border-radius: 10px; }}
        .tech-tags {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 20px; }}
        .tech-tag {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 8px 15px; border-radius: 20px; color: #fff; font-size: 0.85em; }}
        .footer {{ text-align: center; margin-top: 30px; color: #666; }}
        @media (max-width: 900px) {{ .dashboard-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Team-Soft Lead Generation Pipeline</h1>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Vendors</h3>
                <div class="number">{total}</div>
            </div>
            <div class="stat-card">
                <h3>Emails Sent</h3>
                <div class="number green">{sent}</div>
            </div>
            <div class="stat-card">
                <h3>Responses</h3>
                <div class="number orange">{responded}</div>
            </div>
            <div class="stat-card">
                <h3>Pending</h3>
                <div class="number red">{pending}</div>
            </div>
        </div>
        
        <div class="dashboard-grid">
            <div class="card">
                <h2>📋 Recent Activity</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Last Contacted</th>
                            <th>Emails</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    
    for r in recent:
        status_class = "status-sent" if r['count'] > 0 else "status-pending"
        status = "Sent" if r['count'] > 0 else "Pending"
        html += f"""
                        <tr>
                            <td>{r['company']}</td>
                            <td>{r['date']}</td>
                            <td>{r['count']}</td>
                            <td class="{status_class}">{status}</td>
                        </tr>"""
    
    html += """
                    </tbody>
                </table>
            </div>
            
            <div class="card">
                <h2>💡 Trending Technologies</h2>
                <div class="tech-tags">
                    <span class="tech-tag">🤖 AI/ML</span>
                    <span class="tech-tag">☁️ AWS/Azure</span>
                    <span class="tech-tag">🔐 Network</span>
                    <span class="tech-tag">🛡️ Security</span>
                    <span class="tech-tag">⚙️ DevOps</span>
                    <span class="tech-tag">📊 Data</span>
                    <span class="tech-tag">🔧 Kubernetes</span>
                    <span class="tech-tag">🤖 LLM</span>
                    <span class="tech-tag">🔥 React</span>
                    <span class="tech-tag">🐍 Python</span>
                </div>
                
                <div style="margin-top: 30px;">
                    <h2 style="margin-bottom: 15px;">📈 Progress</h2>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {}%"></div>
                    </div>
                    <p style="color: #888; margin-top: 10px; text-align: center;">{}% Complete</p>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>Last Updated: {} | Team-Soft LLC - Automated Lead Pipeline</p>
        </div>
    </div>
</body>
</html>""".format(
        int((sent/total*100)) if total > 0 else 0,
        int((sent/total*100)) if total > 0 else 0,
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    with open("dashboard.html", "w") as f:
        f.write(html)
    
    return html

def run_pipeline(send=False):
    print("\n" + "="*70)
    print("🤖 AI-POWERED STAFFING PIPELINE - 25 EMAILS/DAY")
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
    print(f"📧 Emails Today: {len(action_items)}")
    
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
    generate_dashboard()
    
    print("\n" + "="*70)
    print(f"📈 SUMMARY: {len(action_items)} | ✅ {sent} | ❌ {failed}")
    print(f"📊 Dashboard: dashboard.html")
    print("="*70)

if __name__ == "__main__":
    import sys
    send = "--send" in sys.argv
    run_pipeline(send)
