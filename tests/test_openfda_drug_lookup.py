import unittest

import openfda_drug_lookup


class OpenFdaDrugLookupTest(unittest.TestCase):
    def test_build_query_url(self):
        url = openfda_drug_lookup.build_query_url("cefixime", limit=3)
        self.assertIn("limit=3", url)
        self.assertIn("openfda.generic_name", url)
        self.assertIn("cefixime", url)

    def test_parse_drug_results(self):
        payload = {
            "results": [
                {
                    "openfda": {"manufacturer_name": ["Example Pharma"]},
                    "products": [
                        {
                            "brand_name": "CEF",
                            "dosage_form": "TABLET",
                            "active_ingredients": [{"name": "CEFIXIME", "strength": "400MG"}],
                            "route": ["ORAL"],
                            "marketing_status": "Prescription",
                        }
                    ],
                }
            ]
        }

        meds = openfda_drug_lookup.parse_drug_results(payload)

        self.assertEqual(len(meds), 1)
        self.assertEqual(meds[0]["brand_name"], "CEF")
        self.assertEqual(meds[0]["manufacturer"], "Example Pharma")
        self.assertEqual(meds[0]["active_ingredients"], "CEFIXIME 400MG")


if __name__ == "__main__":
    unittest.main()
