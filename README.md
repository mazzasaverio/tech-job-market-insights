# TechJobMarketInsights

## Overview
This web application aims to track the tech job market by providing various features:

### Sections
1. **InterviewPrepHub**: A Q&A section to help users prepare for tech and data job interviews. Users can filter questions based on tags, types, and categories.
2. **TechInsights**: A blog section where articles related to the tech industry can be posted and read.
3. **JobMarketTrends**: A statistics section that displays information scraped from job descriptions.

## Deployment
The application can be deployed using Docker containers. Specific instructions will be added soon.

### Environment Variables
Before deploying or running the application, make sure to set the following environment variables:

- `MONGO_URL`: The URL for connecting to your MongoDB instance.
- `DB_NAME`: The name of the MongoDB database. Default is `tech-job-market-insights`.
- `COLLECTION_NAME`: The name of the MongoDB collection. Default is `interview-prep-questions`.
