# flask-frontend-hostname
Front end for `flask-backend-hostname`.

In the azure-pipelines.yml update the `azdo-gcp-dev` with your google  
project name.

This application has a dependency on the `flask-backend-hostname`  
service.

It will try and connect to the kubernetes service named  
`backend-service` within the same namespace.

If it cannot detect the `POD_NAMESPACE` environment variable as defined
in the [deployment.yaml](deployment.yaml) then it will default to:
`http://localhost:5000` for the purposes of local development.