import boto3

# сначала надо зарегатся в aws3 потом создать bucket

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration
# можно так  делать и можно указать в ~/.aws/credentials там указывае
# ассess токен !!! --> важно чтобы находился в корневом каталоге
s3 = boto3.resource('s3',aws_access_key_id='AKIA4LJFIHLRIJSNYFNS',
                    aws_secret_access_key ='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')




obj = s3.Object("myservise", "photo_5325622133096824942_x.jpg")
photo = obj.get()['Body'].read()
print(photo)


with open("test.jpg", "wb") as file:
    file.write(photo)

