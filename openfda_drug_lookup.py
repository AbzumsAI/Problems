from __future__ import annotations

import json
from typing import Any
from urllib import parse, request

OPENFDA_URL = "https://api.fda.gov/drug/drugsfda.json"


def build_query_url(generic_name: str, limit: int = 5) -> str:
    if not generic_name.strip():
        raise ValueError("Generic name cannot be empty")
    params = {
        "limit": str(limit),
        "search": f'openfda.generic_name:"{generic_name.strip()}"',
    }
    return f"{OPENFDA_URL}?{parse.urlencode(params)}"


def ingredient_text(ingredients: list[dict[str, Any]]) -> str:
    names = []
    for ingredient in ingredients:
        name = ingredient.get("name") or ingredient.get("ingredient_name")
        strength = ingredient.get("strength")
        if name and strength:
            names.append(f"{name} {strength}")
        elif name:
            names.append(str(name))
    return " & ".join(names)


def parse_drug_results(payload: dict[str, Any]) -> list[dict[str, str]]:
    meds: list[dict[str, str]] = []
    for result in payload.get("results", []):
        openfda = result.get("openfda") or {}
        manufacturer = " & ".join(openfda.get("manufacturer_name") or [])
        for product in result.get("products") or []:
            meds.append(
                {
                    "brand_name": str(product.get("brand_name", "")),
                    "manufacturer": manufacturer,
                    "dosage_form": str(product.get("dosage_form", "")),
                    "active_ingredients": ingredient_text(product.get("active_ingredients") or []),
                    "route": " & ".join(product.get("route") or []),
                    "marketing_status": str(product.get("marketing_status", "")),
                }
            )
    return meds


def fetch_drug_info(generic_name: str, limit: int = 5) -> list[dict[str, str]]:
    url = build_query_url(generic_name, limit)
    req = request.Request(url, headers={"Accept": "application/json"})
    with request.urlopen(req, timeout=10) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return parse_drug_results(payload)


if __name__ == "__main__":
    for med in fetch_drug_info("cefixime"):
        print(med)
