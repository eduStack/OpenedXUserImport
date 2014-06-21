import commands
import time
file = open('user.txt')

for line in file:
    line = line[:-1]
    info= "Try to add user "+line
    print info
    log = open('user.log', 'a')
    log.write(info+'\n')
    log.close()
    my_cmd="sudo -u www-data /edx/bin/python.edxapp /edx/app/edxapp/edx-platform/manage.py lms --settings aws create_user -e %s -p edx " % (line)
    user_cmd_op=commands.getstatusoutput(my_cmd)
    if len(user_cmd_op[1])>510:
        log = open('user.err', 'a')
        error= "Something wrong when add user:\n"+ line + "\nMessage:\n" +user_cmd_op[1]+ "\n"
        print error
        log.write(info+'\n'+error)
        log.close()
    time.sleep(2)
file.close()
