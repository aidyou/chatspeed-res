---
title: "Virtual_Pet"
description: "In the digital wave, MCPet rekindles the warm memories of 90s electronic pets, reconstructing a nostalgic experience with modern AI technology. This MCP server, developed based on TypeScript, creates…"
---

# Virtual_Pet

In the digital wave, MCPet rekindles the warm memories of 90s electronic pets, reconstructing a nostalgic experience with modern AI technology. This MCP server, developed based on TypeScript, creates…

# Project Overview

MCPet is a Model Context Protocol (MCP) server application developed in TypeScript, designed to bring a nostalgic virtual pet experience to users in the AI era. It recreates the classic Tamagotchi toy's nurturing gameplay, integrating modern AI technology and model context protocols. Users can adopt, nurture, and interact with their digital companions, watching them grow from infants to adults. Even when offline, the pet's various statistics will naturally change over time, providing a realistic and emotionally engaging virtual pet nurturing experience.

## Core Features

- **Full Lifecycle Nurturing:** Supports the complete growth process of pets from infancy to adulthood, where every interaction influences the pet's growth trajectory.
- **Rich Interactive Gameplay:** Offers diverse interactive methods such as feeding, cleaning, and playing. The pet's personality and status will change based on the user's care.
- **AI-Driven Characteristics:** Based on the Model Context Protocol (MCP), the pet has certain learning and feedback capabilities. The more frequent the interactions, the smarter the pet behaves.
- **Offline Dynamic Updates:** Even when the user is not online, the pet's hunger, cleanliness, and other statuses will change in real-time, simulating the survival logic of a real pet.

## Technical Architecture

- **Development Language:** TypeScript, providing strong type support to enhance code maintainability and stability.
- **Frameworks and Libraries:** Uses Node.js as the runtime environment, combined with the Express framework to build the server, and WebSocket for real-time state synchronization.
- **Data Storage:** By default, uses an in-memory database to store pet data, with support for expanding to persistent storage solutions like MongoDB.
- **Protocol Support:** Deeply implements the Model Context Protocol (MCP) to dynamically associate user actions with pet states.

## Installation and Configuration

### 4.1 Environment Requirements
- Node.js Version: >= v14.0.0
- npm Version: >= v6.14.0

### 4.2 Installation Steps
Clone the project repository:

git clone https://github.com/shreyaskarnik/mcpet.git

Enter the project directory:

cd mcpet

Install dependencies:

npm install

### 4.3 Configuration Instructions
**Environment Variable Setup:**
- Create a `.env` file in the root directory of the project and configure the following environment variables:
  - Server port number, default is 3000
    
    PORT=3000
    
  - Pet data storage directory, must be a writable directory
    
    PET_DATA_DIR=/path/to/writable/directory
    
  - (Optional) If using MongoDB, configure the database connection string
    
    MONGODB_URI=mongodb://localhost:27017/mcpet
    

**Other Configurations:**
- You can modify the configuration files under the `config` directory according to your needs, adjusting server parameters and feature options.

## Usage

### 5.1 Start the Service

npm start

After starting the service, the default access address is http://localhost:3000.

### 5.2 User Operation Guide
- **Adopt a Pet:** Visit the service page and follow the guide to adopt your own virtual pet.
- **Daily Interactions:** Use the provided buttons for feeding, cleaning, and playing on the page to interact with your pet and observe changes in its status.
- **View Pet Information:** On the pet details page, you can view detailed information about the pet's health, happiness, and growth progress.

## API Documentation

This project provides some RESTful APIs for interacting with the pet service. The specific API documentation can be found in the `docs/api` directory or generated through an online documentation tool. The main APIs include:
- Get pet list: `GET /api/pets`
- Get single pet details: `GET /api/pets/{petId}`
- Feed the pet: `POST /api/pets/{petId}/feed`
- Clean the pet: `POST /api/pets/{petId}/clean`

## Contributions and Feedback

- **Contribution Guidelines:** Developers are welcome to submit code contributions. Please refer to CONTRIBUTING.md for the specific process.
- **Issue Reporting:** If you encounter any issues or have suggestions for improvements during use, please submit feedback via the GitHub Issues section or send an email to [author's email].

## License

This project is licensed under the MIT License, allowing free use, modification, and distribution, but retaining the copyright notice.
This README covers the key information of the MCPet project, meeting basic usage and technical reference needs. If you feel there's content that needs to be added or adjusted, feel free to let me know.

**Official site: ** [https://github.com/shreyaskarnik/mcpet?tab=readme-ov-file](https://github.com/shreyaskarnik/mcpet?tab=readme-ov-file)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/mcpet/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/xsc202406-virtual-pet.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
