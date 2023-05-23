# Backend-Internship-Assignment
# Nudge Creations Api Docs

## **Object Data Model**

The Nudge object has the following properties:

- **`id`** (primary key, unique): The unique identifier for the nudge.
- **`event`** (event, foreign key): Event for which Nudge is creating.
- **`title`** (Char Field): The title of the nudge.
- **`image`** (Image Field): The image used as the cover for the nudge.
- **`time`** (Date Time): The time at which the nudge should be sent.
- **`description`** (Text Field): The description of the nudge.
- **`icon`** (Image Field): The icon associated with the nudge.
- **`invitationMsg`** (string): The one-line invitation text shown when the nudge is minimized or displayed alongside an event/article.

## **API Endpoints**

1. Create a Nudge

   **Endpoint:** **`POST /nudges`**

   Creates a new nudge.

   **Payload:**

   ```json
   {
     "title": "Sample Nudge",
     "event": "Farewell",
     "image": "https://example.com/nudge-image.jpg",
     "time": "2023-06-01T09:00:00",
     "description": "This is a sample nudge.",
     "icon": "https://example.com/nudge-icon.png",
     "invitation": "Join us for an exciting event!"
   }
   ```

   **Response: `Status code: 201 Created`**

   ```json
   {
     "id": "abc123",
     "title": "Sample Nudge",
     "event": "Farewell",
     "image": "https://example.com/nudge-image.jpg",
     "time": "2023-06-01T09:00:00",
     "description": "This is a sample nudge.",
     "icon": "https://example.com/nudge-icon.png",
     "invitation": "Join us for an exciting event!"
   }
   ```

2. Retrieve a Nudge

   **Endpoint:** **`GET /nudges/{id}`**

   Retrieves the details of a specific nudge.

   **Response: `Status code: 200 OK`**

   ```json
   {
     "id": "abc123",
     "title": "Sample Nudge",
     "event": "Farewell",
     "image": "https://example.com/nudge-image.jpg",
     "time": "2023-06-01T09:00:00",
     "description": "This is a sample nudge.",
     "icon": "https://example.com/nudge-icon.png",
     "invitation": "Join us for an exciting event!"
   }
   ```

3. Update a Nudge

   **Endpoint:** **`PUT /nudges/{id}`**

   Updates an existing nudge with new data.

   **Payload:**

   ```json
   jsonCopy code
   {
   	"id": "abc123",
     "title": "Updated Nudge",
   	"event": "Farewell",
     "image": "https://example.com/updated-image.jpg",
     "time": "2023-06-01T10:00:00",
     "description": "This is an updated nudge.",
     "icon": "https://example.com/updated-icon.png",
     "invitation": "Don't miss out on the event!"
   }

   ```

   **Response: `Status code: 200 OK`**

   ```json
   {
     "id": "abc123",
     "title": "Updated
   }
   ```

4. Delete a Nudge

   **Endpoint:** **`DELETE /nudges/{id}`**

   Delete an existing nudge.

   **Response: `Status: 200 No Content`**

