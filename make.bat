@echo off

if "%1" == "build" (
  if "%2" == "cli" goto :buildcli
  if "%2" == "gui" goto :buildgui
  goto :buildall
)
if "%1" == "clean" (
  if "%2" == "cli" goto :cleancli
  if "%2" == "gui" goto :cleangui
  goto :cleanall
)
goto :eof

:buildcli
call :cleancli
echo building cli...
pyinstaller --noconfirm --onefile --console --name trag --distpath dist\cli  main.py
@echo d | xcopy /s /q config dist\cli\config
@echo d | xcopy /s /q static dist\cli\static
@echo f | xcopy /q "docs\CLI_USAGE.md" "dist\cli\README.md"
call :postbuild
goto :eof

:buildgui
call :cleangui
echo building gui...
rem yet to implement
call :postbuild
goto :eof

:postbuild
del /q *.spec
rmdir /s /q __pycache__
rmdir /s /q build
goto :eof

:buildall
call :cleanall
call :buildcli
call :buildgui
goto :eof

:cleancli
echo cleaning the dist\cli directory...
rd /s /q dist\cli
md dist\cli
goto :eof

:cleangui
echo cleaning the dist\gui directory...
rd /s /q dist\gui
md dist\gui
goto :eof

:cleanall
call :cleancli
call :cleangui
goto :eof
