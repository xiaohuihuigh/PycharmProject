from core import *
import sys
import time
if not os.path.isdir(CONFIG_DIR):
    os.mkdir(CONFIG_DIR)
if not os.path.isfile(os.path.join(CONFIG_DIR,'config.lock')) or sys.argv[1] == 'init' or sys.argv[1] == 'quickinit':
    echon("Uploader initialization will be begin. If you have already configured the uploader before, your old settings will be overwritten.")
    continueornot()
    du_init(sys.argv[1] == 'quickinit')
    with open(os.path.join(CONFIG_DIR,'config.lock'),'a+')as f:
        f.write(time.time())
    exit()
with open(os.path.join(CONFIG_DIR,'access_token'),'r')as f:
    access_token = f.read()
with open(os.path.join(CONFIG_DIR,'refresh_token'),'r')as f:
    refresh_token = f.read()
if refresh_token:
    with open(os.path.join(CONFIG_DIR, 'appkey'), 'r')as f:
        appkey = f.read()
    with open(os.path.join(CONFIG_DIR, 'appsec'), 'r')as f:
        appsec = f.read()
    token_array =do_oauth_refresh(appkey,appsec,refresh_token)
    if token_array["access_token"] and token_array["refresh_token"]:
        access_token = token_array["access_token"]
        refresh_token = token_array["refresh_token"]
        with open(os.path.join(CONFIG_DIR, 'access_token'), 'w')as f:
            f.write(access_token)
        with open(os.path.join(CONFIG_DIR, 'refresh_token'), 'w')as f:
             f.write(refresh_token)
if sys.argv[1] == 'quota':
    quota = get_quota(access_token)
    u = quota['used']/1024/1024/1024
    a = quota['quota']/1024/1024/1024
    echon("Your Storage Status: %.2fG/%.2fG (%.2f%%)"%(u,a,u/a*100))
elif sys.argv[1] == 'upload':
    if len(sys.argv)<3:
        echon("Missing parameters. Please check again.")
        exit()
    res = upload_file(access_token,sys.argv[3],sys.argv[2])
#
elif sys.argv[1] == 'download':
    pass
    if len(sys.argv)<3:
        echon("Missing parameters. Please check again.")
        exit()
    if sys.argv[3][1] == '/':
        sys.argv[3] = sys.argv[3]["1:"]
    with open(os.path.join(CONFIG_DIR,'appname'),'r')as f:
        appname = f.read()
    path = "/apps/{}/{}".format(appname,sys.argv[3])
