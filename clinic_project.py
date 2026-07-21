from __future__ import annotations

from copy import deepcopy
from typing import Any

DEFAULT_SLOTS = {
    "Monday": ["9:00", "10:00", "11:00"],
    "Wednesday": ["9:00", "10:00", "11:00"],
    "Saturday": ["9:00", "10:00", "11:00"],
}

SYMPTOM_SEVERITY = {
    "fever": 4,
    "cough": 2,
    "chest pain": 5,
    "fatigue": 3,
    "headache": 2,
    "nausea": 3,
    "shortness of breath": 5,
}


def new_state() -> dict[str, Any]:
    return {
        "next_id": 1,
        "patients": {},
        "appointments": {},
        "available_slots": deepcopy(DEFAULT_SLOTS),
    }


def add_patient(
    state: dict[str, Any],
    name: str,
    age: int,
    gender: str,
    weight_kg: float,
    height_cm: float,
    conditions: list[str],
    symptoms: list[str],
) -> str:
    if age < 0:
        raise ValueError("Age cannot be negative")
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive")

    patient_id = str(state["next_id"])
    state["next_id"] += 1
    state["patients"][patient_id] = {
        "name": name.strip(),
        "age": age,
        "gender": gender.strip().upper(),
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "conditions": [item.strip() for item in conditions if item.strip()],
        "symptoms": [item.strip().lower() for item in symptoms if item.strip()],
    }
    return patient_id


def book_appointment(state: dict[str, Any], patient_id: str, day: str, time: str) -> dict[str, str]:
    if patient_id not in state["patients"]:
        raise KeyError("Patient not found")
    if patient_id in state["appointments"]:
        raise ValueError("Patient already has an appointment")
    if day not in state["available_slots"] or time not in state["available_slots"][day]:
        raise ValueError("Slot is not available")

    state["available_slots"][day].remove(time)
    appointment = {"day": day, "time": time, "status": "Booked"}
    state["appointments"][patient_id] = appointment
    return appointment


def update_symptoms(state: dict[str, Any], patient_id: str, symptoms: list[str]) -> None:
    if patient_id not in state["patients"]:
        raise KeyError("Patient not found")
    state["patients"][patient_id]["symptoms"] = [item.strip().lower() for item in symptoms if item.strip()]


def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive")
    height_m = height_cm / 100
    return weight_kg / (height_m**2)


def symptom_score(symptoms: list[str]) -> int:
    return sum(SYMPTOM_SEVERITY.get(symptom.lower(), 0) for symptom in symptoms)


def patient_report(state: dict[str, Any], patient_id: str) -> dict[str, Any]:
    if patient_id not in state["patients"]:
        raise KeyError("Patient not found")
    patient = state["patients"][patient_id]
    return {
        "patient_id": patient_id,
        "name": patient["name"],
        "age": patient["age"],
        "bmi": round(calculate_bmi(patient["weight_kg"], patient["height_cm"]), 2),
        "conditions": list(patient["conditions"]),
        "symptoms": list(patient["symptoms"]),
        "symptom_score": symptom_score(patient["symptoms"]),
        "appointment": state["appointments"].get(patient_id),
    }


if __name__ == "__main__":
    clinic = new_state()
    patient_id = add_patient(clinic, "Mina", 31, "F", 62, 165, ["asthma"], ["fever", "cough"])
    book_appointment(clinic, patient_id, "Monday", "9:00")
    print(patient_report(clinic, patient_id))
