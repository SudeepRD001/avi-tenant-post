# 🚀 AVI Load Balancer – Tenant Creation (Postman & Python)

This project demonstrates how to create a tenant in the **VMware AVI Load Balancer Controller** using:
- ✅ Postman (with manual session + CSRF handling)
- ✅ Python script (automated using `requests`)

---

## 📌 Task Details

- **Controller URL**: [https://35.200.176.139](https://35.200.176.139)
- **Login Credentials**:
  - Username: `hiring-2`
  - Password: `hiring-2`
- **Time Window**: *Accessible only between 7 PM – 11 PM*

---
## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SudeepRD001/avi-tenant-post.git
cd avi-tenant-post
```
### 2. Create & Activate Virtual Environment

### Create Virtual Environment
```bash
python -m venv venv
```
### Activate Virtual Environment
```bash
venv\Scripts\activate # Windows
source venv/bin/activate # macOS / Linux
```
### 🧪 Python Script Usage

### 🔧 Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
```
### Run the script
```bash
python create_tenant.py
```
### 🧠 What It Does

This script performs the following actions:

1. Logs into the AVI Controller via `/login`.
2. Retrieves a CSRF token and session cookie for authentication.
3. Sends a `POST` request to `/api/tenant` with the following payload to create a new tenant:

```json
{
  "name": "Enter_Your_Name"
}
```
---

# 📮 Postman Workflow

## 🔐 Step-by-Step: Login to AVI Controller

### 1. Login

- **Method**: `POST`  
- **URL**: `https://35.200.176.139/login`  
- **Body** (raw JSON):

```json
{
  "username": "hiring-2",
  "password": "hiring-2"
}
```

### 2. Capture Cookies
After a successful login, copy the following values from the response cookies:

- avi-sessionid
- csrftoken

### 3. Send Tenant POST Request

- **Method**: `POST`  
- **URL**: `https://35.200.176.139/api/tenant` 
- **Headers:**

| Key               | Value                          |
|------------------|--------------------------------|
| Content-Type      | application/json               |
| X-CSRFToken       | `<paste CSRF token>`           |
| Referer           | https://35.200.176.139         |
| Cookie            | `avi-sessionid=<your-session>` |

> 🔐 *Make sure to replace `<paste CSRF token>` and `avi-sessionid` with actual values from the login response.*

- **Body** (raw JSON):

```json
{
  "name": "Enter_Your_Name",
  "description": "Tenant created for testing CSRF",
  "config_settings": {
    "se_in_provider_context": true,
    "tenant_access_to_provider_se": true,
    "tenant_vrf": false
  }
}
```
---

## 🔗 Resources

- [AVI API Documentation](https://avinetworks.com/docs/)
- [Python `requests` Library Documentation](https://docs.python-requests.org/)
- [Postman Documentation](https://learning.postman.com/docs/)
---
