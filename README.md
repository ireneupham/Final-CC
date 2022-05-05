# Query State Covid Data

Using the information from the [Johns Hopkins University COVID-19](https://github.com/CSSEGISandData/COVID-19) repo, this provides a sample application that uses the querying feature of Amazon AWS S3, processed by a Lambda function, served by an API Gateway and distributed through Cloudfront. It simulates how one could scale and deploy applications from a single lambda function to many backed by AWS Services.

## Architecture
![Architecture](/images/architecture.png)
