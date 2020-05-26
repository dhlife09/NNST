from bs4 import BeautifulSoup
import requests
import sys

print('NNST by Dohyun Park(dhlife09)')
print('')
print('GitHub - https://github.com/dhlife09')
print('Email - dhlife09@gmail.com')
print('')
print('프로그램을 종료하려면 /exit 를 입력하세요.')
print('')

while True:
  print('')
  userInput = input('검색할 뉴스 주제: ')
  if userInput == '/exit':
    print('사용자의 요청에 의해 프로그램이 종료되었습니다.')
    sys.exit()
  else:
    ## HTTP GET Request
    req = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + userInput)

    ## HTML 소스 가져오기
    html = req.text
    ## HTTP Header 가져오기
    header = req.headers
    ## HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    ## HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok

    if req.ok:  
        html = req.text
        print('')
        print('===========')
        print('')
        soup = BeautifulSoup(html,'html.parser')
        titles_by_select = soup.select(
        'ul.type01 > li > dl > dt > a'
        )
        for title in titles_by_select:
          print(title.get('title'))
          print('')

    print('===========')
