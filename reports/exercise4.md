# Bug reports for exercise4.py

Line: 4
Problem: The docstring says "true if the password is the admin password", but the current code returns True when the password is empty or different from "admin123". Specifically, it returns True when password is empty (since ADMIN_PASSWORD is not empty and password == ADMIN_PASSWORD fails, so the condition becomes false). Actually, the condition is flawed: it returns True only if ADMIN_PASSWORD is not empty AND password equals ADMIN_PASSWORD. But if password is empty, it will return False, which is correct. However, the hardcoded password "admin123" in the code violates security principles — it should not be hardcoded. The docstring implies the function should verify the password against a secret, but using a hardcoded value makes it vulnerable to exposure and bypass. This is a security bug.
Example: check_admin("admin123") returns True, expected True (correct), but check_admin("") returns False, expected False (correct), but the hardcoded password is a security risk. An attacker can see the password directly from the source code.
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

Line: 14
Problem: The function uses string formatting without escaping, which allows SQL injection. The docstring says "The user's row, or None if the username does not exist", but it builds a SQL query with user input directly in a string, which can be exploited by an attacker. For example, an attacker could pass a username like ' OR '1'='1' to get unauthorized access.
Example: find_user(db, "'; DROP TABLE users; --") returns a row (or error) instead of None, which violates security and can lead to data loss or unauthorized access.
Fix: return db.execute(f"SELECT * FROM users WHERE username = ?", (username,)).fetchone()
