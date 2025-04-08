# Step to use Knative in kubernetes

## Process

```
-> kubectl apply -f https://github.com/knative/net-contour/releases/download/knative-v1.12.0/contour.yaml
-> kubectl apply -f https://github.com/knative/net-contour/releases/download/knative-v1.12.0/net-contour.yaml

-> kubectl create namespace knative-serving

-> kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.12.0/serving-crds.yaml
-> kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.12.0/serving-core.yaml
-> kubectl patch configmap/config-network \
  --namespace knative-serving \
  --type merge \
  --patch '{"data":{"ingress.class":"contour.ingress.networking.knative.dev"}}'

```