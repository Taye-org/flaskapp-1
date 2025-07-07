# Flask App 1 – Welcome App

This is your first deployed Flask app!

## What It Does

When you visit the app, it greets you like this:

> Hey Taye, welcome to your first app deployment! You still have 2 more to go. 🚀

## Run Locally

```bash
docker build -t flask-app-1 .
docker run --rm -p 5000:5000 --env-file .env flask-app-1
