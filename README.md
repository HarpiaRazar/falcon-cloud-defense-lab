# Falcon Cloud Defense Lab

Laboratório de DevSecOps e segurança de containers utilizando:

- GitHub
- Jenkins
- Docker
- Amazon ECR
- Amazon EKS
- CrowdStrike Falcon Cloud Security
- Falcon Kubernetes Admission Controller
- Falcon Container Sensor

## Objetivo

Demonstrar o ciclo de proteção de uma aplicação desde o desenvolvimento e análise da imagem até a proteção em runtime dentro do Kubernetes.

## Fluxo planejado

Código → GitHub → Jenkins → Security Scans → Docker → ECR → EKS → Falcon KAC → Runtime Protection