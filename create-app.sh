#!/bin/sh
echo "アプリ名（半角英字）："
read app_name

python3 manage.py startapp $app_name