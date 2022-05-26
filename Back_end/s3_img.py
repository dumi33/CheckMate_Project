from urllib import response
import boto3
import os 
import io
from PIL import Image
from more_itertools import bucket
from config import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY
from config import AWS_S3_BUCKET_NAME, AWS_S3_BUCKET_REGION





def s3_connection():
    '''
    s3 bucket에 연결
    :return: 연결된 s3 객체
    '''
    try:
        s3 = boto3.client('s3',
    		aws_access_key_id = AWS_ACCESS_KEY,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
        
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3

# img read 사용을 위해 
def s4_connection():
    try:
        s4 = boto3.resource('s3',
            aws_access_key_id = AWS_ACCESS_KEY,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
        
    except Exception as e:
        print(e)
    else:
        print("s4 bucket connected!")
        return s4



# 이미지 업로드 1
# 로컬에 있는 이미지 업로드 
def handle_upload_img(s3,f): # f = 파일명
	response = s3.upload_file(
            os.getcwd()+'\\'+f+'.jpg',
            AWS_S3_BUCKET_NAME, 
            'capture_image/'+f+'.jpg',
            ExtraArgs={ # url을 통해 Read (not download)
                'ContentType': 'image/jpeg'
            }
    )
    # 로컬파일경로 + 파일명 + 파일종류, 버킷명, s3버킷의 원하는경로 + 파일명 + 파일종류

# 이미지 업로드 2
# 로컬에 있지 않은 이미지 업로드 
def handle_upload_img2(s3,f,u): # f = 파일명 u = 저장될 이름 
	s3.upload_fileobj( f,
            AWS_S3_BUCKET_NAME, 
            u,
            ExtraArgs={ # url을 통해 Read (not download)
                'ContentType': 'image/jpeg'
            }
    )


def s3_delete_img(s3,filename) :
    s3.delete_object(Bucket = AWS_S3_BUCKET_NAME,Key =filename )


# s3에 저장된 이미지 파일 반환  
def read_image_from_s4(s4,filename):
    buckets = s4.Bucket(AWS_S3_BUCKET_NAME)
    objects = buckets.Object(filename)
    response = objects.get()
    file_stream = response['Body']
    img = Image.open(file_stream)
    return img


# 이미지 url 반환 
def s3_get_image_url(s3, filename):
    '''
    s3 : 연결된 s3 객체(boto3 client)
    filename : s3에 저장된 파일 명
    '''
    location = s3.get_bucket_location(Bucket=AWS_S3_BUCKET_NAME)["LocationConstraint"]
    return f"https://{AWS_S3_BUCKET_NAME}.s3.{location}.amazonaws.com/capture_image/{filename}.jpg"


"""


def s3_get_object(s3, bucket, object_name, file_name):
    '''
    s3 bucket에서 지정 파일 다운로드
    :param s3: 연결된 s3 객체(boto3 client)
    :param bucket: 버킷명
    :param object_name: s3에 저장된 object 명
    :param file_name: 저장할 파일 명(path)
    :return: 성공 시 True, 실패 시 False 반환
    '''
    try:
        s3.download_file(bucket, object_name, file_name)
    except Exception as e:
        print(e)
        return False
    return True

def s3_put_object(s3, bucket, filepath, access_key):
    '''
    s3 bucket에 지정 파일 업로드
    :param s3: 연결된 s3 객체(boto3 client)
    :param bucket: 버킷명
    :param filepath: 파일 위치
    :param access_key: 저장 파일명
    :return: 성공 시 True, 실패 시 False 반환
    '''
    try:
        s3.upload_file(filepath, bucket, access_key)
    except Exception as e:
        print(e)
        return False
    return True
    
"""