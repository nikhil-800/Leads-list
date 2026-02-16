#!/usr/bin/env python3
"""
Balanced Prime Vendor Pipeline - Mix of ALL Types
Private prime vendors, government prime vendors, commercial contractors
Focus on IT contractor opportunities across all industries
"""

import json
import csv
from datetime import datetime, timedelta
import random

def create_balanced_prime_vendors():
    """Balanced mix of private, government, and commercial prime vendors"""
    
    balanced_prime_vendors = {
        "private_consulting_primes": [
            {
                "company": "Accenture",
                "vendor_type": "Global Consulting Prime Vendor",
                "contract_signals": "2000+ contractors across Fortune 500 clients",
                "preferred_engagement": "C2C through MSP, 1099 for specialized roles",
                "typical_duration": "6-18 months",
                "hourly_rates": "$70-140/hour",
                "clearance_required": "Not required for most roles",
                "technologies": ["Salesforce", "Java", "React", "Cloud", "Data Analytics", "ServiceNow"],
                "collaboration_partners": ["Microsoft", "AWS", "Salesforce", "ServiceNow"],
                "frequent_collaborators": "Partners with 500+ boutique firms globally",
                "contract_recruiters": [
                    {"title": "Enterprise Contractor Lead", "email": "firstname.lastname@accenture.com", "phone": "312-XXX-XXXX"},
                    {"title": "Technology Contractor Specialist", "email": "firstname.lastname@accenture.com", "phone": "312-XXX-XXXX"},
                    {"title": "Digital Contractor Manager", "email": "firstname.lastname@accenture.com", "phone": "312-XXX-XXXX"}
                ],
                "linkedin_search": "Accenture contractor technology recruiter",
                "urgency": "Continuous Fortune 500 client project demands",
                "notes": "High volume contractor placement across multiple industries",
                "clients": ["Fortune 500 companies", "Banking", "Healthcare", "Retail", "Manufacturing"]
            },
            {
                "company": "Deloitte Consulting",
                "vendor_type": "Big 4 Consulting Prime Vendor",
                "contract_signals": "1500+ contractors for client transformation projects",
                "preferred_engagement": "C2C preferred, 1099 for specialists",
                "typical_duration": "8-24 months",
                "hourly_rates": "$80-160/hour",
                "clearance_required": "Not required for commercial projects",
                "technologies": ["SAP", "Oracle", "Salesforce", "Cloud Migration", "Data Analytics"],
                "collaboration_partners": ["SAP", "Oracle", "Microsoft", "Google Cloud"],
                "frequent_collaborators": "Works with 300+ implementation specialists",
                "contract_recruiters": [
                    {"title": "Consulting Contractor Lead", "email": "firstname.lastname@deloitte.com", "phone": "212-XXX-XXXX"},
                    {"title": "Transformation Contractor Specialist", "email": "firstname.lastname@deloitte.com", "phone": "212-XXX-XXXX"},
                    {"title": "Enterprise Solutions Recruiter", "email": "firstname.lastname@deloitte.com", "phone": "212-XXX-XXXX"}
                ],
                "linkedin_search": "Deloitte contractor SAP Oracle recruiter",
                "urgency": "Digital transformation projects across industries",
                "notes": "Premium rates for enterprise software expertise",
                "clients": ["Fortune 1000", "Financial Services", "Healthcare", "Energy", "Consumer Products"]
            },
            {
                "company": "IBM Consulting",
                "vendor_type": "Technology Services Prime Vendor",
                "contract_signals": "3000+ contractors for hybrid cloud and AI projects",
                "preferred_engagement": "C2C through vendor programs",
                "typical_duration": "12-36 months",
                "hourly_rates": "$75-150/hour",
                "clearance_required": "Not required for commercial clients",
                "technologies": ["IBM Cloud", "Red Hat", "AI/ML", "Hybrid Cloud", "Mainframe", "Java"],
                "collaboration_partners": ["Red Hat", "AWS", "Microsoft", "Palantir"],
                "frequent_collaborators": "Global network of 1000+ technology partners",
                "contract_recruiters": [
                    {"title": "Hybrid Cloud Contractor Lead", "email": "firstname.lastname@ibm.com", "phone": "914-XXX-XXXX"},
                    {"title": "AI Contractor Specialist", "email": "firstname.lastname@ibm.com", "phone": "914-XXX-XXXX"},
                    {"title": "Enterprise Modernization Recruiter", "email": "firstname.lastname@ibm.com", "phone": "914-XXX-XXXX"}
                ],
                "linkedin_search": "IBM contractor hybrid cloud AI recruiter",
                "urgency": "Enterprise AI and cloud transformation surge",
                "notes": "Focus on hybrid cloud and AI/ML contractor expertise",
                "clients": ["Global Fortune 500", "Banks", "Airlines", "Retailers", "Manufacturers"]
            }
        ],

        "financial_services_primes": [
            {
                "company": "JPMorgan Chase Technology",
                "vendor_type": "Financial Services Prime Contractor",
                "contract_signals": "1000+ IT contractors for digital banking initiatives",
                "preferred_engagement": "C2C through approved vendor programs",
                "typical_duration": "12-24 months",
                "hourly_rates": "$90-170/hour",
                "clearance_required": "Background check required",
                "technologies": ["Java", "Python", "React", "Cloud", "Microservices", "APIs"],
                "collaboration_partners": ["AWS", "Google Cloud", "Palantir", "Snowflake"],
                "frequent_collaborators": "Partners with 200+ fintech contractors",
                "contract_recruiters": [
                    {"title": "Technology Contractor Lead", "email": "firstname.lastname@jpmchase.com", "phone": "212-XXX-XXXX"},
                    {"title": "Digital Banking Contractor", "email": "firstname.lastname@jpmchase.com", "phone": "212-XXX-XXXX"},
                    {"title": "Fintech Contractor Specialist", "email": "firstname.lastname@jpmchase.com", "phone": "212-XXX-XXXX"}
                ],
                "linkedin_search": "JPMorgan contractor technology digital banking",
                "urgency": "Digital transformation and regulatory compliance projects",
                "notes": "Premium rates for fintech expertise, regulatory knowledge valued",
                "clients": ["JPMorgan Chase internal divisions", "Investment banking", "Consumer banking"]
            },
            {
                "company": "Goldman Sachs Technology",
                "vendor_type": "Investment Banking Technology Prime",
                "contract_signals": "800+ contractors for trading systems and risk platforms",
                "preferred_engagement": "C2C preferred for specialized roles",
                "typical_duration": "6-18 months",
                "hourly_rates": "$120-200/hour",
                "clearance_required": "Financial background check",
                "technologies": ["Java", "Python", "C++", "React", "Trading Systems", "Risk Management"],
                "collaboration_partners": ["AWS", "Microsoft", "Palantir", "Snowflake"],
                "frequent_collaborators": "Works with 150+ fintech specialists",
                "contract_recruiters": [
                    {"title": "Trading Technology Contractor", "email": "firstname.lastname@gs.com", "phone": "212-XXX-XXXX"},
                    {"title": "Risk Systems Contractor Lead", "email": "firstname.lastname@gs.com", "phone": "212-XXX-XXXX"},
                    {"title": "Quantitative Developer Recruiter", "email": "firstname.lastname@gs.com", "phone": "212-XXX-XXXX"}
                ],
                "linkedin_search": "Goldman Sachs contractor trading systems",
                "urgency": "Trading platform modernization and regulatory compliance",
                "notes": "Highest rates in financial services, quantitative skills premium",
                "clients": ["Goldman Sachs divisions", "Institutional clients", "Wealth management"]
            }
        ],

        "technology_primes": [
            {
                "company": "Microsoft Consulting Services",
                "vendor_type": "Technology Prime Vendor",
                "contract_signals": "5000+ contractors for Azure and M365 implementations",
                "preferred_engagement": "C2C through partner network",
                "typical_duration": "6-24 months",
                "hourly_rates": "$80-160/hour",
                "clearance_required": "Not required for most roles",
                "technologies": ["Azure", "M365", "Power Platform", ".NET", "C#", "PowerShell"],
                "collaboration_partners": ["Accenture", "Deloitte", "PwC", "EY"],
                "frequent_collaborators": "Global partner network of 2000+ firms",
                "contract_recruiters": [
                    {"title": "Azure Contractor Specialist", "email": "firstname.lastname@microsoft.com", "phone": "425-XXX-XXXX"},
                    {"title": "M365 Implementation Lead", "email": "firstname.lastname@microsoft.com", "phone": "425-XXX-XXXX"},
                    {"title": "Cloud Contractor Manager", "email": "firstname.lastname@microsoft.com", "phone": "425-XXX-XXXX"}
                ],
                "linkedin_search": "Microsoft contractor Azure M365 recruiter",
                "urgency": "Enterprise cloud migration and digital workplace projects",
                "notes": "High demand for Azure and M365 expertise across industries",
                "clients": ["Enterprise customers", "Government", "SMB", "Healthcare", "Education"]
            },
            {
                "company": "Amazon Web Services (AWS)",
                "vendor_type": "Cloud Services Prime Vendor",
                "contract_signals": "4000+ contractors for cloud migrations and DevOps",
                "preferred_engagement": "C2C through consulting partner network",
                "typical_duration": "6-18 months", 
                "hourly_rates": "$90-180/hour",
                "clearance_required": "Not required for commercial, required for GovCloud",
                "technologies": ["AWS", "Python", "Java", "DevOps", "Kubernetes", "Terraform"],
                "collaboration_partners": ["Accenture", "Deloitte", "Capgemini", "Slalom"],
                "frequent_collaborators": "Works with 1000+ consulting partners globally",
                "contract_recruiters": [
                    {"title": "Cloud Migration Contractor", "email": "firstname.lastname@amazon.com", "phone": "206-XXX-XXXX"},
                    {"title": "DevOps Contractor Specialist", "email": "firstname.lastname@amazon.com", "phone": "206-XXX-XXXX"},
                    {"title": "AWS Solutions Contractor Lead", "email": "firstname.lastname@amazon.com", "phone": "206-XXX-XXXX"}
                ],
                "linkedin_search": "AWS contractor cloud migration DevOps",
                "urgency": "Enterprise cloud adoption and modernization surge",
                "notes": "Premium rates for AWS certifications and cloud expertise",
                "clients": ["Enterprise migrations", "Startups", "Government", "Healthcare", "Financial Services"]
            }
        ],

        "healthcare_pharma_primes": [
            {
                "company": "Epic Systems Partners",
                "vendor_type": "Healthcare IT Prime Vendor",
                "contract_signals": "2000+ contractors for Epic implementations nationwide",
                "preferred_engagement": "C2C and 1099 for certified specialists",
                "typical_duration": "12-36 months",
                "hourly_rates": "$85-160/hour",
                "clearance_required": "Healthcare background check",
                "technologies": ["Epic", "HL7", "FHIR", "Healthcare APIs", "SQL", "Crystal Reports"],
                "collaboration_partners": ["Epic", "Cerner", "Allscripts", "Healthcare IT vendors"],
                "frequent_collaborators": "Network of 500+ Epic certified contractors",
                "contract_recruiters": [
                    {"title": "Epic Contractor Specialist", "email": "firstname.lastname@epic.com", "phone": "608-XXX-XXXX"},
                    {"title": "Healthcare IT Contractor Lead", "email": "firstname.lastname@epic.com", "phone": "608-XXX-XXXX"},
                    {"title": "EHR Implementation Recruiter", "email": "firstname.lastname@epic.com", "phone": "608-XXX-XXXX"}
                ],
                "linkedin_search": "Epic contractor healthcare IT EHR",
                "urgency": "Hospital system modernization and Epic rollouts",
                "notes": "Epic certification essential, healthcare domain knowledge valued",
                "clients": ["Hospitals", "Health systems", "Clinics", "Healthcare networks"]
            },
            {
                "company": "Cerner (Oracle Health)",
                "vendor_type": "Healthcare Technology Prime",
                "contract_signals": "1500+ contractors for Cerner implementations and support",
                "preferred_engagement": "C2C preferred for certified roles",
                "typical_duration": "8-24 months",
                "hourly_rates": "$80-150/hour",
                "clearance_required": "Healthcare background check required",
                "technologies": ["Cerner", "Oracle", "HL7", "Healthcare Integration", "SQL"],
                "collaboration_partners": ["Oracle", "Microsoft", "AWS", "Healthcare IT firms"],
                "frequent_collaborators": "Works with 300+ healthcare IT contractors",
                "contract_recruiters": [
                    {"title": "Cerner Contractor Lead", "email": "firstname.lastname@cerner.com", "phone": "816-XXX-XXXX"},
                    {"title": "Healthcare Systems Contractor", "email": "firstname.lastname@cerner.com", "phone": "816-XXX-XXXX"},
                    {"title": "Oracle Health Recruiter", "email": "firstname.lastname@cerner.com", "phone": "816-XXX-XXXX"}
                ],
                "linkedin_search": "Cerner contractor Oracle Health EHR",
                "urgency": "Oracle Health transition and system upgrades",
                "notes": "Cerner/Oracle Health certification valuable, transition projects",
                "clients": ["Hospitals", "Health systems", "Government healthcare", "International health organizations"]
            }
        ],

        "retail_ecommerce_primes": [
            {
                "company": "Shopify Plus Partners",
                "vendor_type": "E-commerce Platform Prime Vendor",
                "contract_signals": "1000+ contractors for enterprise e-commerce projects",
                "preferred_engagement": "C2C and 1099 for Shopify specialists",
                "typical_duration": "4-12 months",
                "hourly_rates": "$75-140/hour",
                "clearance_required": "Not required",
                "technologies": ["Shopify", "Ruby on Rails", "React", "GraphQL", "E-commerce APIs"],
                "collaboration_partners": ["Shopify", "Accenture", "Deloitte Digital", "E-commerce agencies"],
                "frequent_collaborators": "Network of 200+ Shopify Plus agencies",
                "contract_recruiters": [
                    {"title": "Shopify Contractor Specialist", "email": "firstname.lastname@shopify.com", "phone": "613-XXX-XXXX"},
                    {"title": "E-commerce Contractor Lead", "email": "firstname.lastname@shopify.com", "phone": "613-XXX-XXXX"},
                    {"title": "Plus Partner Recruiter", "email": "firstname.lastname@shopify.com", "phone": "613-XXX-XXXX"}
                ],
                "linkedin_search": "Shopify contractor e-commerce Ruby Rails",
                "urgency": "Enterprise e-commerce platform migrations and customizations",
                "notes": "Shopify Plus expertise in high demand, e-commerce domain knowledge",
                "clients": ["Enterprise retailers", "D2C brands", "B2B commerce", "International merchants"]
            },
            {
                "company": "Salesforce Commerce Cloud Partners",
                "vendor_type": "Enterprise E-commerce Prime Vendor", 
                "contract_signals": "800+ contractors for Commerce Cloud implementations",
                "preferred_engagement": "C2C through certified partner network",
                "typical_duration": "6-18 months",
                "hourly_rates": "$90-170/hour",
                "clearance_required": "Not required",
                "technologies": ["Salesforce Commerce Cloud", "JavaScript", "Node.js", "APIs", "Integration"],
                "collaboration_partners": ["Salesforce", "Accenture", "Deloitte", "PwC"],
                "frequent_collaborators": "Certified partner network of 150+ agencies",
                "contract_recruiters": [
                    {"title": "Commerce Cloud Contractor", "email": "firstname.lastname@salesforce.com", "phone": "415-XXX-XXXX"},
                    {"title": "E-commerce Solutions Lead", "email": "firstname.lastname@salesforce.com", "phone": "415-XXX-XXXX"},
                    {"title": "Digital Commerce Recruiter", "email": "firstname.lastname@salesforce.com", "phone": "415-XXX-XXXX"}
                ],
                "linkedin_search": "Salesforce Commerce Cloud contractor e-commerce",
                "urgency": "Enterprise digital commerce transformation projects", 
                "notes": "Salesforce Commerce Cloud certification highly valued",
                "clients": ["Fortune 500 retailers", "Luxury brands", "B2B commerce", "Global enterprises"]
            }
        ],

        "government_it_primes": [
            {
                "company": "CACI International",
                "vendor_type": "Government IT Prime Contractor",
                "contract_signals": "Intelligence and federal IT contracts need 1000+ contractors",
                "preferred_engagement": "C2C with clearance requirements",
                "typical_duration": "12-48 months",
                "hourly_rates": "$95-200/hour",
                "clearance_required": "Secret to TS/SCI depending on project",
                "technologies": ["Java", "Python", "Cloud", "DevOps", "Data Analytics", "Cybersecurity"],
                "collaboration_partners": ["AWS", "Microsoft", "Palantir", "Other cleared contractors"],
                "frequent_collaborators": "Works with 200+ cleared IT contractors",
                "contract_recruiters": [
                    {"title": "Federal IT Contractor Lead", "email": "firstname.lastname@caci.com", "phone": "703-XXX-XXXX"},
                    {"title": "Cleared IT Specialist", "email": "firstname.lastname@caci.com", "phone": "703-XXX-XXXX"},
                    {"title": "Government Technology Recruiter", "email": "firstname.lastname@caci.com", "phone": "703-XXX-XXXX"}
                ],
                "linkedin_search": "CACI contractor cleared IT federal",
                "urgency": "Federal agency modernization and cloud migration",
                "notes": "Security clearance required, premium rates for cleared IT roles",
                "clients": ["Federal agencies", "Intelligence community", "DoD", "DHS", "Civilian agencies"]
            },
            {
                "company": "Accenture Federal Services",
                "vendor_type": "Federal & State IT Prime Vendor",
                "contract_signals": "Government modernization projects need 2000+ contractors",
                "preferred_engagement": "C2C through vendor programs",
                "typical_duration": "12-36 months",
                "hourly_rates": "$80-160/hour",
                "clearance_required": "Public Trust to Secret depending on project",
                "technologies": ["Salesforce", "ServiceNow", "Cloud", "Java", "Data Analytics"],
                "collaboration_partners": ["Salesforce", "ServiceNow", "AWS", "Microsoft"],
                "frequent_collaborators": "Network of 400+ government IT contractors",
                "contract_recruiters": [
                    {"title": "Federal Contractor Lead", "email": "firstname.lastname@accenture.com", "phone": "703-XXX-XXXX"},
                    {"title": "Government IT Specialist", "email": "firstname.lastname@accenture.com", "phone": "703-XXX-XXXX"},
                    {"title": "Public Sector Recruiter", "email": "firstname.lastname@accenture.com", "phone": "703-XXX-XXXX"}
                ],
                "linkedin_search": "Accenture Federal contractor government IT",
                "urgency": "Federal and state government modernization initiatives",
                "notes": "Mix of cleared and non-cleared government IT roles",
                "clients": ["Federal agencies", "State governments", "Local governments", "Public sector"]
            }
        ]
    }
    
    return balanced_prime_vendors

def generate_balanced_daily_massive_list():
    """Generate massive daily list with balanced mix of all prime vendor types"""
    
    today = datetime.now()
    day_name = today.strftime('%A').lower()
    
    # Balanced daily focus across all sectors
    daily_focus_balanced = {
        "monday_focus": {
            "target_count": 150,
            "focus_sectors": ["private_consulting_primes", "financial_services_primes"],
            "priority_technologies": ["Java", "Python", "Salesforce", "Cloud", "React"],
            "vendor_mix": "70% Private, 30% Financial Services"
        },
        
        "tuesday_focus": {
            "target_count": 160,
            "focus_sectors": ["technology_primes", "healthcare_pharma_primes"], 
            "priority_technologies": ["AWS", "Azure", "Epic", "Healthcare IT", "APIs"],
            "vendor_mix": "60% Technology, 40% Healthcare"
        },
        
        "wednesday_focus": {
            "target_count": 140,
            "focus_sectors": ["retail_ecommerce_primes", "government_it_primes"],
            "priority_technologies": ["E-commerce", "Shopify", "Government IT", "DevOps"],
            "vendor_mix": "50% Retail/E-commerce, 50% Government IT"
        },
        
        "thursday_focus": {
            "target_count": 170,
            "focus_sectors": ["private_consulting_primes", "technology_primes", "financial_services_primes"],
            "priority_technologies": ["SAP", "Oracle", "Consulting", "Integration", "Data"],
            "vendor_mix": "40% Consulting, 30% Technology, 30% Financial"
        },
        
        "friday_focus": {
            "target_count": 180,
            "focus_sectors": ["All sectors - comprehensive mix"],
            "priority_technologies": ["Full Stack", "Mobile", "QA", "BA", "Specialized"],
            "vendor_mix": "Balanced mix across all prime vendor types"
        }
    }
    
    # Get today's focus
    today_focus = daily_focus_balanced.get(f"{day_name}_focus", daily_focus_balanced["monday_focus"])
    
    balanced_prime_vendors = create_balanced_prime_vendors()
    
    # Generate balanced massive list
    balanced_massive_list = []
    target_id = 1
    
    for sector, companies in balanced_prime_vendors.items():
        if sector in today_focus["focus_sectors"] or "All sectors" in today_focus["focus_sectors"][0]:
            for company in companies:
                for tech in today_focus["priority_technologies"]:
                    for recruiter_info in company["contract_recruiters"]:
                        balanced_massive_list.append({
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
                            "clearance_required": company.get("clearance_required", "Not required"),
                            "urgency": company["urgency"],
                            "recruiter_title": recruiter_info["title"],
                            "recruiter_email": recruiter_info["email"],
                            "recruiter_phone": recruiter_info["phone"],
                            "linkedin_search": f'"{company["company"]}" AND "{recruiter_info["title"]}" AND "contract" AND "{tech}"',
                            "boolean_search": f'site:linkedin.com/in "{company["company"]}" AND ("{recruiter_info["title"]}" OR "contractor") AND "{tech}"',
                            "collaboration_partners": "; ".join(company["collaboration_partners"]),
                            "frequent_collaborators": company["frequent_collaborators"],
                            "client_base": "; ".join(company["clients"]),
                            "contract_opportunity_type": "Prime Vendor",
                            "search_priority": "Critical" if "clearance" in company.get("clearance_required", "").lower() else "High" if tech in ["Java", "Python", "AWS", "Salesforce"] else "Medium",
                            "research_status": "Not Started",
                            "contact_found": "No",
                            "email_verified": "No",
                            "email_sent": "No", 
                            "response_received": "No",
                            "notes": company["notes"]
                        })
                        target_id += 1
    
    # Shuffle for variety and limit to target count
    random.shuffle(balanced_massive_list)
    target_count = max(today_focus["target_count"], 150)
    balanced_massive_list = balanced_massive_list[:target_count]
    
    return balanced_massive_list, today_focus

def export_balanced_prime_vendor_system():
    """Export the complete balanced prime vendor system"""
    
    today = datetime.now()
    date_str = today.strftime('%Y-%m-%d')
    day_name = today.strftime('%A')
    
    print(f"🚀 GENERATING BALANCED PRIME VENDOR MIX - {day_name.upper()} {date_str}")
    print("=" * 70)
    
    # Generate balanced massive list
    balanced_massive_list, today_focus = generate_balanced_daily_massive_list()
    
    # Export to CSV with all details
    filename = f'balanced_prime_vendors_daily_{date_str}.csv'
    with open(filename, 'w', newline='') as f:
        if balanced_massive_list:
            writer = csv.DictWriter(f, fieldnames=balanced_massive_list[0].keys())
            writer.writeheader()
            writer.writerows(balanced_massive_list)
    
    # Create balanced summary
    summary = {
        "date": date_str,
        "day": day_name,
        "total_targets": len(balanced_massive_list),
        "vendor_mix": today_focus["vendor_mix"],
        "focus_sectors": today_focus["focus_sectors"],
        "priority_technologies": today_focus["priority_technologies"],
        "private_vendors": len([t for t in balanced_massive_list if "Private" in t["vendor_type"] or "Consulting" in t["vendor_type"]]),
        "government_vendors": len([t for t in balanced_massive_list if "Government" in t["vendor_type"] or "Federal" in t["vendor_type"]]),
        "technology_vendors": len([t for t in balanced_massive_list if "Technology" in t["vendor_type"] or "Cloud" in t["vendor_type"]]),
        "financial_vendors": len([t for t in balanced_massive_list if "Financial" in t["vendor_type"] or "Banking" in t["vendor_type"]]),
        "healthcare_vendors": len([t for t in balanced_massive_list if "Healthcare" in t["vendor_type"]]),
        "retail_vendors": len([t for t in balanced_massive_list if "E-commerce" in t["vendor_type"] or "Retail" in t["vendor_type"]]),
        "balanced_mix": True,
        "email_addresses_included": True,
        "contract_only_focus": True
    }
    
    summary_filename = f'balanced_summary_{date_str}.json'
    with open(summary_filename, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"✅ Generated {len(balanced_massive_list)} BALANCED prime vendor targets for {day_name}")
    print(f"✅ Vendor Mix: {today_focus['vendor_mix']}")
    print(f"✅ Focus Sectors: {', '.join(today_focus['focus_sectors'])}")
    print(f"✅ Technologies: {', '.join(today_focus['priority_technologies'])}")
    
    # Detailed breakdown
    print(f"\n📊 BALANCED VENDOR BREAKDOWN:")
    sector_counts = {}
    for target in balanced_massive_list:
        sector = target["sector"]
        sector_counts[sector] = sector_counts.get(sector, 0) + 1
    
    for sector, count in sector_counts.items():
        print(f"  • {sector}: {count} targets")
    
    print(f"\n💼 VENDOR TYPE BREAKDOWN:")
    print(f"  • Private/Consulting Vendors: {summary['private_vendors']} targets")
    print(f"  • Government IT Vendors: {summary['government_vendors']} targets") 
    print(f"  • Technology Vendors: {summary['technology_vendors']} targets")
    print(f"  • Financial Services: {summary['financial_vendors']} targets")
    print(f"  • Healthcare Vendors: {summary['healthcare_vendors']} targets")
    print(f"  • Retail/E-commerce: {summary['retail_vendors']} targets")
    
    print(f"\n📁 FILES CREATED:")
    print(f"  📋 {filename} - Balanced prime vendor targets with emails")
    print(f"  📊 {summary_filename} - Balanced vendor mix summary")
    
    print(f"\n🎯 BALANCED MIX FOCUS:")
    print("  ✅ Private consulting primes (Accenture, Deloitte, IBM)")
    print("  ✅ Financial services (JPMorgan, Goldman Sachs)")
    print("  ✅ Technology vendors (Microsoft, AWS)")
    print("  ✅ Healthcare IT (Epic, Cerner/Oracle Health)")
    print("  ✅ E-commerce platforms (Shopify, Salesforce Commerce)")
    print("  ✅ Government IT (CACI, Accenture Federal)")
    print("  ✅ ALL with email addresses included")
    
    print(f"\n💰 RATE RANGES BY SECTOR:")
    print("  • Private Consulting: $70-160/hour")
    print("  • Financial Services: $90-200/hour") 
    print("  • Technology Vendors: $80-180/hour")
    print("  • Healthcare IT: $80-160/hour")
    print("  • E-commerce: $75-170/hour")
    print("  • Government IT: $80-200/hour (clearance dependent)")
    
    print(f"\n🚀 IMMEDIATE ACTIONS:")
    print("1. Open CSV - mix of private, government, and commercial prime vendors")
    print("2. Start with high-rate financial services and technology vendors")
    print("3. Use sector-specific expertise in contractor matching")
    print("4. Reference collaboration partnerships in outreach")
    print("5. Track industry domain expertise requirements")
    
    return balanced_massive_list, filename, summary_filename

if __name__ == "__main__":
    export_balanced_prime_vendor_system()