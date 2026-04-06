pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      agent {
        node {
          label 'docker-agent'
        }

      }
      steps {
        git(url: 'https://github.com/macg9268/sre', branch: 'trace')
      }
    }

    stage('Shell command') {
      parallel {
        stage('Shell command') {
          steps {
            sh 'ls -lsha'
          }
        }

        stage('') {
          steps {
            sh 'cd /opt/jenkins'
          }
        }

      }
    }

  }
}