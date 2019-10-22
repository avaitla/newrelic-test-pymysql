Issue:

We are noticing that even if we send traffic to newrelic (see perf_overview.png) which generates database queries, newrelic can't find the underlying queries (see no_database_queries.png).

Reproducing Locally:

1. Setup MySQL locally

2. Install requirements pip install -r requirements.txt

3. Include App name and newrelic key in newrelic.ini

4. Run (fill in variables): MYSQL_HOST=127.0.0.1 MYSQL_USER=root MYSQL_PASSWORD= MYSQL_DB=mysql NEW_RELIC_STARTUP_DEBUG=true NEW_RELIC_CONFIG_FILE=$(pwd)/newrelic.ini  NEW_RELIC_LICENSE_KEY=*** NEW_RELIC_APP_NAME="Newrelic Test" newrelic-admin run-program gunicorn -w 4 myapp:app --bind 0.0.0.0:8000 --access-logfile=-

4. Send test traffic: ab locally (increase n for longer duration): ab -n 100000 -c 2 "http://0.0.0.0:8000/"
