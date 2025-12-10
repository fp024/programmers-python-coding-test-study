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





## 디펜던시 관리자 (pip)

[Poetry](https://github.com/python-poetry/poetry)나 [PDM](https://github.com/pdm-project/pdm)가 더 나은 것 같은데, 일단은 추가 설치없이 바로 사용할 수 있는 [pip](https://github.com/pypa/pip)로 사용해보자

먼저 pip만을 사용하는 것에 비해 향샹된 기능을 제공하는 pip-tools를 설치한다.



#### `pip-tools`로 파이썬 의존성 관리하기

#### 0\. ✨ `venv` 가상 환경 설치

먼저 venv 환경을 생성하고 시작하자!

* [venv환경\_만들기.md](docs/venv환경_만들기.md)

#### 1\. `pip-tools` 설치

먼저, `pip-tools`를 개발 환경의 가상 환경(.venv)에 설치함.

```sh
pip install pip-tools
```

#### 2\. `requirements.in` 파일 생성

프로젝트의 \*\*최상위 종속성(Top-level dependencies)\*\*만 `requirements.in` 파일에 기록하면된다. 이곳에 직접 설치하고 싶은 패키지들만 나열하면 됨.

```sh
# requirements.in
pytest
black
jupyter
pre-commit
```

#### 3\. `requirements.txt` 파일 생성

다음 명령은 `requirements.in` 파일을 기반으로 **모든 하위 종속성까지 포함하고 버전을 고정한** `requirements.txt` 파일을 자동으로 생성한다.

```sh
pip-compile --strip-extras requirements.in
```

#### 4\. 라이브러리 설치

생성된 `requirements.txt` 파일을 이용해 필요한 모든 라이브러리를 가상 환경에 설치함.

```sh
pip install -r requirements.txt
```

#### 5\. 라이브러리 업데이트

기존 라이브러리를 최신 호환 버전으로 업데이트하려면, 다음 두 명령을 순서대로 실행함.

```sh
pip-compile --strip-extras requirements.in  # requirements.txt를 최신 버전으로 업데이트
pip install -r requirements.txt # 가상 환경의 라이브러리를 업데이트된 requirements.txt에 맞춰 설치/업데이트
pre-commit autoupdate # pre-commit에 설정된 black의 버전업은 이 명령으로 가능함
```

* `pre-commit autoupdate` : .pre-commit-config.yaml의 버전정보가 수정됨

  ```
  (.venv) C:\git\programmers-python-coding-test-study>pre-commit autoupdate
  [https://github.com/psf/black] updating 25.1.0 -> 25.11.0
  
  (.venv) C:\git\programmers-python-coding-test-study>
  ```

#### 6\. pip 업그레이드

```sh
python -m pip install --upgrade pip
```

> 💡 pip 같은 경우는... 가상환경 내부, 가상환경 외부 모두 업그레이드를 따로 해주도록 하자!
> 가상환경 외부에서는 기본 설치된 것이 pip 하나만 있음.




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

## 

## 코드 포맷터

* Black
  * https://github.com/psf/black

[Google Java Format](https://github.com/google/google-java-format) 처럼 사용자 커스터마이징 없이 알아서 해주는 강제 포멧터이다. 👍

이것도 위의 pip-tools 설명 부분에서  requirements.in 설정을 통해 설치가 되었다.

PyCharm에서도 그냥 저장시 액션에 등록해두면 바로 사용이 가능함. 

커밋할 때, Black으로 체크하도록 훅 설정을 등록 해두었는데, 

현재 프로젝트는 기본 설정을 다 해둔 상태여서, 앞의 설정들을 모두 마쳤다면 다음 명령만 수행해주면 된다.

```bash
pre-commit install
```

* **세부 사항**: [pre-commit과\_black을\_활용한\_커밋\_전\_포맷팅.md](docs/pre-commit과_black을_활용한_커밋_전_포맷팅.md)

