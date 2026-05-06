import subprocess
import sqlite3
import os

# Hardcoded secrets (Gitleaks will catch these)
# AWS-style key (passes format validation)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7ABCD1234"
AWS_SECRET_ACCESS_KEY = "abc123def456ghi789jkl012mno345pqr678stu9"

# Generic high entropy string (triggers generic secret rule)
DB_PASSWORD = "xK9#mP2$nQ7@wL4&vR8"
DATABASE_PASSWORD = "xK9#mP2$nQ7@wL4&vR8"

# Private key pattern
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA2a2rwplBQLF29amygykEMmYz"

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

# Eval injection (Semgrep will catch this!!!)
def calculate(expression):
    return eval(expression)

# Hardcoded password in code (Semgrep will catch this)
def authenticate(username, password):
    if password == "Y4theirth6;":
        return True
    return False

# Path traversal (Semgrep will c
