
import paramiko
def Arp(ip, tim):
    s = paramiko.SSHClient() 
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
    s.connect("192.168.0.141",22,"root", "wsy456")   
    while True:
        s.exec_command("sed -i '$d' /home/nancy/yy.py")
        s.exec_command('echo "sha('+ "'" + ip + "'" +  ',' + tim +')" >> /home/nancy/yy.py')
        s.exec_command("python /home/nancy/yy.py")
        s.close()
        break
