# OncoXBiomarker
A Django-based web application that allows users to explore a curated cancer biomarker database. The site enables users to view biomarkers associated with specific cancer types, explore cancer subtypes, and access relevant clinical data and research references. The project is designed to support researchers and clinicians by providing a user-friendly interface to navigate biomarker-impact relationships.

## Features
- Interactive homepage with buttons for each cancer type
- Cancer-specific pages with tables showing:
  -  Biomarkers
  -  Cancer name and subtype
  -  Clinical impact data (role, mutation, treatment, etc.)
- Hyperlinks to biomarker reference sources
- Subtype detail pages with ICD and cancer description

<p align="center">
  <img width="600" alt="Screenshot 2025-04-08 at 3 43 26 PM" src="https://github.com/user-attachments/assets/2a8e2735-8f3c-487a-aa42-ba63c052ef2b" />
</p>

## Tech Stack
- Frontend: HTML and CSS
- Backend: Django (Python)
- Database: MySQL

<p align="center">
  <img width="504" alt="Screenshot 2025-04-08 at 3 39 29 PM" src="https://github.com/user-attachments/assets/dca4dc38-9904-4696-840a-4601ce723f28" />
</p>

## Folder Structure
- `cancerdb/`: Your main Django app containing all views, models, HTML templates, and route definitions.
  - `migrations/`: Auto-generated files for managing database schema changes.
  - `templates/`: All HTML pages shown to the user
  - `static/`: Contains static assets such as JavaScript files, and images used by the frontend.
- `finalproject/`: The main Django project settings folder (configures databases, static files, etc.).

## Authors
- Sahiti Somalraju, IU Luddy School of Informatic, Computing, and Engineering
- Rebekah Lanning, IU Luddy School of Informatic, Computing, and Engineering
- Bijal Patel, Richard M. Fairbanks School of Public Health
- Jessica Kersey, IU School of Medicine
