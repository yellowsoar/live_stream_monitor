export C_FORCE_ROOT="true"

celery \
	-A live_stream_monitor \
	worker \
	-l INFO &

python manage.py \
	collectstatic \
	--clear \
	--link \
	--noinput

python manage.py \
	migrate

uvicorn \
	live_stream_monitor.asgi:application \
	--host 0.0.0.0 \
	--port 8000 \
	--access-log
