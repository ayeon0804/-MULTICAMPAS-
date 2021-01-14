# 퀴즈 ^^
import csv
# 퀴즈1 :
# data.csv 파일을 이용하여
# 4과목('kor', 'eng', 'mat', 'bio')의 총점과 전체 평균을 구하여라.
'''
 kor 총점 = ... ?
 eng 총점 = ... ?
 mat 총점 = ... ?
 bio 총점 = ... ?
4과목의 총점은 ... ?
전체 평균은 ... ?
'''

with open('data/data.csv', 'r') as f:
    data_list = list(csv.reader(f, delimiter=','))

kor_sum, eng_sum, mat_sum, bio_sum = 0, 0, 0, 0
for c, n, k, e, m, b in data_list[1:]:
    kor_sum += int(k)
    eng_sum += int(e)
    mat_sum += int(m)
    bio_sum += int(b)

print(f'kor 총점 = {kor_sum}')
print(f'eng 총점 = {eng_sum}')
print(f'mat 총점 = {mat_sum}')
print(f'bio 총점 = {bio_sum}')
print(f'4과목의 총점은 {kor_sum+eng_sum+mat_sum+bio_sum}')
print(f'전체 평균은 {(kor_sum+eng_sum+mat_sum+bio_sum)/4}')

# 퀴즈2 :
print('-'*100)
# 미국 주별 인구수 population.csv 파일을 이용하여 리스트 구조로 변경하고
# 출력하여라
# 이때 인구와 관련된 데이타는 정수 리스트로 변환해야 한다.
'''
State Population
Alabama 4780131
Alaska 710249
Arizona 6392301
  ...
'''
with open('data/population.csv', 'r') as f:
    data_list = list(csv.reader(f))

state_list = []
pop_list = []
for state, pop in data_list[1:]:
    state_list.append(state)
    pop_list.append(int(pop.replace(',','')))

for idx in range(len(state_list)):
    print(state_list[idx],pop_list[idx])


# 퀴즈3 :
print('-'*100)
# 퀴즈2의 리스트에서
# 가장 인구가 많은 주(State)와 가장 인구가 적은 주(state)는?

max_value = max(pop_list)
max_idx = pop_list.index(max_value)

min_value = min(pop_list)
min_idx = pop_list.index(min_value)

print(f'가장 인구가 많은 주 : {state_list[max_idx]}')
print(f'가장 인구가 적은 주 : {state_list[min_idx]}')

# 퀴즈5 :
print('-'*100)
# traffic_2017.csv 각 지역별 대중교통 파일을 이용하여
# 아래와 같은 딕셔너리 구조로 대중교통총사용자수를 출력하여라

'''
{'서울': 4423933, '부산': 952394, '대구': 547568, ... }

'''

with open('data/traffic_2017.csv', 'r') as f:
    traffic_data = list(csv.reader(f))

traffic_dic = {}
for city, pop1, pop2, pop3, pop4 in traffic_data[1:]:
    if pop4 == '':
        pop4 = 0
    traffic_dic[city] = int(pop1) + int(pop2) + int(pop3) + int(pop4)
print(traffic_dic)

# 퀴즈6 :
# 퀴즈 5번의 데이타 리스트에서 가장 낮은 대중교통 사용자수와 관련된 도시는?

min_value = min(traffic_dic.values())
for city, pop in traffic_dic.items():
    if pop == min_value:
        print(f'가장 낮은 대중교통 사용자수와 관련된 도시는 {city}입니다.')

# 퀴즈7 :
# 2018.csv 파일을 이용하여 다음을 구하여라.

# 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?
# 100인 미만의 회사에 들어간 취업자수가 가장 적은 도시는?

with open('data/2018.csv', 'r') as f:
    data_list = list(csv.reader(f))
under_100_list = []
over_1000_lsit = []
for a, b, c, d, e, f, g, h, i in data_list[1:]:
    under_100_list.append(int(d.replace(',','')) + int(e.replace(',','')) + int(f.replace(',','')))
    over_1000_lsit.append(int(i.replace(',','')))

max_value = max(over_1000_lsit)
max_idx = over_1000_lsit.index(max_value)
min_value = min(under_100_list)
min_idx = under_100_list.index(min_value)

print(f'1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시 : {data_list[max_idx+1][1]}')
print(f'100명 미만의 회사에 들어간 취업자수가 가장 적은 도시 : {data_list[min_idx+1][1]}')

# 퀴즈8 :
# 2018.csv 파일에서 '학제', '분석대상자수'  컬럼만 제외한 후
# output 폴더안에 2018_result.csv
# 파일로 저장하여라.

header = data_list[0]
header.remove('학제')
header.remove('분석대상자수')

result = []
for a, b, c, d, e, f, g, h, i in data_list[1:]:
    result.append([b, d, e, f, g, h, i])

result.insert(0,header)

with open('output/2018_result.csv', 'w', encoding='utf-8', newline='') as f:
    csv_data = csv.writer(f, delimiter = ',')
    csv_data.writerows(result)

# 퀴즈9 :
# gapminder.tsv 파일을 이용하여 Asia 대륙의 데이타만 저장하여 별도 파일로 저장하여라.
# output 폴더안의 asia.tsv

with open('data/gapminder.tsv', 'r') as f:
    data_list = list(csv.reader(f, delimiter = '\t'))

asia_list = []
for country, continent, year, lifeExp, pop, gpdPercap in data_list[1:]:
    if continent == 'Asia':
        asia_list.append([country, continent, year, lifeExp, pop, gpdPercap])

asia_list.insert(0,data_list[0])
with open('output/asia.tsv', 'w', newline='') as f:
    tsv_data = csv.writer(f, delimiter = '\t')
    tsv_data.writerows(asia_list)

# 퀴즈 10:
# gapminder.tsv 파일의 데이타를 이용하여 다음과 같이 출력하여라.
'''
 평균 수명이 가장 길었던 데이타 : ? 년도의 ? 
 평균 수명이 가장 짧았던 데이타 : ? 년도의 ?
'''

with open('data/gapminder.tsv', 'r') as f:
    data_list = list(csv.reader(f, delimiter='\t'))

lifeExp_dict = {}
for country, continent, year, lifeExp, pop, gpdPercap in data_list[1:]:
    lifeExp_dict[lifeExp] = year

max_lifeExp = max(lifeExp_dict)
min_lifeExp = min(lifeExp_dict)

print(f'평균 수명이 가장 길었던 데이타 : {lifeExp_dict.get(max_lifeExp)}년도의 {max_lifeExp}')
print(f'평균 수명이 가장 짧았던 데이타 : {lifeExp_dict.get(min_lifeExp)}년도의 {min_lifeExp}')

# 퀴즈 11:
# movies.dat 파일을 이용하여
# 1980년도 (1980~1989) 영화만
# movies_1980_1989.csv 파일로 저장하여라.

'''
MovieID,Title,Year,Genres
142,Shadows (Cienie),1988,Drama
541,Blade Runner,1982,Film-Noir|Sci-Fi
592,Batman,1989,Action|Adventure|Crime|Drama
 ... 
'''

with open('data/movies.dat', 'r',  encoding='ISO-8859-1') as f:
    data_list = f.readlines()
    movies_list = []
    for row in data_list:
        temp = row.replace('\n', '').split('::')
        movies_list.append(temp)

movies_1980_1989 = []
for id, title_year, genres in movies_list[:]:
    title = title_year[:-6].strip()
    year = int(title_year[-5:-1])
    if 1980 <= year <= 1989:
        movies_1980_1989.append([int(id), title, year, genres])

movies_1980_1989.insert(0,['MovieID','Title','Year','Genres'])

with open('output/movies_1980_1989.csv', 'w', encoding='utf-8', newline='') as f:
    csv_data = csv.writer(f, delimiter = ',')
    csv_data.writerows(movies_1980_1989)

# 퀴즈 12:
# movies.dat 파일을 이용하여
# Animation 장르의 데이타만 animation_movies.csv 파일로 저장하여라.
'''
MovieID,Title,Year,Genres
1,Toy Story,1995,Animation|Children's|Comedy
13,Balto,1995,Animation|Children's
48,Pocahontas,1995,Animation|Children's|Musical|Romance
...

'''

animation_movies = []
for id, title_year, genres in movies_list[:]:
    title = title_year[:-6].strip()
    year = int(title_year[-5:-1])
    if genres.find('Animation') != -1:
        animation_movies.append([int(id), title, year, genres])

animation_movies.insert(0,['MovieID','Title','Year','Genres'])

with open('output/animation_movies.csv', 'w', encoding='utf-8', newline='') as f:
    csv_data = csv.writer(f, delimiter = ',')
    csv_data.writerows(animation_movies)