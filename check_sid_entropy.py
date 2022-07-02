#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import math
import sys


class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class CheckEntropy:
    def __init__(self, session_id):
        self.session_id = session_id

    def __get_check_entropy(self):
        sid = self.session_id.strip()
        sid_char_len = len(sid)
        sid_len = len(list(set(list(sid))))
        sid_strength = round(math.log2(sid_len ** sid_char_len), 1)
        sid_result = Colors.GREEN+"Good"+Colors.RESET
        if int(sid_strength) < 128:
            sid_result = Colors.RED+"Vulnerable"+Colors.RESET
        return sid_len, sid_char_len, sid_strength, sid_result

    def get_check(self):
        try:
            data = self.__get_check_entropy()
            ret = """
            + Session ID Check Entropy + 
            Session ID : {sid}
            String Length : {sid_len}
            Characters : {sid_char_len} Type
            Strength : {sid_strength} Bit
            Result : {sid_result}
            """.format(sid=self.session_id, sid_len=data[1], sid_char_len=data[0], sid_strength=data[2], sid_result=data[3])
            return ret
        except Exception as err:
            print("Check Error:: {err}".format(err=err))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Check Session ID Entropy Bit', description='Check Session ID Entropy Bit')
    try:
        parser.add_argument('-s', '--session', dest='sid', type=str, help='Session ID')
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
        args = parser.parse_args()
        if not args.sid:
            print("Input Session ID")
            sys.exit(0)
        ce = CheckEntropy(args.sid)
        print(ce.get_check())
        sys.exit(0)
    except Exception as err:
        print("main:: {err}".format(err=err))
        sys.exit(0)
