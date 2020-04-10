import smtplib
from email.mime.text import MIMEText

title = 'My title'
msg_content = '''
  PROTECT YOURSELF FROM CORONAVIRUS - SHIPPING FROM USA WAREHOUSES - 24H DELIVERY

<a href="https://bit.ly/2RcNsGX" target="_parent"><img src="https://ae01.alicdn.com/kf/Hc9243ac65d4846219bf692ffd3d4e42fa/M-scara-quir-rgica-DHL-EMS-500-Uds-KF94-m-scara-facial-m-scaras-m-dicas.jpg"></a></p><a href="https://s.click.aliexpress.com/e/_dYxU6u8" target="_parent"><span style="display: block;">AliExpress.com Product - ANTICORONAVIRUS FDA APROVED MASKS</span><p><br>
    '''

message = MIMEText(msg_content, 'html')
message['From'] = 'ANTICORONAVIRUS MASKS <peter@cheap.dx.am >'
message['Subject'] = 'ANTICORONAVIRUS MASKS'

msg_full = message.as_string()

server = smtplib.SMTP('31.47.37.50:25')
#Auth login --> admin/null in Base64
server.docmd("auth login")
server.docmd("YWRtaW4=")
server.docmd("AA==")
server.set_debuglevel(1)

#mail-lists
archivo = open("/etc/2.txt", "r")
for linea in archivo.readlines():
    server.sendmail('peter@cheap.dx.am',
                [linea],
                msg_full)
    print(linea)
archivo.close() 
server.quit()