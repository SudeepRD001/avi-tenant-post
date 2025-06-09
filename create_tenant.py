import requests
import urllib3

# Disable SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Base URL
base_url = "https://35.200.176.139"

# Step 1: Login
login_url = f"{base_url}/login"
credentials = {
    "username": "hiring-2",
    "password": "hiring-2"
}

session = requests.Session()

# Login
login_response = session.post(login_url, json=credentials, verify=False)

# Check if login successful
if login_response.status_code != 200:
    print("❌ Login failed.")
    print("Status Code:", login_response.status_code)
    print("Response:", login_response.text)
    exit()

print("✅ Login successful.")

# Step 2: Get CSRF token from cookies
csrf_token = session.cookies.get('csrftoken') or session.cookies.get('csrf_token')
if not csrf_token:
    print("❌ CSRF token not found in cookies.")
    exit()

# Step 3: Prepare tenant creation request
tenant_url = f"{base_url}/api/tenant"
tenant_data = {
    "name": "Sudeep_R_Doddamani"
}

headers = {
    "Content-Type": "application/json",
    "X-CSRFToken": csrf_token,
    "Referer": base_url + "/tenant"
}

# POST tenant with CSRF token and session cookie
response = session.post(tenant_url, json=tenant_data, headers=headers, verify=False)

if response.status_code == 201:
    print("✅ Tenant created successfully!")
    print(response.json())
else:
    print("❌ Failed to create tenant.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
