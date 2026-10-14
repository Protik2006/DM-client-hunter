import os
import json
import gspread
from google.oauth2.service_account import Credentials

def save_to_google_sheets(leads):
    creds_json = os.environ.get("GCP_SERVICE_ACCOUNT_JSON")
    sheet_id = os.environ.get("GOOGLE_SHEET_ID")
    
    if not creds_json or not sheet_id:
        print("Error: Missing credentials or Sheet ID.")
        return

    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds_dict = json.loads(creds_json)
    creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id).sheet1

    print("Saving leads to Google Sheets...")
    for lead in leads:
        sheet.append_row([lead['name'], lead['service_needed'], lead['contact'], "New"])
    
    print("Leads saved successfully!")

def hunt_clients():
    print("Searching for digital marketing clients...")
    
    # টেস্ট লিড ডাটা
    scraped_leads = [
        {"name": "E-commerce Shop BD", "service_needed": "Facebook & Google Ads", "contact": "info@ecomshop.com"},
        {"name": "Sylhet Agency", "service_needed": "SEO & YouTube SEO", "contact": "contact@sylhetagency.com"}
    ]
    
    if scraped_leads:
        save_to_google_sheets(scraped_leads)

if __name__ == "__main__":
    hunt_clients()
