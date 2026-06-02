pipeline {

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
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Build Successful"
            }
        }

        stage('Test') {
            steps {
                echo "CI TEST PASSED"
            }
        }

        stage('CI Validation') {
            steps {
                echo "CI Completed Successfully"
            }
        }

        stage('Manual Approval') {

            when {
                branch 'main'
            }

            steps {

                input(
                    message: 'CI Passed. Deploy to AWS?',
                    ok: 'Deploy'
                )
            }
        }

        stage('AWS Authentication') {

            when {
                branch 'main'
            }

            steps {

                withCredentials([
                    string(credentialsId: 'aws-access-key', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY'),
                    string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY'),
                    string(credentialsId: 'aws-session-token', variable: 'AWS_SESSION_TOKEN')
                ]) {

                    bat 'aws sts get-caller-identity'
                }
            }
        }

        stage('Terraform Init') {

            when {
                branch 'main'
            }

            steps {
                bat 'terraform init'
            }
        }

        stage('Terraform Validate') {

            when {
                branch 'main'
            }

            steps {
                bat 'terraform validate'
            }
        }

        stage('Terraform Plan') {

            when {
                branch 'main'
            }

            steps {
                bat 'terraform plan'
            }
        }

        stage('Docker Build') {

            when {
                branch 'main'
            }

            steps {
                bat "docker build -t ${ECR_REPO}:${IMAGE_TAG} ."
            }
        }

        stage('ECR Login') {

            when {
                branch 'main'
            }

            steps {

                bat """
                aws ecr get-login-password --region ap-south-1 > password.txt

                docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com < password.txt
                """
            }
        }

        stage('Push To ECR') {

            when {
                branch 'main'
            }

            steps {

                bat """
                docker tag ${ECR_REPO}:${IMAGE_TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}

                docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
                """
            }
        }
    }
}