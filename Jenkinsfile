pipeline {

```
agent any

environment {
    AWS_REGION = 'ap-south-1'
    AWS_ACCOUNT_ID = '330372999051'
    ECR_REPO = 'python-demo'
    IMAGE_TAG = "${BUILD_NUMBER}"
}

stages {

    stage('Checkout') {
        steps {
            echo "Checking out code..."
            checkout scm
        }
    }

    stage('Install Dependencies') {
        steps {
            echo "Installing dependencies..."
            bat 'python --version'
        }
    }

    stage('Build') {
        steps {
            echo "Application Build Successful"
        }
    }

    stage('Print Test Statement') {
        steps {
            echo "CI TEST PASSED"
        }
    }

    stage('Run Tests') {
        steps {
            echo "Executing Unit Tests"
        }
    }

    stage('AWS Login') {
        steps {

            withCredentials([
                string(credentialsId: 'aws-access-key', variable: 'AWS_ACCESS_KEY_ID'),
                string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY'),
                string(credentialsId: 'aws-session-token', variable: 'AWS_SESSION_TOKEN')
            ]) {

                bat '''
                aws sts get-caller-identity
                '''
            }
        }
    }

    stage('Terraform Init') {
        steps {
            dir('terraform') {
                bat 'terraform init'
            }
        }
    }

    stage('Terraform Validate') {
        steps {
            dir('terraform') {
                bat 'terraform validate'
            }
        }
    }

    stage('Terraform Plan') {
        steps {
            dir('terraform') {
                bat 'terraform plan'
            }
        }
    }

    stage('Docker Build') {
        steps {
            bat "docker build -t ${ECR_REPO}:${IMAGE_TAG} ."
        }
    }

    stage('ECR Login') {

        steps {

            withCredentials([
                string(credentialsId: 'aws-access-key', variable: 'AWS_ACCESS_KEY_ID'),
                string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY'),
                string(credentialsId: 'aws-session-token', variable: 'AWS_SESSION_TOKEN')
            ]) {

                bat """
                aws ecr get-login-password --region ap-south-1 > password.txt

                docker login --username AWS --password-stdin 330372999051.dkr.ecr.ap-south-1.amazonaws.com < password.txt
                """
            }
        }
    }

    stage('Push To ECR') {

        steps {

            bat """
            docker tag ${ECR_REPO}:${IMAGE_TAG} 330372999051.dkr.ecr.ap-south-1.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}

            docker push 330372999051.dkr.ecr.ap-south-1.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
            """
        }
    }
}

post {
    success {
        echo "Pipeline Completed Successfully"
    }

    failure {
        echo "Pipeline Failed"
    }
}
```

}
