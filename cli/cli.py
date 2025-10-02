import typer
import requests
import json
import uuid

app = typer.Typer(help="Simple Service CLI")

API_URL = "http://127.0.0.1:8000/api"

@app.command()
def create(name: str, description: str = ""):
    """Yeni item oluştur"""
    payload = { "name": name, "description": description, "id": str(uuid.uuid4()) }
    r = requests.post(f"{API_URL}/items", json=payload)
    r.raise_for_status()
    typer.echo(f"Item created")
    typer.echo(json.dumps(r.json(), indent=2))

@app.command()
def list_items():
    r = requests.get(f"{API_URL}/items")
    r.raise_for_status()
    typer.echo(r.text)

@app.command()
def get(item_id: str):
    r = requests.get(f"{API_URL}/items/{item_id}")
    if r.status_code == 404:
        typer.echo(f"Item not found", err=True)
        raise typer.Exit(code=1)
    r.raise_for_status()
    typer.echo(r.text)

if __name__ == "__main__":
    app()