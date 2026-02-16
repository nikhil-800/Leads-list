#!/usr/bin/env python3
"""
Simple AI/ML Vendor Research Framework
Creates research templates and target lists for Team-Soft LLC
"""

import json
import csv
import os

def create_target_vendors():
    """Create list of target vendors and companies"""
    
    prime_vendors = [
        {
            'company': 'Kelly Services', 
            'type': 'Prime Vendor',
            'focus': 'AI/ML, Tech Staff Augmentation',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'kellyservices.com',
            'priority': 'High'
        },
        {
            'company': 'Robert Half Technology',
            'type': 'Prime Vendor', 
            'focus': 'IT Staffing, Data Science',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'roberthalf.com',
            'priority': 'High'
        },
        {
            'company': 'TEKsystems',
            'type': 'Prime Vendor',
            'focus': 'Technology Consulting, AI Engineers',
            'contact_info': 'TBD - LinkedIn research needed', 
            'website': 'teksystems.com',
            'priority': 'High'
        },
        {
            'company': 'Insight Global',
            'type': 'Prime Vendor',
            'focus': 'IT Staffing, Contract Placements',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'insightglobal.net',
            'priority': 'High'
        },
        {
            'company': 'Apex Systems', 
            'type': 'Prime Vendor',
            'focus': 'Technology Staffing, AI/ML',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'apexsystems.com',
            'priority': 'Medium'
        },
        {
            'company': 'Randstad Technologies',
            'type': 'Prime Vendor',
            'focus': 'Digital & Technology',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'randstadusa.com',
            'priority': 'Medium'
        }
    ]
    
    target_companies = [
        {
            'company': 'Netflix',
            'type': 'Direct Client',
            'focus': 'ML Engineers, Data Science',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'netflix.com',
            'priority': 'High'
        },
        {
            'company': 'Spotify',
            'type': 'Direct Client', 
            'focus': 'AI/ML, Recommendation Systems',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'spotify.com',
            'priority': 'High'
        },
        {
            'company': 'Uber',
            'type': 'Direct Client',
            'focus': 'ML Engineers, Data Engineers',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'uber.com', 
            'priority': 'Medium'
        },
        {
            'company': 'Airbnb',
            'type': 'Direct Client',
            'focus': 'Data Science, ML Infrastructure',
            'contact_info': 'TBD - LinkedIn research needed',
            'website': 'airbnb.com',
            'priority': 'Medium'
        }
    ]
    
    return prime_vendors + target_companies

def create_email_templates():
    """Create email templates for outreach"""
    
    templates = {
        'initial_contact_prime_vendor': {
            'subject': 'Partnership Opportunity - AI/ML Staffing Solutions',
            'body': '''Hi {contact_name},

I hope this email finds you well. I'm reaching out from Team-Soft LLC, a specialized IT staffing company focusing on high-demand AI/ML and technology roles.

We're interested in exploring partnership opportunities with {company_name} for:

🔹 AI/ML Engineers & Data Scientists
🔹 Software Engineers (Python, Java, Go)  
🔹 DevOps & Cloud Engineers
🔹 QA Engineers & Test Automation
🔹 Business Analysts & Product Managers

Our engagement models:
• Corp-to-Corp (C2C) arrangements
• Contract-to-Hire (C2H)
• 1099 Independent contractor placements

We specialize in hard-to-fill positions and maintain a strong bench of pre-vetted candidates. Our turnaround time is typically 48-72 hours for qualified submissions.

Would you be open to a brief 15-minute call this week to discuss potential collaboration?

Best regards,
[Your Name]
Team-Soft LLC
Phone: [Your Phone]
Email: [Your Email]'''
        },
        
        'initial_contact_direct_client': {
            'subject': 'AI/ML Staffing Solutions for {company_name}',
            'body': '''Hello {contact_name},

I'm writing from Team-Soft LLC regarding your AI/ML and data science staffing needs.

We noticed {company_name} has been actively hiring for {specific_role} positions. As a specialized IT staffing firm, we focus exclusively on:

🎯 Artificial Intelligence & Machine Learning Engineers
🎯 Data Scientists & Analytics Engineers  
🎯 Software Engineers (AI/ML stack)
🎯 DevOps Engineers (MLOps focus)

Why partner with us:
• Pre-vetted candidates with proven AI/ML experience
• Flexible engagement: C2C, C2H, or 1099 arrangements
• Fast turnaround - qualified candidates within 48 hours
• Specialization in hard-to-fill technical positions
• Competitive rates and terms

We understand the challenge of finding qualified AI/ML talent in today's market. Let's discuss how we can support {company_name}'s growing technology needs.

Available for a quick call this week?

Best,
[Your Name]
Team-Soft LLC'''
        },
        
        'follow_up_template': {
            'subject': 'Following up - AI/ML Staffing Partnership',
            'body': '''Hi {contact_name},

I wanted to follow up on my previous email regarding AI/ML staffing solutions for {company_name}.

Given the current talent shortage in AI/ML roles, many companies are turning to specialized staffing partners like Team-Soft LLC to:

✅ Access pre-qualified candidates faster
✅ Reduce hiring overhead and time-to-fill
✅ Scale teams flexibly with contract arrangements  
✅ Focus internal resources on core business

We've successfully placed {number}+ AI/ML professionals in similar roles over the past year.

Could we schedule a brief 10-minute call to explore how we might support your hiring goals?

I'm available {availability} this week.

Best regards,
[Your Name]'''
        }
    }
    
    return templates

def create_linkedin_search_queries():
    """Create LinkedIn search queries for finding contacts"""
    
    search_queries = {
        'hiring_managers': [
            'AI hiring manager site:linkedin.com',
            'ML engineering manager site:linkedin.com', 
            'data science manager site:linkedin.com',
            'technical recruiting manager AI site:linkedin.com'
        ],
        
        'hr_contacts': [
            'HR manager technology site:linkedin.com',
            'talent acquisition AI ML site:linkedin.com',
            'technical recruiter artificial intelligence site:linkedin.com',
            'staffing manager IT site:linkedin.com'
        ],
        
        'company_specific': [
            '{company_name} hiring manager AI site:linkedin.com',
            '{company_name} technical recruiter site:linkedin.com',
            '{company_name} talent acquisition site:linkedin.com'
        ]
    }
    
    return search_queries

def create_research_checklist():
    """Create research checklist for manual execution"""
    
    checklist = {
        'daily_tasks': [
            '□ Check Indeed for new AI/ML contract postings',
            '□ Monitor LinkedIn for hiring manager posts', 
            '□ Search target company career pages',
            '□ Update contact database with new finds',
            '□ Send 5-10 outreach emails',
            '□ Follow up on previous communications'
        ],
        
        'weekly_tasks': [
            '□ Research 10 new target companies',
            '□ Update email templates based on responses',
            '□ Review and prioritize lead pipeline', 
            '□ Analyze response rates and optimize approach',
            '□ Connect with new contacts on LinkedIn'
        ],
        
        'linkedin_research_process': [
            '1. Search for company name + "hiring manager"',
            '2. Look for recent AI/ML job postings from company',
            '3. Find the hiring manager or recruiter who posted',
            '4. Check their profile for contact preferences',
            '5. Send connection request with personalized note',
            '6. Follow up with email if contact info available'
        ],
        
        'contact_qualification_criteria': [
            '✓ Company actively hiring AI/ML roles',
            '✓ Open to contract/C2C arrangements', 
            '✓ Company size 100-5000 employees',
            '✓ Recent job postings (last 30 days)',
            '✓ Hard-to-fill or specialized requirements',
            '✓ Remote-friendly positions'
        ]
    }
    
    return checklist

def export_all_data():
    """Export all research data to files"""
    
    print("Creating AI/ML Vendor Research Framework...")
    
    # Get all data
    vendors = create_target_vendors()
    templates = create_email_templates()  
    search_queries = create_linkedin_search_queries()
    checklist = create_research_checklist()
    
    # Export to JSON
    with open('vendor_targets.json', 'w') as f:
        json.dump(vendors, f, indent=2)
    
    with open('email_templates.json', 'w') as f:
        json.dump(templates, f, indent=2)
        
    with open('linkedin_search_queries.json', 'w') as f:
        json.dump(search_queries, f, indent=2)
        
    with open('research_checklist.json', 'w') as f:
        json.dump(checklist, f, indent=2)
    
    # Export vendors to CSV for easy editing
    with open('vendor_targets.csv', 'w', newline='') as f:
        if vendors:
            writer = csv.DictWriter(f, fieldnames=vendors[0].keys())
            writer.writeheader()
            writer.writerows(vendors)
    
    print(f"✅ Created {len(vendors)} target vendor/company records")
    print("✅ Generated email templates for outreach")
    print("✅ Created LinkedIn search queries")
    print("✅ Built research checklist and process")
    
    print("\nFiles created:")
    print("📄 vendor_targets.csv - Edit this to add contacts as you find them")
    print("📄 vendor_targets.json - Structured data version")
    print("📧 email_templates.json - Copy/paste for outreach")  
    print("🔍 linkedin_search_queries.json - Search terms for LinkedIn")
    print("✅ research_checklist.json - Daily/weekly task list")
    
    print("\n🚀 Next Steps:")
    print("1. Open vendor_targets.csv and start researching contacts")
    print("2. Use LinkedIn search queries to find hiring managers")
    print("3. Use email templates for outreach campaigns")
    print("4. Follow the daily/weekly research checklist")
    print("5. Track responses and optimize approach")

if __name__ == "__main__":
    export_all_data()