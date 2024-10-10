<div align="center">
  <img src="static/img/logo.png" alt="DiscoveryDataLab" style="width: 50%;">

  <p align="center">
    <strong>Main repository for the blog website.</strong>
  </p>

<hr>

![Static Hugo Website](https://img.shields.io/badge/%27Static%20Hugo%20Website%27%20-20B2AA?style=for-the-badge)
![Automatic Deploy Workflow](https://img.shields.io/badge/%27Automatic%20Deploy%20Workflow%27%20-20B2AA?style=for-the-badge)
![Simple To Customize](https://img.shields.io/badge/%27Simple%20To%20Customize%27%20-20B2AA?style=for-the-badge)

</div>

### Overview

This repository contains the source code for the Hugo-based static blog site. The site is designed to be easily customizable and deployable, with automated workflows to ensure seamless updates.

## Documentation 📚

### Theme Customization

- **[Required Tools](#required-tools)**
- **[Running the Site Locally](#running-the-site-locally)**

### Deployment

- **[Easy Deployment](#easy-deployment)**  
   Learn how to deploy the site using Hugo and GitHub Pages (or any preferred platform). The guide covers building and pushing the static files to the deployment server.

- **[Customizing the Workflow](#customizing-the-workflow)**  
   Instructions on modifying the CI/CD pipeline for automated deployment, including configuring build triggers and customizing the environment.

---

## Required Tools

- [Install Hugo to preview changes locally](https://gohugo.io/getting-started/installing/)
- [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Running the Site Locally

To preview and develop the site locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Discovery-Data-Lab/blog
   ```

2. Navigate to the project folder:
   ```bash
   cd blog
   ```

3. Start the Hugo development server:
   ```bash
   hugo server
   ```

4. Open your browser and go to `http://localhost:1313` to view the site.

## Easy Deployment

This project utilizes a GitHub Actions workflow located in `github/workflows/deploy.yml` for automated deployment. Simply create a pull request, and the deployment will be triggered automatically. Be aware that errors might occur if the FTP server is down.

## Customizing the Workflow

- The current workflow uses `hugo-version: 0.111.3`. While this isn't the latest version, it is compatible with the project's tools (comments, styles, etc.).
- The deployment process employs `lftp` to remove old static files from the FTP server and replace them with the new ones. Although resource-intensive, it's effective. Feel free to suggest improvements if you have any ideas.
- If FTP credentials are incorrect or missing, check the site configuration and update them as necessary.