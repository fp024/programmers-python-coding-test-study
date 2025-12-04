# Pre-commit과 Black을 활용한 커밋 전 포맷팅 가이드

## 📋 목차
1. [설치 / 제거](#설치--제거)
2. [사용](#사용)
3. [주의점](#주의점)

---

## 🔧 설치 / 제거

### 📦 설치 과정

#### 1. Black과 Pre-commit 설치
```shell script
# pip 사용 시
pip install black pre-commit

# pip-tools 사용 시 (권장)
# requirements-dev.in에 추가
```


```
black==24.3.0
pre-commit==3.6.0
```
* requirements.txt 파일을 dev로 분리하기를 권장하는데, 프로젝트 특성상 하나로 쓰기로 했다.
  ```shell script
  pip-compile requirements-dev.in
  pip-sync requirements.txt requirements-dev.txt
  ```


#### 2. Pre-commit 설정 파일 생성
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0  # 설치된 Black 버전과 동일하게
    hooks:
      - id: black
        language_version: python3
```


#### 3. Git Hook 설치
```shell script
pre-commit install
```


#### 4. 설치 확인
```shell script
# Hook 파일 확인
ls -la .git/hooks/pre-commit

# 버전 확인
black --version
pre-commit --version
```


### 🗑️ 제거 방법

#### 완전 제거
```shell script
# 1. Git Hook 제거
pre-commit uninstall

# 2. 패키지 제거
pip uninstall black pre-commit

# 3. 설정 파일 제거 (선택사항)
rm .pre-commit-config.yaml
```


#### 일시적 비활성화
```shell script
# Hook 파일만 제거 (재설치 쉬움)
rm .git/hooks/pre-commit
```


---

## 🚀 사용

### 🔄 기본 워크플로우

#### 정상적인 커밋 프로세스
```shell script
# 1. 코드 작성
echo "print('hello world')" > example.py

# 2. 스테이징
git add example.py

# 3. 커밋 (자동으로 Black 실행됨)
git commit -m "예제 코드 추가"
# → Black이 포맷팅 검사
# → 문제없으면 커밋 완료
# → 문제있으면 커밋 취소되고 수정사항 표시
```


#### 포맷팅 오류 시 대응
```shell script
# 1. 오류 발생 시 Black이 자동 수정
git add .  # 수정된 파일 다시 스테이징

# 2. 다시 커밋
git commit -m "예제 코드 추가"
```


### 🎯 다양한 사용법

#### 수동 포맷팅 (커밋 전 미리 확인)
```shell script
# 전체 프로젝트 포맷팅
black .

# 특정 파일만
black src/main.py

# 검사만 하고 수정 안함
black --check .
```


#### Hook 우회 (긴급 상황)
```shell script
# 이번 커밋만 Hook 무시
git commit -m "긴급 수정" --no-verify

# 또는 짧게
git commit -m "긴급 수정" -n
```


#### 특정 도구만 스킵
```shell script
# Black만 스킵
SKIP=black git commit -m "WIP: 작업 중"

# 여러 도구 스킵
SKIP=black,flake8 git commit -m "실험 코드"

# 모든 Hook 스킵
SKIP=all git commit -m "백업 커밋"
```


### 🛠️ 유용한 Git Alias

```shell script
# 자주 사용하는 명령어들을 alias로 등록
git config alias.ncommit 'commit --no-verify'
git config alias.format '!black . && git add .'
```


사용법:
```shell script
# Hook 우회 커밋
git ncommit -m "작업 저장"

# 포맷팅 후 스테이징
git format
git commit -m "포맷팅 적용"
```


### 📊 Pre-commit 관리 명령어

```shell script
# Hook 상태 확인
pre-commit --version

# 설정 파일 검증
pre-commit validate-config

# 모든 파일에 대해 Hook 실행
pre-commit run --all-files

# 특정 Hook만 실행
pre-commit run black

# Hook 업데이트
pre-commit autoupdate
```


---

## ⚠️ 주의점

### 🔄 버전 동기화

#### 문제 상황
```
로컬 Black 버전:     25.1.0
Pre-commit Black:    24.1.1
     ↓
포맷팅 결과가 달라질 수 있음!
```


#### 해결 방법
1. **현재 Black 버전 확인**
```shell script
black --version
pip show black
```


2. **Pre-commit 설정 맞추기**
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0  # pip 버전과 동일하게, .venv/Scripts/pre-commit autoupdate를 해주면 최신으로 맞춰줌.
    hooks:
      - id: black
        language_version: python3
```


3. **pip-tools 사용 시 관리**
```
black==25.1.0  # 명시적 버전 고정
pre-commit==3.6.0
```


### 🚫 자주 발생하는 문제들

#### 1. Hook이 실행되지 않는 경우
```shell script
# 문제: Hook 파일이 실행 권한이 없음
# 해결:
chmod +x .git/hooks/pre-commit

# 또는 재설치
pre-commit uninstall
pre-commit install
```


#### 2. 무한 루프 상황
```shell script
# 문제: Black이 계속 파일을 수정함
# 원인: Black 버전 불일치 또는 설정 충돌

# 해결: 버전 통일 후
pre-commit run --all-files  # 한 번에 모든 파일 정리
```


#### 3. 대용량 파일 처리
```shell script
# 문제: 큰 파일에서 Hook이 느림
# 해결: 파일 제외 설정
```


```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
        language_version: python3
        exclude: ^(large_file\.py|generated/.*\.py)$
```


### 💡 팀 프로젝트에서의 고려사항

#### 1. 팀원 간 설정 통일
```shell script
# 프로젝트 루트에 설치 스크립트 생성
```


```shell script
#!/bin/bash
echo "🔧 개발 환경 설정 중..."

# 의존성 설치
pip-sync requirements.txt requirements-dev.txt

# Pre-commit Hook 설치
pre-commit install

# 초기 포맷팅
pre-commit run --all-files

echo "✅ 설정 완료!"
```


#### 2. CI/CD 연동
```yaml
# .github/workflows/pre-commit.yml
name: Pre-commit

on: [push, pull_request]

jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    - uses: pre-commit/action@v3.0.0
```


### 🎯 실무 팁

#### 1. 점진적 적용
```shell script
# 기존 프로젝트에 적용 시
# 1단계: 새 파일만 적용
pre-commit install

# 2단계: 기존 파일 점진적 적용
pre-commit run --files src/new_module.py

# 3단계: 전체 적용
pre-commit run --all-files
```


#### 2. 개발 단계별 전략
```shell script
# 개발 초기: 엄격하게
git commit -m "기능 구현"  # Hook 실행

# 실험/프로토타입: 유연하게
git ncommit -m "실험 코드"  # Hook 우회

# 코드 리뷰 전: 정리
black .
git add .
git commit -m "코드 포맷팅"
```


#### 3. 성능 최적화
```shell script
# 변경된 파일만 체크하도록 설정
```


```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0
    hooks:
      - id: black
        language_version: python3
        files: \.py$  # Python 파일만
        stages: [commit]  # 커밋 시에만 실행
```


---

## 🎉 마무리

Pre-commit + Black 조합은 처음에는 빡세게 느껴질 수 있지만, 익숙해지면 코드 품질 향상에 큰 도움이 됩니다. 

**적응 과정:**
- **1주차**: "아, 또 실패했네..." 😅
- **2-3주차**: "미리 `black .` 하는 습관 생김" 🔄
- **1달 후**: "실수 방지에 도움된다" 👍
- **2달 후**: "이거 없으면 불안해" 😎

**기억하세요**: 언제든 `--no-verify`로 우회 가능하니 부담갖지 마세요! 🚀