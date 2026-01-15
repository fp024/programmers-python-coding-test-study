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

### 1. 최초 설치

먼저 uv 도구를 설치해준다.

```sh
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

이후 프로젝트 루트에서 다음 명령어로 가상환경(`.venv`) 생성 및 패키지를 전체 설치(동기화)한다.

```sh
uv sync
```

### 2. 라이브러리 추가/제거

새로운 라이브러리를 추가하면 `pyproject.toml`과 `uv.lock`에 자동으로 반영된다.

```sh
# 패키지 추가
uv add <패키지명>

# 패키지 제거
uv remove <패키지명>
```

### 3. 라이브러리 업데이트

전체 라이브러리를 최신 버전으로 업데이트한다.

```sh
uv sync --upgrade
```

### 4. pre-commit 훅 버전 업데이트

```sh
uv run pre-commit autoupdate
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
uv run pytest

# 특정 파일만 실행
uv run pytest tests/lv02/test_exam004_17684.py

# 자세한 출력 (verbose)
uv run pytest tests/lv02/test_exam004_17684.py -v

# 패턴 매칭으로 실행 (파일명/함수명에 'exam026' 포함)
uv run pytest -k exam004_17684

# 특정 테스트 함수만 실행
uv run pytest tests/lv02/test_exam004_17684.py::test_solution_me

# 가상환경에서 실행
uv run python -m pytest tests/lv02/test_exam004_17684.py -v
```



## 코드 포매터 & 자동화 (pre-commit)

`pre-commit`을 사용하여 커밋 시 코드를 자동 포매팅하고, 푸시 전 테스트를 수행합니다.

### 1. 훅 설치

```bash
# 방법 1: 현재 README처럼 각각 실행 (권장)
uv run pre-commit install                     # 커밋 시 실행될 훅 설치 (Black 등)
uv run pre-commit install --hook-type pre-push # 푸시 시 실행될 훅 설치 (Pytest)

# 방법 2: 한 번에 설치
uv run pre-commit install --hook-type pre-commit --hook-type pre-push
```

### 2. 설정 내용 ([`.pre-commit-config.yaml`](.pre-commit-config.yaml))

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.12.0
    hooks:
      - id: black
      - id: black-jupyter

  # pytest는 로컬 명령이므로 repo: local로 분리
  - repo: local
    hooks:
      - id: pytest
        name: pytest (pre-push)
        entry: uv run pytest -vv -s
        language: system
        pass_filenames: false
        stages: [pre-push]
```

- **commit 단계**: `black`, `black-jupyter` 실행 (코드 포매팅)
- **push 단계**: `pytest` 실행 (전체 테스트 통과 시에만 푸시 허용)

> 💡 테스트를 건너뛰고 강제 푸시하려면: `git push --no-verify`


* Black
  * https://github.com/psf/black

[Google Java Format](https://github.com/google/google-java-format) 처럼 사용자 커스터마이징 없이 알아서 해주는 강제 포매터이다. 👍

`pyproject.toml`의 dependencies에 포함되어 있어 `uv sync` 시 자동 설치된다.

PyCharm에서도 저장 시 액션에 등록하여 바로 사용 가능하다.

* **세부 사항**: [pre-commit과\_black을\_활용한\_커밋\_전\_포맷팅.md](docs/pre-commit과_black을_활용한_커밋_전_포맷팅.md)

### 특정 코드 블록에서 Black 포매팅을 무시하기

특정 코드 블록에서 Black 포매팅을 무시하고 싶을 때는 다음 주석을 사용:

```python
# fmt: off
# 이 사이의 코드는 Black이 포매팅하지 않음
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
]
# fmt: on
```