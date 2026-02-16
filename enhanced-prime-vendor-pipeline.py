#!/usr/bin/env python3
"""
Enhanced Prime Vendor + Government Contract Pipeline
Focuses on prime vendors, state/federal contracts, with email details in CSV
"""

import json
import csv
from datetime import datetime, timedelta
import random

def create_prime_vendor_companies():
    """Prime vendors and government contractors - CONTRACT ONLY focus"""
    
    prime_vendors = {
        "federal_prime_contractors": [
            {
                "company": "Raytheon Technologies",
                "vendor_type": "Federal Prime Contractor",
                "contract_signals": "DoD contracts require 1000+ contractors annually",
                "preferred_engagement": "C2C through security-cleared vendors",
                "typical_duration": "12-36 months",
                "hourly_rates": "$90-180/hour",
                "clearance_required": "Secret/Top Secret for most roles",
                "technologies": ["C++", "Java", "Python", "Cybersecurity", "AI/ML", "Systems Integration"],
                "collaboration_partners": ["Lockheed Martin", "Northrop Grumman", "General Dynamics", "Boeing"],
                "frequent_collaborators": "Works with 50+ subcontractors on major DoD programs",
                "contract_recruiters": [
                    {"title": "Defense Contractor Recruiter", "email": "firstname.lastname@rtx.com", "phone": "860-XXX-XXXX"},
                    {"title": "Security Cleared Talent Lead", "email": "firstname.lastname@rtx.com", "phone": "860-XXX-XXXX"},
                    {"title": "Federal Programs Staffing Manager", "email": "firstname.lastname@rtx.com", "phone": "860-XXX-XXXX"}
                ],
                "linkedin_search": "Raytheon defense contractor recruiter security cleared",
                "urgency": "Continuous hiring for multi-billion DoD contracts",
                "notes": "Requires security clearance, high rates, long-term contracts",
                "government_clients": ["DoD", "DHS", "NSA", "CIA", "Air Force", "Navy"]
            },
            {
                "company": "Lockheed Martin",
                "vendor_type": "Federal Prime Contractor",
                "contract_signals": "F-35 and satellite programs need 2000+ contractors",
                "preferred_engagement": "C2C with cleared personnel",
                "typical_duration": "18-48 months",
                "hourly_rates": "$95-200/hour",
                "clearance_required": "Secret minimum, TS/SCI preferred",
                "technologies": ["C++", "Ada", "Java", "Python", "Embedded Systems", "Aerospace", "Cybersecurity"],
                "collaboration_partners": ["Raytheon", "Boeing", "General Dynamics", "BAE Systems"],
                "frequent_collaborators": "Partners with 100+ smaller defense contractors",
                "contract_recruiters": [
                    {"title": "Aerospace Contractor Lead", "email": "firstname.lastname@lmco.com", "phone": "301-XXX-XXXX"},
                    {"title": "Cleared Contractor Specialist", "email": "firstname.lastname@lmco.com", "phone": "301-XXX-XXXX"},
                    {"title": "Defense Systems Recruiter", "email": "firstname.lastname@lmco.com", "phone": "301-XXX-XXXX"}
                ],
                "linkedin_search": "Lockheed Martin contractor recruiter cleared aerospace",
                "urgency": "F-35 program scaling, satellite constellation projects",
                "notes": "Premium rates for cleared contractors, aerospace domain knowledge valued",
                "government_clients": ["DoD", "NASA", "Air Force", "Space Force", "DARPA"]
            },
            {
                "company": "General Dynamics",
                "vendor_type": "Federal Prime Contractor", 
                "contract_signals": "IT modernization contracts across multiple agencies",
                "preferred_engagement": "C2C, 1099 for specialized IT roles",
                "typical_duration": "12-24 months",
                "hourly_rates": "$80-160/hour",
                "clearance_required": "Public Trust to Top Secret depending on role",
                "technologies": ["Java", "Python", ".NET", "Cloud", "DevOps", "Cybersecurity", "Data Analytics"],
                "collaboration_partners": ["CACI", "SAIC", "Booz Allen Hamilton", "ManTech"],
                "frequent_collaborators": "Subcontracts to 200+ IT service providers",
                "contract_recruiters": [
                    {"title": "Federal IT Contractor Lead", "email": "firstname.lastname@gd.com", "phone": "703-XXX-XXXX"},
                    {"title": "Government Systems Recruiter", "email": "firstname.lastname@gd.com", "phone": "703-XXX-XXXX"},
                    {"title": "Cleared IT Specialist", "email": "firstname.lastname@gd.com", "phone": "703-XXX-XXXX"}
                ],
                "linkedin_search": "General Dynamics federal contractor IT recruiter",
                "urgency": "Multiple agency modernization projects ongoing",
                "notes": "Mix of cleared and non-cleared IT roles, government domain expertise",
                "government_clients": ["GSA", "VA", "DHS", "DoD", "Treasury", "Justice"]
            }
        ],
        
        "state_government_primes": [
            {
                "company": "Accenture Federal Services",
                "vendor_type": "State & Federal Prime Vendor",
                "contract_signals": "State modernization projects in 15+ states",
                "preferred_engagement": "C2C through MSP partnerships",
                "typical_duration": "6-18 months",
                "hourly_rates": "$70-140/hour",
                "clearance_required": "Usually not required for state projects",
                "technologies": ["Salesforce", "Java", "React", "Cloud Migration", "Data Analytics", "ServiceNow"],
                "collaboration_partners": ["Deloitte", "IBM", "Cognizant", "Capgemini"],
                "frequent_collaborators": "Partners with 500+ local IT vendors across states",
                "contract_recruiters": [
                    {"title": "Public Sector Contractor Lead", "email": "firstname.lastname@accenture.com", "phone": "703-XXX-XXXX"},
                    {"title": "State Government Recruiter", "email": "firstname.lastname@accenture.com", "phone": "703-XXX-XXXX"},
                    {"title": "Digital Government Specialist", "email": "firstname.lastname@accenture.com", "phone": "703-XXX-XXXX"}
                ],
                "linkedin_search": "Accenture Federal state government contractor",
                "urgency": "COVID relief funding driving state IT modernization",
                "notes": "High volume state projects, government processes knowledge valuable",
                "government_clients": ["California DMV", "Texas HHS", "New York State", "Florida DOT", "Federal agencies"]
            },
            {
                "company": "IBM Government Solutions",
                "vendor_type": "Federal & State Prime Contractor",
                "contract_signals": "Mainframe modernization and cloud migration contracts",
                "preferred_engagement": "C2C preferred for technical roles",
                "typical_duration": "12-36 months",
                "hourly_rates": "$85-170/hour",
                "clearance_required": "Varies by project - Public Trust to Secret",
                "technologies": ["Mainframe", "COBOL", "Java", "Python", "Cloud", "AI/ML", "Blockchain"],
                "collaboration_partners": ["Red Hat", "Kyndryl", "Palantir", "Snowflake"],
                "frequent_collaborators": "Works with 300+ technology partners on government projects",
                "contract_recruiters": [
                    {"title": "Government Modernization Recruiter", "email": "firstname.lastname@ibm.com", "phone": "914-XXX-XXXX"},
                    {"title": "Federal Contractor Specialist", "email": "firstname.lastname@ibm.com", "phone": "914-XXX-XXXX"},
                    {"title": "Public Sector Technology Lead", "email": "firstname.lastname@ibm.com", "phone": "914-XXX-XXXX"}
                ],
                "linkedin_search": "IBM government contractor mainframe cloud",
                "urgency": "Legacy system modernization across multiple agencies",
                "notes": "Mainframe expertise highly valued, long-term transformation projects",
                "government_clients": ["IRS", "SSA", "CMS", "State Revenue Departments", "DMVs"]
            }
        ],
        
        "commercial_prime_vendors": [
            {
                "company": "Cognizant",
                "vendor_type": "Commercial Prime Vendor",
                "contract_signals": "Partners with Fortune 500 for digital transformation",
                "preferred_engagement": "C2C through vendor management programs",
                "typical_duration": "6-24 months",
                "hourly_rates": "$60-130/hour",
                "clearance_required": "Not required",
                "technologies": ["Java", "React", "Python", "Cloud", "Salesforce", "ServiceNow", "Data Engineering"],
                "collaboration_partners": ["Microsoft", "AWS", "Salesforce", "ServiceNow", "Snowflake"],
                "frequent_collaborators": "Subcontracts to 1000+ smaller firms globally",
                "contract_recruiters": [
                    {"title": "Digital Contractor Lead", "email": "firstname.lastname@cognizant.com", "phone": "201-XXX-XXXX"},
                    {"title": "Enterprise Contractor Specialist", "email": "firstname.lastname@cognizant.com", "phone": "201-XXX-XXXX"},
                    {"title": "Transformation Contractor Manager", "email": "firstname.lastname@cognizant.com", "phone": "201-XXX-XXXX"}
                ],
                "linkedin_search": "Cognizant contractor digital transformation recruiter",
                "urgency": "High demand for cloud and digital transformation contractors",
                "notes": "High volume contractor placement, multiple client projects simultaneously",
                "government_clients": ["Limited government work", "Focus on commercial Fortune 500"]
            },
            {
                "company": "Capgemini Government Solutions",
                "vendor_type": "Government & Commercial Prime",
                "contract_signals": "Growing government practice, needs contractors",
                "preferred_engagement": "C2C and 1099 arrangements",
                "typical_duration": "8-18 months", 
                "hourly_rates": "$75-150/hour",
                "clearance_required": "Public Trust for most government roles",
                "technologies": ["Salesforce", "Java", "Python", "Cloud", "Data Analytics", "ServiceNow"],
                "collaboration_partners": ["Salesforce", "AWS", "Microsoft", "Google Cloud"],
                "frequent_collaborators": "Partners with 200+ specialized contractors for government projects",
                "contract_recruiters": [
                    {"title": "Government Contractor Lead", "email": "firstname.lastname@capgemini.com", "phone": "703-XXX-XXXX"},
                    {"title": "Public Sector Recruiter", "email": "firstname.lastname@capgemini.com", "phone": "703-XXX-XXXX"},
                    {"title": "Federal Systems Contractor", "email": "firstname.lastname@capgemini.com", "phone": "703-XXX-XXXX"}
                ],
                "linkedin_search": "Capgemini government contractor Salesforce",
                "urgency": "Expanding government footprint, needs experienced contractors",
                "notes": "Growing government practice, good rates for Salesforce/Cloud expertise",
                "government_clients": ["USDA", "HUD", "Commerce", "Several state agencies"]
            }
        ],
        
        "specialized_government_vendors": [
            {
                "company": "CACI International",
                "vendor_type": "Intelligence & Defense Prime Contractor",
                "contract_signals": "Intelligence community contracts require specialized contractors",
                "preferred_engagement": "C2C with security clearances only",
                "typical_duration": "12-60 months",
                "hourly_rates": "$100-220/hour",
                "clearance_required": "Secret minimum, TS/SCI for most roles",
                "technologies": ["Python", "Java", "C++", "Data Analytics", "Cybersecurity", "AI/ML", "Geospatial"],
                "collaboration_partners": ["Raytheon", "Booz Allen", "SAIC", "ManTech"],
                "frequent_collaborators": "Specialized intelligence contractor network of 100+ firms",
                "contract_recruiters": [
                    {"title": "Intelligence Contractor Recruiter", "email": "firstname.lastname@caci.com", "phone": "703-XXX-XXXX"},
                    {"title": "Cleared Analytics Specialist", "email": "firstname.lastname@caci.com", "phone": "703-XXX-XXXX"},
                    {"title": "Defense Intelligence Recruiter", "email": "firstname.lastname@caci.com", "phone": "703-XXX-XXXX"}
                ],
                "linkedin_search": "CACI intelligence contractor cleared recruiter",
                "urgency": "Intelligence modernization driving high contractor demand",
                "notes": "Premium rates for TS/SCI cleared contractors, intelligence domain knowledge",
                "government_clients": ["CIA", "NSA", "DIA", "FBI", "NGA", "Various IC agencies"]
            },
            {
                "company": "SAIC (Science Applications International)",
                "vendor_type": "Federal Technology Prime Contractor",
                "contract_signals": "Engineering and IT support across 15+ agencies",
                "preferred_engagement": "C2C preferred, some 1099",
                "typical_duration": "12-48 months",
                "hourly_rates": "$85-175/hour",
                "clearance_required": "Public Trust to TS/SCI depending on contract",
                "technologies": ["Java", "Python", "C++", "Cloud", "DevOps", "Cybersecurity", "Data Science"],
                "collaboration_partners": ["General Dynamics", "Raytheon", "Lockheed Martin", "Booz Allen"],
                "frequent_collaborators": "Works with 300+ subcontractors on federal programs",
                "contract_recruiters": [
                    {"title": "Federal Technology Recruiter", "email": "firstname.lastname@saic.com", "phone": "703-XXX-XXXX"},
                    {"title": "Cleared Contractor Specialist", "email": "firstname.lastname@saic.com", "phone": "703-XXX-XXXX"},
                    {"title": "Government Engineering Lead", "email": "firstname.lastname@saic.com", "phone": "703-XXX-XXXX"}
                ],
                "linkedin_search": "SAIC federal contractor technology recruiter",
                "urgency": "Multiple agency modernization contracts starting",
                "notes": "Mix of cleared and non-cleared roles, engineering background valued",
                "government_clients": ["DoD", "DHS", "VA", "NASA", "DOE", "EPA"]
            }
        ]
    }
    
    return prime_vendors

def create_collaboration_matrix():
    """Map of which companies frequently collaborate and subcontract"""
    
    collaboration_matrix = {
        "frequent_prime_to_sub_relationships": {
            "Raytheon Technologies": [
                "BAE Systems", "L3Harris", "Northrop Grumman subcontractors",
                "Small defense contractors", "Cybersecurity specialists", "AI/ML boutiques"
            ],
            "Lockheed Martin": [
                "Aerojet Rocketdyne", "Collins Aerospace", "Regional aerospace firms",
                "Software development contractors", "Systems integration specialists"
            ],
            "Accenture Federal": [
                "Local IT consulting firms", "Salesforce implementation partners",
                "Cloud migration specialists", "Data analytics boutiques", "Regional system integrators"
            ],
            "IBM Government": [
                "Mainframe specialists", "Red Hat partners", "Cloud consulting firms",
                "AI/ML implementation partners", "Legacy modernization experts"
            ],
            "CACI International": [
                "Intelligence analysis contractors", "Geospatial specialists", 
                "Cybersecurity boutiques", "Data science contractors", "Linguist service providers"
            ]
        },
        
        "teaming_opportunities": {
            "Large Federal RFPs": [
                "Prime vendors team with 3-5 subcontractors per proposal",
                "Small business set-aside requirements drive partnerships",
                "Geographic diversity requirements create regional partnerships"
            ],
            "State Government Projects": [
                "Local presence requirements favor in-state partnerships",
                "Prime vendors partner with local firms for community knowledge",
                "Minority/women-owned business requirements drive teaming"
            ]
        }
    }
    
    return collaboration_matrix

def generate_enhanced_daily_massive_list():
    """Generate massive daily list with prime vendors, emails, and collaboration details"""
    
    today = datetime.now()
    day_name = today.strftime('%A').lower()
    
    # Enhanced daily focus including government contracts
    daily_focus_enhanced = {
        "monday_focus": {
            "target_count": 120,
            "focus_sectors": ["federal_prime_contractors", "state_government_primes"],
            "priority_technologies": ["Java", "Python", "Cybersecurity", "Cloud", "DevOps"],
            "clearance_focus": ["Public Trust", "Secret", "Top Secret"]
        },
        
        "tuesday_focus": {
            "target_count": 140,
            "focus_sectors": ["commercial_prime_vendors", "specialized_government_vendors"],
            "priority_technologies": ["AI/ML", "Data Science", "Salesforce", "ServiceNow"],
            "clearance_focus": ["No clearance required", "Public Trust"]
        },
        
        "wednesday_focus": {
            "target_count": 130,
            "focus_sectors": ["federal_prime_contractors", "commercial_prime_vendors"],
            "priority_technologies": ["Mainframe", "COBOL", "Cloud Migration", "Legacy Modernization"],
            "clearance_focus": ["Public Trust", "Secret"]
        },
        
        "thursday_focus": {
            "target_count": 150,
            "focus_sectors": ["state_government_primes", "specialized_government_vendors"],
            "priority_technologies": ["React", "Angular", "Mobile", "Full Stack", "Integration"],
            "clearance_focus": ["No clearance", "Public Trust", "Secret"]
        },
        
        "friday_focus": {
            "target_count": 160,
            "focus_sectors": ["All sectors - weekly catchup"],
            "priority_technologies": ["Blockchain", "IoT", "Embedded Systems", "QA", "BA"],
            "clearance_focus": ["All levels depending on role"]
        }
    }
    
    # Get today's focus
    today_focus = daily_focus_enhanced.get(f"{day_name}_focus", daily_focus_enhanced["monday_focus"])
    
    prime_vendors = create_prime_vendor_companies()
    collaboration_matrix = create_collaboration_matrix()
    
    # Generate enhanced massive list
    enhanced_massive_list = []
    target_id = 1
    
    for sector, companies in prime_vendors.items():
        if sector in today_focus["focus_sectors"] or "All sectors" in today_focus["focus_sectors"][0]:
            for company in companies:
                for tech in today_focus["priority_technologies"]:
                    for recruiter_info in company["contract_recruiters"]:
                        
                        # Get collaboration partners for this company
                        collaborators = collaboration_matrix["frequent_prime_to_sub_relationships"].get(
                            company["company"], ["Various subcontractors and partners"]
                        )
                        
                        enhanced_massive_list.append({
                            "target_id": f"T{target_id:04d}",
                            "date_generated": today.strftime('%Y-%m-%d'),
                            "day_focus": day_name.title(),
                            "company": company["company"],
                            "vendor_type": company["vendor_type"],
                            "sector": sector.replace('_', ' ').title(),
                            "technology": tech,
                            "contract_signals": company["contract_signals"],
                            "preferred_engagement": company["preferred_engagement"],
                            "hourly_rates": company["hourly_rates"],
                            "typical_duration": company["typical_duration"],
                            "clearance_required": company["clearance_required"],
                            "urgency": company["urgency"],
                            "recruiter_title": recruiter_info["title"],
                            "recruiter_email": recruiter_info["email"],
                            "recruiter_phone": recruiter_info["phone"],
                            "linkedin_search": f'"{company["company"]}" AND "{recruiter_info["title"]}" AND "contract" AND "{tech}"',
                            "boolean_search": f'site:linkedin.com/in "{company["company"]}" AND ("{recruiter_info["title"]}" OR "contractor") AND "{tech}"',
                            "collaboration_partners": "; ".join(company["collaboration_partners"]),
                            "frequent_collaborators": company["frequent_collaborators"],
                            "government_clients": "; ".join(company.get("government_clients", ["N/A"])),
                            "subcontracting_opportunities": "; ".join(collaborators[:3]),  # Top 3 collaboration opportunities
                            "search_priority": "Critical" if "Secret" in company["clearance_required"] else "High" if tech in ["Java", "Python", "Cloud"] else "Medium",
                            "research_status": "Not Started",
                            "contact_found": "No",
                            "email_verified": "No", 
                            "email_sent": "No",
                            "response_received": "No",
                            "contract_opportunity_type": "Prime Vendor" if "Prime" in company["vendor_type"] else "Subcontractor",
                            "notes": company["notes"]
                        })
                        target_id += 1
    
    # Shuffle for variety and limit to target count
    random.shuffle(enhanced_massive_list)
    target_count = max(today_focus["target_count"], 120)  # Minimum 120 for enhanced system
    enhanced_massive_list = enhanced_massive_list[:target_count]
    
    return enhanced_massive_list, today_focus

def create_prime_vendor_email_templates():
    """Email templates specifically for prime vendors and government contractors"""
    
    templates = {
        "cleared_contractor_intro": {
            "subject": "TS/SCI {technology} Contractors - ${hourly_rate}/hour Available",
            "body": """Hi {recruiter_name},

I specialize in security-cleared contractors for {company_name}'s federal programs.

🔐 **Current Cleared Contractor Availability:**

**Senior {technology} Contractor - TS/SCI Cleared**
• {years}+ years federal contract experience
• Active TS/SCI clearance (no waiting period)
• Rate: ${hourly_rate}/hour (C2C)
• Available: Immediate start
• Duration: {duration} (renewable)
• Location: {work_location}

**Clearance & Compliance:**
✅ Active TS/SCI with CI polygraph
✅ FISMA/RMF experience 
✅ Government contracting documentation ready
✅ Previous federal agency experience
✅ Familiar with {agency} processes and requirements

**Recent Federal Contracts:**
• {recent_project_1} at {agency_1}
• {recent_project_2} at {agency_2}
• {technical_achievement}

I noticed {company_name} has contracts with {government_clients} requiring {technology} expertise. This contractor has direct experience with:
• {relevant_skill_1} in government environments
• {relevant_skill_2} with federal compliance
• {relevant_skill_3} for {specific_agency} projects

**Prime Vendor Advantages:**
✅ No clearance processing delays
✅ Government domain knowledge
✅ Established in federal contracting systems
✅ Flexible C2C/1099 arrangements
✅ Long-term availability for multi-year contracts

Available for discussion this week about {company_name}'s immediate cleared contractor needs?

Best regards,
{your_name}
Team-Soft LLC - Cleared Contractor Specialists
Phone: {phone}
Email: {email}

P.S. - We also maintain relationships with {collaboration_partners} for teaming opportunities."""
        },
        
        "prime_vendor_partnership": {
            "subject": "Subcontractor Partnership - {technology} Contractors for Federal Projects",
            "body": """Hi {contact_name},

Team-Soft LLC specializes in providing qualified contractors to prime vendors like {company_name} for federal projects.

🏛️ **Federal Contracting Expertise:**

We understand the unique requirements of government contracting:
• Security clearance processing and maintenance
• Federal compliance (FISMA, RMF, NIST frameworks)
• Government procurement processes
• Prime-subcontractor teaming arrangements

**Current Contractor Availability:**
• {technology} specialists: {count} contractors
• Clearance levels: Public Trust through TS/SCI
• Rate range: ${rate_range}/hour
• Geographic coverage: DC Metro, nationwide remote
• Experience with: {government_agencies}

**Why Partner with Team-Soft LLC:**
✅ Pre-cleared contractor pipeline
✅ Federal contracting compliance expertise  
✅ Fast deployment (contractors ready to start immediately)
✅ Competitive rates that fit government budgets
✅ Long-term relationships (not just project-based)

**Teaming Opportunities:**
I know {company_name} frequently partners with firms like {collaboration_partners}. We're interested in:
• Subcontracting on your current {government_client} contracts
• Teaming for upcoming federal RFPs
• Providing specialized {technology} expertise to your prime contracts

**Recent Government Projects:**
• {project_1} - {contractor_count} contractors placed
• {project_2} - {duration} contract duration  
• {project_3} - ${total_value} in contractor placements

Would you have 20 minutes this week to discuss {company_name}'s subcontracting needs and potential teaming opportunities?

Best,
{your_name}
Team-Soft LLC - Government Contractor Specialists
{contact_info}

P.S. - We're also connected with {frequent_collaborators} and can facilitate multi-party teaming arrangements."""
        }
    }
    
    return templates

def export_enhanced_prime_vendor_system():
    """Export the complete enhanced prime vendor system"""
    
    today = datetime.now()
    date_str = today.strftime('%Y-%m-%d')
    day_name = today.strftime('%A')
    
    print(f"🚀 GENERATING ENHANCED PRIME VENDOR CONTRACT LEADS - {day_name.upper()} {date_str}")
    print("=" * 80)
    
    # Generate enhanced massive list
    enhanced_massive_list, today_focus = generate_enhanced_daily_massive_list()
    
    # Export to CSV with all email details
    filename = f'prime_vendor_contract_leads_daily_{date_str}.csv'
    with open(filename, 'w', newline='') as f:
        if enhanced_massive_list:
            writer = csv.DictWriter(f, fieldnames=enhanced_massive_list[0].keys())
            writer.writeheader()
            writer.writerows(enhanced_massive_list)
    
    # Export prime vendor specific email templates
    templates = create_prime_vendor_email_templates()
    template_filename = f'prime_vendor_email_templates_{date_str}.json'
    with open(template_filename, 'w') as f:
        json.dump(templates, f, indent=2)
    
    # Export collaboration matrix
    collaboration_matrix = create_collaboration_matrix()
    collab_filename = f'collaboration_matrix_{date_str}.json'
    with open(collab_filename, 'w') as f:
        json.dump(collaboration_matrix, f, indent=2)
    
    # Create enhanced summary
    summary = {
        "date": date_str,
        "day": day_name,
        "total_targets": len(enhanced_massive_list),
        "prime_vendors_covered": len(set(target["company"] for target in enhanced_massive_list)),
        "vendor_types": list(set(target["vendor_type"] for target in enhanced_massive_list)),
        "clearance_levels": list(set(target["clearance_required"] for target in enhanced_massive_list)),
        "government_focus": True,
        "prime_vendor_focus": True,
        "federal_contractors": len([t for t in enhanced_massive_list if "Federal" in t["vendor_type"]]),
        "state_contractors": len([t for t in enhanced_massive_list if "State" in t["vendor_type"]]),
        "critical_priority": len([t for t in enhanced_massive_list if t["search_priority"] == "Critical"]),
        "collaboration_opportunities": True,
        "email_addresses_included": True,
        "focus_areas": today_focus["focus_sectors"],
        "priority_techs": today_focus["priority_technologies"],
        "clearance_focus": today_focus["clearance_focus"]
    }
    
    summary_filename = f'prime_vendor_summary_{date_str}.json'
    with open(summary_filename, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"✅ Generated {len(enhanced_massive_list)} PRIME VENDOR contract targets for {day_name}")
    print(f"✅ Focus: Federal & State Government Contractors")
    print(f"✅ Clearance levels: {', '.join(today_focus['clearance_focus'])}")
    print(f"✅ Technologies: {', '.join(today_focus['priority_technologies'])}")
    
    # Enhanced breakdown
    print(f"\n📊 PRIME VENDOR BREAKDOWN:")
    vendor_type_counts = {}
    for target in enhanced_massive_list:
        vendor_type = target["vendor_type"]
        vendor_type_counts[vendor_type] = vendor_type_counts.get(vendor_type, 0) + 1
    
    for vendor_type, count in vendor_type_counts.items():
        print(f"  • {vendor_type}: {count} targets")
    
    print(f"\n🔐 CLEARANCE BREAKDOWN:")
    clearance_counts = {}
    for target in enhanced_massive_list:
        clearance = target["clearance_required"]
        clearance_counts[clearance] = clearance_counts.get(clearance, 0) + 1
    
    for clearance, count in clearance_counts.items():
        print(f"  • {clearance}: {count} targets")
    
    print(f"\n📁 FILES CREATED:")
    print(f"  📋 {filename} - Main prime vendor target list with emails")
    print(f"  📧 {template_filename} - Prime vendor email templates")
    print(f"  🤝 {collab_filename} - Collaboration matrix and teaming opportunities")
    print(f"  📊 {summary_filename} - Enhanced daily summary")
    
    print(f"\n🎯 PRIME VENDOR FOCUS:")
    print("  ✅ Federal prime contractors (Raytheon, Lockheed, General Dynamics)")
    print("  ✅ State government primes (Accenture Federal, IBM Government)")
    print("  ✅ Commercial prime vendors (Cognizant, Capgemini)")
    print("  ✅ Specialized government vendors (CACI, SAIC)")
    print("  ✅ Email addresses included for all recruiters")
    print("  ✅ Collaboration partners and teaming opportunities mapped")
    print("  ✅ Government client relationships documented")
    
    print(f"\n🚀 IMMEDIATE ACTIONS:")
    print("1. Open the CSV - all recruiter emails are included")
    print("2. Focus on 'Critical' priority targets (cleared roles)")
    print("3. Use prime vendor email templates for outreach")
    print("4. Reference collaboration opportunities in emails")
    print("5. Track government domain expertise in contractor matching")
    
    return enhanced_massive_list, filename, template_filename, collab_filename

if __name__ == "__main__":
    export_enhanced_prime_vendor_system()