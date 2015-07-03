from optparse import OptionParser 


MSG_USAGE = "configRsync.py --path <dirname> --user <username> --password <password> [--max_connections <number>] [--secrets_file <filename>] [--uid <username>] [--gid <groupname>]" 

optParser = OptionParser(MSG_USAGE) 
optParser.add_option("--path", help = "backup dirname path");
optParser.add_option("--user", help = "auth user name");
optParser.add_option("--password", help = "auth user password");
optParser.add_option("--max_connections", help = "max connections of server");
optParser.add_option("--secrets_file", help = "file to save auth user information");
optParser.add_option("--uid", help = "uid of backup dirname");
optParser.add_option("--gid", help = "gid of backup dirname");



# fakeArgs = ['-f','file.txt','-v','good luck to you', 'arg2', 'arge'] 
#  
# options, args = optParser.parse_args(fakeArgs) 


# print options.fileName 

# print options.verbose 
# 
# print options 
# 
# print args 

print optParser.print_help() 
