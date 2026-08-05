from fastapi import FastAPI

app = FastAPI(
    title="Falcon Cloud Defense Lab",
    description="Aplicação utilizada no laboratório DevSecOps com CrowdStrike Falcon.",
    version="1.0.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    """Retorna informações básicas sobre a aplicação."""
    return {
        "application": "Falcon Cloud Defense Lab",
        "status": "running",
        "message": "Aplicação executando com sucesso",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """Endpoint utilizado para verificar a saúde da aplicação."""
    return {
        "status": "healthy",
    }