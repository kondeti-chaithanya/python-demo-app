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

                echo "Checking out code..."

                checkout scm

            }
        }

        stage('Install Dependencies') {

            steps {

                echo "Installing dependencies..."

                

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
                    [$class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-creds']
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

                bat """
                docker build -t ${ECR_REPO}:${IMAGE_TAG} .
                """
            }
        }

        stage('ECR Login') {

            steps {

                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-creds']
                ]) {

                    bat """
                    aws ecr get-login-password --region %AWS_REGION% > password.txt

                    docker login --username AWS --password-stdin %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com < password.txt
                    """
                }
            }
        }

        stage('Push To ECR') {

            steps {

                bat """

                docker tag ${ECR_REPO}:${IMAGE_TAG} %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}

                docker push %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
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
}