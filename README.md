# Check Session ID Entropy Calculator(CSId-Calc)
<div>
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fhappylie%2FCSId-Calc&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=view&edge_flat=false"/>
<img src="https://img.shields.io/badge/Python->=3.5-blue?logo=python&logoColor=white" />
</div>

## Check Session ID Entropy Calculator
### 세션 ID 엔트로피 계산기
- https://happylie.tistory.com/145

### 설치 방법
1. Git Clone
```
$ git clone https://github.com/happylie/CSId-Calc.git
```

### 실행 방법
1. Help
```
$ python csid.py -h       
usage: Check Session ID Entropy Bit [-h] [-s SID] [-v]

Check Session ID Entropy Bit

optional arguments:
  -h, --help            show this help message and exit
  -s SID, --session SID
                        Session ID
  -v, --version         show program's version number and exit
```
2. Session ID Entropy Check
```
$ python csid.py -s a00a0a100203
### Session ID Check Entropy ###
+ Session ID : a00a0a100203
+ String Length : 12
+ Characters : 36 Type
+ Strength : 62.0 Bits
+ Result : Vulnerable(At least 128 Bits)

$ python csid.py -s 1a44f079183C8492d55805ef18f1079b0357c8d6                                                                
### Session ID Check Entropy ###
+ Session ID : 1a44f079183C8492d55805ef18f1079b0357c8d6
+ String Length : 40
+ Characters : 62 Type
+ Strength : 238.2 Bits
+ Result : Good
```
3. 결과값 설명
   - Session ID : 입력한 Session ID(세션 ID)
   - String Length :  Session ID 값의 길이
   - Characters : Session ID 값의 조합된 글자수
   - Strength : Session ID 의 강도
       - 128 Bits 이상이 안전
   - Result : 결과( Vulnerable / Good )


4. Characters Check
   - Lower Case : 26
   - Upper Case : 26
   - Lower & Upper Case : 52
   - Arabic numerals : 10
   - Lower Case & Arabic numerals : 36
   - Upper Case & Arabic numerals : 36
   - Lower & Upper Case & Arabic numerals : 62


### 참고문서
- https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
