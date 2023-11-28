import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import netifaces as ni
import time

# Configurações de email
SEU_EMAIL = 'raphaeldiniz@alunos.utfpr.edu.br'
SEU_EMAIL_PASSWORD = 'gbrv aukt ecyj sdnu'
DESTINATARIO_EMAIL = 'dinizraphael45@gmail.com'


def get_ipv4_address():
    try:
        # Obtém o endereço IPv4 da interface wlp0s20f3
        ni.ifaddresses('wlp0s20f3')
        ip_address = ni.ifaddresses('wlp0s20f3')[ni.AF_INET][0]['addr']
        return ip_address
    except Exception as e:
        print(f"Erro ao obter o endereço IPv4: {str(e)}")
        return None

def send_email(subject, message):
    try:
        # Configura a conexão com o servidor SMTP do Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SEU_EMAIL, SEU_EMAIL_PASSWORD)

        # Cria a mensagem de email
        msg = MIMEMultipart()
        msg['From'] = SEU_EMAIL
        msg['To'] = DESTINATARIO_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Envia o email
        server.sendmail(SEU_EMAIL, DESTINATARIO_EMAIL, msg.as_string())
        print("Email enviado com sucesso!")
        server.quit()
    except Exception as e:
        print(f"Erro ao enviar o email: {str(e)}")

if __name__ == "__main__":
    # Obtém o endereço IPv4
    ipv4_address = get_ipv4_address()

    if ipv4_address:
        subject = "Novo Endereço IPv4"
        message = f"Seu novo endereço IPv4 é: {ipv4_address}"
        send_email(subject, message)
