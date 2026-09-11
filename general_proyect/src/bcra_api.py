"""Clients for the public BCRA APIs used in this project.

Two separate APIs are involved:

- **Estadisticas / Principales Variables (v4.0)** — aggregate monetary and
  financial series (reserves, exchange rate, policy rate, etc.).
  Docs: https://principales-variables.bcra.apidocs.ar/
- **Central de Deudores (v1.0)** — per-debtor lookup by CUIT/CUIL/CDI:
  current debt, historical debt (up to 24 months) and rejected checks.
  Docs: https://deudores.bcra.apidocs.ar/

Important: Central de Deudores answers "what does this specific CUIT owe and
where", it does NOT expose aggregate mora-by-entity or mora-by-portfolio
(consumo/comercial) statistics. That aggregate breakdown is only published by
BCRA as the "Anexo estadístico del Informe sobre Bancos", a downloadable
Excel file with no JSON API:
https://www.bcra.gob.ar/catalogo_de_datos/anexo-estadistico-del-informe-sobre-bancos/

Both APIs are public and require no API key. `api.bcra.gob.ar` is known to
serve an incomplete TLS certificate chain, which makes `requests` raise
`SSLError` on some systems even though the certificate itself is valid;
`verify=False` is exposed on every function as an opt-in workaround for that.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

import requests

BASE_URL = "https://api.bcra.gob.ar"
MONETARIAS_URL = f"{BASE_URL}/estadisticas/v4.0/Monetarias"
DEUDAS_URL = f"{BASE_URL}/centraldedeudores/v1.0/Deudas"


def _get(url: str, params: Optional[Dict[str, Any]] = None, verify: bool = True) -> Dict[str, Any]:
    response = requests.get(url, params=params, verify=verify, timeout=30)
    response.raise_for_status()
    return response.json()


def list_monetary_variables(verify: bool = True) -> List[Dict[str, Any]]:
    """List every monetary/financial variable BCRA publishes (id, description, latest value and date)."""
    return _get(MONETARIAS_URL, verify=verify).get("results", [])


def get_monetary_series(
    id_variable: int,
    desde: Optional[str] = None,
    hasta: Optional[str] = None,
    offset: int = 0,
    limit: int = 3000,
    verify: bool = True,
) -> List[Dict[str, Any]]:
    """Fetch the historical values of one monetary variable as a flat list of `{"fecha", "valor"}`.

    `id_variable` comes from `list_monetary_variables()`. `desde`/`hasta` are
    "YYYY-MM-DD" strings; the API caps each response at `limit` rows (max
    3000), so paginate with `offset` for longer ranges. The raw response
    wraps the series as `results: [{"idVariable": ..., "detalle": [...]}]`;
    this returns just the `detalle` list.
    """
    params: Dict[str, Any] = {"offset": offset, "limit": limit}
    if desde:
        params["desde"] = desde
    if hasta:
        params["hasta"] = hasta
    results = _get(f"{MONETARIAS_URL}/{id_variable}", params=params, verify=verify).get("results", [])
    return results[0].get("detalle", []) if results else []


def get_deudas(identificacion: int, verify: bool = True) -> Dict[str, Any]:
    """Current debt situation for one CUIT/CUIL/CDI (single-subject lookup, not aggregate)."""
    return _get(f"{DEUDAS_URL}/{identificacion}", verify=verify)


def get_deudas_historicas(identificacion: int, verify: bool = True) -> Dict[str, Any]:
    """Historical (up to 24 months) debt situation for one CUIT/CUIL/CDI."""
    return _get(f"{DEUDAS_URL}/Historicas/{identificacion}", verify=verify)


def get_cheques_rechazados(identificacion: int, verify: bool = True) -> Dict[str, Any]:
    """Rejected checks for one CUIT/CUIL/CDI."""
    return _get(f"{DEUDAS_URL}/ChequesRechazados/{identificacion}", verify=verify)
