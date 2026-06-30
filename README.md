# A Comprehensive Measure of Well-Being

## Entity Relationship (ER) Diagram

The ER diagram represents the core entities involved in the project and shows how they are connected.

### Entities

1. User
2. Country
3. HDI Input Data
4. Dataset
5. ML Model
6. HDI Prediction
7. Visualization Report
8. Session

### Relationships

- One User can create many HDI Input Data records.
- One Country can have many HDI Input Data records.
- One HDI Input Data record generates one HDI Prediction.
- One ML Model can generate many HDI Predictions.
- One Dataset can train many ML Models.
- One HDI Prediction can generate many Visualization Reports.
- One User can have many Sessions.

### User Attributes

- user_id (Primary Key)
- name
- email
- role
- created_at

### ER Diagram

See the file: `ER_Diagram.png`
