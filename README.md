# Lec0 Search

### 1. degrees [link](https://cs50.harvard.edu/extension/ai/2020/spring/projects/0/degrees/)
케빈 베이컨의 6단계 법칙을 이용해 2명의 할리우드 배우가 몇 사람을 거쳐 연결되어 있는지 알아내기 (링크는 같이 출연한 영화)

( BFS + linked list )

실행 
```
python degrees.py small

python degrees.py large
```
실행화면

<img width="407" alt="degrees" src="https://user-images.githubusercontent.com/33231313/110240520-b2198580-7f8f-11eb-985c-3eab409834fa.PNG">

### 2. tictactoe [link](https://cs50.harvard.edu/extension/ai/2020/spring/projects/0/tictactoe/)
유저와 tictactoe 게임하는 AI 만들기

패키지설치
```
pip install pygame    
```

실행
```
python runner.py
```

실행화면
![ttt](https://user-images.githubusercontent.com/33231313/110240266-7631f080-7f8e-11eb-8d02-e4e9c3a40318.png)


# Lec1 Search

### 1. knights [link](https://cs50.harvard.edu/extension/ai/2020/spring/projects/1/knights/)
knight이면 진실만 말하고 knave이면 거짓만 말한다.
각 사람이 말하는 정보를 가지고 knight인지 knave인지 맞추기


실행
```
python puzzle.py
```

실행결과

<img width="199" alt="knights" src="https://user-images.githubusercontent.com/33231313/110239998-27d02200-7f8d-11eb-98de-6e30a215aa76.PNG">

### 2. minesweeper [link](https://cs50.harvard.edu/extension/ai/2020/spring/projects/1/minesweeper/)
혼자서 지뢰찾기 게임하는 AI 만들기.

새로 이동할 때마다 얻은 이웃 지뢰 개수 정보로 안전함을 확실할 수 있는 cell이 있으면 그곳으로 이동하고, 없으면 랜덤으로 이동한다.

패키지설치
```
pip install pygame    
```

실행
```
python runner.py
```

실행화면
![pygame](https://user-images.githubusercontent.com/33231313/110239580-1259f880-7f8b-11eb-9b8a-1592c247babc.png)


### 3. py2ocaml
"x ⊨ y means x models (semantically entails) y"

정보들을 propositional logic 형태로 바꾸고, 이미 알고 있는 정보로 새 쿼리를 entails 할 수 있는지 true/false로 리턴하는 함수를 구현한 logic.py와 똑같이 작동하는 ocaml 코드를 작성해봄 (잘 이해하기 위해 개인적으로 진행)

ocaml 인터프리터에 파일 로드하기
```
#use "logic.ml"
```

실행 결과 (비교)
![harry](https://user-images.githubusercontent.com/33231313/110240942-9fa04b80-7f91-11eb-9354-21b4f5c30ad3.png)
![clue](https://user-images.githubusercontent.com/33231313/110240951-ae86fe00-7f91-11eb-9ea6-66bb7e0ebd88.png)

