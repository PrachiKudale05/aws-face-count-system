import json
import boto3
import pymysql
import urllib.parse

# ---------------- AWS CLIENT ----------------
rekognition = boto3.client('rekognition')

def lambda_handler(event, context):

    print("EVENT RECEIVED:", json.dumps(event))

    try:
        # ---------------- S3 DATA ----------------
        bucket = event['Records'][0]['s3']['bucket']['name']
        image = event['Records'][0]['s3']['object']['key']
        image = urllib.parse.unquote_plus(image)

        print("Bucket:", bucket)
        print("Image:", image)

        # ---------------- REKOGNITION ----------------
        response = rekognition.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': image
                }
            },
            Attributes=['ALL']
        )

        face_count = len(response['FaceDetails'])
        print("Face Count:", face_count)

        # ---------------- RDS CONNECTION ----------------
        connection = pymysql.connect(
            host='database-1.c9omy8m64l6j.ap-south-1.rds.amazonaws.com',
            user='admin',
            password='awsPrachi05',
            database='facedetectdb',
            port=3306
        )

        cursor = connection.cursor()

        # ---------------- INSERT QUERY ----------------
        sql = "INSERT INTO facecount(image_name, face_count) VALUES (%s, %s)"
        values = (image, face_count)

        cursor.execute(sql, values)
        connection.commit()

        cursor.close()
        connection.close()

        print("DATA INSERTED SUCCESSFULLY")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "image": image,
                "faces_detected": face_count
            })
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }