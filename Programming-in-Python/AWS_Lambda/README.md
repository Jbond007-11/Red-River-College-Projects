# AWS Lambda Standard Deviation Calculator

This project demonstrates a basic client-server architecture using AWS. It consists of a cloud-based Lambda function that performs a standard deviation calculation and a local Python script that invokes the function and retrieves the result.

This project was developed using the **AWS Academy Learner Lab**, which uses temporary, session-based credentials.

### Project Architecture
This project is split into two main parts:
1.  **AWS Lambda Function (`lambda_function.py`):** This Python script runs in the AWS cloud. It's designed to receive a list of numbers, calculate their standard deviation, and return the result in a JSON format.
2.  **Local Invocation Script (`aws_lambda.py`):** This Python script runs on your local machine. It uses the `boto3` library to securely connect to your AWS account, send the list of numbers to the `StdDev` Lambda function, and print the returned result.

---
### Setup and Deployment

#### Part 1: AWS Lambda Setup (Cloud Environment)
1.  Start your AWS Academy Learner Lab environment.
2.  Navigate to the **AWS Lambda** service in the console.
3.  Create a new Lambda function from scratch and name it **`StdDev`**. Use a recent Python runtime (e.g., Python 3.9+).
4.  Once created, replace the default code in the `lambda_function.py` editor with the following script:
    ```python
    import json
    import math

    def standard_deviation(nums):
        """Calculate standard deviation of a list of numbers"""
        if not nums or len(nums) < 2:
            return 0
        
        mean = sum(nums) / len(nums)
        variance = sum([(x - mean) ** 2 for x in nums]) / (len(nums) - 1)
        return math.sqrt(variance)

    def lambda_handler(event, context):
        """AWS Lambda entry point"""
        nums = event['nums']
        result = standard_deviation(nums)
        
        return {
            'statusCode': 200,
            'nums': nums,
            'result': result
        }
    ```
5.  Click the **Deploy** button to save your changes.
6.  To test the function within AWS, navigate to the "Test" tab, create a new event, and use the following JSON as the payload:
    ```json
    {
      "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    ```

#### Part 2: Local Environment Setup
1.  **Get Credentials:** In the AWS Academy Learner Lab terminal, click "AWS Details" to get your temporary credentials. You will need the **Access Key ID**, **Secret Access Key**, and **Session Token**.
2.  **Create Credential Files:** On your local Windows machine, navigate to `C:\Users\YOUR_USERNAME\`. Create a new folder named **`.aws`**.
3.  Inside the `.aws` folder, create two new text files: `credentials` and `config`.
4.  **Populate `credentials` file:** Open the `credentials` file and paste your keys in the following format. The session token is required for the lab environment.
    ```ini
    [default]
    aws_access_key_id = PASTE_YOUR_ACCESS_KEY_ID_HERE
    aws_secret_access_key = PASTE_YOUR_SECRET_ACCESS_KEY_HERE
    aws_session_token = PASTE_YOUR_SESSION_TOKEN_HERE
    ```
5.  **Populate `config` file:** Open the `config` file and set your default region.
    ```ini
    [default]
    region = us-east-1
    ```
**Important:** You must repeat Step 1 and Step 4 every time you restart your AWS Learner Lab, as the credentials will change.

---
### How to Run
1.  Complete all steps in the "Setup and Deployment" section.
2.  On your local machine, install the AWS SDK for Python: `pip install boto3`.
3.  Run the local invocation script from your terminal:
    ```bash
    python "aws_lambda.py"
    ```
4.  The script will connect to your Lambda function, send the numbers `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, and print the calculated standard deviation.