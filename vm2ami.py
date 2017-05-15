#!/usr/bin/python
import argparse
import AWSUtilities
from OvfExporter import OvfExporter
import tempfile
import os
import sys


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
    parser.add_argument('-b', '--aws_bucket', type=str, required=True,
                        help='The aws_bucket of the profile to upload and save vmdk to')
    parser.add_argument('-m', '--ami_name', type=str, required=False, help='The name to give to the uploaded ami. '
                                                                           'Defaults to the name of the file')
    args = parser.parse_args()

    return args


def validate_args(args):
    """
    Call all required validation methods
    :param args:
    :return:
    """
    if not os.path.isdir(args.directory):
        print "Directory {} does not exist".format(args.directory)
        sys.exit(5)

    aws_importer = AWSUtilities.AWSUtils(args.directory, args.aws_profile, args.s3_bucket,
                                         args.aws_regions, args.ami_name, None)
    aws_importer.validate()


def vm2ami(args):
    """
    Download VMDKs from vCenter, and upload them to AWS s3 bucket, convert the file into an AMI. Then rename the AMI,
    and copy it to all other required regions
    :param args:
    :return:
    """
    exporter = OvfExporter(user=args.vcenter_user,password=args.vcenter_pass, host=args.vcenter_host, port=args.vcenter_port,
                           vm_name=args.vm_name, dir=args.directory)
    vmdk_file = exporter.export_ovf()

    aws_importer = AWSUtilities.AWSUtils(args.directory, args.aws_profile, args.s3_bucket,
                                         args.aws_regions, args.ami_name, vmdk_file)
    aws_importer.import_vmdk()


if __name__ == "__main__":
    args = parse_args()
    vm2ami(args)
