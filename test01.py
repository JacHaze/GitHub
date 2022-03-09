host = "128.127.130.18"
port = 22
username = "cyril"
password = "S9z34zmi!"
command = "sudo -S bash "
command2 = "shutdown -r now"
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)

stdin, stdout, stderr = ssh.exec_command(command2)
lines2 = stdout.readlines()
print (lines2)
ssh.close()
