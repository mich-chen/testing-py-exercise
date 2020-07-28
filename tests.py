"""Tests for Balloonicorn's Flask app."""

import unittest
import server


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        # test_client method to create a pretend web browser
        # make this an attribute .client
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        # self.client to get homepage route
        result = self.client.get('/')
        # check if string is in result.data which is the homepage html
        self.assertIn(b'having a party', result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get('/')
        self.assertIn(b'Please RSVP', result.data)
        # test that you don't see the party details
        self.assertNotIn(b'Party Details', result.data)
        

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': 'Jane', 'email': 'jane@jane.com'}

        result = self.client.post('/rsvp', data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        self.assertIn(b'Party Details', result.data)
        self.assertNotIn(b'Please RSVP', result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        rsvp_info = {'name': 'Mel Melitpolski', 'email': 'mel@ubermelon.com'}
        result = self.client.post('/rsvp', data=rsvp_info,
                                  follow_redirects=True)
        self.assertNotIn(b'Party Details', result.data)
        self.assertIn(b'Please RSVP', result.data)



if __name__ == '__main__':
    unittest.main()
