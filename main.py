#!/usr/bin/env python3
"""
Mobile Number Lookup Tool - Termux Edition
Powered By ZAP PAPA

A CLI tool to look up mobile number details via a REST API.
Designed for Termux (Android Linux environment).
GitHub-ready, zero-config installation.
"""

import requests  # HTTP requests library
import json      # JSON parsing (for manual use, though requests handles it)
import sys       # System-specific parameters (exit codes)
import os        # OS interface (clear screen)
import re        # Regular expressions (input validation)


# ─── Configuration ───────────────────────────────────────────────────────────

API_URL = "https://anishexploits.com/api/api.php?key=KEY_AE2E95D4_ZAP3X&type=number&num="

# Base URL only — full URL built as: API_URL + <phone_number>


# ─── Helper Functions ─────────────────────────────────────────────────────────

def clear_screen():
    """Clear the terminal screen for a clean UI."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    """Display a professional ASCII banner."""
    banner = r"""
╔═══════════════════════════════════════════╗
║        MOBILE NUMBER LOOKUP TOOL          ║
║           Termux Edition v1.0             ║
╚═══════════════════════════════════════════╝
    """
    print(banner)


def validate_number(number):
    """
    Validate a 10-digit Indian mobile number.
    
    Args:
        number (str): The raw input string.
    
    Returns:
        bool: True if valid 10-digit number, False otherwise.
    """
    # Must be exactly 10 digits, only numeric characters
    return bool(re.fullmatch(r'\d{10}', number))


def fetch_number_details(number):
    """
    Send API request and parse the JSON response.
    
    Args:
        number (str): Valid 10-digit mobile number.
    
    Returns:
        tuple: (success_flag, data_or_error_message)
               success_flag=True  → data is a list of records
               success_flag=False → data is an error string
    """
    url = API_URL + number
    
    try:
        # Send GET request with a timeout (prevents hanging)
        response = requests.get(url, timeout=15)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse JSON response
        data = response.json()
        
        # Check API status
        if data.get("status") != "success":
            return False, "⚠ API Error"
        
        # Extract the "result" array — IGNORE everything else
        records = data.get("result", [])
        
        if not records:
            return False, "❌ No information found"
        
        return True, records
        
    except requests.exceptions.Timeout:
        return False, "⚠ API Error (Request timed out)"
    except requests.exceptions.ConnectionError:
        return False, "⚠ API Error (Connection failed)"
    except requests.exceptions.RequestException:
        return False, "⚠ API Error"
    except (json.JSONDecodeError, ValueError):
        return False, "⚠ API Error (Invalid response)"


def display_records(records):
    """
    Format and print record(s) to the console.
    
    Only the 'result' array is displayed. Fields:
        fname, name, aadhar, address, alt, circle, email, num
    
    Args:
        records (list): List of record dictionaries from the API.
    """
    for index, record in enumerate(records, start=1):
        # Record separator header
        print(f"\n──────── #{index}────────")
        
        # Extract fields with safe defaults
        fname    = record.get("fname", "N/A") or "N/A"
        name     = record.get("name", "N/A") or "N/A"
        aadhar   = record.get("aadhar", "N/A") or "N/A"
        address  = record.get("address", "N/A") or "N/A"
        alt      = record.get("alt", "N/A") or "N/A"
        circle   = record.get("circle", "N/A") or "N/A"
        email    = record.get("email", "N/A") or "N/A"
        mobile   = record.get("num", "N/A") or "N/A"
        
        # Print formatted output
        print(f"👤 Name: {name}")
        print(f"👨 Father Name: {fname}")
        print(f"🆔 Aadhaar: {aadhar}")
        print(f"📍 Address: {address}")
        print(f"📞 Alternate Number: {alt}")
        print(f"🌐 Circle: {circle}")
        print(f"📧 Email: {email}")
        print(f"📱 Mobile: {mobile}")
    
    # Footer after all records
    print("\n" + "━" * 20)
    print("⚡ Powered By ZAP PAPA")
    print("━" * 20)


def main():
    """Main program loop: prompt → validate → fetch → display → repeat."""
    
    clear_screen()
    print_banner()
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter Number: ").strip()
            
            # Check for exit command
            if user_input.lower() == "exit":
                print("\n[✓] Exiting... Goodbye!\n")
                sys.exit(0)
            
            # Validate 10-digit number
            if not validate_number(user_input):
                print("Invalid Number")
                continue
            
            # Fetch details from API
            success, result = fetch_number_details(user_input)
            
            if success:
                display_records(result)
            else:
                print(result)  # Error message string
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n[✓] Interrupted. Exiting...\n")
            sys.exit(0)
        except EOFError:
            # Handle Ctrl+D gracefully
            print("\n\n[✓] Exiting...\n")
            sys.exit(0)


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
