import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json

# Path to the firebase service account credentials key
KEY_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'firebase-key.json')

db = None
firebase_initialized = False
firebase_disabled = False

import streamlit as st

def initialize_firebase():
    """Initializes Firebase Admin SDK using credentials from secrets, environment variables, or local file."""
    global db, firebase_initialized, firebase_disabled
    if firebase_disabled:
        return False
    if firebase_initialized:
        return True
        
    cred = None
    
    # 1. Try loading from Streamlit secrets (Production Cloud)
    try:
        if hasattr(st, "secrets") and "firebase" in st.secrets:
            cred_dict = dict(st.secrets["firebase"])
            cred = credentials.Certificate(cred_dict)
    except Exception as e:
        print(f"Could not load Firebase from Streamlit secrets: {e}")
        
    # 2. Try loading from environment variable
    if not cred:
        try:
            env_key = os.environ.get("FIREBASE_KEY")
            if env_key:
                cred_dict = json.loads(env_key)
                cred = credentials.Certificate(cred_dict)
        except Exception as e:
            print(f"Could not load Firebase from environment variable: {e}")
            
    # 3. Fallback to local credential key file
    if not cred and os.path.exists(KEY_PATH):
        try:
            cred = credentials.Certificate(KEY_PATH)
        except Exception as e:
            print(f"Error loading Firebase local key file: {e}")

    if cred:
        try:
            # Check if app is already initialized
            try:
                firebase_admin.get_app()
            except ValueError:
                firebase_admin.initialize_app(cred)
            db = firestore.client()
            firebase_initialized = True
            return True
        except Exception as e:
            print(f"Error initializing Firebase SDK: {e}")
            return False
            
    return False

def disable_firebase():
    """Permanently disables Firebase operations for the rest of this execution session."""
    global db, firebase_initialized, firebase_disabled
    firebase_initialized = False
    firebase_disabled = True
    db = None

def get_firestore_client():
    """Returns Firestore client if initialized, otherwise None."""
    if initialize_firebase():
        return db
    return None

def is_firebase_active():
    """Returns True if Firebase is successfully configured and active."""
    return initialize_firebase()
