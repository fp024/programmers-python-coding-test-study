# 프로그래머스 Python 코딩 테스트 - 스터디

> 코딩 테스트 연습을 JS/TS, Java, C++ 환경에서 하고 있었는데, Python으로 해봐도 재밌을 것 같아서 프로젝트를 만들었다.
>
> * JS/TS
>   * https://github.com/fp024/programmers-js-coding-test-study
>
> * Java
>   * https://github.com/fp024/programmers-java-coding-test-study
> * C++
>   * https://github.com/fp024/programmers-c-coding-test-study
>



## 스터디 프로젝트  구성

### 개발 도구

* PyCharm
  * https://www.jetbrains.com/pycharm/
* VSCode
  
  * https://code.visualstudio.com/
  
  > 뭔가 지원이 좋은것같다. 😊,  Python 확장하고, Black만 설치하면 잘됨..👍
  >
  > * Python
  >   * https://github.com/Microsoft/vscode-python
  > * Black Formatter
  >   * https://github.com/microsoft/vscode-black-formatter





## 디펜던시 관리자 (uv)

[uv](https://github.com/astral-sh/uv)는 Rust로 작성된 초고속 Python 패키지 관리자이다. pip/pip-tools를 대체하며, 락 파일 기반으로 재현 가능한 환경을 제공한다.

> 💡 기존 pip/pip-tools 가이드는 [README-2026-01-09.md](docs/history/README-2026-01-09.md)에 보관.


### uv 설치

```sh
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### 프로젝트 구조

```
pyproject.toml   ← 의존성 선언 (npm의 package.json과 유사)
uv.lock          ← 잠금 파일 (npm의 package-lock.json과 유사, Git 커밋 권장)
.python-version  ← Python 버전 지정
.venv/           ← 가상환경 (uv sync 시 자동 생성)
```


### 기본 명령

#### 1. 의존성 동기화 (설치)

```sh
# pyproject.toml + uv.lock 기반으로 .venv 생성/동기화
uv sync

# 캐시 재검증하며 동기화
uv sync --refresh

# 락 최신화 후 바로 설치
uv sync --upgrade

# CI/엄격 모드: 락만 신뢰(락과 불일치 시 실패)
uv sync --locked
```

#### 2. 패키지 추가/제거

```sh
# 패키지 추가 (pyproject.toml에 자동 기록)
uv add <패키지명>

# 패키지 제거
uv remove <패키지명>
```

#### 3. 락 파일 갱신

```sh
# uv.lock 갱신 (최신 호환 버전으로)
uv lock --refresh
```

#### 4. 캐시 관리

```sh
# 캐시 비우기
uv cache clean

# 캐시 위치 확인
uv cache dir
```

#### 5. pre-commit 훅 버전 업데이트

```sh
pre-commit autoupdate
```


### ⚠️ Windows 하드링크 이슈

uv는 성능을 위해 캐시에서 venv로 하드링크를 사용한다. 그런데 **하드링크는 같은 물리 드라이브에서만 가능**하다.

**증상**: 캐시(C:)와 프로젝트(G: 등 다른 드라이브)가 다르면 경고 발생 후 복사로 대체됨.

| 링크 방식 | 드라이브 제한 | 권한 요구 |
|-----------|---------------|-----------|
| hardlink (기본) | 같은 드라이브만 | 없음 (일반 사용자 OK) |
| symlink | **드라이브 달라도 가능** | 개발자 모드 또는 gpedit 권한 추가 필요 (*) |
| copy | 제한 없음 | 없음 |

> (*) **symlink 권한 설정**: Windows는 기본적으로 관리자만 심볼릭 링크 생성 가능.  
> 일반 사용자는 다음 중 하나 필요:
>
> - **개발자 모드 활성화**: 설정 → 개발자용 → 개발자 모드 켜기
> - **gpedit.msc**: 
>   - `Computer Configuration` → `Windows Settings` → 
>     `Security Settings` → `Local Policies` → `User Rights Assignment`
>     - `Create symbolic links`에서 로그인 유저 추가

**해결책 (택1)**:

```cmd
:: 방법 1: 캐시를 프로젝트와 같은 드라이브로 이동
mkdir G:\uv-cache
setx UV_CACHE_DIR "G:\uv-cache"
uv cache clean
uv sync --refresh

:: 방법 2: 심볼릭 링크 사용 (드라이브 달라도 OK, 권한 설정 필요)
setx UV_LINK_MODE "symlink"

:: 방법 3: 복사 모드 사용 (속도 약간 느림, 권한 이슈 없음)
setx UV_LINK_MODE "copy"
```

또는 `pyproject.toml`에 프로젝트별 설정:

```toml
[tool.uv]
link-mode = "symlink"  # 또는 "copy"
```

> 💡 환경변수 설정 후 VS Code/터미널 재시작 필요




## 단위 테스트 프레임워크

* pytest
  * https://github.com/pytest-dev/pytest

파이썬에서는 컨테이너 비교가 언어자체적으로 간단해서.. 매처라이브러리를 따로 설치하지 않아도 될 것 같다.

> 💡**Pytest는 기본 assert 문을 적극적으로 활용하는 것을 강력히 권장한다.**

### pytest 실행 방법

```bash
# 모든 테스트 실행
pytest

# 특정 파일만 실행
pytest tests/lv02/test_exam004_17684.py

# 자세한 출력 (verbose)
pytest tests/lv02/test_exam004_17684.py -v

# 패턴 매칭으로 실행 (파일명/함수명에 'exam026' 포함)
pytest -k exam004_17684

# 특정 테스트 함수만 실행
pytest tests/lv02/test_exam004_17684.py::test_solution_me

# 가상환경에서 실행
python -m pytest tests/lv02/test_exam004_17684.py -v
```



## 코드 포맷터 & 자동화 (pre-commit)

`pre-commit`을 사용하여 커밋 시 코드를 자동 포맷팅하고, 푸시 전 테스트를 수행합니다.

### 1. 훅 설치

```bash
# 기본 훅 설치 (Commit 시 Black 실행)
uv run pre-commit install

# pre-push 훅 설치 (Push 시 Pytest 실행)
uv run pre-commit install --hook-type pre-push
```

### 2. 설정 내용 ([`.pre-commit-config.yaml`](.pre-commit-config.yaml))

- **commit 단계**: `black`, `black-jupyter` 실행 (코드 포맷팅)
- **push 단계**: `pytest` 실행 (전체 테스트 통과 시에만 푸시 허용)

> 💡 테스트를 건너뛰고 강제 푸시하려면: `git push --no-verify`


* Black
  * https://github.com/psf/black

[Google Java Format](https://github.com/google/google-java-format) 처럼 사용자 커스터마이징 없이 알아서 해주는 강제 포멧터이다. 👍

pyproject.toml의 dependencies에 포함되어 있어 `uv sync` 시 자동 설치된다.

PyCharm에서도 그냥 저장시 액션에 등록해두면 바로 사용이 가능함. 

커밋할 때, Black으로 체크하도록 훅 설정을 등록 해두었는데, 

현재 프로젝트는 기본 설정을 다 해둔 상태여서, 앞의 설정들을 모두 마쳤다면 다음 명령만 수행해주면 된다.

```bash
pre-commit install
```

* **세부 사항**: [pre-commit과\_black을\_활용한\_커밋\_전\_포맷팅.md](docs/pre-commit과_black을_활용한_커밋_전_포맷팅.md)

### 특정 코드 블록에서 Black 포멧팅을 무시하기

특정 코드 블록에서 Black 포멧팅을 무시하고 싶을 때는 다음 주석을 사용:

```python
# fmt: off
# 이 사이의 코드는 Black이 포멧팅하지 않음
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
]
# fmt: on
```