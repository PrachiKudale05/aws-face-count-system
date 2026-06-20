# AWS-Face-Count-System

## Project Summary

Designed and implemented a serverless image-processing pipeline on AWS that automatically detects faces in uploaded images and stores analysis results in a MySQL database.

The solution uses event-driven architecture to eliminate manual image processing and demonstrates real-world cloud automation using AWS managed services.

---

## Key Highlights

* Built a fully serverless architecture using AWS services
* Automated image analysis workflow using Amazon Rekognition
* Implemented event-driven processing with Amazon S3 and AWS Lambda
* Stored processed results in Amazon RDS MySQL
* Configured IAM roles and CloudWatch monitoring
* Reduced manual image analysis effort through automation

---

## Architecture

User Upload
→ Amazon S3
→ AWS Lambda Trigger
→ Amazon Rekognition
→ Face Detection
→ Amazon RDS MySQL
→ CloudWatch Monitoring

---

## Technologies Used

### AWS Services

* Amazon S3
* AWS Lambda
* Amazon Rekognition
* Amazon RDS (MySQL)
* AWS IAM
* Amazon CloudWatch

### Programming Language

* Python

### Database

* MySQL

---

## Workflow

1. User uploads an image to Amazon S3.
2. S3 generates an event notification.
3. AWS Lambda is automatically triggered.
4. Lambda invokes Amazon Rekognition.
5. Rekognition detects faces in the image.
6. Lambda calculates total face count.
7. Results are stored in Amazon RDS.
8. CloudWatch logs capture execution details.

---

## Skills Demonstrated

* Serverless Computing
* Event-Driven Architecture
* Cloud Automation
* AWS Security & IAM
* Database Integration
* Python Development
* Cloud Monitoring
* AI/ML Service Integration

---

## Business Value

This solution demonstrates how cloud-native architectures can automate image processing workflows, improve scalability, and reduce operational overhead without managing servers.

---

## Future Enhancements

* Emotion Detection
* Age and Gender Analysis
* Real-Time Dashboard
* SNS Notifications
* Face Recognition Collections

---

## Author

Prachi Kudale
AWS Cloud | Python Developer | DevOps Enthusiast
