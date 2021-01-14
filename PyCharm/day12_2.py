import re

# 정규표현식 메타문자
# | : OR 또는
# +:바로 앞의 문자가 하나 이상 있음
# ^:문자열의 처음을 나타냄
# $:문자열의 끝
# . :임의의 문자가 와도 됨
# *:바로 앞의 문자가 없거나 하나 이상 있음
# ?:앞의 문자가 없거나 하나임

# 퀴즈 : 리스트에서 주민등록번호 양식에 맞는 데이타를 출력하여라
# 주민등록번호 패턴
# 6자리숫자-[1|2|3|4]6자리숫자
quizList = ['020-28261', '564873-3300998', '가나다-3300998', '564873-8800998', '123456-1234567', 'abc456-1234567']

pattern = '[0-9]{6}-[1|2|3|4][0-9]{6}'
for item in quizList:
    # print(re.findall(pattern, item))
    if re.findall(pattern, item):
        print(re.findall(pattern, item)[0])
print('-'*50)
for item in quizList:
    # print(re.search(pattern, item))
    if re.search(pattern, item):
        print(re.search(pattern, item).group())

# ^ : 문자열의 처음을 나타냄 : '가'로 시작하는 글자
# $ : 문자열의 끝 : '지'로 끝나는 글자
wordList = ['가로수', '도시락', '파이썬', '가지', '강아지', '망아지', '도라지']
pattern1 = '^가' # '가'로 시작하는 글자
pattern2 = '지$' # '지'로 끝나는 글자
result = []
for item in wordList:
    if re.findall(pattern1, item):
        result.append(item)
print(result)

xml_str = '''
<book category="web">
<title lang="en">XQuery Kick Start</title>
<author>James McGovern</author>
<author>Per Bothner</author>
<author>Kurt Cagle</author>
<author>James Linn</author>
<author>Vaidyanathan Nagarajan</author>
<year>2003</year>
<price>49.99</price>
</book>
'''
pattern1 = re.compile('<.')
pattern2 = re.compile('<.....?')
pattern3 = re.compile('<.*>')
pattern4 = re.compile('<.*?>')
print(pattern1.findall(xml_str))
print(pattern2.findall(xml_str))
print(pattern3.findall(xml_str))
print(pattern4.findall(xml_str))

# 그룹핑이용
# 정규표현식의 패턴을 그룹화 : group(index)
juminPattern = '([0-9]{6})-([1|2|3|4][0-9]{6})'
result = re.match(juminPattern, '123456-1234567')
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))

# 퀴즈 : 주민번호데이타에서 주민번호뒷자리 '*******' 마킹하기
# 다음 리스트에서 주민번호 패턴에 맞는 리스트요소만
# '-' 뒷자리 부분을 '*******' 마킹하여라
# 패턴 그룹핑 이용

quizList = ['020-28261', '564873-3300998', '가나다-3300998', '564873-8800998', '123456-1234567', 'abc456-1234567',
             '5555564873-3377777700998', '564873-1234567890']

pat = '([0-9]{6})-([1|2|3|4]){1}([0-9]{6})'
for item in quizList:
    result = re.search(pat, item)
    if result:
        print(result.group(1),'-','*'*7)
        print(result.group(1),'-',result.group(2),'*'*6)
print('-'*50)

