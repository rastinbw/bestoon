#!/bin/bash

curl --data "token=123456789&description=$1&amount=$2" http://localhost:8000/submit/expense



