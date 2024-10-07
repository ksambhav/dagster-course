FROM python:3.12-slim
WORKDIR /home/dagster

RUN pip install \
    dagster==1.8 \
    dagster-postgres \
    dagster-duckdb \
    geopandas \
    kaleido \
    pandas \
    plotly \
    shapely \
    pyarrow \
    dagster-cloud \
#    dagster-aws \
    dagster-k8s \
    dagster-celery[flower,redis,kubernetes] \
    dagster-celery-k8s
#    dbt-duckdb \
#    duckdb \
#    dagster-dbt
EXPOSE 3030
# Get example pipelines
COPY ./dagster_university/ dagster_university/
COPY ./data data/
COPY /wb_etl wb_etl/
COPY workspace.yaml workspace.yaml