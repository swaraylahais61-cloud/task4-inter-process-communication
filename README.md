# Task 4: Inter-Process Communication

## Overview

This project demonstrates Inter-Process Communication (IPC) using Python socket programming. It consists of a server program and a client program that communicate by exchanging messages over a TCP connection.

## Objectives

- Create a server that listens for client connections.
- Allow a client to send text messages to the server.
- Send an acknowledgment from the server to the client.
- Display received messages and test the communication process.

## Project Structure

```text
Task4_IPC/
├── src/
│   ├── client.py
│   └── server.py
├── docs/
│   └── screenshots/
│       ├── client1_Output.png
│       ├── client2_Output.png
│       └── server_Output.png
└── README.md
```

## Requirements

- Python 3
- Two PowerShell terminal windows
- No third-party Python packages

## Running the Application

Open two PowerShell terminals in the project root directory.

### 1. Start the Server

In the first terminal, run:

```powershell
py src\server.py
```

Wait until the server reports that it is running and waiting for clients.

### 2. Start the Client

In the second terminal, run:

```powershell
py src\client.py
```

### 3. Test the Communication

Enter a message in the client terminal. The server displays the received message and sends an acknowledgment back to the client.

Type `exit` to end the client session. Start the server before starting the client.

## Connection Configuration

The application uses the local IP address `127.0.0.1` and port `5000`. Both programs must run on the same computer with this configuration.

## Screenshots

Screenshots showing the server output and two client test sessions are available in the [`docs/screenshots/`](docs/screenshots/) directory.

## Assignment Information

- **Course:** Parallel and Distributed Systems
- **Assignment:** Task 4 - Inter-Process Communication (IPC)
- **Student:** LAHAI SIMONE SWARAY
- **Student ID:** 20250040**8
