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


class CheckCharacters:
    """
    # Lower Case : 26
    # Upper Case : 26
    # Lower & Upper Case : 52
    # Arabic numerals : 10
    # Lower Case & Arabic numerals : 36
    # Upper Case & Arabic numerals : 36
    # Lower & Upper Case & Arabic numerals : 62
    """

    def __init__(self, sid):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.arabic_numerals = '0123456789'
        self.sid = sid

    def __get_lowercase(self) -> int:
        for c in self.sid:
            if c in self.alphabet:
                return 26
        return 0

    def __get_uppercase(self) -> int:
        for c in self.sid:
            if c in self.alphabet.upper():
                return 26
        return 0

    def __get_numer(self) -> int:
        for c in self.sid:
            if c in self.arabic_numerals:
                return 10
        return 0

    def str_length(self) -> int:
        lc = self.__get_lowercase()
        up = self.__get_uppercase()
        n = self.__get_numer()
        return lc+up+n


class CheckEntropy:
    def __init__(self, session_id):
        self.sid = session_id.strip()
        self.cc = CheckCharacters(self.sid)

    def __get_check_entropy(self):
        sid_char_len = len(self.sid)
        sid_len = self.cc.str_length()
        sid_strength = round(math.log2(sid_len ** sid_char_len), 1)
        sid_result = Colors.GREEN+'Good'+Colors.RESET
        if int(sid_strength) < 128:
            sid_result = Colors.RED+'Vulnerable(At least 128 Bits)'+Colors.RESET
        return sid_char_len, sid_len, sid_strength, sid_result

    def get_check(self):
        try:
            data = self.__get_check_entropy()
            print('### Session ID Check Entropy ###')
            print('+ Session ID : {sid}'.format(sid=self.sid))
            print('+ String Length : {sid_len}'.format(sid_len=data[0]))
            print('+ Characters : {sid_char_len} Type'.format(sid_char_len=data[1]))
            print('+ Strength : {sid_strength} Bits'.format(sid_strength=data[2]))
            print('+ Result : {sid_result}'.format(sid_result=data[3]))
        except Exception as err:
            print("Check Error:: {err}".format(err=err))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Check Session ID Entropy Calculator',
                                     description='Check Session ID Entropy Calculator')
    try:
        parser.add_argument('-s', '--session', dest='sid', type=str, help='Session ID')
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
        args = parser.parse_args()
        if not args.sid:
            print('Input Session ID Value')
            sys.exit(0)
        ce = CheckEntropy(args.sid)
        ce.get_check()
        sys.exit(0)
    except Exception as err:
        print("main:: {err}".format(err=err))
        sys.exit(0)
