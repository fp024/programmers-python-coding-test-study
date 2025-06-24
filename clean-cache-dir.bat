@echo off
setlocal enabledelayedexpansion

REM =============================================================
REM Python 프로젝트 캐시 및 임시 파일 정리 스크립트
REM - __pycache__, .pytest_cache, .mypy_cache, .ipynb_checkpoints 등을 삭제합니다.
REM - 이 스크립트는 실행되는 폴더(루트) 및 하위 폴더의 모든 캐시 파일을 정리합니다.
REM =============================================================

REM 현재 배치 파일이 있는 디렉터리를 프로젝트 루트로 설정합니다.
set "ROOT_DIR=%~dp0"

echo.
echo =============================================================
echo 캐시 및 임시 파일 정리 시작
echo 대상 경로: %ROOT_DIR%
echo -------------------------------------------------------------
echo 다음 유형의 폴더를 삭제합니다: __pycache__, .pytest_cache, .mypy_cache, .ipynb_checkpoints
echo -------------------------------------------------------------
echo.
echo 삭제를 시작하려면 엔터 키를 누르십시오...
set /p DUMMY_VAR=""
echo.

set "deleted_count=0"

REM =============================================================
REM 1. __pycache__ 폴더 삭제
REM =============================================================
echo Cleaning __pycache__ folders...
for /d /r "%ROOT_DIR%" %%d in (__pycache__) do (
    if exist "%%d" (
        rd /s /q "%%d"
        echo  - Deleted: "%%d"
        set /a deleted_count+=1
    )
)

REM =============================================================
REM 2. .pytest_cache 폴더 삭제 (Pytest 캐시)
REM =============================================================
echo Cleaning .pytest_cache folders...
for /d /r "%ROOT_DIR%" %%d in (.pytest_cache) do (
    if exist "%%d" (
        rd /s /q "%%d"
        echo  - Deleted: "%%d"
        set /a deleted_count+=1
    )
)

REM =============================================================
REM 3. .mypy_cache 폴더 삭제 (Mypy 타입 체크 캐시)
REM =============================================================
echo Cleaning .mypy_cache folders...
for /d /r "%ROOT_DIR%" %%d in (.mypy_cache) do (
    if exist "%%d" (
        rd /s /q "%%d"
        echo  - Deleted: "%%d"
        set /a deleted_count+=1
    )
)

REM =============================================================
REM 4. .ipynb_checkpoints 폴더 삭제 (Jupyter Notebook 체크포인트)
REM =============================================================
echo Cleaning .ipynb_checkpoints folders...
for /d /r "%ROOT_DIR%" %%d in (.ipynb_checkpoints) do (
    if exist "%%d" (
        rd /s /q "%%d"
        echo  - Deleted: "%%d"
        set /a deleted_count+=1
    )
)

REM =============================================================
echo.
echo -------------------------------------------------------------
echo 캐시 및 임시 파일 정리 완료!
echo 총 %deleted_count%개의 캐시 폴더가 삭제되었습니다.
echo -------------------------------------------------------------
echo.
echo 창을 닫으려면 엔터 키를 누르십시오...
set /p DUMMY_VAR=""

endlocal