#!/bin/bash
rm -rf dist
mkdir -p dist
cd lambdas
zip lambdas.zip *
mv lambdas.zip ../dist