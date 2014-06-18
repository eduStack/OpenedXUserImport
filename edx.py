import commands

file = open("user.txt")

for line in file:
    line = line[:-1]
    print "Try to add user "+line
    my_cmd="sudo -u www-data /edx/bin/python.edxapp /edx/app/edxapp/edx-platform/manage.py lms --settings aws create_user -e %s -p edx -s " % (line)
    user_cmd_op=commands.getstatusoutput(my_cmd)
    if len(user_cmd_op[1])>515:
        print "Something wrong when add user:\n"+ line + "\nMessage:\n" +user_cmd_op[1]+ "\n"
        break
