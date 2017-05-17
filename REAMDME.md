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
Ensure you have the local silo repository in your .pip config and:

```
$ pip install vm2ami
```


## Running
    All arguments and parameters are specified in the help menu when running the script
    Example Run:

    ```
    $ vm2ami -h
    ```