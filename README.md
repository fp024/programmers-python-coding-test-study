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

* PyCham
  * https://www.jetbrains.com/pycharm/
* VSCode
  * ...



### 디펜던시 관리자 (pip)

[Poetry](https://github.com/python-poetry/poetry)나 [PDM](https://github.com/pdm-project/pdm)가 더 나은 것 같은데, 일단은 추가 설치없이 바로 사용할 수 있는 [pip](https://github.com/pypa/pip)로 사용해보자

##### pytest 설치

```sh
pip install pytest
```

.venv 가상환경에 해당 라이브러리가 설치된다.

##### 디펜던시 기록

```sh
pip freeze > requirements.txt
```

pytest 설치로인한 연관 디펜던시들의 라이브러리 이름, 버전 정보를 파일로 저장한다.

pytest 최초 설치후 디펜던시 기록을 했을 때, 나는 아래와 같이 저장되었다.

```
colorama==0.4.6
iniconfig==2.1.0
packaging==25.0
pluggy==1.6.0
Pygments==2.19.2
pytest==8.4.1

```



### 단위 테스트 프레임워크

* pytest
  * https://github.com/pytest-dev/pytest

파이썬에서는 컨테이너 비교가 언어자체적으로 간단해서.. 매처라이브러리를 따로 설치하지 않아도 될 것 같다.

> **Pytest는 기본 assert 문을 적극적으로 활용하는 것을 강력히 권장한다.**



### 코드 포맷터

* black
  * https://github.com/psf/black

[Google Java Format](https://github.com/google/google-java-format) 같이 사용자 커스터마이징 없이 알아서 해주는 포멧터이다. 

이것도 pip로 설치해주고 requirements.txt에 디펜던시를 새로 기록했다.

```sh
pip install black
pip freeze > requirements.txt
```

PyCharm에서도 그냥 저장시 액션에 등록해두면 바로 사용이 가능함. 

