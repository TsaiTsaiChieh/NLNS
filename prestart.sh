echo "Let the DB start ..."
sleep 10;
echo "Run migration ..."
alembic upgrade head
