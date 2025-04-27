print("✅ run.py is being executed...")
from flask_talisman import Talisman

from app import create_app

app = create_app()

# Set relaxed CSP
csp = {
    'default-src': ["'self'"],
    'style-src': ["'self'", 'https://cdn.jsdelivr.net'],
}

Talisman(app, content_security_policy=csp)

if __name__ == '__main__':
    print("🚀 Starting Flask App...")
    app.run(debug=True)


