import unittest

import clinic_project


class ClinicProjectTest(unittest.TestCase):
    def test_add_patient_and_report(self):
        state = clinic_project.new_state()
        patient_id = clinic_project.add_patient(
            state,
            name="Mina",
            age=31,
            gender="f",
            weight_kg=62,
            height_cm=165,
            conditions=["asthma"],
            symptoms=["fever", "cough"],
        )

        clinic_project.book_appointment(state, patient_id, "Monday", "9:00")
        report = clinic_project.patient_report(state, patient_id)

        self.assertEqual(report["name"], "Mina")
        self.assertEqual(report["bmi"], 22.77)
        self.assertEqual(report["symptom_score"], 6)
        self.assertEqual(report["appointment"]["status"], "Booked")

    def test_slot_cannot_be_booked_twice(self):
        state = clinic_project.new_state()
        first = clinic_project.add_patient(state, "Ali", 20, "M", 70, 175, [], [])
        second = clinic_project.add_patient(state, "Sara", 22, "F", 60, 165, [], [])

        clinic_project.book_appointment(state, first, "Monday", "9:00")

        with self.assertRaises(ValueError):
            clinic_project.book_appointment(state, second, "Monday", "9:00")


if __name__ == "__main__":
    unittest.main()
