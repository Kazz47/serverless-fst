# serverless-fst

Repository for OpenFST Utilities as AWS Serverless Applications

Made with ❤️ by Kyle Goehner. Available on the [AWS Serverless Application Repository](https://aws.amazon.com/serverless)

## fstinfo

Once your application is deployed, you can get the fst info for a binary FST by posting it to the /info URI.

```bash
curl -X POST https://<invoke url>/Prod/info -H Content-Type:application/octet-stream --data-binary @test/data/binary.fst
```

## Building executables for Lambda

In order to build the OpenFST tools for AWS Lambda we need to build the executables on an AmazonLinux 2012 AMI. You can use the startup.sh bootstrap script to download and build the OpenSFT tools on EC2 startup.
