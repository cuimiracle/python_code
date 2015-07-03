#!/usr/bin/env python
# -*- coding:utf-8 -*- 

# python configRsync.py --path /var/www/html --user cui --password 123456 --uid emily --gid emily
import getopt,sys,os,re
from optparse import OptionParser 
from stat import S_IWRITE, S_IREAD

rsyncd_config_file = '/etc/rsync/rsyncd.conf';
secrets_config_file = '/etc/rsync/rsyncd.secrets';

path = auth_users = auth_users_password = secrets_file = uid = gid = '';
max_connections = 5;

try:
    if os.geteuid() != 0:
        raise Exception("This script must be run as root.");

    #--uid emily --gid emily
    opts,args = getopt.getopt(sys.argv[1:],"h",["max_connections=", "path=", "user=", "password=", "secrets_file=", "uid=", "gid=", "help"])
   
    for key,value in opts: 
        if key in ("-h", "--help"):
            MSG_USAGE = "configRsync.py --path <dirname> --user <username> --password <password> [--max_connections <number>] [--secrets_file <filename>] [--uid <username>] [--gid <groupname>]" 
            
            optParser = OptionParser(MSG_USAGE) 
            optParser.add_option("--path", help = "backup dirname path");
            optParser.add_option("--user", help = "auth user name");
            optParser.add_option("--password", help = "auth user password");
            optParser.add_option("--max_connections", help = "max connections of server");
            optParser.add_option("--secrets_file", help = "file to save auth user information");
            optParser.add_option("--uid", help = "uid of backup dirname");
            optParser.add_option("--gid", help = "gid of backup dirname");
            
            optParser.print_help();
            exit();
        elif key in ("--max_connections"):
            max_connections = value;
        elif key in ("--path"):
            path = value;
        elif key in ("--user"):
            auth_users = value;
        elif key in ("--password"):
            auth_users_password = value;
        elif key in ("--secrets_file"):
            secrets_file = value;
        elif key in ("--uid"):
            uid = value;
        elif key in ("--gid"):
            gid = value;
        
            
    gid = uid;
    if gid == '':
        uid = gid = 'root';
    if secrets_file == '':
        secrets_file = secrets_config_file;
    
    if path == '':
        raise Exception("path is none.")
    if auth_users == '':
        raise Exception("user is none.")
    if auth_users_password == '':
        raise Exception("password is none.")
    
    
    if not os.path.isdir(os.path.dirname(rsyncd_config_file)):
        os.makedirs(os.path.dirname(rsyncd_config_file));
    
    if not os.path.isdir(os.path.dirname(secrets_file)):
        os.makedirs(os.path.dirname(secrets_file));
   
    file_handle = open(rsyncd_config_file, 'w');
    file_handle.write('uid = ' + uid + '\ngid = ' + gid + '\nuse chroot = no\nmax connections = ' + str(max_connections) + '\npid file = /var/run/rsyncd.pid\nlock file = /var/run/rsync.lock\nlog file = /var/log/rsyncd.log\n\n[server]\npath = ' + path + '\nauth users = ' + auth_users + '\nignore errors\nsecrets file = ' + secrets_file + '\nread only = no');
    file_handle.close()
    
    file_handle = open(secrets_file, 'w');
    file_handle.write(auth_users + ':' + auth_users_password);
    file_handle.close()
    os.chmod(secrets_file, S_IREAD + S_IWRITE);
    
    # get rc.local path
    file_handle = os.popen("whereis rc.local")
    rc_path = file_handle.read()
    rc_path_matches = re.search(".*(\s+.+rc\.local\s+).*", rc_path);
    if rc_path_matches == None:
        raise Exception("lack of the file: rc.local")
    else:
        rc_path = rc_path_matches.group(1);
        rc_path = rc_path.strip()
    
    rc_list = [];
    for line in open(rc_path, 'r'):  
        if line.find('/usr/bin/rsync --daemon') == -1 and line.find('#rsync') == -1:
            rc_list.append(line);
            
    rc_list.append("lsof -i :873 | awk '{IGNORECASE=1;}/rsync(.+)root/{print $2}' > /tmp/savevar #rsync\n");
    rc_list.append('read savevar < /tmp/savevar #rsync\n');
    rc_list.append('if [ "$savevar" != "" ]; then #rsync\n');
    rc_list.append('    kill $savevar #rsync\n');
    rc_list.append('fi #rsync\n');

    rc_list.append('/usr/bin/rsync --daemon --config=' + rsyncd_config_file + '\n');
    
    file_handle = open(rc_path, 'w');
    file_handle.write(''.join(rc_list));
    file_handle.close()
    
    os.popen('iptables -D INPUT -p tcp --dport 873 -j ACCEPT');
    os.popen('iptables -I INPUT -p tcp --dport 873 -j ACCEPT');
    file_handle = os.popen('service iptables save');
    output = file_handle.read();
    if output.find('FAILED') != -1:
        raise Exception('Failed to allow 873 port in iptables.');
    
#     file_handle = os.popen('/usr/bin/rsync --daemon --config=' + rsyncd_config_file);
#     output = file_handle.read();
#   
#     if output:
#         raise Exception(output);
    
    print "Config rsync [ OK ]";
except Exception as err:
    print "Failed to config rsync.\nError message:";
    print err;
    exit();
    







