import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/prakash126ml/mlops-mini-project.mlflow")

# Initialize MLflow and connect to the Dagshub repository
dagshub.init(repo_owner='prakash126ml', repo_name='mlops-mini-project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)