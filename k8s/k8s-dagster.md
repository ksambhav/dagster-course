# [Dagster on Kubernetes](https://artifacthub.io/packages/helm/dagster/dagster)

```commandline
kubectl create ns dagster
```

```commandline
helm repo add dagster https://dagster-io.github.io/helm
```
### Using postgres cluster running in K8s

Host : `my-postgres-postgresql.postgres.svc.cluster.local`

```commandline
create database my_dagster;
```
```commandline
create user dagster with password 'password';
```
```commandline
grant all privileges on database my_dagster to dagster;
```
```commandline
ALTER DATABASE my_dagster OWNER TO dagster;
```

```commandline
psql -U dagster -d my_dagster
```
```commandline
helm upgrade --install my-dagster dagster/dagster -n dagster -f k8s/values.yaml
```