import subprocess as sp
from scan import scan
from pb import pb
import os
import operator as op
import time

class greenBluetooth:

    def main():
        sc = scan()
        pbs = pb()

        p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
        (stdout, stdin) = (p.stdout, p.stdin)

        data = stdout.readlines()
        myMac = 'FC:2A:9C:86:13:F9'

        while True:
            scan_ = False
            scan_ = sc.scanBt()
            print(scan_)
            for device in data:
                if scan_ == True:
                    if op.eq(device, myMac):

                        pbs.send_notification_via_pushbullet()

            time.sleep(10)

    main() 
