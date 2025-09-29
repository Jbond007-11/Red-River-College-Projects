# Flask Math Calculator on AWS EC2

This project is a fully functional web application that calculates the maximum, average, and standard deviation of a list of numbers. It's built with Python using the Flask micro-framework and is designed to be deployed and run on a live AWS EC2 server.

### Features
* User-friendly web interface for entering comma-separated numbers.
* Calculates maximum, average, and sample standard deviation of the input.
* Styled with a clean, external CSS stylesheet.
* Uses HTML templates to dynamically render the user interface and results.
* Demonstrates a complete workflow for deploying a Python web application to a cloud environment.

### Technology Stack
* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Cloud Platform:** Amazon Web Services (AWS) EC2

### Project Structure
The project is organized into the standard Flask application structure with separate folders for static assets and templates.

    AWS_Calculator/
    ├── app.py
    ├── static/
    │   └── styles.css
    └── templates/
        ├── index.html
        └── results.html
---
### Local Setup & Run
To run this application on your local machine:
1.  Install Flask: `pip install flask`.
2.  Navigate to the project's root directory.
3.  Run the application: `python app.py`.
4.  Open your web browser and go to `http://localhost:5000`.

---
### Cloud Deployment to AWS EC2

These steps detail how to deploy the application to an Ubuntu server on AWS EC2.

#### Part 1: Launching the EC2 Instance
1.  Log into the AWS Academy Learner Lab and navigate to the **EC2** service.
2.  Launch a new instance and name it **`MyMath`**.
3.  Select **Ubuntu** as the operating system (AMI).
4.  Create a **new key pair**, name it, and download the `.pem` file. Store this file securely, as it's required for connecting to the server.
5.  In "Network settings", edit the security group to add a new rule:
    * **Type:** Custom TCP
    * **Port Range:** `5000`
    * **Source:** `0.0.0.0/0` (This allows access from any IP address).
6.  Launch the instance.

#### Part 2: Preparing the Server
1.  Connect to your instance using the EC2 console's connection feature or a local SSH client.
2.  Update the server's package manager: `sudo apt update`.
3.  Install the Python package installer (pip): `sudo apt install python3-pip`.
4.  Install Flask: `pip3 install flask`.

#### Part 3: Transferring Project Files
1.  Use an SFTP client like **FileZilla** or **WinSCP**.
2.  Create a new connection with the following details:
    * **Host:** Your instance's **Public IPv4 address**.
    * **Username:** `ubuntu`
    * **Authentication:** Use the `.pem` key file you downloaded in Part 1.
3.  Connect to the server and transfer the entire `AWS_Calculator` project folder to the `ubuntu` home directory.

#### Part 4: Running the Application on the Server
1.  In your server's terminal, navigate into the project folder: `cd AWS_Calculator`.
2.  To run the Flask app persistently in the background (so it keeps running after you disconnect), use the `nohup` command:
    ```bash
    nohup python3 app.py &
    ```
3.  You can verify it's running by checking the `nohup.out` file: `cat nohup.out`.

#### Accessing the Live Application
Once running, the application can be accessed in a web browser using your instance's public IP address followed by port 5000: `http://<Your-Public-IPv4-Address>:5000`.