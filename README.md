# Spotify-Data-Engineering-Project

Implemented this Architecture

![ARCHITECTURE](https://github.com/user-attachments/assets/12ec7cec-c01c-4612-8eef-6583a9a1f93b)




**Spotify-ETL Pipeline:**

<img width="928" alt="Screenshot 2024-09-29 at 12 41 25 AM" src="https://github.com/user-attachments/assets/fed6f115-44b3-4aa8-b9d7-4e515cb87964">



**Steps to Execute this Project:**

**S3 Bucket:**

1. Create the S3 Bucket
2. Create the Source Folder Where the Input Data is uploaded
3. Create the Target Folder-> To store the transformed data from Glue

**AWS Glue:**

4. Launch the AWS GLue Console and Open the Script Editor and upload the Spotify ETL.py
5. Include the Source and Target Path of S3 in the Script file
6. Name the Job Name
7. In Job Details Section, Add the IAM role which has policy like "AmazonS3FullAccess".
8. Save the Job role and Run the Job 
9. Switch to Jobs run Monitoring tab under AWS Glue and Monitor the Job running Status.

**Crawlers:**

10. Then Goto AWS Glue Data Catalog -> Crawlers
11. Create a Database
12. While Creating a Crawler, Add the permissions to the IAM role like "AmazonS3ReadOnlyAccess", "AWSGlueServiceRole"
13. Make sure Tables are created, after the run is successfull

**AWS Athena:**

14. Launch AWS Athena
15. Open the Athena Query Editor and Configure the Database and tables.
16. Create a S3 bucket to store the Athena output results and after querying check whether the results are saved in S3 bucket

**QuickSight:**

17. Launch QuickSight
18. Link the S3 Athena stored output Results and Visualize the Data 



**Folder Structure inside the S3 Buckets:**


<img width="428" alt="Screenshot 2024-09-29 at 1 06 01 AM" src="https://github.com/user-attachments/assets/25bdae76-1d77-431e-93ce-d3c695ef255f">


<img width="884" alt="Screenshot 2024-09-29 at 1 06 19 AM" src="https://github.com/user-attachments/assets/b0a30729-1466-4298-80b6-36fa40b3660a">




**IAM Role - Policies used to execute this Project**



<img width="935" alt="Screenshot 2024-09-29 at 12 52 48 AM" src="https://github.com/user-attachments/assets/7f61aa43-2711-4991-8237-464368d45b40">


