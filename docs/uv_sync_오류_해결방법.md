# uv sync 오류 해결방법

## 문제 현상

`uv sync --upgrade` 실행 시 다음과 같은 오류가 발생할 수 있습니다:

```
❯ uv sync --upgrade
Using CPython 3.13.12 interpreter at: C:\Users\사용자이름\AppData\Local\Programs\Python\Python313\python.exe
error: failed to remove directory `G:\git\programmers-python-coding-test-study\.venv\Scripts`: Access is denied. (os error 5)
```

## 원인

### 1. 프로세스 잠금 (일반적인 경우)

Windows 환경에서 `.venv` 폴더의 파일이 다른 프로세스에 의해 사용 중일 때 발생합니다:

- **IDE/편집기**: VS Code, PyCharm 등이 가상환경의 Python 인터프리터를 사용 중
- **터미널**: 활성화된 가상환경을 사용하는 터미널 세션이 열려있음
- **백그라운드 프로세스**: Language Server(Pylance), Linter, Formatter 등이 `.venv` 내 파일 접근 중
- **Python 프로세스**: 실행 중인 Python 스크립트가 가상환경의 모듈 사용 중

### 2. 시스템 Python 버전 변경 (특수한 경우)

시스템에 설치된 Python 버전을 업데이트한 경우 (예: 3.13.11 → 3.13.12):

- `.venv`가 이전 Python 버전(3.13.11)을 참조하도록 생성됨
- 시스템 Python 업데이트 후 `.venv` 내부의 링크/바이너리가 깨진 상태
- `uv sync --upgrade` 시도 시 유효하지 않은 인터프리터 경로로 인해 오류 발생
- **특징**: 프로세스 잠금과 달리 `.venv` 폴더 삭제는 가능하지만 업그레이드는 실패

> 💡 이 경우 `.venv`를 삭제하고 새로 생성하는 것이 가장 확실한 해결책입니다.

## 해결 방법

### 1. 기본 해결 방법 (권장)

```cmd
# 1단계: 가상환경 사용 중인 프로세스 모두 종료
#  - VS Code, PyCharm 등 모든 IDE 종료
#  - 열려있는 모든 터미널 창 종료

# 2단계: .venv 폴더 삭제
rmdir /s /q .venv

# 3단계: 다시 동기화
uv sync
```

### 2. 삭제가 안될 때

#### 방법 A: 작업 관리자에서 프로세스 종료

1. `Ctrl + Shift + Esc`로 작업 관리자 열기
2. `python.exe`, `pythonw.exe` 프로세스 찾아서 모두 강제 종료
3. `.venv` 폴더 다시 삭제 시도

#### 방법 B: 탐색기에서 직접 삭제

1. 파일 탐색기에서 `.venv` 폴더로 이동
2. 폴더 우클릭 → 삭제
3. 삭제가 안되면 어떤 프로세스가 사용 중인지 확인

#### 방법 C: 재부팅 후 삭제

위 방법들이 모두 실패하면:

1. Windows 재부팅
2. IDE/터미널 실행 **전에** `.venv` 폴더 삭제
3. `uv sync` 실행

### 3. PowerShell에서 강제 삭제 (고급)

```powershell
# 관리자 권한으로 PowerShell 실행 후
Remove-Item -Path .venv -Recurse -Force
```

## 예방책

### 업그레이드 전 준비사항

```cmd
# 1. 모든 IDE와 터미널을 먼저 종료
# 2. 그 다음 업그레이드 실행
uv sync --upgrade
```

### VS Code 사용 시

업그레이드 전에 VS Code를 완전히 종료하는 것이 가장 확실합니다. 또는:

1. **명령 팔레트** (`Ctrl + Shift + P`) 열기
2. `Python: Clear Cache and Reload Window` 실행
3. 터미널 모두 종료: `Terminal: Kill All Terminals`
4. VS Code 재시작
5. `uv sync --upgrade` 실행

### PyCharm 사용 시

1. 프로젝트 설정에서 Python 인터프리터 설정 해제
2. 실행 중인 모든 Run Configuration 중지
3. PyCharm 종료
4. `uv sync --upgrade` 실행
5. PyCharm 재시작 후 인터프리터 재설정

### 시스템 Python 버전 변경 시

시스템 Python을 업데이트한 경우(예: 3.13.11 → 3.13.12), 기존 `.venv`가 무효화됩니다:

```cmd
# Python 버전 업데이트 후 권장 절차
# 1. 기존 가상환경 제거
rmdir /s /q .venv

# 2. 새로운 Python 버전으로 가상환경 재생성
uv sync

# 또는 특정 Python 버전 지정
uv sync --python 3.13.12
```

> ⚠️ **중요**: 시스템 Python 버전을 변경하면 반드시 `.venv`를 재생성해야 합니다.  
> `uv sync --upgrade`로는 해결되지 않으며 "Access is denied" 오류가 발생할 수 있습니다.

## 참고사항

`.venv` 폴더를 삭제해도 `pyproject.toml`과 `uv.lock` 파일에 의존성 정보가 보존되어 있으므로, `uv sync` 실행 시 동일한 환경이 재구성됩니다.

```cmd
# 삭제 전과 동일한 환경이 복원됨
uv sync
```

만약 특정 버전으로 업그레이드하고 싶다면:

```cmd
# 전체 라이브러리 업데이트
uv sync --upgrade

# 특정 패키지만 업데이트
uv add <패키지명>@latest
```
