"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from unittest.mock import patch, Mock

from GitHubAPI import getRepos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    git_info = {
        "id": "Jhector10",
        "repoCount": 2,
        "repos": [
            {
                'Repo': 'ClassifyTriangles',
                 "Commits": 9
            },
            {
                'Repo': 'GitHubAPI',
                'Commits': 15
            }
        ]
    }

    def testUserID(self): 
        with patch('GitHubAPI.getRepos') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = self.git_info
        self.assertEqual(getRepos("Jhector10")["id"], 'Jhector10')

    def testRepoCount(self): 
        with patch('GitHubAPI.getRepos') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = self.git_info
        self.assertEqual(getRepos("Jhector10")["repoCount"], 2)
        
    def testFirstRepo(self): 
        with patch('GitHubAPI.getRepos') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = self.git_info
        self.assertEqual(getRepos("Jhector10")["repos"][0], {"Repo": "ClassifyTriangles", "Commits": 9})

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()