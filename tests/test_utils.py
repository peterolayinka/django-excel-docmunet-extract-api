from django.test import Client
from django.test import TestCase

from test_plus.test import TestCase

from utils import SubjectPricing
# Create your tests here.
class SubjectPricingExtract(TestCase):
    def setUp(self):
        self.subject_pricing = SubjectPricing()

    def test_get_all_states_with_vicinities(self):
        states = self.subject_pricing.get_all_states_with_vicinities()
        state = [state_ for state_ in states if state_["state"].lower() == "lagos"]
        self.assertIn({"factor": 112.5, "name": "Yaba"}, state[0]["vicinities"])

        self.assertIn({"factor": 87.5, "name": "Abule-Egba"}, state[0]["vicinities"])

    def test_get_state_vicinities(self):
        state_vicinities = self.subject_pricing.get_state_vicinities("lagos")
        self.assertIn({"factor": 112.5, "name": "Yaba"}, state_vicinities)

        self.assertIn({"factor": 87.5, "name": "Abule-Egba"}, state_vicinities)

        state_vicinities = self.subject_pricing.get_state_vicinities("zamfara")
        self.assertIn({"factor": 87.5, "name": "Anka"}, state_vicinities)

        self.assertIn({"factor": 87.5, "name": "Zurmi"}, state_vicinities)

    def test_get_state_factor(self):
        factor = self.subject_pricing.get_state_factor("lagos")
        self.assertEqual(factor, 100)

        factor = self.subject_pricing.get_state_factor("zamfara")
        self.assertEqual(factor, 75)

        factor = self.subject_pricing.get_state_factor("kebbi")
        self.assertEqual(factor, 75)

    def test_get_vicinity_factor(self):
        factor = self.subject_pricing.get_vicinity_factor("gbagada")
        self.assertEqual(factor, 112.5)

        factor = self.subject_pricing.get_vicinity_factor("ewekoro")
        self.assertEqual(factor, 75)

        factor = self.subject_pricing.get_vicinity_factor("Magajin Gari")
        self.assertEqual(factor, 87.5)

    def test_get_hour_factor(self):
        hour_factor = self.subject_pricing.get_hour_factor(hour=2)
        self.assertEquals(hour_factor, 0)

        hour_factor2 = self.subject_pricing.get_hour_factor(hour=1.5)
        self.assertEquals(hour_factor2, 0.25)

        hour_factor3 = self.subject_pricing.get_hour_factor()
        self.assertEquals(hour_factor3, 0.5)

    def test_get_all_curriculums_and_factors(self):
        curriculums = self.subject_pricing.get_all_curriculums_and_factors()

        self.assertEqual(
            [
                {"name": "Nigerian", "factor": 100},
                {"name": "British", "factor": 150},
                {"name": "American", "factor": 250},
                {"name": "IPC ", "factor": 200},
                {"name": "Not Sure", "factor": 125},
            ],
            curriculums,
        )

    def test_get_curriculum_factor(self):
        curriculum_factor = self.subject_pricing.get_curriculum_factor()
        self.assertEquals(curriculum_factor, 125)

        curriculum_factor2 = self.subject_pricing.get_curriculum_factor(
            curriculums=["American"]
        )
        self.assertEquals(curriculum_factor2, 250)

        curriculum_factor3 = self.subject_pricing.get_curriculum_factor(
            curriculums=["British"]
        )
        self.assertEquals(curriculum_factor3, 150)

    def test_get_all_purposes_and_factors(self):
        purposes = self.subject_pricing.get_all_purposes_and_factors()

        self.assertIn({"name": "ACT Prep", "factor": 150}, purposes)
        self.assertIn({"name": "Phonics & Reading", "factor": 120}, purposes)
        self.assertIn({"name": "Grades Improvement", "factor": 120}, purposes)

    def test_get_purpose_factor(self):
        purpose_factor = self.subject_pricing.get_purpose_factor()
        self.assertEquals(purpose_factor, 100)

        purpose_factor2 = self.subject_pricing.get_purpose_factor(purposes=["sat prep"])
        self.assertEquals(purpose_factor2, 120)

        purpose_factor3 = self.subject_pricing.get_purpose_factor(
            purposes=["special needs"]
        )
        self.assertEquals(purpose_factor3, 150)

    def test_get_all_hours_and_factors(self):
        hours = self.subject_pricing.get_all_hours_and_factors()
        self.assertEqual(
            [{"hours": 1.0, "factor": 50}, {"hours": 1.5, "factor": 25}], hours
        )

    def test_get_hour_factor(self):
        hour_factor = self.subject_pricing.get_hour_factor(hour=2)
        self.assertEquals(hour_factor, 0)

        hour_factor2 = self.subject_pricing.get_hour_factor(hour=1.5)
        self.assertEquals(hour_factor2, 25)

        hour_factor3 = self.subject_pricing.get_hour_factor()
        self.assertEquals(hour_factor3, 50)

    def test_get_all_subjects_and_their_prices(self):
        subject_and_price = self.subject_pricing.get_all_subjects_and_their_prices()
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
                self.assertEqual(
                    self.subject_pricing.get_subject_price(subject),
                    expected_prices[index],
                )

    def test_calculate_hourly_price(self):

        hourly_price1 = self.subject_pricing.calculate_hourly_price(
            [{"goal": "phonics & reading"}],
            vicinity="gbagada",
            curriculums=["british"],
        )
        self.assertEqual(hourly_price1[0], 2025.0)

        hourly_price2 = self.subject_pricing.calculate_hourly_price(
            [{"goal": "special needs"}],
            vicinity="victoria island",
            curriculums=["american"],
        )
        self.assertEqual(hourly_price2[0], 4690.0)
        hourly_price3 = self.subject_pricing.calculate_hourly_price(
            [
                {"goal": "phonics & reading"},
                {"goal": "special needs"},
                {"goal": "school exam prep"},
            ],
            vicinity="ilupeju",
            curriculums=["american"],
        )
        self.assertEqual(hourly_price3[0], 6200.0)

    def test_if_curriculum_field_was_updated(self):
        purposes = ['Checkpoint Prep','Homeschooling']
        curriculums = ['Nigerian']
        self.assertEqual(len(curriculums),1)
        new_curriculum = self.subject_pricing.update_curriculums(purposes,curriculums)
        self.assertEqual(len(new_curriculum),2)
        self.assertIn('British',new_curriculum)
        