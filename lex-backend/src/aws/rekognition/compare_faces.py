import boto3
from botocore.exceptions import NoCredentialsError
from src.aws.ses.send_match_mail import send_match_mail


def compare_faces(source_image_key, id):
    print('entrou no comparece faces')
    rekognition_client = boto3.client('rekognition', region_name='us-east-1')
    bucket_name = 'alopoliciateste'

    s3 = boto3.client('s3')
    objects = s3.list_objects(
        Bucket=bucket_name, Prefix='missing_people/')['Contents']
    try:
        source_image_obj = s3.get_object(
            Bucket=bucket_name, Key=source_image_key)
        source_image_data = source_image_obj['Body'].read()
    except NoCredentialsError:
        print("Erro: Credenciais AWS não encontradas.")

    found_match = False
    for obj in objects:
        if obj['Key'].endswith('/'):
            continue
        try:
            target_image_obj = s3.get_object(
                Bucket=bucket_name, Key=obj['Key'])
            target_image_data = target_image_obj['Body'].read()
        except NoCredentialsError as err:
            print(f"Erro: Credenciais AWS não encontradas. {str(err)}")

        response = rekognition_client.compare_faces(
            SourceImage={'Bytes': source_image_data},
            TargetImage={'Bytes': target_image_data}
        )
        if response['FaceMatches'] and response['FaceMatches'][0]['Similarity'] >= 70:
            print(
                f"Match encontrado com taxa de assertividade de {response['FaceMatches'][0]['Similarity']} para a imagem: {obj['Key']}")
            found_match = True
            image_source = f"https://s3.amazonaws.com/alopoliciateste/{source_image_key}"
            image_target = f"https://s3.amazonaws.com/alopoliciateste/{obj['Key']}"
            similarity = response['FaceMatches'][0]['Similarity']
            send_match_mail(image_source,image_target,similarity,id)

            return {
                'foundMatch': 'Yes',
                'sourceImageKey': source_image_key,
                'targetImageKey': obj['Key'],
                'accuracy': str(similarity)
            }
            

    if not found_match:
        return {
            'foundMatch': 'No',
            'sourceImageKey': 'None',
            'targetImageKey': 'None',
            'accuracy': 'None'
        }