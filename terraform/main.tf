provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "sre_server" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  tags = {
    Name = "sre-reliable-api"
  }
}