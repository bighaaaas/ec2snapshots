import boto3

if __name__ == '__main__':
    session = boto3.Session
    ec2 = boto3.resource('ec2')
    for i in ec2.instances.all():
        print(i)
