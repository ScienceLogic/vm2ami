# vCenter vm to AWS ami converter

## About
vm2ami will use the combination of the ovfexporter and amiuploader packages to perform an export of a vCenter vmdk to
the local file system. The exported vmdk will then be uploaded into the specified s3 bucket with amiuploader. After
image fully uploaded, the amiuploader script will perform the calls necessary to convert the image to an AMI, then rename
and copy the image to all specified regions

## Requirements
- vCenter user should have permissions to export a vm

In order to complete all necessary operations to upload, import and copy images the following system requirements must be
met
- awscli installed and configured: In order to perform aws commands, you must configure ~/.awscli/profile
and ~/.awscli/config as defined in: http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
- The specified s3 bucket must already exist in first region chosen for the ami upload
- AWS credentials must have permissions described in: http://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html
- Exported VM must meet AWS pre-reqs: http://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html

This script does its best to validate that you have permissions, but no promises are made


## Installation
It's available in the public pypi repo. Simply:

```
$ pip install vm2ami
```


## Running
All arguments and parameters are specified in the help menu when running the script


    $ vm2ami -h
    
    usage: vm2ami [-h] -i VCENTER_HOST -u VCENTER_USER -p VCENTER_PASS -n VM_NAME
              -r AWS_REGIONS [AWS_REGIONS ...] -a AWS_PROFILE [-d DIRECTORY]
              [-w VCENTER_PORT] -b S3_BUCKET [-m AMI_NAME]

Converts, and downloads a vm by name from vCenter to OVF in specified
directory, then uploads the image as an AMI. AMI will be uploaded using
specified AWS profile, to specified regions.

optional arguments:
  -h, --help            show this help message and exit
  -i VCENTER_HOST, --vcenter_host VCENTER_HOST
                        Hostname or Ip of vCenter API of VM
  -u VCENTER_USER, --vcenter_user VCENTER_USER
                        Username for vCenter authentication
  -p VCENTER_PASS, --vcenter_pass VCENTER_PASS
                        Password for authentication to vCenter API
  -n VM_NAME, --vm_name VM_NAME
                        Name of the VM in vCenter
  -r AWS_REGIONS [AWS_REGIONS ...], --aws_regions AWS_REGIONS [AWS_REGIONS ...]
                        Comma delimited list of AWS regions where uploaded ami
                        should be copied. Available regions: ['us-east-1',
                        'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1',
                        'eu-west-1', 'eu-central-1', 'eu-west-2', 'ap-
                        northeast-1', 'ap-northeast-2', 'ap-southeast-2', 'ap-
                        south-1', 'sa-east-1'].
  -a AWS_PROFILE, --aws_profile AWS_PROFILE
                        AWS profile name to use for aws cli commands
  -d DIRECTORY, --directory DIRECTORY
                        Directory to save the vmdk temp file (defaults to temp
                        location
  -w VCENTER_PORT, --vcenter_port VCENTER_PORT
                        Port to use for communication to vcenter api. Default
                        is 443
  -b S3_BUCKET, --s3_bucket S3_BUCKET
                        The s3 of the profile to upload and save vmdk to
  -m AMI_NAME, --ami_name AMI_NAME
                        The name to give to the uploaded ami. Defaults to the
                        name of the file
