| **Description** | **URI** | **GET** | **POST** | **PUT** | **DELETE** | **Complete** |
|:----------------|:--------|:--------|:---------|:--------|:-----------|:-------------|
| List of Projects | /api/projects/ | List of all projects | -        | Create a new Project |-           | Yes          |
| One Project     | /api/projects/<< project\_number >>/ | Project details | Updates project | -       | -          | Yes          |
| List of Deliverables | /api/deliverables/<< project\_number >>/ | List of Deliverables | -        | -       | -          | No           |
| One Deliverable | /api/deliverables/<< project\_number >>/<< deliverable\_id >>/ | Deliverable detail | Update the deliverable | -       | Delete the deliverable| No           |
| List of Risks   | /api/risks/<< project\_number >>/ | List of Risks | -        | -       | -          | No           |
| One Risk        | /api/risks/<< project\_number >>/<< risk\_id >>/ | Risk detail | Update the Risk | -       | Delete the Risk| No           |
| List of Work Items | /api/wbs/<< project\_number >>/ | List of Work Items | -        | -       | -          | No           |
| One Work Item   | /api/wbs/<< project\_number >>/<< wbs\_id >>/ | Work Item detail | Update the Work Item | -       | Delete the Work Item| No           |
| List of Issues  | /api/issues/<< project\_number >>/ | List of Issues | -        | -       | -          | No           |
| One Issue       | /api/issues/<< project\_number >>/<< issue\_id >>/ | Issue detail | Update the Issue | -       | Delete the Issue| No           |
| List of Lessons | /api/lessons/<< project\_number >>/ | List of Lessons | -        | -       | -          | No           |
| One Lesson      | /api/lessons/<< project\_number >>/<< lesson\_id >>/ | Lesson detail | Update the Lesson | -       | Delete the Lesson| No           |
| List of Reports | /api/reports/<< project\_number >>/ | List of Reports | -        | -       | -          | No           |
| One Report      | /api/report/<< project\_number >>/<< report\_id >>/ | Report detail | Update the Report | -       | Delete the Report| No           |
| List of Files   | /api/files/<< project\_number >>/ | List of Files | -        | -       | -          | No           |
| One File        | /api/files/<< project\_number >>/<< file\_id >>/ | File detail | Update the File | -       | Delete the File| No           |
| Users           | /api/projects/<< project\_number >>/users/ | List of Users | -        | -       | -          | No           |
| Managers        | /api/projects/<< project\_number >>/managers/ | List of Managers | -        | -       | -          | No           |
| Non-managers    | /api/projects/<< project\_number >>/non-managers/ | List of non-Managers | -        | -       | -          | No           |
| Skillsets       | /api/skillsets/ | List of skillsets | Add to list of skillsets | -       | -          | No           |
| Stage Plan      | /api/projects/<< project\_number >>/stage\_plan/ | List of Stages | Add to Stages | -       | -          | No           |
| One Stage       | /api/projects/<< project\_number >>/stage\_plan/<< stage\_id >>/ | Stage detail | Update the stage | -       | Delete the stage | No           |




