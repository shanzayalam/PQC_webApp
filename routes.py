from flask import Blueprint, render_template, request
from .crypto_utils import generate_keys, encrypt_message, decrypt_message

main = Blueprint('main', __name__)

# Temporary storage
current_keys = {}
current_result = {}

@main.route('/', methods=['GET', 'POST'])
def index():
    global current_keys, current_result

    if request.method == 'POST':
        # Check which button was pressed
        if 'generate' in request.form:
            current_keys = generate_keys()
            current_result = {}

        elif 'encrypt' in request.form:
            message = request.form.get('message')
            pub_key = request.form.get('pub_key')
            if message and pub_key:
                current_result = {'encrypted': encrypt_message(message, pub_key)}
            else:
                current_result = {'error': 'Message or Public Key missing!'}

        elif 'decrypt' in request.form:
            ciphertext = request.form.get('ciphertext')
            priv_key = request.form.get('priv_key')
            if ciphertext and priv_key:
                current_result = {'decrypted': decrypt_message(ciphertext, priv_key)}
            else:
                current_result = {'error': 'Ciphertext or Private Key missing!'}

    return render_template('index.html', keys=current_keys, result=current_result)