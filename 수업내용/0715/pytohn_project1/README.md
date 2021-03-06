# 프로젝트 01 - 파이썬 기반 데이터 활용

* [00. 텍스트 데이터 출력 (연습)](./00.py)
  * 텍스트파일을 생성하면서 열어주어 원하는 결과를 print로 출력했다. 
  * 주의 할 점 : 터미널에서 프린트 할 때와는 다르게 txt파일에 write할 때에는 각각 \n로 줄 구분을 확실히 해야한다는 점.
* [01. 텍스트 데이터 입력 (연습)](./01.py)
  * fruits.txt의 각 줄을 읽어주며 줄을 읽을 때 마다 n을 더해 준 후 n을 출력했다.
  * 주의 할 점 : if문과 n을 더해주는 문장의 위치 주의!
* [02. 텍스트 데이터 활용 - 특정 단어 추출](./02.py)
  * fruits.txt의 각 줄을 읽어주며 줄을 읽을 때 마다 단어의 길이-(berry의 글자수+1):단어의 길이 안에 berry가 있는지 검사했다. 이후 해당 단어들을 중복되지 않게 berrys라는 변수에 넣어주며 n에 1을 더해준 후 n과 berrys를 출력했다.
  * 주의 할 점 : 각 단어의 끝이 줄 바꿈으로 끝나서인지 글자수가 한 글자 더 많게 나왔다. 이 점에 주의해서 berry를 검사할 범위를 정했다.
* [03. 텍스트 데이터 활용 - 등장 횟수](./03.py)
  * 마찬가지로 각 줄을 읽어주었고, 단어 끝에 있는 \n을 제거해주었다. 이후 줄을 읽으면서 중복되지 않은 과일이 나올 경우 딕셔너리에 해당 과일을 추가해주고, 중복될 경우는 value에 1을 더해주었다.
  * 주의 할 점 : 02번 문제와 같이 \n을 제거해야 딕셔너리가 깔끔하게 나왔다. 또한 break의 위치에 주의했다.
* [04. JSON 데이터 활용 - 영화 단일 정보](./04.py)
  * 제이슨에서 필요한 정보만을 뽑아 새로 딕셔너리를 만드는 함수 ` movie_info`를 정의했다. 
* [05. JSON 데이터 활용 - 영화 단일 정보 응용](./05.py)
  * 이전에 만든 함수에 덧대고 싶지 않아 장르 코드를 장르 이름으로 바꿔주는 ` genres_info`함수를 새로 정의했다. 이중 for문을 통해 장르 코드들 모두를 장르 이름으로 바꾸어주었고, 이 함수를 이전에 사용한 ` movie_info` 안에서 사용했다.
  * 주의 할 점 : 장르 코드가 여러 개일 경우 모두 이름으로 바꾸어 주기 위해 이중으로 for문을 사용했다. 하지만 이중 for문이 아닌 다른 방식이 있을 것 같아 알아보고 싶다.
* [06. JSON 데이터 활용 - 영화 다중 정보 활용](./06.py) 
  * ` genres_info`함수는 그대로 둔 채로 ` movie_info` 함수를 약간 수정해보았다. 여러 영화의 목록을 모두 다 전환하기 위해 for를 사용해주었다.
  * 주의 할 점 : 알고리즘 자체는 처음 생각한 것에서 그대로 갔으나, 자료구조를 정확히 알지 못해 계속 헤맸다. 그러던 중 이번에 주어진 movies.json은 ***딕셔너리로 이루어진 리스트***  구조라는 것을 알게 된 후 문제가 쉽게 풀렸다.

## 후기

0번에서 6번까지를 해결하면서 천천히 빌드업이 되가는 과정이 느껴서 내가 공부한 것을 순차적으로 적용시키기 좋았다. 특히 마지막 문제에서 자료구조가 무엇인지에 대해 조금은 안 것 같아서 뿌듯했다.