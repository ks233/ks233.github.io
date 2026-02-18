@echo off
:: 设置字符集为 UTF-8，防止中文乱码
chcp 65001 >nul

echo ========================================
echo       🚀 正在执行无痕发布...
echo ========================================
echo.

echo [1/3] 正在暂存所有修改...
git add .

echo.
echo [2/3] 正在覆盖最后一次提交...
git commit --amend --no-edit

echo.
echo [3/3] 正在强制推送到 GitHub...
:: 这里默认你的分支是 main。如果是 master，请把下面的 main 改成 master
git push -f origin main

echo.
echo ========================================
echo       ✅ 发布完成！
echo ========================================
echo.

:: 暂停运行，方便你查看有没有报错提示。看完后按任意键窗口就会关闭
pause