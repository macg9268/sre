#!/bin/bash

while true; do
  curl http://localhost:8000/slow
  curl http://localhost:8000/error
done