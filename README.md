# GitHubAPI

[![build status of HW05a_Mocking](https://travis-ci.org/Jhector10/GitHubAPI.svg?branch=HW05a_Mocking)](https://travis-ci.org/Jhector10/GitHubAPI)

Testing on git api calls. Testing fails if it reachs a total of 2 repo calls.

Write a function that will take as input a GitHub user ID.  The output from the function will be a 
list of the names of the repositories that the user has, along with the number of commits that are in each 
of the listed repositories.

In this assignment you will use a mocking package to "mock" your program's external dependence on GitHub, 
so that you can guarantee that your unit tests will run consistently ever time you run them, no matter 
how many times you run them, and no matter what changes you make to your repos.
