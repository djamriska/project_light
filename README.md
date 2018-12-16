# project_light
Hate Speech Detector for UIUC Project

This is a project designed to scan the comments sections of news articles seeking to identify keywords related to hate speech.  Key components. By shining the light on these comments we can shame these individuals for promoting hate and potentially raise information to law enforcement.


Please view the project website for this application under the /html folder. 

The application runs behind the scenes against a collection of articles and associated comments. Each article is evaluated against a list of keywords indicating it may be a topic that generates comments of interest. For the identified articles it then extracts all comments and ranks them according to the keywords discovered. A list of articles ranked by the content of their comments is then returned to the end user on the results page.

Currently the application comes preconfigured to run against a set of articles and comments that have been scrapped from the web to allow the user to test the function

