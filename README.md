# project_light
Hate Speech Detector for UIUC Project

This is a project designed to scan the comments sections of news sites seeking to identify keywords related to hate speech.  Key components
- Article Scan filter - filters which articles are scanned.  Article keywords are used to to identify which articles are scanned.  Keywords have time periods to reflect hot topics of the moment.
- Comment keyword search - allows users to identify keywords for review and assigns a weight to each keyword.  Keywords can be filtered for a set period of time.
- Source definitions - xPath filters used to help the article scanner identify articles and comments
