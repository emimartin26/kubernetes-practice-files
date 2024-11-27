# Configurar ingress local

## Requeriments:
 - minikube
 - kubectl


 ## Steps

 1. [Set up Ingress on Minikube with the NGINX Ingress Controller](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/#enable-the-ingress-controller)
    - key points:
        - run `minikube tunnel`
        - run ```bash
            curl --resolve "test.local:80:127.0.0.1" -i http://test.local
            ```
        - Add `127.0.0.1 test.local` in `/etc/hosts`

`


 2. eval $(minikube docker-env)
 3. docker build -t webserver:v1 ./webserver
 4. docker build -t frontend:v1 ./frontend
 2. kubectl apply -f kube/deploy-backend.yaml
 2. kubectl apply -f kube/deploy-backend.yaml
 3. kubectl apply -f kube/deploy-frontend.yaml
 4. kubectl apply -f kube/ingress.yaml
 5. Check:

 ```bash
 curl http://test.local/frontend
 curl http://test.local/api
 ```


 ## Utils commands
 - kubectl port-forward service/fastapi-app 8080:8080
 - kubectl logs fastapi-app-69f859466f-cd96c
 - kubectl describe pod|service|deployment|ingress
 - kubectl get services
 - kubectl get pods
 - kubectl get deployments
 - docker build -t {image_name}:{version}
 ***para que kubernetes veas las imagenes docker, hay que buildear la imagen en el contexto de minikube, correr el siguiente comando***
`eval $(minikube docker-env)`y ejecutar build anterior.

