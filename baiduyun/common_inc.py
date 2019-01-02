import subprocess
import os
def echon(str, debug=False, color=34):
    if debug:
        print('error:',str)
    else:
        print(str)

#
def getpath(path):
    return path
    pass
def oaerr(arr, exitonerror=1):
    if 'error' in arr:
        echon('OAuth error {} : {}'.format(arr['error'],arr['error_description']))
        if exitonerror:
            exit()
        return False
    return True

def apierr(arr, exitonerror=1):
    if 'error_code' in arr:
        echon('OAuth error {} : {}'.format(arr['error_code'],arr['error_msg']))
        if exitonerror:
            exit()
        return False
    return True

def continueornot():
    yn = raw_input('Continue?[y/N]:')
    if yn == 'n' or yn == 'N':
        exit()

def cmd(cfe,ispopen=False):
    if ispopen:
        handle = subprocess.Popen(cfe)
    # pass
    res = ''
    echon(cfe,True)
    if cfe:
        p = os.popen(cfe)
        res = p.read()
        p.close()
    echon(res,True)
    return res

def do_api(url, param, method='POST'):
    if method == 'POST':
        cmds = "curl -X POST -k -L --data {} {}".format(param,url)
    else:
        cmds = "curl -X {} -k -L {}?{}".format(method,url,method)
    return cmd(cmds)
def error_handle(errno,errstr,errfile,errline):
    if errno == 'E_USER_ERROR':
        echon("Fatal ERROR :{} ({}) {}".format(errfile,errline,errstr))
        echon("Exiting with a fatal error.")
        exit(9002)
    elif errno == 'E_USER_WARRING':
        echon("WARNING : {} ({}) {}".format(errfile,errline,errstr))
    elif errno == 'E_USER_NOTICE':
        echon("Notice : {} ({}) {}".format(errfile, errline, errstr))
    else:
        echon("err{} : {} ({}) {}".format(errno, errfile, errline, errstr))
    return True
