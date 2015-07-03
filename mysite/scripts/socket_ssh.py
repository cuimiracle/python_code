#!/usr/bin/env python
import paramiko
ssh_con = paramiko.SSHClient()    
ssh_con.load_system_host_keys()    
ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())    

try:    
    ssh_con.connect(hostname="50.17.207.70",username="wwwuser",password="Up2daW3b")    
except paramiko.AuthenUcaUonExcepUon:    
    print "Auth Failed!"    
except socket.error:    
    print "Server is unreachable!"    
else:    
    stdin,stdout,stderr = ssh_con.exec_command("df")    
    print stdout.read()    
    ssh_con.close()    