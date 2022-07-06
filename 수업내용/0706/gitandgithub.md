# git 이란?

**git은 분산버전관리시스템이다.**

## 기본 흐름

작업 파일 >(add)> 커밋할 목록 >(commit)> 버전

### 기본 명령어 - `$git init`

* 특정 폴더를 git 저장소(repository)를 만들어 git으로 관리
  * .git 폴더가 생성되며(숨김폴더)
  * git bash에서 master라는 표기를 확인할 수 있음

### 기본명령어 - ` $git add <file>`

* working directory상의 변경 내용을 staging area에 추가하기 위해 사용
  * untracked,modifyed 상태의 파일을 staged로 변경

### 기본 명령어 - ` $git commit -m '<커밋메세지>'`

* staged상태의 파일들을 커밋을 통해 버전으로 기록
* 커밋 메세지는 변경사항을 나타낼 수 있도록 명확하게 작성해야함

## 현태 상태를 알려면?

### 기본 명령어 - ` $git status`

* git 저장소에 있는 파일의 상태를 확인하기 위하여 활용

### 기본 명령어 - ` $git log`

* 현재 저장소에 기록된 커밋 조회
* 다양한 옵션을 통해 로그 조회 가능
  * ` $git log -1`
  * ` $git log --oneline`
  * ` $git log -2 --oneline`

## github 원격저장소 활용하기

### github에 원격저장소 만들기

* 저장소 생성, 설정 및 확인
* ex) https://github.com/githubusername/repositoiryname

### 로컬저장소의 버전을 원격저장소로 보내주기

* ` $git remote add origin https://github.com/githubusername/repositoiryname`
* 깃 원격저장소에 origin 으로 추가한다 이 저장소를

### 원격저장소 활용 명령어 - ` $git push <원격저장소이름> <브랜치이름>`

* 원격 저장소로 로컬 저장소 변경사항을 올림

### 원격저장소 활용 명령어 - ` $git pull <원격저장소이름> <브랜치이름>`

* 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함

### 원격저장소 활용 명령어 - ` $git clone <원격저장소이름>`

* 원격저장소를 복제하여 가져옴