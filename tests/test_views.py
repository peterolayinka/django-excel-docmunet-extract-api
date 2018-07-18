import json

from django.test import Client
from django.test import TestCase
from django.urls import reverse
from test_plus.test import TestCase

from utils import SubjectPricing

# Create your tests here.
class SubjectPricingExtractViews(TestCase):
    def setUp(self):
        self.subject_pricing = SubjectPricing()

    def test_get_all_states_with_vicinities(self):
        resp = self.client.get(reverse("all_state_with_vicinity"))
        state = [
            state_
            for state_ in resp.json()["data"]
            if state_["state"].lower() == "lagos"
        ]
        self.assertIn({"factor": 112.5, "name": "Yaba"}, state[0]["vicinities"])

        self.assertIn({"factor": 87.5, "name": "Abule-Egba"}, state[0]["vicinities"])

    def test_get_state_vicinities(self):
        resp = self.client.get(reverse("state_with_vicinities", args=["lagos"]))
        state_vicinities = resp.json()["data"]
        self.assertIn({"factor": 112.5, "name": "Yaba"}, state_vicinities)

        self.assertIn({"factor": 87.5, "name": "Abule-Egba"}, state_vicinities)

        resp = self.client.get(reverse("state_with_vicinities", args=["zamfara"]))
        state_vicinities = resp.json()["data"]
        self.assertIn({"factor": 87.5, "name": "Anka"}, state_vicinities)

        self.assertIn({"factor": 87.5, "name": "Zurmi"}, state_vicinities)

    def test_get_state_factor(self):
        resp = self.client.get(reverse("get_state_factor", args=["lagos"]))
        self.assertEqual(resp.json(), {"data": 100.0})

        resp = self.client.get(reverse("get_state_factor", args=["zamfara"]))
        self.assertEqual(resp.json(), {"data": 75})

        resp = self.client.get(reverse("get_state_factor", args=["kebbi"]))
        self.assertEqual(resp.json(), {"data": 75})

    def test_get_vicinity_factor(self):
        resp = self.client.get(reverse("vicinity_factor", args=["gbagada"]))
        self.assertEqual(resp.json()["data"], 112.5)

        resp = self.client.get(reverse("vicinity_factor", args=["ewekoro"]))
        self.assertEqual(resp.json()["data"], 75)
        resp = self.client.get(reverse("vicinity_factor", args=["Magajin-Gari"]))
        self.assertEqual(resp.json()["data"], 87.5)

    def test_get_hour_factor(self):
        resp = self.client.get(reverse("hour_factor", args=[2]))
        self.assertEqual(resp.json()["data"], 0)

        resp = self.client.get(reverse("hour_factor", args=[1.5]))
        self.assertEqual(resp.json()["data"], 25)

        resp = self.client.get(reverse("default_hour_factor"))
        self.assertEqual(resp.json()["data"], 50)

    def test_get_all_curriculums_and_factors(self):
        resp = self.client.get(reverse("all_curriculum_factor"))

        self.assertEqual(
            [
                {"name": "Nigerian", "factor": 100},
                {"name": "British", "factor": 150},
                {"name": "American", "factor": 250},
                {"name": "IPC ", "factor": 200},
                {"name": "Not Sure", "factor": 125},
            ],
            resp.json()["data"],
        )

    def test_get_curriculum_factor(self):
        resp = self.client.get(reverse("default_curriculum_factor"))
        self.assertEquals(resp.json()["data"], 125)

        resp = self.client.get(reverse("curriculum_factor", args=["american"]))
        self.assertEquals(resp.json()["data"], 250)

        resp = self.client.get(reverse("curriculum_factor", args=["american, british"]))
        self.assertEquals(resp.json()["data"], 250)

    def test_get_all_purposes_and_factors(self):
        resp = self.client.get(reverse("all_purpose_and_factor"))
        purposes = resp.json()["data"]
        self.assertIn({"name": "ACT Prep", "factor": 150}, purposes)
        self.assertIn({"name": "Phonics & Reading", "factor": 120}, purposes)
        self.assertIn({"name": "Grades Improvement", "factor": 120}, purposes)

    def test_get_purpose_factor(self):
        resp = self.client.get(reverse("default_purpose_and_factor"))
        purpose_factor = resp.json()["data"]
        self.assertEquals(purpose_factor, 100)

        resp = self.client.get(reverse("purpose_and_factor", args=["sat-prep"]))
        purpose_factor2 = resp.json()["data"]
        self.assertEquals(purpose_factor2, 120)

        resp = self.client.get(reverse("purpose_and_factor", args=["special-needs"]))
        purpose_factor3 = resp.json()["data"]
        self.assertEquals(purpose_factor3, 150)

    def test_get_all_hours_and_factors(self):
        resp = self.client.get(reverse("all_hour_factor"))
        hours = resp.json()["data"]
        self.assertEqual(
            [{"hours": 1.0, "factor": 50}, {"hours": 1.5, "factor": 25}], hours
        )

    def test_get_all_subjects_and_their_prices(self):
        resp = self.client.get(reverse("all_subject_price"))
        subject_and_price = resp.json()["data"]
        self.assertIn({"name": "Home Tutoring", "price": 1000}, subject_and_price)
        self.assertIn({"name": "Web Development", "price": 2000}, subject_and_price)
        self.assertIn({"name": "Yoga", "price": 1750}, subject_and_price)

    def test_get_subject_price(self):
        subjects = [
            "Business Development",
            "Data Structures",
            "C Programming",
            "Graphic Design",
            "Web Development",
        ]
        expected_prices = [3000, 2500, 2500, 1500, 2000]
        for index, subject in enumerate(subjects):
            with self.subTest(subject=subject):
                resp = self.client.get(reverse("subject_price", args=[subject]))
                subject_and_price = resp.json()["data"]
                self.assertEqual(subject_and_price, expected_prices[index])

    def test_calculate_hourly_price(self):
        resp = self.client.post(
            reverse("hourly_price"),
            data=json.dumps(
                {
                    "students": [{"goal": "phonics & reading"}],
                    "no_of_hours": 1,
                    "subject": "home tutoring",
                    "vicinity": "gbagada",
                    "curriculums": ["british"],
                }
            ),
            content_type="application/json",
        )
        subject_and_price = resp.json()["data"]
        self.assertEqual(subject_and_price, {'hourly_price': 2025.0, 'transport_fare': 1012.5})

        resp = self.client.post(
            reverse("hourly_price"),
            data=json.dumps(
                {
                    "students": [
                        {"goal": "special needs"},
                    ],
                    "no_of_hours": 2,
                    "subject": "home tutoring",
                    "vicinity": "victoria island",
                    "curriculums": ["american"],
                }
            ),
            content_type="application/json",
        )
        subject_and_price = resp.json()["data"]
        self.assertEqual(subject_and_price, {'hourly_price': 4690.0, 'transport_fare': 0})

        resp = self.client.post(
            reverse("hourly_price"),
            data=json.dumps(
                {
                    "students": [
                        {"goal": "phonics & reading"},
                        {"goal": "special needs"},
                        {"goal": "school exam prep"},
                    ],
                    "state": "lagos",
                    "vicinity": "ilupeju",
                    "curriculums": ["american"],
                }
            ),
            content_type="application/json",
        )
        subject_and_price = resp.json()["data"]
        self.assertEqual(subject_and_price, {'hourly_price': 6200.0, 'transport_fare': 3101})
