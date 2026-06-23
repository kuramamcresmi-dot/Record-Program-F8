@echo off
chcp 65001 >nul
cls

echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║                                                          ║
echo  ║              ShivaClips v2.0  - Setup                   ║
echo  ║           Made By MrShivada For Public Service          ║
echo  ║                                                          ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.
echo  ────────────────────────────────────────────────────────────
echo.
echo   Türkçe için  [ TR ] yazın
echo   For English  [ EN ] type
echo.
echo  ────────────────────────────────────────────────────────────
echo.

:ask_lang
set /p LANG_INPUT=  Language / Dil: 

if /i "%LANG_INPUT%"=="tr" goto :set_tr
if /i "%LANG_INPUT%"=="en" goto :set_en
echo.
echo   [!] Geçersiz giriş / Invalid input. Lütfen TR veya EN yazın.
echo.
goto :ask_lang

:set_tr
echo {"lang":"tr"} > lang.json
echo.
echo  ✓ Dil Türkçe olarak ayarlandı.
goto :install

:set_en
echo {"lang":"en"} > lang.json
echo.
echo  ✓ Language set to English.
goto :install

:install
echo.
echo  ────────────────────────────────────────────────────────────
echo.
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  [HATA / ERROR] Python bulunamadi - Python not found!
    echo  https://python.org  ^(Python 3.10+^)
    pause
    exit /b 1
)

echo  [1/4] Upgrading pip...
python -m pip install --upgrade pip -q

echo  [1/5] Upgrading pip...
python -m pip install --upgrade pip -q

echo  [2/5] Installing dependencies...
pip install -r requirements.txt -q

echo  [3/5] Bundled FFmpeg (imageio-ffmpeg)...
python -c "import imageio_ffmpeg; print('  FFmpeg path:', imageio_ffmpeg.get_ffmpeg_exe())" 2>nul || pip install imageio-ffmpeg -q

echo  [4/5] Detecting GPU codec...
python -c "from core.recorder import _BEST_VCODEC; print('  Best video codec:', _BEST_VCODEC)" 2>nul || echo   (GPU check will run on first launch)

echo  [5/5] Creating folders...
if not exist "assets" mkdir assets
if not exist "clips"  mkdir clips
if not exist "temp"   mkdir temp
if not exist "logs"   mkdir logs

echo  Done!
echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║                                                          ║
echo  ║   Kurulum tamam!  /  Installation complete!             ║
echo  ║                                                          ║
echo  ║   Başlatmak için  /  To launch:                         ║
echo  ║                                                          ║
echo  ║              run.bat                                     ║
echo  ║                                                          ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.
pause
