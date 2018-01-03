# serverless-fst
Repository for OpenFST Utilities as AWS Serverless Applications

## fstinfo

Once your application is deployed, you can get the fst info for a binary FST by converting your fst to base64 and posting it to the /info URI.

```bash
base64 -i binary.fst -o base64.fst
curl -X POST https://<invoke url>/Prod/info --data-binary @tests/data/base64.fst
```

## Building executables for Lambda

In order to build the OpenFST tools for AWS Lambda we need to build the executables on an AmazonLinux 2012 AMI. You can use the startup.sh bootstrap script to download and build the OpenSFT tools on EC2 startup.
