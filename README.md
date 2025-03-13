# TeamFlask: AWS App Runner Containerized Deployment

A simple Flask web application deployed to AWS using App Runner and containerization. This project demonstrates how to build and deploy a containerized Flask application that displays team information through environment variables.

![TeamFlask Screenshot](screenshots/teamflask-screenshot.png)

## Project Overview

This project showcases a seamless deployment workflow for Flask applications using Docker containers and AWS App Runner. The application is a simple web page that displays team information set through environment variables, demonstrating how containerized applications can be quickly deployed and scaled in AWS without managing the underlying infrastructure.

## Features

- Simple Flask web application with environment variable support
- Containerized using Docker
- Deployed to AWS App Runner
- Custom domain setup with Route 53
- Infrastructure as Code approach

## Technologies Used

- **Backend**: Python, Flask
- **Containerization**: Docker
- **Cloud Services**: 
  - AWS App Runner
  - Amazon ECR (Elastic Container Registry)
  - AWS Route 53 (for custom domain)
- **DevOps**: AWS CLI, Docker CLI

## Getting Started

### Prerequisites

- AWS Account
- Docker installed locally
- AWS CLI configured
- Python 3.x

### Local Development

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/teamflask-aws-app-runner.git
   cd teamflask-aws-app-runner
   ```

2. Run the application locally using Docker:
   ```bash
   docker build -t flask-team-image .
   docker run -d -p 80:80 -e TEAM="YourTeamName" flask-team-image
   ```

3. Access the application at `http://localhost:80`

### AWS Deployment

#### 1. Connect Docker to AWS ECR

```bash
aws ecr get-login-password | docker login --username AWS --password-stdin <AWS-Account-ID>.dkr.ecr.<AWS-Region>.amazonaws.com
```

#### 2. Create ECR Repository

```bash
aws ecr create-repository --repository-name teamflask-repo
```

#### 3. Build, Tag and Push Docker Image

```bash
docker build -t flask-team-image .
docker tag flask-team-image <AWS-Account-ID>.dkr.ecr.<AWS-Region>.amazonaws.com/teamflask-repo:latest
docker push <AWS-Account-ID>.dkr.ecr.<AWS-Region>.amazonaws.com/teamflask-repo:latest
```

#### 4. Deploy with AWS App Runner

1. Go to AWS App Runner console
2. Create a new App Runner service
3. Choose "Container registry" as repository type
4. Select "Amazon ECR" as provider
5. Browse and select your ECR repository and image tag
6. Configure the service:
   - Set port to 80
   - Add environment variable: TEAM=YourTeamName
   - Create necessary service role
   - Choose appropriate compute resources
7. Deploy the service
8. (Optional) Configure custom domain with Route 53

## Project Structure

```
teamflask-aws-app-runner/
├── app.py               # Flask application code
├── Dockerfile           # Docker configuration
├── screenshots/         # Application screenshots
└── README.md            # Project documentation
```

## Architecture Diagram

**AWS Cloud**  
├── **Local Development Environment**  
│   ├── **Docker**  
│   │   └── **Flask Application Container**  
│   │       └── **app.py** (Team Display Application)  
│   └── **AWS CLI** (For Authentication & Deployment)  
│  
├── **Amazon ECR**  
│   └── **teamflask-repo**  
│       └── **flask-team-image** (Container Image)  
│  
├── **AWS App Runner Service**  
│   ├── **Container Instance**  
│   │   └── **Flask Application** (Running on Port 80)  
│   │       └── **Environment Variable: TEAM**  
│   ├── **App Runner Service Role**  
│   │   └── **AppRunnerECRAccessRole** (Permissions to pull from ECR)  
│   └── **Default Domain** (apprunner-service.region.awsapprunner.com)  
│  
└── **Route 53**  
    └── **Custom Domain**  
        └── **myapprunner.cctstudents.com**  
            └── **ALIAS Record** (Points to App Runner Service) 

---


## Environment Variables

- `TEAM`: Sets the team name displayed on the web page. Defaults to "Unknown" if not set.

## Lessons Learned

- AWS App Runner simplifies container deployment by managing infrastructure
- Proper Docker image architecture is crucial for AWS compatibility (using `--platform=linux/amd64`)
- Environment variables provide a clean way to configure applications across environments
- AWS ECR integrates seamlessly with Docker for image management

## Future Improvements

- Add CI/CD pipeline integration
- Implement more complex application logic
- Add database integration
- Create infrastructure as code using AWS CDK or Terraform

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- AWS Documentation for App Runner and ECR
- Flask Documentation
- Docker Documentation
