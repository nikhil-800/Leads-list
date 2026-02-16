#!/usr/bin/env python3
"""
AI/ML Vendor Research Automation Script
Finds hiring vendors and HR contacts for Team-Soft LLC
"""

import requests
import csv
import json
from bs4 import BeautifulSoup
import time
import pandas as pd

class VendorResearcher:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.results = []
    
    def search_indeed_jobs(self):
        """Search Indeed for AI/ML contract positions"""
        print("Searching Indeed for AI/ML positions...")
        
        search_terms = [
            "artificial intelligence engineer contract",
            "machine learning engineer contract", 
            "data scientist contract",
            "AI engineer remote contract"
        ]
        
        for term in search_terms:
            url = f"https://www.indeed.com/jobs?q={term.replace(' ', '+')}&l=Remote"
            try:
                response = self.session.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    jobs = soup.find_all('div', class_='job_seen_beacon')
                    
                    for job in jobs[:10]:  # Limit to 10 per search
                        company_elem = job.find('span', class_='companyName')
                        title_elem = job.find('h2', class_='jobTitle')
                        
                        if company_elem and title_elem:
                            company = company_elem.get_text(strip=True)
                            title = title_elem.get_text(strip=True)
                            
                            self.results.append({
                                'source': 'Indeed',
                                'company': company,
                                'position': title,
                                'search_term': term,
                                'status': 'found'
                            })
                
                time.sleep(2)  # Rate limiting
            except Exception as e:
                print(f"Error searching Indeed for {term}: {e}")
    
    def search_prime_vendors(self):
        """Research known prime vendors"""
        print("Researching prime vendors...")
        
        prime_vendors = [
            "Kelly Services",
            "Robert Half Technology",
            "Randstad Technologies", 
            "TEKsystems",
            "Insight Global",
            "Apex Systems",
            "Modis",
            "CyberSeek"
        ]
        
        for vendor in prime_vendors:
            print(f"Researching {vendor}...")
            self.results.append({
                'source': 'Prime Vendor List',
                'company': vendor,
                'position': 'Target Vendor',
                'search_term': 'prime_vendor',
                'status': 'research_needed'
            })
    
    def find_company_contacts(self, company_name):
        """Find HR/hiring manager contacts for a company"""
        print(f"Finding contacts for {company_name}...")
        
        # This would typically use LinkedIn API or scraping
        # For now, we'll create placeholder structure
        return {
            'company': company_name,
            'hr_contact': f"hr@{company_name.lower().replace(' ', '')}.com",
            'hiring_manager': "TBD - needs LinkedIn research",
            'phone': "TBD",
            'notes': "Needs manual LinkedIn research"
        }
    
    def generate_email_templates(self):
        """Generate email templates for outreach"""
        templates = {
            'initial_contact': '''
Subject: AI/ML Staffing Partnership - Team-Soft LLC

Hi {contact_name},

I'm reaching out from Team-Soft LLC, a specialized IT staffing firm focusing on high-demand technology roles.

We have a strong bench of AI/ML engineers, data scientists, and software engineers available for:
- Corp-to-Corp (C2C) arrangements  
- Contract-to-Hire (C2H)
- 1099 independent contractor roles

I noticed {company_name} has been hiring for {position_type} roles. We specialize in hard-to-fill positions and can provide qualified candidates quickly.

Would you be open to a brief call to discuss partnership opportunities?

Best regards,
[Your Name]
Team-Soft LLC
''',
            'follow_up': '''
Subject: Following up - AI/ML Staffing Solutions

Hi {contact_name},

Following up on my previous email about staffing partnership opportunities between Team-Soft LLC and {company_name}.

Our candidates specialize in:
- AI/ML Engineering
- Data Science & Analytics  
- DevOps & Cloud Architecture
- Software Engineering

We work exclusively on C2C, C2H, and 1099 basis, making us ideal for companies needing specialized talent without long-term commitments.

Quick 15-minute call this week?

Best,
[Your Name]
'''
        }
        
        return templates
    
    def export_results(self):
        """Export results to CSV and JSON"""
        print("Exporting results...")
        
        # Export to CSV
        df = pd.DataFrame(self.results)
        df.to_csv('/Users/nikhil_muddappa/.openclaw/workspace/vendor_research_results.csv', index=False)
        
        # Export to JSON  
        with open('/Users/nikhil_muddappa/.openclaw/workspace/vendor_research_results.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        # Generate email templates
        templates = self.generate_email_templates()
        with open('/Users/nikhil_muddappa/.openclaw/workspace/email_templates.json', 'w') as f:
            json.dump(templates, f, indent=2)
        
        print(f"Found {len(self.results)} potential vendors/contacts")
        print("Results exported to:")
        print("- vendor_research_results.csv")  
        print("- vendor_research_results.json")
        print("- email_templates.json")
    
    def run_automation(self):
        """Execute the full automation pipeline"""
        print("Starting AI/ML Vendor Research Automation...")
        print("=" * 50)
        
        # Research prime vendors
        self.search_prime_vendors()
        
        # Search job boards 
        self.search_indeed_jobs()
        
        # Export results
        self.export_results()
        
        print("=" * 50)
        print("Automation completed!")
        print("\nNext steps:")
        print("1. Review vendor_research_results.csv")
        print("2. Use LinkedIn to find HR contacts for each company")
        print("3. Use email_templates.json for outreach")
        print("4. Set up CRM tracking for follow-ups")

if __name__ == "__main__":
    researcher = VendorResearcher()
    researcher.run_automation()