import subprocess
import sqlite3
import os

# Hardcoded secrets (Gitleaks will catch these)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "supersecretpassword123"
GITHUB_TOKEN = "ghp_exampletoken1234567890abcdef"

# SQL Injection (Semgrep will catch this)
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# Command Injection (Semgrep will catch this)
def ping_host(host):
    result = subprocess.run("ping -c 1 " + host, shell=True)
    return result

# Eval injection (Semgrep will catch this)
def calculate(expression):
    return eval(expression)

# Hardcoded password in code (Semgrep will catch this)
def authenticate(username, password):
    if password == "admin123":
        return True
    return False

# Path traversal (Semgrep will c