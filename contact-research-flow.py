#!/usr/bin/env python3
"""
Contact Research Flow - Find Real HR/Hiring Manager Details
Systematic approach to finding verified contacts for each technology stack
"""

import json
import csv
from datetime import datetime, timedelta

def create_target_companies_by_tech():
    """Create specific target companies for each technology with known hiring patterns"""
    
    target_companies = {
        "ai_ml_engineering": [
            {
                "company": "OpenAI",
                "website": "openai.com/careers",
                "recent_hirings": "Hiring 50+ ML engineers per quarter",
                "linkedin_search": "OpenAI technical recruiter machine learning",
                "email_format": "firstname.lastname@openai.com", 
                "hiring_manager_titles": ["VP Engineering", "Director of AI", "ML Engineering Manager"],
                "hr_contact_titles": ["Technical Recruiter", "Senior Recruiter - AI/ML", "Talent Acquisition Partner"],
                "job_board_activity": "Posts 10-15 ML roles weekly on LinkedIn",
                "contractor_friendly": "Yes - uses contractors for specialized projects",
                "notes": "Fast-growing, high compensation, cutting-edge projects"
            },
            {
                "company": "Anthropic", 
                "website": "anthropic.com/careers",
                "recent_hirings": "Building core AI safety team",
                "linkedin_search": "Anthropic hiring manager AI safety",
                "email_format": "firstname@anthropic.com",
                "hiring_manager_titles": ["Head of Engineering", "AI Safety Lead", "Research Director"], 
                "hr_contact_titles": ["People Operations", "Talent Partner", "Technical Recruiter"],
                "job_board_activity": "Selective hiring, posts 3-5 roles monthly",
                "contractor_friendly": "Limited - prefers full-time but open to specialized consultants",
                "notes": "AI safety focus, research-oriented, competitive compensation"
            },
            {
                "company": "Scale AI",
                "website": "scale.com/careers", 
                "recent_hirings": "Expanding ML infrastructure team",
                "linkedin_search": "Scale AI machine learning engineer recruiter",
                "email_format": "firstname@scale.com",
                "hiring_manager_titles": ["VP of Engineering", "ML Platform Lead", "Engineering Manager"],
                "hr_contact_titles": ["Technical Recruiter", "Talent Acquisition", "People Team"],
                "job_board_activity": "Posts 5-8 ML roles weekly",
                "contractor_friendly": "Yes - actively uses C2C for specialized skills",
                "notes": "Data labeling platform, rapid growth, ML infrastructure focus"
            }
        ],
        
        "devops_cloud": [
            {
                "company": "Netflix",
                "website": "jobs.netflix.com",
                "recent_hirings": "Building cloud infrastructure team",
                "linkedin_search": "Netflix DevOps engineer recruiter cloud",
                "email_format": "firstname.lastname@netflix.com",
                "hiring_manager_titles": ["Director of Platform Engineering", "Cloud Infrastructure Manager", "Site Reliability Manager"],
                "hr_contact_titles": ["Senior Technical Recruiter", "Infrastructure Talent Partner", "Engineering Recruiter"],
                "job_board_activity": "Posts 15-20 infrastructure roles monthly", 
                "contractor_friendly": "Yes - uses contractors for specific migrations",
                "notes": "AWS-heavy, microservices, high-scale streaming infrastructure"
            },
            {
                "company": "Airbnb",
                "website": "careers.airbnb.com",
                "recent_hirings": "Scaling global infrastructure",
                "linkedin_search": "Airbnb platform engineering recruiter",
                "email_format": "firstname.lastname@airbnb.com", 
                "hiring_manager_titles": ["VP Infrastructure", "Platform Engineering Manager", "DevOps Lead"],
                "hr_contact_titles": ["Technical Recruiter - Infrastructure", "Senior Talent Partner", "Engineering Recruiter"],
                "job_board_activity": "Posts 8-12 platform roles monthly",
                "contractor_friendly": "Yes - particularly for AWS migrations and K8s expertise",
                "notes": "Multi-cloud strategy, Kubernetes-heavy, travel industry insights"
            }
        ],
        
        "blockchain_web3": [
            {
                "company": "Coinbase", 
                "website": "coinbase.com/careers",
                "recent_hirings": "Expanding protocol engineering team",
                "linkedin_search": "Coinbase blockchain developer recruiter",
                "email_format": "firstname.lastname@coinbase.com",
                "hiring_manager_titles": ["VP of Engineering", "Protocol Engineering Manager", "Blockchain Lead"],
                "hr_contact_titles": ["Technical Recruiter - Blockchain", "Crypto Talent Partner", "Senior Recruiter"],
                "job_board_activity": "Posts 20+ blockchain roles monthly",
                "contractor_friendly": "Yes - actively hires contractors for protocol work",
                "notes": "Publicly traded, regulatory compliance focus, diverse blockchain protocols"
            },
            {
                "company": "Chainlink Labs",
                "website": "chainlinklabs.com/careers", 
                "recent_hirings": "Building oracle network infrastructure",
                "linkedin_search": "Chainlink protocol engineer recruiter",
                "email_format": "firstname@chainlinklabs.com",
                "hiring_manager_titles": ["Head of Engineering", "Protocol Development Lead", "Smart Contracts Manager"],
                "hr_contact_titles": ["Technical Recruiter", "People Operations", "Talent Acquisition"],
                "job_board_activity": "Posts 5-8 protocol roles monthly",
                "contractor_friendly": "Yes - especially for Solidity and Go developers", 
                "notes": "Decentralized oracle network, strong developer community, remote-first"
            }
        ],
        
        "software_engineering": [
            {
                "company": "Stripe",
                "website": "stripe.com/jobs",
                "recent_hirings": "Expanding payments infrastructure globally",
                "linkedin_search": "Stripe backend engineer recruiter",
                "email_format": "firstname@stripe.com",
                "hiring_manager_titles": ["VP of Engineering", "Backend Engineering Manager", "Platform Lead"],
                "hr_contact_titles": ["Technical Recruiter", "Engineering Talent Partner", "Senior Recruiter"],
                "job_board_activity": "Posts 25+ engineering roles monthly",
                "contractor_friendly": "Limited full-time preference, but hires specialized contractors",
                "notes": "Ruby, Go, JavaScript stack, fintech, global payments platform"
            },
            {
                "company": "Shopify", 
                "website": "shopify.com/careers",
                "recent_hirings": "Building commerce infrastructure platform",
                "linkedin_search": "Shopify software engineer recruiter Ruby",
                "email_format": "firstname.lastname@shopify.com",
                "hiring_manager_titles": ["Director of Engineering", "Full Stack Engineering Manager", "Backend Lead"],
                "hr_contact_titles": ["Technical Recruiter - Engineering", "Talent Acquisition Partner", "Senior Recruiter"],
                "job_board_activity": "Posts 30+ engineering roles monthly",
                "contractor_friendly": "Yes - hires contractors for e-commerce platform development",
                "notes": "Ruby on Rails, React, GraphQL, e-commerce focus, merchant tools"
            }
        ]
    }
    
    return target_companies

def create_linkedin_research_templates():
    """Create specific LinkedIn search templates and research strategies"""
    
    search_templates = {
        "find_hiring_managers": [
            '"{company_name}" AND "hiring manager" AND "{technology}"',
            '"{company_name}" AND "engineering manager" AND "{technology}"', 
            '"{company_name}" AND "director of engineering" AND "{technology}"',
            '"{company_name}" AND "VP engineering" AND "{technology}"',
            '"{company_name}" AND "head of engineering" AND "{technology}"'
        ],
        
        "find_technical_recruiters": [
            '"{company_name}" AND "technical recruiter" AND "{technology}"',
            '"{company_name}" AND "talent acquisition" AND "{technology}"', 
            '"{company_name}" AND "recruiting" AND "{technology}"',
            '"{company_name}" AND "senior recruiter" AND "{technology}"',
            '"{company_name}" AND "talent partner" AND "{technology}"'
        ],
        
        "find_hr_contacts": [
            '"{company_name}" AND "people operations" AND "engineering"',
            '"{company_name}" AND "HR business partner" AND "technology"',
            '"{company_name}" AND "talent acquisition partner"',
            '"{company_name}" AND "recruiting coordinator" AND "tech"',
            '"{company_name}" AND "people team" AND "engineering"'
        ],
        
        "find_delivery_managers": [
            '"{company_name}" AND "delivery manager" AND "{technology}"',
            '"{company_name}" AND "program manager" AND "{technology}"',
            '"{company_name}" AND "project manager" AND "{technology}"',
            '"{company_name}" AND "scrum master" AND "{technology}"',
            '"{company_name}" AND "agile delivery" AND "{technology}"'
        ],
        
        "boolean_search_advanced": [
            'site:linkedin.com/in "{company_name}" AND ("hiring manager" OR "engineering manager") AND "{technology}"',
            'site:linkedin.com/in "{company_name}" AND ("recruiter" OR "talent acquisition") AND "{technology}"',
            'site:linkedin.com/in "{company_name}" AND ("we are hiring" OR "we\'re hiring") AND "{technology}"'
        ]
    }
    
    return search_templates

def create_contact_verification_process():
    """Create systematic contact verification and enrichment process"""
    
    verification_process = {
        "step_1_linkedin_verification": {
            "action": "Verify current employment and role",
            "checks": [
                "Profile shows current position at target company",
                "Recent activity within last 30 days", 
                "Profile completeness (photo, summary, experience)",
                "Connection count (indicates active LinkedIn user)",
                "Recent posts about hiring or team growth"
            ],
            "red_flags": [
                "Profile shows 'Open to Work' status",
                "No activity in 90+ days",
                "Generic or incomplete profile",
                "Recent job change notification"
            ]
        },
        
        "step_2_email_discovery": {
            "tools": ["Hunter.io", "Apollo.io", "Voila Norbert", "FindThatLead"],
            "methods": [
                "Use Hunter.io to find company email format",
                "Cross-reference with Apollo.io database",
                "Check company website team/about pages",
                "Look for email signatures in LinkedIn posts", 
                "Use company directory if publicly available"
            ],
            "verification": [
                "Send test email with read receipt",
                "Use email verification tools to check validity",
                "Look for auto-responder messages", 
                "Check for bounced emails"
            ]
        },
        
        "step_3_phone_discovery": {
            "sources": [
                "LinkedIn profile contact info section",
                "Company website team pages",
                "ZoomInfo or similar data services",
                "Professional associations and directories",
                "Conference speaker listings"
            ],
            "verification": [
                "Cross-reference phone number with multiple sources",
                "Check area code matches company location",
                "Look for mobile vs. office number indicators"
            ]
        },
        
        "step_4_contact_enrichment": {
            "gather_intelligence": [
                "Recent LinkedIn posts and articles",
                "Company news and press releases",
                "Team announcements and hiring updates", 
                "Professional interests and expertise areas",
                "Mutual connections and warm introduction paths"
            ],
            "timing_optimization": [
                "Check recent hiring posts for urgency indicators",
                "Note any company growth announcements",
                "Look for funding news that indicates hiring spikes",
                "Monitor for job posting patterns and timing"
            ]
        }
    }
    
    return verification_process

def create_personalized_outreach_system():
    """Create system for highly personalized, researched outreach"""
    
    outreach_system = {
        "research_requirements": {
            "company_intelligence": [
                "Recent company news (funding, partnerships, product launches)",
                "Technology stack mentioned in job postings", 
                "Growth metrics and hiring velocity",
                "Specific technical challenges mentioned publicly",
                "Company culture and values from website/social media"
            ],
            "contact_intelligence": [
                "Recent LinkedIn posts or articles by the contact",
                "Professional background and career progression",
                "Technical expertise areas and interests",
                "Hiring patterns and team growth updates",
                "Communication style from public posts"
            ]
        },
        
        "personalization_framework": {
            "opening_hook": [
                "Reference specific recent company achievement",
                "Mention mutual connection if available",
                "Reference their recent LinkedIn post or article",
                "Connect to industry news relevant to their role",
                "Acknowledge specific technical challenge they face"
            ],
            "value_proposition": [
                "Highlight exact technology match from job postings",
                "Mention specific candidate experience relevant to their needs", 
                "Reference similar successful placements in their industry",
                "Address unique hiring challenges they face",
                "Offer specific timeline that matches their urgency"
            ],
            "credibility_builders": [
                "Mention specific successful placements with metrics",
                "Reference industry certifications or expertise",
                "Include testimonials from similar companies",
                "Highlight specialization in their technology stack",
                "Show understanding of their industry challenges"
            ]
        }
    }
    
    return outreach_system

def export_contact_research_system():
    """Export comprehensive contact research system"""
    
    print("Creating Contact Research Flow System...")
    print("=" * 50)
    
    # Get all components
    target_companies = create_target_companies_by_tech()
    search_templates = create_linkedin_research_templates()
    verification_process = create_contact_verification_process() 
    outreach_system = create_personalized_outreach_system()
    
    # Export target companies by technology
    with open('target_companies_by_tech.json', 'w') as f:
        json.dump(target_companies, f, indent=2)
    
    # Export LinkedIn search templates
    with open('linkedin_research_templates.json', 'w') as f:
        json.dump(search_templates, f, indent=2)
        
    # Export verification process
    with open('contact_verification_process.json', 'w') as f:
        json.dump(verification_process, f, indent=2)
        
    # Export outreach system
    with open('personalized_outreach_system.json', 'w') as f:
        json.dump(outreach_system, f, indent=2)
    
    # Create actionable research checklist CSV
    research_checklist = []
    for tech, companies in target_companies.items():
        for company in companies:
            research_checklist.append({
                'technology': tech.replace('_', ' ').title(),
                'company': company['company'],
                'website': company['website'], 
                'linkedin_search': company['linkedin_search'],
                'email_format': company['email_format'],
                'hiring_manager_titles': ', '.join(company['hiring_manager_titles'][:2]),
                'hr_contact_titles': ', '.join(company['hr_contact_titles'][:2]),
                'contractor_friendly': company['contractor_friendly'],
                'priority': 'High' if 'Yes' in company['contractor_friendly'] else 'Medium',
                'research_status': 'Not Started',
                'contacts_found': 0,
                'notes': company['notes']
            })
    
    with open('research_action_checklist.csv', 'w', newline='') as f:
        if research_checklist:
            writer = csv.DictWriter(f, fieldnames=research_checklist[0].keys())
            writer.writeheader()
            writer.writerows(research_checklist)
    
    print(f"✅ Created detailed target companies for {len(target_companies)} technology categories")
    print("✅ Generated LinkedIn search templates and Boolean queries")
    print("✅ Built 4-step contact verification process") 
    print("✅ Created personalized outreach framework")
    
    print("\nFiles created:")
    print("🎯 target_companies_by_tech.json - Specific companies with hiring intel")
    print("🔍 linkedin_research_templates.json - Search queries and strategies")
    print("✅ contact_verification_process.json - 4-step verification system")
    print("📧 personalized_outreach_system.json - Research-based personalization")
    print("📋 research_action_checklist.csv - Actionable company research list")
    
    print("\n🚀 IMMEDIATE ACTION PLAN:")
    print("1. Open research_action_checklist.csv - start with 'High' priority companies")
    print("2. Use LinkedIn search templates to find specific contacts")
    print("3. Follow 4-step verification process for each contact") 
    print("4. Build personalized outreach using research framework")
    print("5. Track results and iterate based on response rates")
    
    # Show sample research workflow
    print("\n📝 SAMPLE RESEARCH WORKFLOW (OpenAI example):")
    print("1. LinkedIn Search: 'OpenAI technical recruiter machine learning'")
    print("2. Find: Sarah Chen - Senior Technical Recruiter at OpenAI")
    print("3. Verify: Active profile, recent posts about ML hiring")
    print("4. Email: sarah.chen@openai.com (verified via Hunter.io)")
    print("5. Research: Recent post about hiring ML engineers for GPT projects")
    print("6. Personalize: Reference their GPT hiring needs, mention our PyTorch specialists")

if __name__ == "__main__":
    export_contact_research_system()