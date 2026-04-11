#!/bin/bash

while true; do
  curl http://api_python:8000/slow
  curl http://api_python:8000/error
done