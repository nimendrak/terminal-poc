# Terminal POC

This repository contains a project that has a emulated terminal. The commands can be triggered through the backend and realtime data can be displayed in the fronend using a websocket.

## Prerequisites
- React
- Python 3.7

## Demonstration

Following demonstration executed by running `ping www.google.lk` 

<img src="https://github.com/nimendrak/terminal-poc/blob/main/preview/preview.gif?raw=true" alt="animated-banner">

## Instructions to Run the Project

01. Install all the mentioned node modules by running `npm install` inside frontend folder.
02. Install python libraries by running `pip3 install -r requirements.txt` inside backend folder.
03. Run FastAPI backen by `uvicorn server.py:app` (Default port is `localhost/8000`)
04. Go to socketapp, Open CMD and type `npm start`