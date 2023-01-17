#!/bin/bash
# sends GET req to URL and display response body
curl -Lsf "$1" -X GET
