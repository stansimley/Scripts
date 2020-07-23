# google-cloud-database
*python script to push all .csv type data from a folder to a Google Cloud Platform (GCP) MySQL database*

## Prerequisites:
* Set up GCP account: Create project, instance and database
* Download google_cloud_proxy to connect Cloud SQL to external applications (python in this case)

Useful links:  
https://cloud.google.com/sql/docs/mysql/create-manage-databases  
https://cloud.google.com/sql/docs/mysql/create-instance  
https://cloud.google.com/sql/docs/mysql/connect-external-app  

## Abstract
Converting various types of CSV files to SQL may require different specifications depending on encoding, delimiting, datatypes, etc.
This script aims to tackle the problem in the most general way possible to provide ease of uploading data when demands for optimization are not too heavy.
