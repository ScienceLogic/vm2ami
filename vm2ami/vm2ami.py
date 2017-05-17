#!/usr/bin/python
import argparse
from amiimporter import amiupload
from amiimporter import AWSUtilities
from ovfexporter import ovfexport
import tempfile


def parse_args():
    """
    Argument Parser and Validator
    """
    parser = argparse.ArgumentParser(description="Converts, and downloads a vm by name from vCenter to OVF in specified"
                                                 " directory, then uploads the image as an AMI. AMI will be uploaded "
                                                 "using specified AWS profile, to specified regions. ")
    parser.add_argument('-i', '--vcenter_host', type=str, required=True, help='Hostname or Ip of vCenter API of VM')
    parser.add_argument('-u', '--vcenter_user', type=str, required=True, help='Username for vCenter authentication')
    parser.add_argument('-p', '--vcenter_pass', type=str, required=True, help='Password for authentication to vCenter API')
    parser.add_argument('-n', '--vm_name', type=str, required=True, help='Name of the VM in vCenter')
    parser.add_argument('-r', '--aws_regions', type=str, nargs='+', required=True,
                        help='Comma delimited list of AWS regions where uploaded ami should be copied. Available'
                             ' regions: {}.'.format(AWSUtilities.aws_regions))
    parser.add_argument('-a', '--aws_profile', type=str, required=True, help='AWS profile name to use for aws cli commands')
    parser.add_argument('-d', '--directory', type=str, default=tempfile.mkdtemp(),
                        help='Directory to save the vmdk temp file (defaults to temp location')
    parser.add_argument('-w', '--vcenter_port', type=str, default='443',
                        help='Port to use for communication to vcenter api. Default is 443')
    parser.add_argument('-b', '--s3_bucket', type=str, required=True,
                        help='The s3 of the profile to upload and save vmdk to')
    parser.add_argument('-m', '--ami_name', type=str, required=False, help='The name to give to the uploaded ami. '
                                                                           'Defaults to the name of the file')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    ovfexport.validate_args(args)
    amiupload.validate_args(args)
    downloaded_vmdk = ovfexport.convert(args)

    args.vmdk_upload_file = downloaded_vmdk
    amiupload.vmdk_to_ami(args)

