python manage.py collectstatic --no-input
python manage.py makemigrations

# python manage.py makemigrations authentication content student_loan event api
python manage.py migrate

python manage.py migrate --run-syncdb
# python manage.py compilemessages -l th

python manage.py runserver 0.0.0.0:8000
