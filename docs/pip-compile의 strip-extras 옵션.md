# pip-compile의 strip-extras 옵션

> ### `--strip-extras` 옵션에 대한 설명



## Extra Dependencies란?

Python 패키지는 선택적 기능을 위한 추가 의존성을 정의할 수 있습니다. 이를 "extras"라고 합니다.

**예시:**
```python
# setup.py에서 정의된 extras
extras_require={
    'dev': ['pytest', 'black'],
    'docs': ['sphinx', 'mkdocs'],
    'all': ['pytest', 'black', 'sphinx', 'mkdocs']
}
```

설치할 때는 이렇게 사용합니다:
```bash
pip install mypackage[dev]     # dev extras 포함
pip install mypackage[dev,docs] # 여러 extras 포함
```

## `--strip-extras` 옵션의 효과

### 1. **`--strip-extras` 없이** 컴파일한 경우:
```txt
# requirements.txt
pytest==7.4.0
black==23.7.0
jupyter==1.0.0
pre-commit==3.3.3
    # via -r requirements.in
somepackage[dev,testing]==1.0.0
    # via pytest (extras: dev, testing)
```

### 2. **`--strip-extras` 옵션**을 사용한 경우:
```txt
# requirements.txt  
pytest==7.4.0
black==23.7.0
jupyter==1.0.0
pre-commit==3.3.3
    # via -r requirements.in
somepackage==1.0.0
    # via pytest
```

## 왜 제거하는 게 좋을까?

### 1. **깔끔한 파일**
- extras 정보가 없어서 requirements.txt가 더 읽기 쉽습니다.

### 2. **재현성 향상**
- extras 정보가 있으면 다른 환경에서 설치할 때 혼란을 줄 수 있습니다.

### 3. **호환성**
- 일부 도구들이 extras 문법을 제대로 파싱하지 못할 수 있습니다.

## 현재 프로젝트에 미치는 영향

현재 requirements.in의 패키지들:
- `pytest` - 테스트 도구, extras 거의 없음
- `black` - 포매터, extras 거의 없음  
- `jupyter` - 노트북, 몇 가지 extras 있지만 기본 기능으로 충분
- `pre-commit` - Git 훅 도구, extras 거의 없음

이 프로젝트에서는 **extras가 거의 없는 도구들**이라 `--strip-extras`를 사용해도 전혀 문제없습니다! 

오히려 더 깔끔하고 안정적인 requirements.txt가 생성될 것입니다. 👍