# Login Flow Sequence Diagram

```mermaid
sequenceDiagram
  participant User
  participant Camera
  participant Frontend
  participant Backend
  participant Model
  participant DB

  User->>Camera: Show hand gesture
  Camera->>Frontend: Capture image frame
  Frontend->>Backend: Send image
  Backend->>Model: Predict sign label
  Model-->>Backend: Return predicted label
  Backend->>Frontend: Display label
  Backend->>DB: (Optional) Save gesture + label

