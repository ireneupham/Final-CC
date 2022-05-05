# Query State Covid Data

Using the information from the [Johns Hopkins University COVID-19](https://github.com/CSSEGISandData/COVID-19) repo, this provides a sample application that uses the querying feature of Amazon AWS S3, processed by a Lambda function, served by an API Gateway and distributed through Cloudfront. It simulates how one could scale and deploy applications from a single lambda function to many backed by AWS Services.

This application can be deployed using the sample cloudformation.yaml file in AWS.

## Architecture
![Architecture](/images/architecture.png)

Cloudfront was used to distribute and cache browser requests to both the static assets in S3 and the results of the Lambda function query. It includes many web application security features as well and provides low latency requests all over the world.

API Gateway behind CloudFront allows you to deploy many Lambda functions and provide an API for web applications to use. It's widely configurable and provides options for security like CORS and logging.

Since the data provided was in a CSV form, S3 buckets have the capability of loading these files directly without loading it into an intermediate database. Using a lambda function to call the AWS api, we can then gather the data requested and return it in a scalable form.

## Demo
A demo of this application is available at https://dwnfnrr39gbkn.cloudfront.net/index.html
![Demo](/images/demo.png)

## Demo Video 
A demo video of this application is availible via recording here ()
