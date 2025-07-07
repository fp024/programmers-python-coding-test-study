# venv 가상환경 만들기

> IDE로 하면 알아서 다 해주긴 하는데, 커맨드 라인에서 한번 시도해보았다. 😊



### `venv` (가상 환경) 생성 커맨드 라인 명령

`venv`는 파이썬 프로젝트마다 독립적인 실행 환경을 만들어주는 매우 중요한 도구이다.  프로젝트마다 필요한 라이브러리들을 각각 관리할 수 있게 해주어 의존성 충돌을 방지하고 환경을 깔끔하게 유지할 수 있다.

다음은 `venv`를 만들고 활성화하는 기본적인 명령이다.



#### 1. 가상 환경 생성

프로젝트의 루트 디렉토리에서 다음 명령어를 실행한다:

Bash

```sh
python -m venv 가상환경_폴더이름
```

- `python`: 현재 시스템에 설치된 파이썬 실행 파일을 지칭한다.
- `-m venv`: 파이썬 모듈 `venv`를 실행하라는 의미입니다. `venv`는 파이썬 표준 라이브러리에 포함되어 있어서 별도 설치 없이 사용할 수 있다.
- `가상환경_폴더이름`: 생성될 가상 환경 디렉토리의 이름입니다. 관례적으로 `venv`, `.venv`, 또는 `env` 등으로 많이 사용합니다. 예를 들어 `venv`라고 하면 `my_project/venv/` 디렉토리가 생성된다.

**예시:**

Bash

```sh
python -m venv venv
```

이렇게 실행하면 현재 디렉토리 안에 `venv`라는 이름의 새 폴더가 생기고, 그 안에 독립적인 파이썬 환경과 `pip`가 설치된다.



#### 2. 가상 환경 활성화 (Activate)

가상 환경을 만들었으면 이제 이 환경을 **활성화**해야 한더. 운영체제별로 명령이 조금 다르다.

- **Windows (PowerShell):**

  PowerShell

  ```sh
  .\이름_원하는_가상환경_폴더\Scripts\Activate.ps1
  ```

  **예시:** `.\venv\Scripts\Activate.ps1`

- **Windows (Command Prompt - cmd):**

  DOS

  ```sh
  가상환경_폴더이름\Scripts\activate.bat
  ```

  **예시:** `venv\Scripts\activate.bat`

- **Linux / Git Bash / macOS (Bash/Zsh):**

  Bash

  ```
  source 가상환경_폴더이름/Scripts/activate
  ```

  **예시:** `source venv/bin/activate`

가상 환경이 성공적으로 활성화되면, 터미널 프롬프트 앞에 괄호 안에 가상 환경 이름이 나타난다. (예: `(venv) your_username@your_computer:~/my_project$`) 이제 이 터미널에서는 가상 환경에 설치된 파이썬과 라이브러리를 사용하게 된다.



#### 3. 가상 환경 비활성화 (Deactivate)

활성화된 가상 환경을 비활성화하려면 단순히 다음 명령어를 입력한다:

Bash

```sh
deactivate
```

프롬프트에서 가상 환경 이름이 사라지면 비활성화된 것이다.



#### `requirements.txt`와 함께 사용하기

가상 환경을 활성화한 후에 `pip install -r requirements.txt` 명령어를 사용하면, 이 가상 환경 안에 `requirements.txt`에 명시된 라이브러리들이 설치되어 해당 프로젝트만을 위한 깨끗한 환경을 구축할 수 있다.

Bash

```sh
# 1. 가상 환경 생성
python -m venv .venv

# 2. 가상 환경 활성화 (macOS/Linux 예시)
source .venv/bin/activate

# 3. 필요한 라이브러리 설치 (requirements.txt가 있다면)
pip install -r requirements.txt

# 4. 작업 후 비활성화
deactivate
```

