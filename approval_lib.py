import requests
import time
import json
import os
import uuid

# Configuration
# You can load this from config.json or env variables in your actual projects
CONFIG_FILE = "config_gas.json"

def _load_gas_url():
    """Tries to load GAS URL from local config, otherwise asks user."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("gas_url", "")
        except: pass
    return ""

def request_approval(title, context_str, project_name="Python Script", timeout=300):
    """
    Sends an approval request to Line Bot and waits for User decision.
    
    Args:
        title (str): The concise title of the action (e.g., "Delete 5 Files").
        context_str (str): Detailed description (e.g., "Files: A.py, B.py...").
        project_name (str): Identifier for the calling script.
        timeout (int): Max wait time in seconds (default 300s = 5 mins).
        
    Returns:
        bool: True if Approved, False if Rejected or Timed Out.
    """
    gas_url = _load_gas_url()
    if not gas_url:
        print("❌ Error: config_gas.json not found or missing 'gas_url'.")
        print("   Hint: Copy config_gas.example.json to config_gas.json and fill in your GAS URL.")
        return False
        
    request_id = str(uuid.uuid4())
    print(f"⏳ [{project_name}] Requesting Approval: {title}...")
    
    # 1. Send Request
    try:
        payload = {
            "type": "approval_request",
            "requestId": request_id,
            "project": project_name,
            "title": title,
            "context": context_str,
            "timestamp": time.time()
        }
        resp = requests.post(gas_url, json=payload)
        if resp.status_code != 200:
            print(f"❌ Failed to send request: {resp.text}")
            return False
        print("   -> Request sent to Line. Waiting for response...")
    except Exception as e:
        print(f"❌ Network Error: {e}")
        return False

    # 2. Polling Loop
    start_time = time.time()
    while (time.time() - start_time) < timeout:
        try:
            # Check Status via GET
            # GAS doGet needs generic handling or specific param
            # We assume GAS doGet handles ?action=check_status&requestId=...
            status_url = f"{gas_url}?action=check_status&requestId={request_id}"
            status_resp = requests.get(status_url)
            
            if status_resp.status_code == 200:
                result = status_resp.json() # Expect { status: "PENDING" | "APPROVED" | "REJECTED" }
                status = result.get("status", "PENDING")
                
                if status == "APPROVED":
                    print("✅ Approval Granted!")
                    return True
                elif status == "REJECTED":
                    print("❌ Approval Rejected by User.")
                    return False
                # Else Continue Waiting
                
            time.sleep(3) # Poll every 3 seconds
            print(".", end="", flush=True)
            
        except KeyboardInterrupt:
            print("\n⛔ Cancelled by User (Ctrl+C).")
            return False
        except Exception as e:
            pass # Ignore polling errors (retry)
            
    print(f"\n⏰ Timeout ({timeout}s). Auto-rejecting.")
    return False
