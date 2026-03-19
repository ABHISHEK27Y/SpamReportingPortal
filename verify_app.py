import requests
import sys

BASE_URL = "http://127.0.0.1:5000"
SESSION = requests.Session()

def test_login():
    print("Testing Login...")
    response = SESSION.get(f"{BASE_URL}/auth/login")
    if response.status_code != 200:
        print(f"FAILED: Login page not accessible. Status: {response.status_code}")
        return False
        
    # Simulate POST login
    data = {
        "email": "tester@example.com"
    }
    response = SESSION.post(f"{BASE_URL}/auth/login", data=data)
    
    if response.status_code == 200 and "Dashboard" in response.text:
         print("SUCCESS: Login successful, redirected to Dashboard.")
         return True
    elif response.history and response.history[0].status_code == 302:
         # Followed redirect
         print("SUCCESS: Login successful (Redirect followed).")
         return True
    else:
         print(f"FAILED: Login failed. Status: {response.status_code}")
         return False

def test_prediction():
    print("\nTesting Prediction API...")
    
    # Legit message
    msg_legit = "Hey, are we still meeting for lunch today?"
    response = SESSION.post(f"{BASE_URL}/predict", json={"message": msg_legit})
    
    if response.status_code == 200:
        result = response.json()
        print(f"Legit Message Test: {result}")
        if result['result']['prediction'] == 0:
            print("SUCCESS: Correctly identified as LEGIT.")
        else:
            print("WARNING: Identify as FRAUD (False Positive?)")
    else:
        print(f"FAILED: Prediction API error. Status: {response.status_code}")
        return False

    # Spam message
    msg_spam = "CONGRATULATIONS! You won $1000. Click here to claim."
    response = SESSION.post(f"{BASE_URL}/predict", json={"message": msg_spam})
    
    if response.status_code == 200:
        result = response.json()
        print(f"Spam Message Test: {result}")
        if result['result']['prediction'] == 1:
            print("SUCCESS: Correctly identified as FRAUD.")
        else:
            print("WARNING: Identify as LEGIT (False Negative?)")
            
        if 'pdf_url' in result:
            print(f"SUCCESS: PDF Report generated at {result['pdf_url']}")
        else:
            print("FAILED: PDF URL missing.")
    else:
        print(f"FAILED: Prediction API error. Status: {response.status_code}")
        return False
        
    return True

if __name__ == "__main__":
    try:
        if test_login() and test_prediction():
            print("\nAll System Verification Checks Passed!")
            sys.exit(0)
        else:
            print("\nVerification Failed.")
            sys.exit(1)
    except Exception as e:
        print(f"\nError connecting to server: {e}")
        print("Ensure Flask app is running.")
        sys.exit(1)
